import pandas as pd 

df = pd.read_csv("titanic.csv")

print("Original Dataset:")
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())

df["Age"] = df["Age"].fillna(df["Age"].median())

df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

if "Cabin" in df.columns:
    df.drop("Cabin", axis=1, inplace=True)
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Fare"] = pd.to_numeric(df["Fare"], errors="coerce")

df["Sex"] = df["Sex"].astype(str)
df["Embarked"] = df["Embarked"].astype(str)
df.loc[(df["Age"] < 0) | (df["Age"] > 100), "Age"] = df["Age"].median()

df.loc[df["Fare"] < 0, "Fare"] = df["Fare"].median()

df = df[df["Pclass"].isin([1, 2, 3])]

print("\nNumber of duplicate rows:", df.duplicated().sum())

df.drop_duplicates(inplace=True)

print("\nCleaned Dataset:")
print(df.head())

print("\nInformation after cleaning:")
df.info()