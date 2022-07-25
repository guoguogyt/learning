# 使用1950-1979年的数据来预测1979-1989的数据
# 1950--1979年数据
data = ["E1", "E1", "E2", "E3", "E2", "E1", "E3", "E2", "E1", "E2",
        "E3", "E1", "E2", "E3", "E1", "E2", "E1", "E3", "E3", "E1",
        "E3", "E3", "E2", "E1", "E1", "E3", "E2", "E2", "E1", "E2",
        ]

# 1979-1989年数据
data1 = ["E1", "E3", "E2", "E1", "E1", "E2", "E2", "E3", "E1", "E2"]

E1data = []  # 计算从E1开始的状态
for i in range(len(data) - 1):
    if data[i] == "E1":
        E1data.append(data[i + 1])
E2data = []  # 计算从E2开始的状态
for i in range(len(data) - 1):
    if data[i] == "E2":
        E2data.append(data[i + 1])

E3data = []  # 计算从E3开始的状态
for i in range(len(data) - 1):
    if data[i] == "E3":
        E3data.append(data[i + 1])

E1E1 = 0  # E1->E1个数
E1E2 = 0  # E1->E2个数
E1E3 = 0  # E1->E3个数
for i in range(len(E1data)):
    if E1data[i] == "E1":
        E1E1 = E1E1 + 1
    if E1data[i] == "E2":
        E1E2 = E1E2 + 1
    if E1data[i] == "E3":
        E1E3 = E1E3 + 1

p11 = E1E1 / len(E1data)
p12 = E1E2 / len(E1data)
p13 = E1E3 / len(E1data)
print("p11=", p11)
print("p12=", p12)
print("p13=", p13)

E2E1 = 0  # E2->E1个数
E2E2 = 0  # E2->E2个数
E2E3 = 0  # E2->E3个数
for i in range(len(E2data)):
    if E2data[i] == "E1":
        E2E1 = E2E1 + 1
    if E2data[i] == "E2":
        E2E2 = E2E2 + 1
    if E2data[i] == "E3":
        E2E3 = E2E3 + 1

p21 = E2E1 / len(E2data)
p22 = E2E2 / len(E2data)
p23 = E2E3 / len(E2data)
print("p21=", p21)
print("p22=", p22)
print("p23=", p23)

E3E1 = 0  # E3>E1个数
E3E2 = 0  # E3->E2个数
E3E3 = 0  # E3->E3个数
for i in range(len(E3data)):
    if E3data[i] == "E1":
        E3E1 = E3E1 + 1
    if E3data[i] == "E2":
        E3E2 = E3E2 + 1
    if E3data[i] == "E3":
        E3E3 = E3E3 + 1

p31 = E3E1 / len(E3data)
p32 = E3E2 / len(E3data)
p33 = E3E3 / len(E3data)
print("p31=", p31)
print("p32=", p32)
print("p33=", p33)

import numpy as np

P = np.array([[p11, p12, p13], [p21, p22, p23], [p31, p32, p33]])
# 注意numpy的数字是int32  会截取数据
P  # 状态转移概率

# 因为1979年的状态是E2，所以假设pai1979=[0,1,0]
pai1979 = np.array([0, 1, 0])
pai1980 = pai1979.dot(P)

pai1980
# 可以看出1980的E1概率比较大 array([0.55555556, 0.11111111, 0.33333333])

pai1981 = pai1980.dot(P)
pai1981
# 可以看出1981的E2概率比较大，但与事实相反 array([0.27384961, 0.41301908, 0.31313131])

pai = np.array([0, 1, 0])
for i in range(10):
    pai = pai.dot(P)

    print("%s年=%s,预测状态为E%s" % (1980 + i, pai, list(pai).index(max(list(pai))) + 1))

