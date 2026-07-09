import pandas as pd


# -------------------------
# Drivers DataFrame
# -------------------------

drivers = pd.DataFrame({
    "driver_id": [1,2,3,4,5,6,7,8,9,10],
    "driver_name": [
        "John","Maria","James","Sophia","David",
        "Emma","Jack","Olivia","Liam","Ava"
    ],
    "city": [
        "Charlotte","Atlanta","Dallas","Charlotte","Houston",
        "Atlanta","Dallas",None,"Houston","Charlotte"
    ],
    "rating": [
        4.80,4.60,4.90,4.40,4.70,
        4.30,4.95,4.50,4.20,4.75
    ]
})


# -------------------------
# Trips DataFrame
# -------------------------

trips = pd.DataFrame({
    "trip_id": [
        101,102,103,104,105,
        106,107,108,109,110,
        111,112,113,114,115,
        116,117,118,119,120,
        121,122,123,124,125
    ],

    "driver_id": [
        1,2,3,4,5,
        6,7,8,9,10,
        1,2,3,4,5,
        6,7,8,9,10,
        1,2,3,7,10
    ],

    "fare": [
        45,60,75,25,90,
        35,120,55,40,65,
        30,85,50,20,70,
        45,95,35,80,55,
        100,40,65,110,75
    ],

    "trip_type": [
        "UberX","UberXL","UberX","UberGo","UberXL",
        "UberGo","UberX","UberXL","UberGo","UberX",
        "UberGo","UberXL","UberX","UberGo","UberXL",
        "UberX","UberXL","UberGo","UberX","UberXL",
        "UberX","UberGo","UberXL","UberX","UberXL"
    ],

    "trip_date": pd.to_datetime([
        "2024-01-01","2024-01-02","2024-01-03",
        "2024-01-04","2024-01-05",
        "2024-01-06","2024-01-07","2024-01-08",
        "2024-01-09","2024-01-10",
        "2024-01-11","2024-01-12","2024-01-13",
        "2024-01-14","2024-01-15",
        "2024-01-16","2024-01-17","2024-01-18",
        "2024-01-19","2024-01-20",
        "2024-01-21","2024-01-22","2024-01-23",
        "2024-01-24","2024-01-25"
    ])
})


# -------------------------
# Vehicles DataFrame
# -------------------------

vehicles = pd.DataFrame({
    "vehicle_id": [
        201,202,203,204,205,
        206,207,208,209,210
    ],

    "driver_id": [
        1,2,3,4,5,
        6,7,8,9,10
    ],

    "vehicle_type": [
        "Sedan","SUV","Sedan","Hatchback","SUV",
        "Sedan","Luxury","SUV","Sedan","Hatchback"
    ],

    "vehicle_year": [
        2020,2021,2022,2019,2023,
        2020,2024,2021,2018,2022
    ]
})


# -------------------------
# Display DataFrames
# -------------------------

print("\nDrivers DataFrame")
print(drivers)


print("\nTrips DataFrame")
print(trips)


print("\nVehicles DataFrame")
print(vehicles)

# Answering questions


# 1. Display all drivers
print(drivers)


# 2. Display driver name and city
print(drivers[['driver_name', 'city']])


# 3. Display all trips
print(trips)


# 4. Display all vehicles
print(vehicles)


# 5. Display unique cities
print(drivers['city'].unique())


# 6. Drivers from Charlotte
print(drivers[drivers['city'] == 'Charlotte'])


# 7. Drivers with rating above 4.5
print(drivers[drivers['rating'] > 4.5])


# 8. Trips with fare above 50
print(trips[trips['fare'] > 50])


# 9. Drivers from Charlotte or Atlanta
print(drivers[drivers['city'].isin(['Charlotte','Atlanta'])])


# 10. Drivers from Charlotte and rating above 4.5
print(drivers[(drivers['city']=='Charlotte') & (drivers['rating']>4.5)])


# 11. Drivers from Charlotte, Atlanta and Dallas
print(drivers[drivers['city'].isin(['Charlotte','Atlanta','Dallas'])])


# 12. Trips with fare between 20 and 80
print(trips[trips['fare'].between(20,80)])


# 13. Drivers whose names start with J
print(drivers[drivers['driver_name'].str.startswith('J')])


# 14. Drivers whose city is null
print(drivers[drivers['city'].isnull()])


# 15. Sort drivers by rating descending
print(drivers.sort_values('rating', ascending=False))


# 16. Sort trips by fare descending
print(trips.sort_values('fare', ascending=False))


# 17. Top 5 highest fare trips
print(trips.nlargest(5,'fare'))


# 18. Count drivers
print(len(drivers))


# 19. Count trips
print(len(trips))


# 20. Total revenue
print(trips['fare'].sum())


# 21. Average fare
print(trips['fare'].mean())


# 22. Highest fare
print(trips['fare'].max())


# 23. Lowest fare
print(trips['fare'].min())


# 24. Driver count by city
print(drivers.groupby('city').size())


# 25. Trip count by trip type
print(trips.groupby('trip_type').size())


# 26. Total revenue by driver
print(trips.groupby('driver_id')['fare'].sum())


# 27. Average fare by trip type
print(trips.groupby('trip_type')['fare'].mean())


# 28. Maximum fare by trip type
print(trips.groupby('trip_type')['fare'].max())


# 29. Minimum fare by trip type
print(trips.groupby('trip_type')['fare'].min())


# 30. Drivers earning more than 200 revenue
revenue = trips.groupby('driver_id')['fare'].sum()
print(revenue[revenue > 200])


# 31. Trip types with average fare above 40
avg_fare = trips.groupby('trip_type')['fare'].mean()
print(avg_fare[avg_fare > 40])


# 32. Driver name and fare
print(drivers.merge(trips, on='driver_id')[['driver_name','fare']])


# 33. Driver name and trip type
print(drivers.merge(trips, on='driver_id')[['driver_name','trip_type']])


# 34. Driver name and vehicle type
print(drivers.merge(vehicles, on='driver_id')[['driver_name','vehicle_type']])


# 35. Driver name and vehicle year
print(drivers.merge(vehicles, on='driver_id')[['driver_name','vehicle_year']])


# 36. Driver name, vehicle type and fare
merged = drivers.merge(vehicles, on='driver_id').merge(trips, on='driver_id')
print(merged[['driver_name','vehicle_type','fare']])


# 37. Create rating_bonus column
drivers['rating_bonus'] = drivers['rating'] * 10
print(drivers)


# 38. Create platform_fee column
trips['platform_fee'] = trips['fare'] * 0.10
print(trips)


# 39. Driver names uppercase
print(drivers['driver_name'].str.upper())


# 40. Driver names lowercase
print(drivers['driver_name'].str.lower())


# 41. Drivers whose names contain "a"
print(drivers[drivers['driver_name'].str.contains('a', case=False)])


# 42. Count null values in every column
print(drivers.isnull().sum())


# 43. Replace null cities with Unknown
drivers['city'] = drivers['city'].fillna('Unknown')
print(drivers)


# 44. Remove rows containing null values
print(drivers.dropna())


# 45. Rename driver_name to name
drivers.rename(columns={'driver_name':'name'}, inplace=True)
print(drivers)


# 46. Display 5 random drivers
print(drivers.sample(5))


# 47. Export drivers DataFrame to CSV
drivers.to_csv('drivers.csv', index=False)

print("CSV exported successfully")


# 48. Read CSV back into a new DataFrame
new_drivers = pd.read_csv('drivers.csv')

print(new_drivers)