# while 문
# 반복횟수가 정해지지 않았을 때 사용, 그래서 for 문에는 += 1 과 같은 코드가 없다

hit = 0

while 1:
    hit += 1
    print(f'나무를 {hit:2d} 번 찍었습니다.') # 2자리 정수
    if hit == 10:
        print('나무가 넘어갑니다.')
        break

print('나무찍기를 멈춥니다.')

 
hit = 0

for hit in range(1, 101):
    print(f'나무를 {hit:2d} 번 찍었습니다.') # 2자리 정수
    if hit == 10:
        print('나무가 넘어갑니다.')
        break

print('나무찍기를 멈춥니다.')

#-----------------------------------------------------------------
# '''문자''' 로 쓰면 줄이 넘어간 상태 그대로 출력, def 아래 """문자""" 는 주석과 똑같은 역할
num = 0

while 1:
    print('''처리할 숫자를 입력하세요 
1. 회원입력
2. 회원검색
3. 회원수정
4. 회원삭제
5. 종료

숫자 입력 : ''', end = '')
    num = int(input())

    if num == 1:
        print('회원입력')
    elif num == 2:
        print('회원검색')
    elif num == 3:
        print('회원수정')
    elif num == 4:
        print('회원삭제')
    elif num == 5:
        break
    else:
        print('1 - 5 사이의 수를 입력해주세요. ')
        print('')
        continue


# 무한루프

val = 0

while 1:
    print(val)

    val += 1


#---------- test
# 잔액 출력, 잔액이 부족하면 그대로 출력
money = int(input('입력'))

while 1:
    money = money - 1350
    print(money)

    if money < 1350:
        break
# 일의자리가 3인 수만 출력    
i = 0

while 1:
    i += 1

    if i % 10 == 3:
        print(i, end = ' ')
        continue

    if i > 73:
        break
# 두 숫자 입력, 일의자리 3인것은 건너뜀
while 1:
    start, stop = map(int, input().split())
    if not 0 < start < 201 or not 0 < stop < 201:
        print('숫자가 너무 작거나 높습니다.')
        continue

    if start > stop:
        print('다시 입력해주세요.')
        continue
    
    else:
        for i in range(start, stop):
            if i % 10 == 3:
                continue
            print(i)
    break
