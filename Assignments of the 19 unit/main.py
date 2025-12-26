import pandas as pd

data = pd.read_csv("Workout.csv")

# Convert the data to dictionary.
print(data.to_dict())

# Convert the 'day' column to list.
print(data["day"].to_list())

# Calculate the mean of the 'calories' column.
# The classic methode:
calories = data.burned_calories.to_list()
sum_of_calories = sum(calories)
long_of_calories = len(calories)
print(sum_of_calories / long_of_calories)
# Use the function in pandas:
print(data["burned_calories"].mean())

# Create a DataFrame about sales using ChatGPT.
sales = pd.read_csv("sales.csv")

print(sales.payment_method.mode())
print(sales.payment_method.value_counts())
#todo-> We observe two payment_methodes repet (Credit Card: 6   and    Mobile Payment: 6 )

rabat_data = sales[sales["location"] == "Rabat"].reset_index(drop=True)
rabat_sales = rabat_data.sales.sum()
print(rabat_data)
print(rabat_sales)
#todo-> We select the 'Rabat' city and his sum equal 8200.

# We group by location
grouped = sales.groupby(["location"]).sum(numeric_only=True)
print(grouped)

# Calculate the median of all cities.
grouped_median = sales.groupby(["location"])["sales"].mean()
print(grouped_median)

# to save the csv file:
print(grouped.to_csv("cities grouped.csv"))