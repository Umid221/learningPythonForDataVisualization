import pandas as pd
import matplotlib.pyplot as plt

#loading up the csv file
data = pd.read_csv('countries of the world.csv')
sorted = data.sort_values('GDP_PC', ascending = False).head(10)

# print(sorted.GDP_PC)
print(sorted.Country)

labels =[]
countries = sorted.Country
for country in countries:
    country = country[:len(country)-1]
    if ' ' in country:
        index = country.index(' ')
        labels.append(country[0]+ country[index+1])
        continue
    labels.append(country[:4])
value = sorted.GDP_PC
width = 0.5
fig, ax = plt.subplots()

ax.bar(labels, value, width)
ax.set_ylabel('Values')
ax.set_title('GDP per capita in 2016')
plt.show()
