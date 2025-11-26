import pandas as pd
import os

# CSV file path, this way It works both locally and in production
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
CSV_PATH = os.path.join(BASE_DIR, 'assets', 'sales_data.csv')

# I created a function to extract and transform the dim_ship data, which reads from a CSV file, processes date columns, selects relevant columns, renames them, and enforces data types. And then, stores the result in a DataFrame.
def get_dim_ship():
    # Reading the CSV file
    df = pd.read_csv(CSV_PATH)

    # Selecting and renaming relevant columns for the dim_ship table
    dim_ship = df[[
            "Ship Mode"
        ]].drop_duplicates(subset=['Ship Mode']).copy()

    # Renaming columns to follow naming conventions
    dim_ship.rename(columns={
            "Ship Mode": "ship_mode"
        }, inplace=True)

    # Enforcing data types
    dim_ship = dim_ship.astype({
            "ship_mode": "string"
        })
       

    print(dim_ship.info())
    print(dim_ship.head())

    # I added a print statement to show the number of processed rows, which can be useful for debugging and verification.    
    print(f"Processed rows: {len(dim_ship)}")

    return dim_ship 

# get_dim_ship().to_excel('dim_ship_output.xlsx', index=False)