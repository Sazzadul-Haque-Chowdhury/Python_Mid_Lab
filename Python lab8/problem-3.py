import pandas as pd 
df = pd.read_csv('titanic.csv')

print("First 5 rows:")
print(df.head())

print("Last 5 rows:")
print(df.tail())

print("Dataset info:")
print(df.info())