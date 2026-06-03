# Lists, Tuples, Sets & Dictionaries
# Theory Questions
## 1.
##What is the difference between:
##- List: An ordered collection that allows duplicate elements.
##- Tuple: An ordered collection that is immutable (cannot be changed).
##- Set: An unordered collection that does not allow duplicate elements.
##- Dictionary: A collection of key-value pairs, where keys are unique.
##---
## 2.
##Why are sets used in real-world systems?
##Give 3 real-time use cases.
##1. Removing duplicates from a collection of items (e.g., user IDs).
##2. Checking membership (e.g., if a user is in a list of active users).
##3. Performing mathematical set operations (e.g., finding common elements between two lists).

##---
## 3.
##What is the difference between mutable and immutable datatypes?
##Which collection types are mutable and immutable?
##---
# ==================================================
# 4. List Operations
# ==================================================

# Create a list of 5 cities
cities = ["Michigan", "London", "Tokyo", "Paris", "Sydney"]

# Print first element
print("First city:", cities[0])

# Print last element
print("Last city:", cities[-1])

# Add one new city using append()
cities.append("Dubai")

print("Updated cities list:", cities)


# ==================================================
# 5. Transaction Processing
# ==================================================

# Create a list of transaction amounts
transactions = [2500, 7000, 4500, 12000, 3000, 8500]

# Print all transactions greater than 5000
print("\nTransactions greater than 5000:")
for amount in transactions:
    if amount > 5000:
        print(amount)


# ==================================================
# 6. Tuple Operations
# ==================================================

# Create a tuple of employee IDs
employee_ids = (101, 102, 103, 104, 105)

# Print tuple length
print("\nTuple length:", len(employee_ids))

# Print second element
print("Second element:", employee_ids[1])

# Loop through tuple
print("Employee IDs:")
for emp_id in employee_ids:
    print(emp_id)


# ==================================================
# 7. Set Operations
# ==================================================

# Create a set with duplicate values
numbers = {1, 2, 3, 4, 2, 3, 5, 1}

# Print the final set
print("\nFinal set after duplicate removal:", numbers)


# ==================================================
# 8. Unique Visitors Counter
# ==================================================

# Create a set of visitor IDs
visitor_ids = {101, 102, 103, 104, 102, 101, 105}

# Print total unique visitors
print("Total unique visitors:", len(visitor_ids))


# ==================================================
# 9. Dictionary Operations
# ==================================================

# Create a dictionary for a student
student = {
    "name": "Alice",
    "age": 20,
    "course": "Python Programming"
}

# Print all values using loop
print("\nStudent Details:")
for value in student.values():
    print(value)


# ==================================================
# 10. Employee Record System
# ==================================================

# Create employee dictionary
employee = {
    "id": 101,
    "name": "John",
    "salary": 50000
}

# Update salary to 65000
employee["salary"] = 65000

# Print updated dictionary
print("\nUpdated Employee Record:")
print(employee)