import pandas as pd
import os

# CSV file path, this way It works both locally and in production
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
CSV_PATH = os.path.join(BASE_DIR, 'assets', 'sales_data.csv')

# I created a function to extract and transform the fact_sales data, which reads from a CSV file, processes date columns, selects relevant columns, renames them, and enforces data types. And then, stores the result in a DataFrame.
def get_fact_sales():

    # Reading the CSV file
    df = pd.read_csv(CSV_PATH)

    # Treating date columns
    df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True, errors='coerce')
    df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True, errors='coerce')

    # Selecting and renaming relevant columns for the fact_sales table
    fact_sales = df[[
        "Row ID",
        "Order ID",
        "Customer ID",
        "Product ID",
        "Order Date",
        "Ship Date",
        "Ship Mode",
        # -- Columns to create geo_id foreign key --
        "Postal Code", 
        "City", 
        "State",        
        # -----------------------------------------
        "Sales",
        "Quantity",
        "Discount",
        "Profit"
    ]].copy()

    # Renaming columns to follow naming conventions
    fact_sales.rename(columns={
        "Row ID": "row_id",
        "Order ID": "order_id",
        "Customer ID": "customer_id",
        "Product ID": "product_id",
        "Order Date": "order_date",
        "Ship Date": "ship_date",
        "Ship Mode": "ship_mode",
        # -- Renaming columns for geo_id foreign key --
        "Postal Code": "postal_code", 
        "City": "city", 
        "State": "state", 
        # ---------------------------------------        
        "Sales": "sales_amount", # I renamed Sales to sales_amount for clarity 
        "Quantity": "quantity",
        "Discount": "discount_rate", # I renamed Discount to discount_rate for clarity
        "Profit": "profit_amount" # I renamed Profit to profit_amount for clarity
    }, inplace=True)

    # Creating a geographical key by combining postal_code, city, and state
    fact_sales['geo_id'] = (
        fact_sales['postal_code'].astype(str) + '-' + 
        fact_sales['city'].astype(str) + '-' + 
        fact_sales['state'].astype(str)
    )    

    # Eliminating the now redundant columns used to create geo_id
    fact_sales.drop(columns=['postal_code', 'city', 'state'], inplace=True)

    # Enforcing data types
    fact_sales = fact_sales.astype({
        "row_id": "string",
        "order_id": "string",
        "customer_id": "string",
        "product_id": "string",
        "geo_id": "string",
        "ship_mode": "string",
        "quantity": "int"
    })

    # Converting float columns with error handling
    cols_float = ["sales_amount", "discount_rate", "profit_amount"]
    for col in cols_float:
        fact_sales[col] = pd.to_numeric(fact_sales[col], errors='coerce').fillna(0.0)

    # Reordering columns to place geo_id after product_id
    column_order = [
            "row_id",
            "order_id",
            "customer_id",
            "product_id",
            "geo_id",
            "order_date",
            "ship_date",
            "ship_mode",
            "sales_amount",
            "quantity",
            "discount_rate",
            "profit_amount"
        ]   
    fact_sales = fact_sales[column_order]         

    print(fact_sales.info())
    print(fact_sales.head())
    
    # I added a print statement to show the number of processed rows, which can be useful for debugging and verification.
    print(f"Processed rows: {len(fact_sales)}")

    return fact_sales 