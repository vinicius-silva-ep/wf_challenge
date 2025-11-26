CREATE TABLE IF NOT EXISTS wf_challenge.fact_sales (
    row_id INTEGER PRIMARY KEY,
    order_id TEXT,
    customer_id TEXT NOT NULL,
    product_key TEXT NOT NULL,
    geo_id TEXT NOT NULL,
    ship_mode TEXT NOT NULL,
    order_date TIMESTAMP,
    ship_date TIMESTAMP,
    sales_amount NUMERIC(18, 6),
    quantity INTEGER,
    discount_rate NUMERIC(18, 3),
    profit_amount NUMERIC(18, 6)
);

-- Creating indexes to improve query performance
CREATE INDEX IF NOT EXISTS idx_fact_sales_customer_id ON wf_challenge.fact_sales (customer_id);
CREATE INDEX IF NOT EXISTS idx_fact_sales_product_key ON wf_challenge.fact_sales (product_key);
CREATE INDEX IF NOT EXISTS idx_fact_sales_geo_id ON wf_challenge.fact_sales (geo_id);
CREATE INDEX IF NOT EXISTS idx_fact_sales_ship_mode ON wf_challenge.fact_sales (ship_mode);