# if 구문 - 흐름제어

name = ['a', 'b', 'c', 'd'] # tuple도 가능

if name == 'a':
    print('네~')

elif name == 'b':
    print('오세요~')

else:
    print('아니요~')


name = ['a', 'b', 'c', 'd']

if 'a' in name:
    print('네~')

elif name == 'b':
    print('오세요~')

else:
    print('아니요~')


# 중첩 if

# TODO
# pass를 사용하여 일단 넘어가고 주석처리 해서 나중에 다시 처리
if name == '재성':
    pass # TODO 재성을 입력할 때 처리가 필요함

x = 15

if x > 0:
    print('양수')

    if x > 9:
        print('10보다 큼')
    
    else:
        print('10보다 작은 수')

elif x == 0:
    print(0)

else:
    print('음수')