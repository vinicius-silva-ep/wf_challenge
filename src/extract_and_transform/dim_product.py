import pandas as pd
import os

# CSV file path, this way It works both locally and in production
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
CSV_PATH = os.path.join(BASE_DIR, 'assets', 'sales_data.csv')

# I created a function to extract and transform the dim_product data, which reads from a CSV file, processes date columns, selects relevant columns, renames them, and enforces data types. And then, stores the result in a DataFrame.
def get_dim_product():
    # Reading the CSV file
    df = pd.read_csv(CSV_PATH)

    # Selecting and renaming relevant columns for the dim_product table
    dim_product = df[[
            "Product ID",
            "Category",
            "Sub-Category",
            "Product Name"
        ]].copy()
    
    # Creating a product key by combining Product ID and Product Name
    dim_product['product_key'] = (
            dim_product['Product ID'].astype(str) + '-' + 
            dim_product['Product Name'].astype(str)
        )    
    
    # Removing duplicates based on 'product_key'
    dim_product.drop_duplicates(subset=['product_key'], keep='first', inplace=True)    

    # Renaming columns to follow naming conventions
    dim_product.rename(columns={
            "Product ID": "product_id",
            "Product Name": "product_name",
            "Sub-Category": "sub_category",
            "Category": "category"
        }, inplace=True)

    # Enforcing data types
    dim_product = dim_product.astype({
            "product_id": "string",
            "product_name": "string",
            "sub_category": "string",
            "category": "string",
            "product_key": "string"
        })
    
    # Reordering columns
    column_order = [
        "product_key",
        "product_id",
        "product_name",
        "sub_category",
        "category"
        ]   
    dim_product = dim_product[column_order]       

    print(dim_product.info())
    print(dim_product.head())

    # I added a print statement to show the number of processed rows, which can be useful for debugging and verification.    
    print(f"Processed rows: {len(dim_product)}")

    return dim_product 

# get_dim_product().to_excel('dim_product_output.xlsx', index=False)