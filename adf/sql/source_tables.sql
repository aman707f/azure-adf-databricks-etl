CREATE TABLE sales_transactions (
    transaction_id INT PRIMARY KEY,
    product_id INT,
    quantity INT,
    price DECIMAL(10,2),
    transaction_date DATE
);
