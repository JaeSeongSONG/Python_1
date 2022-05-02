# 기본 for 문
# 반복할 횟수를 알고 있을 때

arr = [1,2,3,4,5]

for i in arr:
    print(f'{i:0.1f}')

# tuple for 문

arr2 = ('me', 'my', 'friend', 'james')

for i in arr2:
    print(f'{i}')


# 합계 for 문

vals = list(range(1, 21, 2))
print(vals)
res = 0 

for i in vals:
    res += i
print(f'{vals[-1]} 까지의 총합은 {res} 입니다.') # vals 의 인덱스 -1을 출력


# 홀수, 짝수 구분

numbers = list(range(1, 21))

for item in numbers:
    if item % 2 == 0:
        print(f'{item}은 짝수입니다')

    else: 
        print(f'{item}은 홀수입니다')


# 13이상이면 탈출 ---------------break와 continue는 무조건 for과 while에 적용된다.

for item in numbers:
    if item >= 13:
        break # break는 상단부에 위치하는 것이 좋음

    else: 
        print(f'{item}은 13보다 작은 수 입니다')

print('종료합니다.')


# 15면 출력하지 않음

numbers = list(range(1, 21))

for item in numbers:
    if item == 15:
        continue # continue는 이하를 실행하지 않고 다시 반복으로 돌아감

    if item % 2 == 1:
        print(f'{item}은 홀수')


# 구구단

for i in range(2, 10):
    if i == 8:
        continue # 8단을 제외하고 출력
    print(f'\n{i}단을 시작합니다.\n')
    for j in range(1, 10):
        print(f'{i} X {j} = {i*j:2d}', end = '  ') # 2자리 확보 후 정수 출력
    print('') # 한줄 내리기


# inline for 문

a = [1, 2, 3, 4]

result = [i * 3 for i in a]
print(result)

result1 = []
for i in a: # 기본 for 문z
    result1.append(i)
print(result)