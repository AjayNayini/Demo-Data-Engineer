CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    age INT,
    city VARCHAR(50)
);

CREATE TABLE accounts (
    account_id INT PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    account_type VARCHAR(20),
    balance NUMERIC(10,2)
);

CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY,
    account_id INT REFERENCES accounts(account_id),
    customer_id INT REFERENCES customers(customer_id),
    transaction_type VARCHAR(20),
    amount NUMERIC(10,2),
    transaction_date DATE
);

INSERT INTO customers VALUES
(1,'John',25,'Dallas'),
(2,'Maria',35,'Austin'),
(3,'James',42,'Houston'),
(4,'Sophia',30,'Chicago'),
(5,'David',45,'Dallas'),
(6,'Emma',28,'Austin'),
(7,'Jack',38,'New York'),
(8,'Olivia',33,NULL),
(9,'Liam',40,'Houston'),
(10,'Ava',27,'Chicago');

SELECT * FROM customers;

INSERT INTO accounts VALUES
(101,1,'Savings',15000),
(102,2,'Checking',20000),
(103,3,'Savings',30000),
(104,4,'Checking',18000),
(105,5,'Savings',25000),
(106,6,'Checking',12000),
(107,7,'Savings',35000),
(108,8,'Checking',8000),
(109,9,'Savings',22000),
(110,10,'Checking',17000);

SELECT * FROM accounts;

INSERT INTO transactions VALUES
(1001,101,1,'DEBIT',5000,'2024-01-10'),
(1002,102,2,'CREDIT',12000,'2024-01-12'),
(1003,103,3,'DEBIT',15000,'2024-01-15'),
(1004,104,4,'CREDIT',7000,'2024-01-18'),
(1005,105,5,'DEBIT',9000,'2024-01-20'),
(1006,106,6,'CREDIT',3000,'2024-01-22'),
(1007,107,7,'DEBIT',20000,'2024-01-25'),
(1008,108,8,'CREDIT',11000,'2024-01-27'),
(1009,109,9,'DEBIT',14000,'2024-01-29'),
(1010,110,10,'CREDIT',6000,'2024-02-01');

SELECT * FROM transactions;

-- 1. Display all records from customers table
SELECT * FROM customers;


-- 2. Display only customer name and city
SELECT customer_name, city
FROM customers;


-- 3. Display all records from transactions table
SELECT * FROM transactions;


-- 4. Display all unique cities
SELECT DISTINCT city
FROM customers;


-- 5. Display all unique transaction types
SELECT DISTINCT transaction_type
FROM transactions;


-- 6. Find all customers from Dallas
SELECT *
FROM customers
WHERE city = 'Dallas';


-- 7. Find all customers older than 35
SELECT *
FROM customers
WHERE age > 35;


-- 8. Find all transactions above 10000
SELECT *
FROM transactions
WHERE amount > 10000;


-- 9. Find customers from Austin whose age is greater than 30
SELECT *
FROM customers
WHERE city = 'Austin'
AND age > 30;


-- 10. Find debit transactions greater than 5000
SELECT *
FROM transactions
WHERE transaction_type = 'DEBIT'
AND amount > 5000;


-- 11. Find customers from Dallas or Houston
SELECT *
FROM customers
WHERE city = 'Dallas'
OR city = 'Houston';


-- 12. Find transactions that are either CREDIT or DEBIT
SELECT *
FROM transactions
WHERE transaction_type IN ('CREDIT','DEBIT');


-- 13. Find customers from Dallas, Austin, and Chicago
SELECT *
FROM customers
WHERE city IN ('Dallas','Austin','Chicago');


-- 14. Find customers whose age is either 25, 35, or 45
SELECT *
FROM customers
WHERE age IN (25,35,45);


-- 15. Find transactions between 5000 and 15000
SELECT *
FROM transactions
WHERE amount BETWEEN 5000 AND 15000;


-- 16. Find customers aged between 30 and 40
SELECT *
FROM customers
WHERE age BETWEEN 30 AND 40;


-- 17. Find customers whose names start with J
SELECT *
FROM customers
WHERE customer_name LIKE 'J%';


-- 18. Find customers whose names end with a
SELECT *
FROM customers
WHERE customer_name LIKE '%a';


-- 19. Find customers whose names contain letter a
SELECT *
FROM customers
WHERE customer_name LIKE '%a%';


-- 20. Find customers whose city is missing
SELECT *
FROM customers
WHERE city IS NULL;


-- 21. Display customers ordered by age ascending
SELECT *
FROM customers
ORDER BY age ASC;


-- 22. Display customers ordered by age descending
SELECT *
FROM customers
ORDER BY age DESC;


-- 23. Display transactions ordered by amount highest to lowest
SELECT *
FROM transactions
ORDER BY amount DESC;


-- 24. Aggregate Functions

-- Total number of customers
SELECT COUNT(*) AS total_customers
FROM customers;

-- Total transaction amount
SELECT SUM(amount) AS total_transaction_amount
FROM transactions;

-- Average transaction amount
SELECT AVG(amount) AS average_transaction_amount
FROM transactions;

-- Highest transaction amount
SELECT MAX(amount) AS highest_transaction_amount
FROM transactions;

-- Lowest transaction amount
SELECT MIN(amount) AS lowest_transaction_amount
FROM transactions;


-- 25(a). Count customers by city
SELECT city, COUNT(*) AS customer_count
FROM customers
GROUP BY city;


-- 25(b). Count transactions by transaction type
SELECT transaction_type, COUNT(*) AS transaction_count
FROM transactions
GROUP BY transaction_type;


-- 25(c). Total transaction amount by customer
SELECT customer_id, SUM(amount) AS total_amount
FROM transactions
GROUP BY customer_id;


-- 25(d). Average transaction amount by transaction type
SELECT transaction_type, AVG(amount) AS average_amount
FROM transactions
GROUP BY transaction_type;


-- 25(e). Highest transaction amount for each transaction type
SELECT transaction_type, MAX(amount) AS highest_amount
FROM transactions
GROUP BY transaction_type;