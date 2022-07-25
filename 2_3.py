# 数据-柱状图展示

from pandas import read_csv
import matplotlib.pyplot as plt

dataset = read_csv('bank\\bank-full.csv', header=0, delimiter=';')

def count(items):
    result = {}
    for i in items:
        result[i] = result.get(i,0) + 1
    return result

job_count = count(dataset['job'])
marital_count = count(dataset['marital'])
edu_count = count(dataset['education'])
y_count = count(dataset['y'])

fig = plt.figure(figsize=(20,18))
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

'''
    x, y, x刻度标签
'''
ax1.bar(range(len(job_count.values())), job_count.values(), tick_label=list(job_count.keys()))
ax1.set_xticklabels(list(job_count.keys()), rotation='45')
ax1.set_title('job', fontsize='20')

ax2.bar(range(len(marital_count.values())), marital_count.values(), tick_label=list(marital_count.keys()))
ax2.set_title('marital', fontsize='20')

ax3.bar(range(len(edu_count.values())), edu_count.values(), tick_label=list(edu_count.keys()))
ax3.set_title('education', fontsize='20')

ax4.bar(range(len(y_count.values())), y_count.values(), tick_label=list(y_count.keys()))
ax4.set_title('y', fontsize='20')

plt.show()