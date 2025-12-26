import pandas as pd

df = pd.read_csv("Workout.csv")

# Convert the df to dictionary.
print(df.to_dict())

# Convert the 'day' column to list.
print(df["day"].to_list())

# Calculate the mean of the 'calories' column.
# The classic methode:
calories = df["burned_calories"].to_list()
sum_of_calories = sum(calories)
long_of_calories = len(calories)
print(sum_of_calories / long_of_calories)
# Use the function in pandas:
print(df["burned_calories"].mean())