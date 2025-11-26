import pandas as pd
import os

# CSV file path, this way It works both locally and in production
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
CSV_PATH = os.path.join(BASE_DIR, 'assets', 'sales_data.csv')

# I created a function to extract and transform the dim_geo data, which reads from a CSV file, processes date columns, selects relevant columns, renames them, and enforces data types. And then, stores the result in a DataFrame.
def get_dim_geo():
    # Reading the CSV file
    df = pd.read_csv(CSV_PATH)

    # Selecting and renaming relevant columns for the dim_geo table
    dim_geo = df[[
            "City",
            "State",
            "Postal Code",
            "Country",
            "Region"
        ]].copy()
    
    # Creating a geographical key by combining postal_code, city, and state
    dim_geo['geo_id'] = (
        dim_geo['Postal Code'].astype(str) + '-' + 
        dim_geo['City'].astype(str) + '-' + 
        dim_geo['State'].astype(str)
    )  
    
    # Removing duplicates based on 'geo_id'
    dim_geo.drop_duplicates(subset=['geo_id'], keep='first', inplace=True)    

    # Renaming columns to follow naming conventions
    dim_geo.rename(columns={
            "City": "city",
            "State": "state",
            "Postal Code": "postal_code",
            "Country": "country",
            "Region": "region"
        }, inplace=True)

    # Enforcing data types
    dim_geo = dim_geo.astype({
            "city": "string",
            "state": "string",
            "postal_code": "string",
            "country": "string",
            "region": "string",
            "geo_id": "string"
        })
    
    # Reordering columns
    column_order = [
        "geo_id",
        "postal_code",
        "city",
        "state",
        "country",
        "region"
        ]   
    dim_geo = dim_geo[column_order]       

    print(dim_geo.info())
    print(dim_geo.head())

    # I added a print statement to show the number of processed rows, which can be useful for debugging and verification.    
    print(f"Processed rows: {len(dim_geo)}")

    return dim_geo 

# get_dim_geo().to_excel('dim_geo_output.xlsx', index=False)