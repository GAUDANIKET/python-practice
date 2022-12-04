import pandas as pd

# Check all pandas function on pynative website
dr = pd.read_csv(r'C:\Users\gauda\Downloads\Automobile_data.csv')

# Clean the dataset and update the CSV file
new_dr = dr.dropna()
# print(new_dr)

# From the given dataset print the first and last five rows
# print(new_dr.tail())
# print(new_dr.head())

# columns of dataset
# print(new_dr.columns)

# Find the most expensive car company name
new_dr = new_dr[['company','price']][new_dr.price==new_dr['price'].max()]
print(new_dr)

# Print All Jaguar Cars details
car_manufacture = dr.groupby('company')
jaguardf = car_manufacture.get_group('jaguar')
print(jaguardf)

# Count total cars per company
print(dr['company'].value_counts())


# Find each company’s Highest price car
price = dr.groupby('company')
maxprice = price['company','price'].max()
print(maxprice)

# Find the average mileage of each car making company
mileage = dr.groupby('company')
average_mileage = mileage['company','average-mileage'].mean()
print(average_mileage)


