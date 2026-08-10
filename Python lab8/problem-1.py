import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}
calories_series = pd.Series(calories)

total_calories = calories_series.sum()

print("Calories:")
print(calories_series)

print("Total calories:", total_calories)