
# RETAIL ANALYTICS CASE STUDY - PYSPARK


from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window


# Create Spark Session

spark = SparkSession.builder \
    .appName("RetailAnalytics") \
    .getOrCreate()




# PART 1 - CREATE DATASETS



# CUSTOMERS 

customers_data = [

(1,"John Smith","Dallas",34),
(2,"Emily Davis","Austin",28),
(3,"Michael Johnson","Houston",45),
(4,"Sarah Wilson","Dallas",31),
(5,"David Brown","Chicago",39),
(6,"Jessica Miller","Austin",26),
(7,"Daniel Moore","Seattle",41),
(8,"Jennifer Taylor","Dallas",37),
(9,"Christopher Anderson","Miami",29),
(10,"Amanda Thomas","Boston",33),
(11,"James Jackson","Dallas",52),
(12,"Sophia White","Houston",24),
(13,"Joseph Harris","Austin",36),
(14,"Olivia Martin","Seattle",27),
(15,"William Thompson","Chicago",48)

]


customers_schema = StructType([

StructField("customer_id",IntegerType()),
StructField("customer_name",StringType()),
StructField("city",StringType()),
StructField("age",IntegerType())

])


customers = spark.createDataFrame(
    customers_data,
    customers_schema
)



# ---------------- PRODUCTS ----------------


products_data = [

(101,"Laptop","Electronics",1200,15),
(102,"Smartphone","Electronics",900,30),
(103,"Tablet","Electronics",600,25),
(104,"Headphones","Electronics",150,60),
(105,"Television","Electronics",1800,10),
(106,"Office Chair","Furniture",220,35),
(107,"Office Desk","Furniture",450,20),
(108,"Sofa","Furniture",950,8),
(109,"Dining Table","Furniture",1200,5),
(110,"Coffee Maker","Home Appliances",180,18),
(111,"Microwave","Home Appliances",350,22),
(112,"Blender","Home Appliances",90,45),
(113,"Air Fryer","Home Appliances",250,19),
(114,"Washing Machine","Home Appliances",1100,12),
(115,"Refrigerator","Home Appliances",1500,9),
(116,"Running Shoes","Fashion",120,55),
(117,"Winter Jacket","Fashion",180,42),
(118,"Smart Watch","Fashion",550,16),
(119,"Backpack","Fashion",95,65),
(120,"Gaming Console","Electronics",700,14)

]


products_schema = StructType([

StructField("product_id",IntegerType()),
StructField("product_name",StringType()),
StructField("category",StringType()),
StructField("price",IntegerType()),
StructField("stock",IntegerType())

])


products = spark.createDataFrame(
    products_data,
    products_schema
)



#ORDERS 


orders_data = [

(1001,1,101,1,1200,"2024-01-05"),
(1002,2,104,2,300,"2024-01-08"),
(1003,3,105,1,1800,"2024-01-12"),
(1004,4,102,2,1800,"2024-01-15"),
(1005,5,110,3,540,"2024-01-20"),

(1006,6,116,2,240,"2024-01-22"),
(1007,7,114,1,1100,"2024-01-25"),
(1008,8,118,2,1100,"2024-02-01"),
(1009,9,111,1,350,"2024-02-05"),
(1010,10,103,3,1800,"2024-02-08"),

(1011,11,109,1,1200,"2024-02-10"),
(1012,12,112,5,450,"2024-02-14"),
(1013,13,120,2,1400,"2024-02-18"),
(1014,14,117,1,180,"2024-02-20"),
(1015,15,108,1,950,"2024-02-24"),

(1016,1,102,1,900,"2024-03-02"),
(1017,2,115,1,1500,"2024-03-05"),
(1018,3,118,1,550,"2024-03-07"),
(1019,4,113,2,500,"2024-03-09"),
(1020,5,101,1,1200,"2024-03-12"),

(1021,6,111,2,700,"2024-03-15"),
(1022,7,119,3,285,"2024-03-18"),
(1023,8,120,1,700,"2024-03-20"),
(1024,9,116,4,480,"2024-03-22"),
(1025,10,104,3,450,"2024-03-24"),

(1026,11,103,2,1200,"2024-03-28"),
(1027,12,117,2,360,"2024-04-01"),
(1028,13,105,1,1800,"2024-04-05"),
(1029,14,110,2,360,"2024-04-08"),
(1030,15,114,1,1100,"2024-04-10"),

(1031,1,118,1,550,"2024-04-12"),
(1032,2,107,1,450,"2024-04-15"),
(1033,3,102,1,900,"2024-04-18"),
(1034,4,101,2,2400,"2024-04-20"),
(1035,5,119,5,475,"2024-04-22"),

(1036,6,112,2,180,"2024-04-25"),
(1037,7,108,1,950,"2024-04-27"),
(1038,8,115,1,1500,"2024-04-29"),
(1039,9,120,2,1400,"2024-05-02"),
(1040,10,106,2,440,"2024-05-05")

]


orders_schema = StructType([

StructField("order_id",IntegerType()),
StructField("customer_id",IntegerType()),
StructField("product_id",IntegerType()),
StructField("quantity",IntegerType()),
StructField("total_amount",IntegerType()),
StructField("order_date",StringType())

])


orders = spark.createDataFrame(
    orders_data,
    orders_schema
)


orders = orders.withColumn(
    "order_date",
    to_date("order_date")
)




# PART 2 - DATA EXPLORATION



# 1
customers.show()


# 2
products.show()


# 3
orders.show()


# 4
customers.select(
    "customer_name",
    "city"
).show()


# 5
products.select(
    "product_name",
    "price"
).show()


# 6
customers.select(
    "city"
).distinct().show()


# 7
products.select(
    "category"
).distinct().show()




# PART 3 - FILTERING



# 8
customers.filter(
    col("city")=="Dallas"
).show()


# 9
customers.filter(
    col("age")>30
).show()


# 10
products.filter(
    col("price")>500
).show()


# 11
products.filter(
    col("stock")<20
).show()


# 12
orders.filter(
    col("total_amount")>1000
).show()


# 13
customers.filter(
    (col("city")=="Dallas") &
    (col("age")>30)
).show()


# 14
customers.filter(
    col("city").isin("Dallas","Austin")
).show()


# 15
products.filter(
    col("category")=="Electronics"
).show()


# 16
orders.filter(
    (col("order_date")>="2024-02-01") &
    (col("order_date")<="2024-03-31")
).show()


# 17
customers.filter(
    col("customer_name").startswith("J")
).show()




# PART 4 - SORTING



# 18
customers.orderBy(
    "age"
).show()


# 19
products.orderBy(
    col("price").desc()
).show()


# 20
orders.orderBy(
    col("total_amount").desc()
).show()


# 21
products.orderBy(
    col("price").desc()
).limit(5).show()


# 22
orders.orderBy(
    col("total_amount").desc()
).limit(5).show()



# PART 5 - AGGREGATIONS


# 23
customers.count()


# 24
products.count()


# 25
orders.count()


# 26
orders.select(
    sum("total_amount")
).show()


# 27
orders.select(
    avg("total_amount")
).show()


# 28
orders.select(
    max("total_amount")
).show()


# 29
orders.select(
    min("total_amount")
).show()


# 30
products.select(
    avg("price")
).show()




# PART 6 - GROUP BY



# 31
customers.groupBy(
    "city"
).count().show()


# 32
products.groupBy(
    "category"
).count().show()


# 33
orders.groupBy(
    "customer_id"
).agg(
    sum("total_amount")
).show()


# 34
orders.groupBy(
    "product_id"
).agg(
    sum("total_amount")
).show()


# 35
orders.join(
    products,
    "product_id"
).groupBy(
    "category"
).agg(
    sum("total_amount")
).show()


# 36
orders.join(
    customers,
    "customer_id"
).groupBy(
    "city"
).agg(
    avg("total_amount")
).show()


# 37
orders.join(
    customers,
    "customer_id"
).groupBy(
    "city"
).agg(
    max("total_amount")
).show()


# 38
orders.groupBy(
    "product_id"
).agg(
    sum("quantity")
).show()




# PART 7 - JOINS



sales_report = (
    customers
    .join(orders,"customer_id")
    .join(products,"product_id")
)


# 39
sales_report.select(
    "customer_name",
    "total_amount"
).show()


# 40
sales_report.select(
    "customer_name",
    "product_name"
).show()


# 41
sales_report.select(
    "customer_name",
    "product_name",
    "quantity",
    "total_amount"
).show()


# 42
sales_report.select(
    "customer_name",
    "city",
    "product_name",
    "category",
    "total_amount"
).show()


# 43
sales_report.show()




# PART 8 - BUSINESS ANALYTICS


# 44
sales_report.groupBy(
    "customer_name"
).agg(
    sum("total_amount").alias("spending")
).orderBy(
    col("spending").desc()
).limit(5).show()


# 45
sales_report.groupBy(
    "product_name"
).agg(
    sum("quantity").alias("units")
).orderBy(
    col("units").desc()
).limit(5).show()


# 46
sales_report.groupBy(
    "city"
).agg(
    sum("total_amount")
).show()


# 47
sales_report.groupBy(
    "category"
).agg(
    sum("total_amount")
).show()


# 48
sales_report.orderBy(
    col("total_amount").desc()
).limit(1).show()


# 49
sales_report.groupBy(
    "customer_name"
).count().filter(
    col("count")>1
).show()


# 50
products.join(
    orders,
    "product_id",
    "left_anti"
).show()


# 51
sales_report.groupBy(
    "category"
).agg(
    sum("total_amount").alias("sales")
).filter(
    col("sales")>10000
).show()


# 52
sales_report.groupBy(
    "city"
).agg(
    sum("total_amount").alias("sales")
).filter(
    col("sales")>20000
).show()


# PART 9 - PYSPARK ONLY OPERATIONS



# 53. Create discount column (10% of price)

products = products.withColumn(
    "discount",
    col("price") * 0.10
)

products.show()



# 54. Create tax column (5% of total_amount)

orders = orders.withColumn(
    "tax",
    col("total_amount") * 0.05
)

orders.show()



# 55. Create final_amount column

orders = orders.withColumn(
    "final_amount",
    col("total_amount") + col("tax")
)

orders.show()



# 56. Rename customer_name to name

customers = customers.withColumnRenamed(
    "customer_name",
    "name"
)

customers.show()



# 57. Convert names to uppercase

customers = customers.withColumn(
    "name_upper",
    upper(col("name"))
)

customers.show()



# 58. Convert names to lowercase

customers = customers.withColumn(
    "name_lower",
    lower(col("name"))
)

customers.show()



# 59. Replace missing city values with Unknown

customers = customers.fillna(
    {
        "city":"Unknown"
    }
)

customers.show()



# 60. Remove duplicate customer records

customers = customers.dropDuplicates()

customers.show()



# 61. Display 5 random orders

orders.sample(
    False,
    0.125
).show(5)




# PART 10 - FINAL REPORTING


# Create final analytics dataset

final_report = (

    orders
    .join(
        customers,
        "customer_id"
    )
    .join(
        products,
        "product_id"
    )

)



final_report = final_report.select(

    col("name").alias("Customer_Name"),
    col("city"),
    col("product_name"),
    col("category"),
    col("price"),
    col("quantity"),
    col("total_amount"),
    col("order_date")

)



print("FINAL SALES REPORT")

final_report.show()




# FINAL QUESTIONS


# 1. Highest spending customer

print("1. Highest Spending Customer")

final_report.groupBy(
    "Customer_Name"
).agg(
    sum("total_amount").alias("spending")
).orderBy(
    col("spending").desc()
).limit(1).show()



# 2. Highest revenue city

print("2. Highest Revenue City")

final_report.groupBy(
    "city"
).agg(
    sum("total_amount").alias("revenue")
).orderBy(
    col("revenue").desc()
).limit(1).show()



# 3. Highest sales category

print("3. Highest Sales Category")

final_report.groupBy(
    "category"
).agg(
    sum("total_amount").alias("sales")
).orderBy(
    col("sales").desc()
).limit(1).show()



# 4. Product sold most units

print("4. Most Sold Product")

final_report.groupBy(
    "product_name"
).agg(
    sum("quantity").alias("units")
).orderBy(
    col("units").desc()
).limit(1).show()



# 5. Products highest revenue

print("5. Highest Revenue Products")

final_report.groupBy(
    "product_name"
).agg(
    sum("total_amount").alias("revenue")
).orderBy(
    col("revenue").desc()
).show()



# 6. Customers placed multiple orders

print("6. Multiple Order Customers")

final_report.groupBy(
    "Customer_Name"
).count().filter(
    col("count")>1
).show()



# 7. Average order value

print("7. Average Order Value")

final_report.select(
    avg("total_amount")
).show()



# 8. Products never purchased

print("8. Products Never Purchased")

products.join(
    orders,
    "product_id",
    "left_anti"
).show()



# 9. Top 10 Customers Report

print("9. Top 10 Customers Report")

top10_customers = (

    final_report
    .groupBy("Customer_Name")
    .agg(
        sum("total_amount")
        .alias("revenue")
    )
    .orderBy(
        col("revenue").desc()
    )
    .limit(10)

)

top10_customers.show()



# 10. Top 10 Products Report

print("10. Top 10 Products Report")

top10_products = (

    final_report
    .groupBy("product_name")
    .agg(
        sum("total_amount")
        .alias("revenue")
    )
    .orderBy(
        col("revenue").desc()
    )
    .limit(10)

)

top10_products.show()



# 11. Revenue by City Report

print("11. Revenue By City")

revenue_city = (

    final_report
    .groupBy("city")
    .agg(
        sum("total_amount")
        .alias("revenue")
    )

)

revenue_city.show()



# 12. Revenue by Category Report

print("12. Revenue By Category")

revenue_category = (

    final_report
    .groupBy("category")
    .agg(
        sum("total_amount")
        .alias("revenue")
    )

)

revenue_category.show()





# Export final report to CSV

final_report.toPandas().to_csv(
    "final_sales_report.csv",
    index=False
)

print("final_sales_report.csv exported successfully")

# Stop Spark

spark.stop()