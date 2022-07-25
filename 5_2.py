# 每次下注赌注不变，一直赌下去，代码如下
# 结果分析：根据大数定理，单倍下注赌久必输
import random
import matplotlib.pyplot as plt

def rollDice():
    roll = random.randint(1,100)
    if roll == 100:
        return False
    elif roll <= 50:
        return False
    elif 100>roll>50:
        return True

def simple_bettor(funds,initial_wager,wager_count):
    value = funds           # 资金
    wager = initial_wager   # 赌注
    wX = []                 # wager X
    vY = []                 # value Y
    currentWager = 1
    while currentWager <= wager_count:
        if rollDice():
            value += wager
            wX.append(currentWager)
            vY.append(value)
        else:
            value -= wager
            wX.append(currentWager)
            vY.append(value)
        currentWager += 1
    plt.plot(wX,vY)         # 画图
    # 分类
    if value<=0:
        return "broke"
    elif value<funds:
        return "lose"
    elif value>funds:
        return "win"
    elif value==funds:
        return "equal"

x = 0
# 赌博人数
people = 100
# funds 赌金
funds = 10000
# 赌注
initial_wager = 100
# 模拟赌博次数,修改值可以得出赌久必输
count = 10000

num_win = 0
num_lose = 0
num_broke = 0
num_equal = 0

while x < people:
    result = simple_bettor(funds,initial_wager,count)
    x += 1
    if result == 'win':
        num_win += 1
    elif result == 'lose':
        num_lose += 1
    elif result == 'broke':
        num_broke += 1
    elif result == 'equal':
        num_equal += 1

print("%d people are betting"%people)
print("people betting %d times"%count)
print("num_win:",num_win)
print("num_lose:",num_lose)
print("num_equal:",num_equal)
print("num_broke:",num_broke)
print("broken rate:",num_broke/people)

plt.ylabel("money in hand")
plt.xlabel("betting Count")
plt.show()
