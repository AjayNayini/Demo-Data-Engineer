-- Retail Analytics Assignment

-- Drop tables if they already exist
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;

-- Create Customers Table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    city VARCHAR(50),
    age INT
);

-- Create Products Table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2),
    stock INT
);

-- Create Orders Table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT,
    total_amount DECIMAL(10,2),
    order_date DATE,
    CONSTRAINT fk_customer
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    CONSTRAINT fk_product
        FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO customers VALUES
(1,'John Smith','Dallas',34),
(2,'Emily Davis','Austin',28),
(3,'Michael Johnson','Houston',45),
(4,'Sarah Wilson','Dallas',31),
(5,'David Brown','Chicago',39),
(6,'Jessica Miller','Austin',26),
(7,'Daniel Moore','Seattle',41),
(8,'Jennifer Taylor','Dallas',37),
(9,'Christopher Anderson','Miami',29),
(10,'Amanda Thomas','Boston',33),
(11,'James Jackson','Dallas',52),
(12,'Sophia White','Houston',24),
(13,'Joseph Harris','Austin',36),
(14,'Olivia Martin','Seattle',27),
(15,'William Thompson','Chicago',48);

INSERT INTO products VALUES
(101,'Laptop','Electronics',1200,15),
(102,'Smartphone','Electronics',900,30),
(103,'Tablet','Electronics',600,25),
(104,'Headphones','Electronics',150,60),
(105,'Television','Electronics',1800,10),
(106,'Office Chair','Furniture',220,35),
(107,'Office Desk','Furniture',450,20),
(108,'Sofa','Furniture',950,8),
(109,'Dining Table','Furniture',1200,5),
(110,'Coffee Maker','Home Appliances',180,18),
(111,'Microwave','Home Appliances',350,22),
(112,'Blender','Home Appliances',90,45),
(113,'Air Fryer','Home Appliances',250,19),
(114,'Washing Machine','Home Appliances',1100,12),
(115,'Refrigerator','Home Appliances',1500,9),
(116,'Running Shoes','Fashion',120,55),
(117,'Winter Jacket','Fashion',180,42),
(118,'Smart Watch','Fashion',550,16),
(119,'Backpack','Fashion',95,65),
(120,'Gaming Console','Electronics',700,14);

INSERT INTO orders VALUES
(1001,1,101,1,1200,'2024-01-05'),
(1002,2,104,2,300,'2024-01-08'),
(1003,3,105,1,1800,'2024-01-12'),
(1004,4,102,2,1800,'2024-01-15'),
(1005,5,110,3,540,'2024-01-20'),
(1006,6,116,2,240,'2024-01-22'),
(1007,7,114,1,1100,'2024-01-25'),
(1008,8,118,2,1100,'2024-02-01'),
(1009,9,111,1,350,'2024-02-05'),
(1010,10,103,3,1800,'2024-02-08'),
(1011,11,109,1,1200,'2024-02-10'),
(1012,12,112,5,450,'2024-02-14'),
(1013,13,120,2,1400,'2024-02-18'),
(1014,14,117,1,180,'2024-02-20'),
(1015,15,108,1,950,'2024-02-24'),
(1016,1,102,1,900,'2024-03-02'),
(1017,2,115,1,1500,'2024-03-05'),
(1018,3,118,1,550,'2024-03-07'),
(1019,4,113,2,500,'2024-03-09'),
(1020,5,101,1,1200,'2024-03-12'),
(1021,6,111,2,700,'2024-03-15'),
(1022,7,119,3,285,'2024-03-18'),
(1023,8,120,1,700,'2024-03-20'),
(1024,9,116,4,480,'2024-03-22'),
(1025,10,104,3,450,'2024-03-24'),
(1026,11,103,2,1200,'2024-03-28'),
(1027,12,117,2,360,'2024-04-01'),
(1028,13,105,1,1800,'2024-04-05'),
(1029,14,110,2,360,'2024-04-08'),
(1030,15,114,1,1100,'2024-04-10'),
(1031,1,118,1,550,'2024-04-12'),
(1032,2,107,1,450,'2024-04-15'),
(1033,3,102,1,900,'2024-04-18'),
(1034,4,101,2,2400,'2024-04-20'),
(1035,5,119,5,475,'2024-04-22'),
(1036,6,112,2,180,'2024-04-25'),
(1037,7,108,1,950,'2024-04-27'),
(1038,8,115,1,1500,'2024-04-29'),
(1039,9,120,2,1400,'2024-05-02'),
(1040,10,106,2,440,'2024-05-05');


/*=============================================================
 PART 2 : DATA EXPLORATION
=============================================================*/

-- 1. Display all customers

SELECT *
FROM customers;


-- 2. Display all products

SELECT *
FROM products;


-- 3. Display all orders

SELECT *
FROM orders;


-- 4. Display customer names and cities

SELECT
    customer_name,
    city
FROM customers;


-- 5. Display product names and prices

SELECT
    product_name,
    price
FROM products;


-- 6. Find all unique cities

SELECT DISTINCT city
FROM customers
ORDER BY city;


-- 7. Find all unique product categories

SELECT DISTINCT category
FROM products
ORDER BY category;



/*=============================================================
 PART 3 : FILTERING
=============================================================*/

-- 8. Customers from Dallas

SELECT *
FROM customers
WHERE city = 'Dallas';


-- 9. Customers older than 30

SELECT *
FROM customers
WHERE age > 30;


-- 10. Products costing more than $500

SELECT *
FROM products
WHERE price > 500;


-- 11. Products with stock less than 20

SELECT *
FROM products
WHERE stock < 20;


-- 12. Orders above $1000

SELECT *
FROM orders
WHERE total_amount > 1000;


-- 13. Customers from Dallas and age greater than 30

SELECT *
FROM customers
WHERE city = 'Dallas'
  AND age > 30;


-- 14. Customers from Dallas or Austin

SELECT *
FROM customers
WHERE city IN ('Dallas', 'Austin');


-- 15. Products belonging to Electronics

SELECT *
FROM products
WHERE category = 'Electronics';


-- 16. Orders placed between two dates

SELECT *
FROM orders
WHERE order_date BETWEEN '2024-02-01' AND '2024-03-31';


-- 17. Customers whose names start with 'J'

SELECT *
FROM customers
WHERE customer_name LIKE 'J%';



/*=============================================================
 PART 4 : SORTING
=============================================================*/

-- 18. Sort customers by age (Ascending)

SELECT *
FROM customers
ORDER BY age ASC;


-- 19. Sort products by price (Descending)

SELECT *
FROM products
ORDER BY price DESC;


-- 20. Sort orders by total amount (Descending)

SELECT *
FROM orders
ORDER BY total_amount DESC;


-- 21. Display the top 5 expensive products

SELECT *
FROM products
ORDER BY price DESC
LIMIT 5;


-- 22. Display the top 5 highest-value orders

SELECT *
FROM orders
ORDER BY total_amount DESC
LIMIT 5;


/*====================================================
 PART 5 - AGGREGATIONS
====================================================*/


-- 23. Count customers
SELECT COUNT(*) AS total_customers
FROM customers;


-- 24. Count products
SELECT COUNT(*) AS total_products
FROM products;


-- 25. Count orders
SELECT COUNT(*) AS total_orders
FROM orders;


-- 26. Total sales
SELECT SUM(total_amount) AS total_sales
FROM orders;


-- 27. Average order value
SELECT AVG(total_amount) AS avg_order_value
FROM orders;


-- 28. Maximum order
SELECT MAX(total_amount) AS max_order
FROM orders;


-- 29. Minimum order
SELECT MIN(total_amount) AS min_order
FROM orders;


-- 30. Average product price
SELECT AVG(price) AS avg_product_price
FROM products;



/*====================================================
 PART 6 - GROUP BY
====================================================*/


-- 31. Customer count by city
SELECT city,
COUNT(*) AS customer_count
FROM customers
GROUP BY city;


-- 32. Product count by category
SELECT category,
COUNT(*) AS product_count
FROM products
GROUP BY category;


-- 33. Total sales by customer
SELECT c.customer_name,
SUM(o.total_amount) AS total_sales
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
GROUP BY c.customer_name;


-- 34. Total sales by product
SELECT p.product_name,
SUM(o.total_amount) AS total_sales
FROM products p
JOIN orders o
ON p.product_id=o.product_id
GROUP BY p.product_name;


-- 35. Total sales by category
SELECT p.category,
SUM(o.total_amount) AS total_sales
FROM products p
JOIN orders o
ON p.product_id=o.product_id
GROUP BY p.category;


-- 36. Average order value by city
SELECT c.city,
AVG(o.total_amount) AS avg_order_value
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
GROUP BY c.city;


-- 37. Maximum order amount by city
SELECT c.city,
MAX(o.total_amount) AS max_order
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
GROUP BY c.city;


-- 38. Total quantity sold by product
SELECT p.product_name,
SUM(o.quantity) AS total_quantity
FROM products p
JOIN orders o
ON p.product_id=o.product_id
GROUP BY p.product_name;



/*====================================================
 PART 7 - JOINS
====================================================*/


-- 39. Customer name and order amount
SELECT c.customer_name,
o.total_amount
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id;


-- 40. Customer name and product purchased
SELECT c.customer_name,
p.product_name
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
JOIN products p
ON o.product_id=p.product_id;


-- 41. Customer, product, quantity, amount
SELECT 
c.customer_name,
p.product_name,
o.quantity,
o.total_amount
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
JOIN products p
ON o.product_id=p.product_id;


-- 42. Customer city product category amount
SELECT
c.customer_name,
c.city,
p.product_name,
p.category,
o.total_amount
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
JOIN products p
ON o.product_id=p.product_id;


-- 43. Complete sales report

SELECT
c.customer_name,
c.city,
p.product_name,
p.category,
p.price,
o.quantity,
o.total_amount,
o.order_date
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
JOIN products p
ON o.product_id=p.product_id;



/*====================================================
 PART 8 - BUSINESS ANALYTICS
====================================================*/


-- 44. Top 5 customers by spending

SELECT
c.customer_name,
SUM(o.total_amount) AS spending
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
GROUP BY c.customer_name
ORDER BY spending DESC
LIMIT 5;


-- 45. Top 5 best selling products

SELECT
p.product_name,
SUM(o.quantity) AS units_sold
FROM products p
JOIN orders o
ON p.product_id=o.product_id
GROUP BY p.product_name
ORDER BY units_sold DESC
LIMIT 5;


-- 46. Revenue by city

SELECT
c.city,
SUM(o.total_amount) AS revenue
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
GROUP BY c.city;


-- 47. Revenue by category

SELECT
p.category,
SUM(o.total_amount) AS revenue
FROM products p
JOIN orders o
ON p.product_id=o.product_id
GROUP BY p.category;


-- 48. Highest single order customer

SELECT
c.customer_name,
o.total_amount
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
ORDER BY o.total_amount DESC
LIMIT 1;


-- 49. Customers with multiple orders

SELECT
customer_id,
COUNT(order_id) AS order_count
FROM orders
GROUP BY customer_id
HAVING COUNT(order_id)>1;


-- 50. Products never sold

SELECT p.*
FROM products p
LEFT JOIN orders o
ON p.product_id=o.product_id
WHERE o.product_id IS NULL;


-- 51. Categories sales > 10000

SELECT
p.category,
SUM(o.total_amount) AS sales
FROM products p
JOIN orders o
ON p.product_id=o.product_id
GROUP BY p.category
HAVING SUM(o.total_amount)>10000;


-- 52. Cities sales > 20000

SELECT
c.city,
SUM(o.total_amount) AS sales
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
GROUP BY c.city
HAVING SUM(o.total_amount)>20000;



/*====================================================
 PART 10 - FINAL REPORTING
====================================================*/


-- Final Analytics Dataset

CREATE VIEW sales_report AS

SELECT
c.customer_name,
c.city,
p.product_name,
p.category,
p.price,
o.quantity,
o.total_amount,
o.order_date

FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id

JOIN products p
ON o.product_id=p.product_id;



-- 1. Highest spending customer

SELECT customer_name,
SUM(total_amount) AS spending
FROM sales_report
GROUP BY customer_name
ORDER BY spending DESC
LIMIT 1;



-- 2. Highest revenue city

SELECT city,
SUM(total_amount) revenue
FROM sales_report
GROUP BY city
ORDER BY revenue DESC
LIMIT 1;



-- 3. Highest sales category

SELECT category,
SUM(total_amount) sales
FROM sales_report
GROUP BY category
ORDER BY sales DESC
LIMIT 1;



-- 4. Product sold most units

SELECT product_name,
SUM(quantity) units
FROM sales_report
GROUP BY product_name
ORDER BY units DESC
LIMIT 1;



-- 5. Products highest revenue

SELECT product_name,
SUM(total_amount) revenue
FROM sales_report
GROUP BY product_name
ORDER BY revenue DESC;



-- 6. Customers with multiple orders

SELECT customer_name,
COUNT(*) orders
FROM sales_report
GROUP BY customer_name
HAVING COUNT(*)>1;



-- 7. Average order value

SELECT AVG(total_amount)
FROM sales_report;



-- 8. Products never purchased

SELECT *
FROM products
WHERE product_id NOT IN
(
SELECT product_id
FROM orders
);



-- 9. Top 10 Customer Report

SELECT
customer_name,
SUM(total_amount) revenue
FROM sales_report
GROUP BY customer_name
ORDER BY revenue DESC
LIMIT 10;



-- 10. Top 10 Product Report

SELECT
product_name,
SUM(total_amount) revenue
FROM sales_report
GROUP BY product_name
ORDER BY revenue DESC
LIMIT 10;



-- 11. Revenue by City Report

SELECT
city,
SUM(total_amount) revenue
FROM sales_report
GROUP BY city;



-- 12. Revenue by Category Report

SELECT
category,
SUM(total_amount) revenue
FROM sales_report
GROUP BY category;