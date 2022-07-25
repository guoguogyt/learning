#蒙特卡洛方法模拟赌博

import pandas as pd
import random

sample_list = []
random_num = 100
person_num = 10

for person in range(1, person_num+1):
    money = 10
    for round in range(1, random_num+1):
        result = random.randint(0,1)
        if result == 1:
            money = money + 1
        elif result == 0:
            money = money - 1
        if money == 0:
            break
    sample_list.append([person,round,money])

sample_df = pd.DataFrame(sample_list, columns=['person', 'round', 'money'])
sample_df.set_index('person', inplace=True)

print(sample_df)

