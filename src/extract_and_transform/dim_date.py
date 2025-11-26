import pandas as pd
import os

# CSV file path, this way It works both locally and in production
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
CSV_PATH = os.path.join(BASE_DIR, 'assets', 'sales_data.csv')

# I created a function to extract and transform the dim_customer data, which reads from a CSV file, processes date columns, selects relevant columns, renames them, and enforces data types. And then, stores the result in a DataFrame.
def get_dim_date():
    # Reading the CSV file
    df = pd.read_csv(CSV_PATH)
    
    # Convert date columns to datetime format
    df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True, errors='coerce')
    df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True, errors='coerce')

    # Find the min and max dates from both date columns
    # Combining both date columns to find the overall min and max dates
    min_date = min(df['Order Date'].min(), df['Ship Date'].min())
    max_date = max(df['Order Date'].max(), df['Ship Date'].max())
        
    # Creating the dim_date DataFrame
    dim_date = pd.DataFrame({'Date': pd.date_range(start=min_date, end=max_date, freq='D')})
    
    # Creating additional date attributes
    dim_date['Year'] = dim_date['Date'].dt.year
    dim_date['Quarter'] = dim_date['Date'].dt.quarter
    dim_date['Month'] = dim_date['Date'].dt.month
    dim_date['Month_name'] = dim_date['Date'].dt.strftime('%B')
    dim_date['Day'] = dim_date['Date'].dt.day
    dim_date['Day_name'] = dim_date['Date'].dt.strftime('%A')
    
    # Renaming columns to follow naming conventions
    dim_date.rename(columns={
        "Date": "date_key",
        "Year": "year",
        "Quarter": "quarter",
        "Month": "month",
        "Month_name": "month_name",
        "Day": "day",
        "Day_name": "day_name"
    }, inplace=True)
    
    # Enforcing data types
    dim_date = dim_date.astype({
        "year": "int",
        "quarter": "int",
        "month": "int",
        "month_name": "string",
        "day": "int",
        "day_name": "string"
    })

    print(dim_date.info())
    print(dim_date.head())

    # I added a print statement to show the number of processed rows, which can be useful for debugging and verification.
    print(f"Processed rows: {len(dim_date)}")

    return dim_date

# get_dim_date().to_excel('dim_date_output.xlsx', index=False)