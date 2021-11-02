import matplotlib.pyplot as plt

# data source: https://en.wikipedia.org/wiki/List_of_countries_by_GDP_sector_composition

labels = 'Industry', 'Services', 'Agriculture'
sizes = [30, 63.6, 6.4]
explode = (0.1, 0.1, 0.1)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, shadow=True, startangle=60, autopct='%1.1f%%')
ax1.axis('equal')

plt.show()
