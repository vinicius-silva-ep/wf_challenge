import os
import sys
from sqlalchemy import create_engine
from src.extract_and_transform.fact_sales import get_fact_sales
from dotenv import load_dotenv

load_dotenv()

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", ".."))
sys.path.insert(0, ROOT_DIR)

def load_fact_sales_to_db():

    # Get the transformed dimension customer data from the extract_and_transform module
    df_fact_sales = get_fact_sales()

    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_SCHEMA = os.getenv("DB_SCHEMA")  # se tiver schema


    pwd = DB_PASSWORD
    postgres_user = DB_USER
    postgres_host = DB_HOST
    postgres_port = DB_PORT
    postgres_database = DB_NAME
    postgres_schema = DB_SCHEMA

    # Create the database connection string for using CockroachDB with SQLAlchemy
    connection_string = f"cockroachdb+psycopg2://{postgres_user}:{pwd}@{postgres_host}:{postgres_port}/{postgres_database}"

    # Engine creation
    engine = create_engine(connection_string)

    # Rename the DataFrame for clarity
    df = df_fact_sales

    # Insert the data into the database
    # This case appends the data to the "fact_sales" table in the specified schema
    df.to_sql("fact_sales", engine, schema=postgres_schema, if_exists="append", index=False)

if __name__ == "__main__":
    load_fact_sales_to_db()
