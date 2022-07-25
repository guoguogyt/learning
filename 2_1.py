# 数据-折线图展示

from pandas import read_csv
import matplotlib.pyplot as plt

'''
header=0，表示文件第0行（即第一行，python，索引从0开始）为列索引
header=None时，即指明原始文件数据没有列索引，这样read_csv为自动加上列索引
delimiter指定分隔符
'''
dataset = read_csv('bank\\bank-full.csv', header=0, delimiter=';')
'''
figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True)
num:图像编号或名称，数字为编号 ，字符串为名称

figsize:指定figure的宽和高，单位为英寸；

dpi参数指定绘图对象的分辨率，即每英寸多少个像素，缺省值为80 1英寸等于2.5cm,A4纸是 21*30cm的纸张

facecolor:背景颜色

edgecolor:边框颜色

frameon:是否显示边框
'''
fig = plt.figure(figsize=(20,10))

'''
add_subplot(2,2,1)  行 列 显示位置
'''
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
