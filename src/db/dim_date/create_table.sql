CREATE TABLE IF NOT EXISTS wf_challenge.dim_date (
    date_key DATE NOT NULL,
    year INTEGER NOT NULL,
    quarter INTEGER NOT NULL,
    month INTEGER NOT NULL,
    month_name TEXT NOT NULL,
    day INTEGER NOT NULL,
    day_name TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_dim_date_date_key ON wf_challenge.dim_date (date_key);