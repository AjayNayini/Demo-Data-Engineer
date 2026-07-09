CREATE TABLE drivers (
    driver_id INT PRIMARY KEY,
    driver_name VARCHAR(50),
    city VARCHAR(50),
    rating DECIMAL(3,2)
);


CREATE TABLE trips (
    trip_id INT PRIMARY KEY,
    driver_id INT,
    fare DECIMAL(10,2),
    trip_type VARCHAR(20),
    trip_date DATE,
    FOREIGN KEY (driver_id) REFERENCES drivers(driver_id)
);


CREATE TABLE vehicles (
    vehicle_id INT PRIMARY KEY,
    driver_id INT,
    vehicle_type VARCHAR(20),
    vehicle_year INT,
    FOREIGN KEY (driver_id) REFERENCES drivers(driver_id)
);

INSERT INTO drivers VALUES
(1,'John','Charlotte',4.80),
(2,'Maria','Atlanta',4.60),
(3,'James','Dallas',4.90),
(4,'Sophia','Charlotte',4.40),
(5,'David','Houston',4.70),
(6,'Emma','Atlanta',4.30),
(7,'Jack','Dallas',4.95),
(8,'Olivia',NULL,4.50),
(9,'Liam','Houston',4.20),
(10,'Ava','Charlotte',4.75);

INSERT INTO trips VALUES
(101,1,45,'UberX','2024-01-01'),
(102,2,60,'UberXL','2024-01-02'),
(103,3,75,'UberX','2024-01-03'),
(104,4,25,'UberGo','2024-01-04'),
(105,5,90,'UberXL','2024-01-05'),
(106,6,35,'UberGo','2024-01-06'),
(107,7,120,'UberX','2024-01-07'),
(108,8,55,'UberXL','2024-01-08'),
(109,9,40,'UberGo','2024-01-09'),
(110,10,65,'UberX','2024-01-10'),

(111,1,30,'UberGo','2024-01-11'),
(112,2,85,'UberXL','2024-01-12'),
(113,3,50,'UberX','2024-01-13'),
(114,4,20,'UberGo','2024-01-14'),
(115,5,70,'UberXL','2024-01-15'),
(116,6,45,'UberX','2024-01-16'),
(117,7,95,'UberXL','2024-01-17'),
(118,8,35,'UberGo','2024-01-18'),
(119,9,80,'UberX','2024-01-19'),
(120,10,55,'UberXL','2024-01-20'),

(121,1,100,'UberX','2024-01-21'),
(122,2,40,'UberGo','2024-01-22'),
(123,3,65,'UberXL','2024-01-23'),
(124,7,110,'UberX','2024-01-24'),
(125,10,75,'UberXL','2024-01-25');

INSERT INTO vehicles VALUES
(201,1,'Sedan',2020),
(202,2,'SUV',2021),
(203,3,'Sedan',2022),
(204,4,'Hatchback',2019),
(205,5,'SUV',2023),
(206,6,'Sedan',2020),
(207,7,'Luxury',2024),
(208,8,'SUV',2021),
(209,9,'Sedan',2018),
(210,10,'Hatchback',2022);

SELECT * FROM drivers;
SELECT * FROM trips;
SELECT * FROM vehicles;

-- 1. Display all drivers
SELECT * FROM drivers;


-- 2. Display driver name and city
SELECT driver_name, city
FROM drivers;


-- 3. Display all trips
SELECT * FROM trips;


-- 4. Display all vehicles
SELECT * FROM vehicles;


-- 5. Display unique cities
SELECT DISTINCT city
FROM drivers;


-- 6. Drivers from Charlotte
SELECT *
FROM drivers
WHERE city = 'Charlotte';


-- 7. Drivers with rating above 4.5
SELECT *
FROM drivers
WHERE rating > 4.5;


-- 8. Trips with fare above 50
SELECT *
FROM trips
WHERE fare > 50;


-- 9. Drivers from Charlotte or Atlanta
SELECT *
FROM drivers
WHERE city IN ('Charlotte','Atlanta');


-- 10. Drivers from Charlotte and rating above 4.5
SELECT *
FROM drivers
WHERE city = 'Charlotte'
AND rating > 4.5;


-- 11. Drivers from Charlotte, Atlanta and Dallas
SELECT *
FROM drivers
WHERE city IN ('Charlotte','Atlanta','Dallas');


-- 12. Trips with fare between 20 and 80
SELECT *
FROM trips
WHERE fare BETWEEN 20 AND 80;


-- 13. Drivers whose names start with J
SELECT *
FROM drivers
WHERE driver_name LIKE 'J%';


-- 14. Drivers whose city is NULL
SELECT *
FROM drivers
WHERE city IS NULL;


-- 15. Sort drivers by rating descending
SELECT *
FROM drivers
ORDER BY rating DESC;


-- 16. Sort trips by fare descending
SELECT *
FROM trips
ORDER BY fare DESC;


-- 17. Top 5 highest fare trips
SELECT *
FROM trips
ORDER BY fare DESC
LIMIT 5;


-- 18. Count drivers
SELECT COUNT(*) AS total_drivers
FROM drivers;


-- 19. Count trips
SELECT COUNT(*) AS total_trips
FROM trips;


-- 20. Total revenue
SELECT SUM(fare) AS total_revenue
FROM trips;


-- 21. Average fare
SELECT AVG(fare) AS average_fare
FROM trips;


-- 22. Highest fare
SELECT MAX(fare) AS highest_fare
FROM trips;


-- 23. Lowest fare
SELECT MIN(fare) AS lowest_fare
FROM trips;


-- 24. Driver count by city
SELECT city, COUNT(*) AS driver_count
FROM drivers
GROUP BY city;


-- 25. Trip count by trip type
SELECT trip_type, COUNT(*) AS trip_count
FROM trips
GROUP BY trip_type;


-- 26. Total revenue by driver
SELECT driver_id, SUM(fare) AS total_revenue
FROM trips
GROUP BY driver_id;


-- 27. Average fare by trip type
SELECT trip_type, AVG(fare) AS average_fare
FROM trips
GROUP BY trip_type;


-- 28. Maximum fare by trip type
SELECT trip_type, MAX(fare) AS max_fare
FROM trips
GROUP BY trip_type;


-- 29. Minimum fare by trip type
SELECT trip_type, MIN(fare) AS min_fare
FROM trips
GROUP BY trip_type;


-- 30. Drivers earning more than 200 revenue
SELECT driver_id, SUM(fare) AS revenue
FROM trips
GROUP BY driver_id
HAVING SUM(fare) > 200;


-- 31. Trip types with average fare above 40
SELECT trip_type, AVG(fare) AS average_fare
FROM trips
GROUP BY trip_type
HAVING AVG(fare) > 40;


-- 32. Driver name and fare
SELECT d.driver_name, t.fare
FROM drivers d
JOIN trips t
ON d.driver_id = t.driver_id;


-- 33. Driver name and trip type
SELECT d.driver_name, t.trip_type
FROM drivers d
JOIN trips t
ON d.driver_id = t.driver_id;


-- 34. Driver name and vehicle type
SELECT d.driver_name, v.vehicle_type
FROM drivers d
JOIN vehicles v
ON d.driver_id = v.driver_id;


-- 35. Driver name and vehicle year
SELECT d.driver_name, v.vehicle_year
FROM drivers d
JOIN vehicles v
ON d.driver_id = v.driver_id;


-- 36. Driver name, vehicle type and fare
SELECT d.driver_name,
       v.vehicle_type,
       t.fare
FROM drivers d
JOIN vehicles v
ON d.driver_id = v.driver_id
JOIN trips t
ON d.driver_id = t.driver_id;


-- 37. Create rating_bonus column
SELECT *,
rating * 10 AS rating_bonus
FROM drivers;


-- 38. Create platform_fee column
SELECT *,
fare * 0.10 AS platform_fee
FROM trips;


-- 39. Driver names uppercase
SELECT UPPER(driver_name) AS driver_name
FROM drivers;


-- 40. Driver names lowercase
SELECT LOWER(driver_name) AS driver_name
FROM drivers;


-- 41. Drivers whose names contain "a"
SELECT *
FROM drivers
WHERE driver_name LIKE '%a%';


-- 42. Count NULL values in every column
SELECT
COUNT(*) - COUNT(driver_id) AS driver_id_nulls,
COUNT(*) - COUNT(driver_name) AS driver_name_nulls,
COUNT(*) - COUNT(city) AS city_nulls,
COUNT(*) - COUNT(rating) AS rating_nulls
FROM drivers;


-- 43. Replace NULL cities with Unknown
SELECT driver_name,
COALESCE(city,'Unknown') AS city,
rating
FROM drivers;


-- 44. Remove rows containing NULL values
SELECT *
FROM drivers
WHERE driver_name IS NOT NULL
AND city IS NOT NULL
AND rating IS NOT NULL;


-- 45. Rename driver_name to name
SELECT driver_name AS name
FROM drivers;


-- 46. Display 5 random drivers
SELECT *
FROM drivers
ORDER BY RANDOM()
LIMIT 5;