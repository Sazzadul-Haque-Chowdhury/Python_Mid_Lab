import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("iris.csv")

print(data.head())

plt.plot(data["sepal_length"][:20], data["petal_length"][:20])
plt.title("Line Plot of Sepal Length and Petal Length")
plt.xlabel("Data Number")
plt.ylabel("Length")
plt.show()

plt.scatter(data["sepal_length"], data["petal_length"])
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.show()

species_count = data["species"].value_counts()

plt.bar(species_count.index, species_count.values)
plt.title("Number of Iris Flowers")
plt.xlabel("Species")
plt.ylabel("Number of Flowers")
plt.show()

plt.hist(data["sepal_length"], bins=10)
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.show()

plt.pie(
    species_count.values,
    labels=species_count.index,
    autopct="%1.1f%%"
)
plt.title("Percentage of Iris Species")
plt.show()


fig, ax = plt.subplots(1, 2)

ax[0].hist(data["petal_length"], bins=10)
ax[0].set_title("Petal Length")

ax[1].scatter(data["sepal_width"], data["petal_width"])
ax[1].set_title("Sepal Width vs Petal Width")
ax[1].set_xlabel("Sepal Width")
ax[1].set_ylabel("Petal Width")

plt.show()