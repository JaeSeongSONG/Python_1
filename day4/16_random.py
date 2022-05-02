# random 함수

#import만 사용하면 모듈 안의 함수를 사용할 때, 모듈명.함수명( )으로 하고, from을 사용하면 바로 함수명( )으로 사용

import random
# from random import *

# print(random.choice(range(1, 6)) # 주사위

numbers = [i for i in range(1, 46)]
print(numbers)
lottery = []

for i in range(6):
    lottery.append(random.choice(numbers))

print(lottery)