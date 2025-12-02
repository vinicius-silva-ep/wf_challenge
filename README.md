# Data Analyst Assessment – Sales Analytics Pipeline

This repository contains the full solution for the Data Analyst Assessment, including Python ETL scripts, SQL database setup, data dictionary, diagrams, and the final Power BI report.

## 📌 Project Overview
The goal of this project was to:
- Convert a raw `sales_data.csv` file into a structured analytical dataset.
- Build a PostgreSQL/CockroachDB data model (dimensions + fact table).
- Develop a Power BI dashboard with dynamic KPIs and visual insights.

## 🚀 Architecture
**CSV → Python (Extract and Transform) → CockroachDB (Load) → Power BI (Model and Dashboard)**

Main steps:
- Extract and clean data using Pandas.
- Generate surrogate keys (`product_key`, `geo_id`).
- Validate and create database schema/tables using SQL.
- Load fact and dimension tables with SQLAlchemy.
- Connect Power BI to the database and build a star schema.

## 📂 Repository Structure
- src/
- extract_and_transform/
- load/
- db/
- assets/

## 📊 KPIs Included
- Revenue  
- Profit  
- Profit Margin  
- Quantity  
- Orders  
- Distinct Customers  
- Average Discount  
- Average Ticket  
- Average Delivery Time  

## 🧠 Key Challenges Addressed
- Duplicate IDs in raw data  
- Understanding metadata before loading  
- Creating new surrogate keys  
- Handling incorrect customer names in the raw dataset  

## 🔗 Additional Resources
- GitHub repository with all commits (ETL + SQL + Power BI)
- Power BI report published in workspace 
- Dashboard Link: https://app.powerbi.com/view?r=eyJrIjoiZDJkNzcwMzAtY2M4My00ODIwLWE1OWEtYThhNWIwY2FmZmYzIiwidCI6IjliZTg5NmYwLWNjMWMtNGQ5Yy1hOWI1LWE4ZTMyM2Y0YzhhOCIsImMiOjh9 

---