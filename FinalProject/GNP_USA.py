import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('D:\programming\python\graduateMonkey\project\GNP.csv')

plt.plot(data.DATE, data.GNP)
plt.xticks(['1950-01-01','1960-01-01', '1970-01-01', '1980-01-01', '1990-01-01', '2000-01-01', '2010-01-01', '2020-01-01'],rotation = 20)
plt.legend(['USA'])
plt.xlabel('year')
plt.ylabel('BILLIONS OF DOLLARS')
plt.title('GNP of the USA (in billion US dollars)')
plt.show()