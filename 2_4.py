# 数据-双变量对比展示

from pandas import read_csv
import matplotlib.pyplot as plt

dataset = read_csv('bank\\bank-full.csv', header=0, delimiter=';')

x = dataset['age']
y = dataset['balance']


fig = plt.figure(figsize=(6,6))
fig.suptitle('age&balance relation')
#将当前区域划分为3x3的网格
grid =plt.GridSpec(4,4,hspace=0.2,wspace=0.2)
main_ax = fig.add_subplot(grid[:-1,1:])
y_hist = fig.add_subplot(grid[:-1,0],xticklabels=[],sharey=main_ax)
x_hist = fig.add_subplot(grid[-1,1:],yticklabels=[],sharex=main_ax)

main_ax.plot(x,y,'ok',markersize=3,alpha=0.2)

x_hist.hist(x,40,histtype='stepfilled',orientation='vertical',color='gray')
x_hist.invert_yaxis()


y_hist.hist(y,40,histtype='stepfilled',orientation='horizontal',color='gray')
y_hist.invert_xaxis()

plt.show()