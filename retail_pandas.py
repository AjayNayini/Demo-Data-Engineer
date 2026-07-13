
# RETAIL ANALYTICS CASE STUDY - PANDAS


import pandas as pd


# PART 1 - CREATE DATASETS

# Customers

customers = pd.DataFrame({

    "customer_id":[
        1,2,3,4,5,
        6,7,8,9,10,
        11,12,13,14,15
    ],

    "customer_name":[
        "John Smith",
        "Emily Davis",
        "Michael Johnson",
        "Sarah Wilson",
        "David Brown",
        "Jessica Miller",
        "Daniel Moore",
        "Jennifer Taylor",
        "Christopher Anderson",
        "Amanda Thomas",
        "James Jackson",
        "Sophia White",
        "Joseph Harris",
        "Olivia Martin",
        "William Thompson"
    ],

    "city":[
        "Dallas",
        "Austin",
        "Houston",
        "Dallas",
        "Chicago",
        "Austin",
        "Seattle",
        "Dallas",
        "Miami",
        "Boston",
        "Dallas",
        "Houston",
        "Austin",
        "Seattle",
        "Chicago"
    ],

    "age":[
        34,28,45,31,39,
        26,41,37,29,33,
        52,24,36,27,48
    ]

})


# Products

products = pd.DataFrame({

    "product_id":range(101,121),

    "product_name":[
        "Laptop",
        "Smartphone",
        "Tablet",
        "Headphones",
        "Television",
        "Office Chair",
        "Office Desk",
        "Sofa",
        "Dining Table",
        "Coffee Maker",
        "Microwave",
        "Blender",
        "Air Fryer",
        "Washing Machine",
        "Refrigerator",
        "Running Shoes",
        "Winter Jacket",
        "Smart Watch",
        "Backpack",
        "Gaming Console"
    ],

    "category":[
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics",
        "Furniture",
        "Furniture",
        "Furniture",
        "Furniture",
        "Home Appliances",
        "Home Appliances",
        "Home Appliances",
        "Home Appliances",
        "Home Appliances",
        "Home Appliances",
        "Fashion",
        "Fashion",
        "Fashion",
        "Fashion",
        "Electronics"
    ],

    "price":[
        1200,900,600,150,1800,
        220,450,950,1200,
        180,350,90,250,1100,1500,
        120,180,550,95,
        700
    ],

    "stock":[
        15,30,25,60,10,
        35,20,8,5,
        18,22,45,19,12,9,
        55,42,16,65,
        14
    ]

})


# Orders

orders = pd.DataFrame([

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

],
columns=[
    "order_id",
    "customer_id",
    "product_id",
    "quantity",
    "total_amount",
    "order_date"
])


orders["order_date"] = pd.to_datetime(
    orders["order_date"]
)



# PART 2 - EXPLORATION


print(customers)

print(products)

print(orders)

print(customers[[
    "customer_name",
    "city"
]])

print(products[[
    "product_name",
    "price"
]])

print(customers["city"].unique())

print(products["category"].unique())




# PART 3 - FILTERING


print(customers[customers.city=="Dallas"])

print(customers[customers.age>30])

print(products[products.price>500])

print(products[products.stock<20])

print(orders[orders.total_amount>1000])

print(
customers[
(customers.city=="Dallas") &
(customers.age>30)
])

print(
customers[
customers.city.isin(["Dallas","Austin"])
])

print(
products[
products.category=="Electronics"
])

print(
orders[
(orders.order_date>="2024-02-01") &
(orders.order_date<="2024-03-31")
])

print(
customers[
customers.customer_name.str.startswith("J")
])




# PART 4 - SORTING


print(customers.sort_values("age"))

print(products.sort_values(
    "price",
    ascending=False
))

print(orders.sort_values(
    "total_amount",
    ascending=False
))

print(products.nlargest(5,"price"))

print(orders.nlargest(5,"total_amount"))




# PART 5 - AGGREGATIONS


print(customers.count())

print(products.count())

print(orders.count())

print(orders.total_amount.sum())

print(orders.total_amount.mean())

print(orders.total_amount.max())

print(orders.total_amount.min())

print(products.price.mean())



# PART 6 - GROUP BY


print(
customers.groupby("city")
.customer_id.count()
)

print(
products.groupby("category")
.product_id.count()
)

print(
orders.groupby("customer_id")
.total_amount.sum()
)

print(
orders.groupby("product_id")
.total_amount.sum()
)

sales = orders.merge(
    products,
    on="product_id"
)

print(
sales.groupby("category")
.total_amount.sum()
)


city_sales = orders.merge(
    customers,
    on="customer_id"
)

print(
city_sales.groupby("city")
.total_amount.mean()
)

print(
city_sales.groupby("city")
.total_amount.max()
)

print(
orders.groupby("product_id")
.quantity.sum()
)




# PART 7 - JOINS


sales_report = (
orders
.merge(customers,on="customer_id")
.merge(products,on="product_id")
)


print(
sales_report[[
"customer_name",
"total_amount"
]]
)


print(
sales_report[[
"customer_name",
"product_name"
]]
)


print(
sales_report[[
"customer_name",
"product_name",
"quantity",
"total_amount"
]]
)


print(
sales_report[[
"customer_name",
"city",
"product_name",
"category",
"total_amount"
]]
)


print(sales_report)




# PART 8 - BUSINESS ANALYTICS


print(
sales_report.groupby("customer_name")
.total_amount.sum()
.sort_values(ascending=False)
.head(5)
)


print(
sales_report.groupby("product_name")
.quantity.sum()
.sort_values(ascending=False)
.head(5)
)


print(
sales_report.groupby("city")
.total_amount.sum()
)


print(
sales_report.groupby("category")
.total_amount.sum()
)


print(
sales_report.loc[
sales_report.total_amount.idxmax(),
[
"customer_name",
"total_amount"
]
]
)


print(
sales_report.groupby("customer_name")
.size()
[
lambda x:x>1
]
)


print(
products[
~products.product_id.isin(
sales_report.product_id.unique()
)
]
)


print(
sales_report.groupby("category")
.total_amount.sum()
[
lambda x:x>10000
]
)


print(
sales_report.groupby("city")
.total_amount.sum()
[
lambda x:x>20000
]
)


# PART 9 - PANDAS ONLY OPERATIONS



# 53. Create discount column (10% of price)

products["discount"] = products["price"] * 0.10

print("\n53. Discount")
print(products)



# 54. Create tax column (5% of total_amount)

orders["tax"] = orders["total_amount"] * 0.05

print("\n54. Tax")
print(orders)



# 55. Create final_amount column

orders["final_amount"] = (
    orders["total_amount"] +
    orders["tax"]
)

print("\n55. Final Amount")
print(orders)



# 56. Rename customer_name to name

customers.rename(
    columns={
        "customer_name":"name"
    },
    inplace=True
)

print("\n56. Rename Column")
print(customers)



# 57. Convert customer names to uppercase

customers["name_upper"] = (
    customers["name"]
    .str.upper()
)

print("\n57. Uppercase Names")
print(customers)



# 58. Convert customer names to lowercase

customers["name_lower"] = (
    customers["name"]
    .str.lower()
)

print("\n58. Lowercase Names")
print(customers)



# 59. Replace missing city values

customers["city"] = (
    customers["city"]
    .fillna("Unknown")
)

print("\n59. Missing City Updated")
print(customers)



# 60. Remove duplicate customer records

customers = (
    customers
    .drop_duplicates()
)

print("\n60. Duplicate Records Removed")
print(customers)



# 61. Display 5 random orders

print("\n61. Random Orders")

print(
    orders.sample(5)
)




# PART 10 - FINAL REPORTING



# Create final analytics dataset

final_report = (
    orders
    .merge(
        customers,
        on="customer_id"
    )
    .merge(
        products,
        on="product_id"
    )
)


final_report = final_report[
[
    "name",
    "city",
    "product_name",
    "category",
    "price",
    "quantity",
    "total_amount",
    "order_date"
]
]


print("\nFINAL SALES REPORT")

print(final_report)




# FINAL QUESTIONS



# 1. Highest spending customer

print("\n1. Highest Spending Customer")

print(
    final_report
    .groupby("name")
    ["total_amount"]
    .sum()
    .sort_values(
        ascending=False
    )
    .head(1)
)



# 2. Highest revenue city

print("\n2. Highest Revenue City")

print(
    final_report
    .groupby("city")
    ["total_amount"]
    .sum()
    .sort_values(
        ascending=False
    )
    .head(1)
)



# 3. Highest sales category

print("\n3. Highest Sales Category")

print(
    final_report
    .groupby("category")
    ["total_amount"]
    .sum()
    .sort_values(
        ascending=False
    )
    .head(1)
)



# 4. Product sold most units

print("\n4. Most Sold Product")

print(
    final_report
    .groupby("product_name")
    ["quantity"]
    .sum()
    .sort_values(
        ascending=False
    )
    .head(1)
)



# 5. Products generating highest revenue

print("\n5. Product Revenue")

print(
    final_report
    .groupby("product_name")
    ["total_amount"]
    .sum()
    .sort_values(
        ascending=False
    )
)



# 6. Customers with multiple orders

print("\n6. Multiple Order Customers")

print(
    final_report
    .groupby("name")
    .size()
    [
        lambda x:x>1
    ]
)



# 7. Average order value

print("\n7. Average Order Value")

print(
    final_report["total_amount"]
    .mean()
)



# 8. Products never purchased

print("\n8. Products Never Purchased")

purchased_products = (
    final_report["product_name"]
    .unique()
)


print(
    products[
        ~products["product_name"]
        .isin(purchased_products)
    ]
)



# 9. Top 10 Customers Report

print("\n9. Top 10 Customers")

top10_customers = (
    final_report
    .groupby("name")
    ["total_amount"]
    .sum()
    .sort_values(
        ascending=False
    )
    .head(10)
)

print(top10_customers)



# 10. Top 10 Products Report

print("\n10. Top 10 Products")

top10_products = (
    final_report
    .groupby("product_name")
    ["total_amount"]
    .sum()
    .sort_values(
        ascending=False
    )
    .head(10)
)

print(top10_products)



# 11. Revenue by City Report

print("\n11. Revenue By City")

revenue_city = (
    final_report
    .groupby("city")
    ["total_amount"]
    .sum()
)

print(revenue_city)



# 12. Revenue by Category Report

print("\n12. Revenue By Category")

revenue_category = (
    final_report
    .groupby("category")
    ["total_amount"]
    .sum()
)

print(revenue_category)



# 62. EXPORT FINAL SALES REPORT TO CSV



final_report.to_csv(
    "final_sales_report.csv",
    index=False
)


print(
    "\nfinal_sales_report.csv exported successfully"
)