CREATE TABLE IF NOT EXISTS sales_cleaned (
    order_id INTEGER PRIMARY KEY,
    order_date DATE,
    customer TEXT,
    product TEXT,
    quantity INTEGER,
    unit_price NUMERIC,
    region TEXT,
    total_sales NUMERIC,
    loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);