import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('D:\programming\python\graduateMonkey\project\gdp.csv')

ch = data[data.country == 'China']
us = data[data.country == 'United States']

plt.plot(ch.year, ch.value/10**9)
plt.plot(us.year, us.value/10**9)

plt.legend(['China','USA'])
plt.xlabel('year')
plt.ylabel('value')
plt.title('GDP of China and USA (in billion US dollars)')
plt.show()