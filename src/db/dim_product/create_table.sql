CREATE TABLE IF NOT EXISTS wf_challenge.dim_product (
    product_key TEXT PRIMARY KEY,
    product_id TEXT NOT NULL,
    product_name TEXT,
    sub_category TEXT,
    category TEXT
);