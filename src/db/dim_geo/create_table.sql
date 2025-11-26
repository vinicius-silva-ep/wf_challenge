CREATE TABLE IF NOT EXISTS wf_challenge.dim_geo (
    geo_id TEXT PRIMARY KEY,
    postal_code TEXT,
    city TEXT,
    state TEXT,
    country TEXT,
    region TEXT
);