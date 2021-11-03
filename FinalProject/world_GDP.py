import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('gdp.csv')

wd = data[data.country == 'World']

plt.plot(wd.year, wd.value/10**9)
plt.legend(['World'])
plt.xlabel('year')
plt.ylabel('value')
plt.title('World GDP(in billion US dollars)')
plt.show()
