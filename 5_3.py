# 马尔科夫
'''
设一个随机系统的状态空间E={1,2,3,4},观测结果如下
 4 3 2 1 4 3 1 1 2 3
 2 1 2 3 4 4 3 3 1 1
 1 3 3 2 1 2 2 2 4 4
 2 3 2 3 1 1 2 4 3 1
马尔科夫模型计算概率P(i,j)

'''
import numpy as np
def str_count(str, sub):
    count = 0
    for i in range(0, len(str) - 1):
        if str[i:i+2] == sub:
            count = count + 1
    return count

def data_to_matrix():
    # 转移状态
    # str = "1110010011111110011110111111001111111110001101101111011011010111101110111101111110011011111100111"
    # count00 = str_count(str, "00")
    # count01 = str_count(str, "01")
    # count10 = str_count(str, "10")
    # count11 = str_count(str, "11")
    # print("count00:", count00)
    # print("count01:", count01)
    # print("count10:", count10)
    # print("count11:", count11)

    str = "4321431123212344331113321222442323112431"
    counts = [
        [str_count(str, "11"), str_count(str, "12"), str_count(str, "13"), str_count(str, "14")],
        [str_count(str, "21"), str_count(str, "22"), str_count(str, "23"), str_count(str, "24")],
        [str_count(str, "31"), str_count(str, "32"), str_count(str, "33"), str_count(str, "34")],
        [str_count(str, "41"), str_count(str, "42"), str_count(str, "43"), str_count(str, "44")]
    ]
    countMatrix = np.array(counts)
    sums = (countMatrix.sum(axis=1)).reshape(-1, 1)
    countMatrix = countMatrix / sums
    print(countMatrix)


if __name__ == '__main__':
    data_to_matrix()
