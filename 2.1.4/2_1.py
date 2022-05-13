# 数据-折线图展示

from pandas import read_csv
import matplotlib.pyplot as plt

dataset = read_csv('bank\\bank-full.csv', header=0, delimiter=';')

fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)

ax1.plot(dataset['age'])
ax1.set_title('age', fontsize='20')
ax2.plot(dataset['balance'])
ax2.set_title('balance', fontsize='20')
ax3.plot(dataset['duration'])
ax3.set_title('duration', fontsize='20')

plt.show()
