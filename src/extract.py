import pandas as pd
import os

# CSV file path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
CSV_PATH = os.path.join(BASE_DIR, 'assets', 'sales_data.csv')

# Reading the CSV file
df = pd.read_csv(CSV_PATH)

