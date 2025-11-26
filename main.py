# This is the main script to orchestrate the loading of data into the database.
from src.load.fact_sales import load_fact_sales_to_db
from src.load.dim_customer import load_dim_customer_to_db
from src.load.dim_date import load_dim_date_to_db
from src.load.dim_geo import load_dim_geo_to_db
from src.load.dim_product import load_dim_product_to_db
from src.load.dim_ship import load_dim_ship_to_db

def main():

    # Step 1: Load fact_sales
    try:
        load_fact_sales_to_db()
        print("fact_sales loaded successfully.")        
    except Exception as e:
        print(f"Error loading fact_sales: {e}")

    # Step 2: Load dim_customer
    try:
        load_dim_customer_to_db()
        print("dim_customer loaded successfully.")        
    except Exception as e:
        print(f"Error loading dim_customer: {e}")     

    # Step 3: Load dim_date
    try:
        load_dim_date_to_db()
        print("dim_date loaded successfully.")        
    except Exception as e:
        print(f"Error loading dim_date: {e}")   

    # Step 4: Load dim_geo
    try:
        load_dim_geo_to_db()
        print("dim_geo loaded successfully.")        
    except Exception as e:
        print(f"Error loading dim_geo: {e}")   

    # Step 5: Load dim_product
    try:
        load_dim_product_to_db()
        print("dim_product loaded successfully.")        
    except Exception as e:
        print(f"Error loading dim_product: {e}")   

    # Step 6: Load dim_ship
    try:
        load_dim_ship_to_db()
        print("dim_ship loaded successfully.")      
          
    except Exception as e:
        print(f"Error loading dim_ship: {e}")                                      

if __name__ == "__main__":
    main()
