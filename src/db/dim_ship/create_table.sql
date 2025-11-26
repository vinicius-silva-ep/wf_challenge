CREATE TABLE IF NOT EXISTS wf_challenge.dim_ship (
    ship_sk SERIAL PRIMARY KEY, -- Surrogate Key
    ship_mode TEXT NOT NULL UNIQUE
);