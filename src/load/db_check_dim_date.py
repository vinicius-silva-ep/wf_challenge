import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Getting the path to the SQL files
base_path = os.path.abspath(
    os.path.dirname(__file__)
)

# Adjusting the path to the dim_date database folder
db_path = os.path.join(
    base_path, "../db/dim_date"
)

# Function to read the SQL query from a file
def read_sql_file(file_path):
    with open(file_path, "r") as file:
        return file.read()
    
# Functions SQL
verify_table = os.path.join(db_path, "verify_table.sql")
create_table = os.path.join(db_path, "create_table.sql") 

def db_operations():
    # Establish the connection using the variables from config.py
    connection = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
    )

    cursor = connection.cursor()

    # Verify and create the 'dim_date' table if it doesn't exist
    cursor.execute(read_sql_file(verify_table))
    if not cursor.fetchone()[0]:
        cursor.execute(read_sql_file(create_table))
        connection.commit()

    # Close the connection
    cursor.close()
    connection.close()

# db_operations()    