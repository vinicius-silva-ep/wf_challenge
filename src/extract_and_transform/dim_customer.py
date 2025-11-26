import pandas as pd
import os

# CSV file path, this way It works both locally and in production
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
CSV_PATH = os.path.join(BASE_DIR, 'assets', 'sales_data.csv')

# I created a function to extract and transform the dim_customer data, which reads from a CSV file, processes date columns, selects relevant columns, renames them, and enforces data types. And then, stores the result in a DataFrame.
def get_dim_customer():
    # Reading the CSV file
    df = pd.read_csv(CSV_PATH)

    # Selecting and renaming relevant columns for the dim_customer table. Also, removing duplicates based on 'Customer ID'.
    dim_customer = df[[
            "Customer ID",
            "Customer Name",
            "Segment"    
    # Removing duplicates based on 'Customer ID'
        ]].drop_duplicates(subset=['Customer ID']).copy()

    # Renaming columns to follow naming conventions
    dim_customer.rename(columns={
            "Customer ID": "customer_id",
            "Customer Name": "customer_name",
            "Segment": "segment"
        }, inplace=True)

    # Enforcing data types
    dim_customer = dim_customer.astype({
            "customer_id": "string",
            "customer_name": "string",
            "segment": "string"
        })

    print(dim_customer.info())
    print(dim_customer.head())

    # I added a print statement to show the number of processed rows, which can be useful for debugging and verification.
    print(f"Processed rows: {len(dim_customer)}")

    return dim_customer 

# get_dim_customer().to_excel('dim_customer_output.xlsx', index=False)