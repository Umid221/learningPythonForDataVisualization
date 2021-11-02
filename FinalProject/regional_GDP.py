import pandas as pd
import matplotlib.pyplot as plt

#loading up the csv file
data = pd.read_csv('D:\programming\python\graduateMonkey\project\gdp(only_regional).csv')

# sorting data
by_year = data.sort_values('year', ascending=False).head(10)

labels = by_year.code
value = by_year.value
width = 0.5
fig, ax = plt.subplots()

ax.bar(labels, value, width)
ax.set_ylabel('Values')
ax.set_title('Regional GDP in 2016')
plt.show()
