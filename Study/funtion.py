# 키보드 단축키

#  상하로 커서 단체로 추가하기

#  Ctrl + Alt + 상/하 방향키 

#  커서가 위치한 단어와 동일한 단어를 순차적으로 선택하기

#  Ctrl + D

#  커서가 위치한 단어와 동일한 단어를 모두 선택하기

#  Ctrl + Shift + L 

#  박스 선택(컬럼 선택)

#  Ctrl + Shift + Alt + 방향키 

#  축소/확장 선택하기

#  Shift + Alt + 왼쪽/오른쪽 방향키	 

# 창분할

# ctrl + \


# 매개변수 parameter 인수 argument 
# 매개변수는 x, y와 같은 변수, 인수는 실제로 들어가는 값

# rjust(), ljust()
print(str(3 * 4).rjust(6))


# map = 매번 int로 바꿔줄 때 # .split = 문자열로 나눠줄 때
a, b, c, d = map(int, input().split(','))
print(int((a + b + c + d) / 4))


# sep = 값 사이에 공백이 아닌 다른 문자를 넣고 싶을 때
print(1, 2, 3, sep = 'X')
print('Hell', 'Python', sep = 'o ')


# 줄 바꿈. tab 
print(1, 2, 3, sep = '\n')
print('1\n2\n3') # \n
print('1\t2\t3') # \t
print('1\\3') # \\: \를 그대로 출력하고 싶을 때


# end
print(1)
print(2)
print(3)

print(1, end = '') # 바로 뒤의 값을 붙여서 출력하고 싶을 때
print(2, end = '')
print(3, end = '')

print('시작', '중간', '끝', sep = '\n', end = '\n진짜 끝')


# lambda
# lambda 매개변수 : 표현식

def plus_ten(x):
    return x + 10
# lambda로 변환 단, 익명함수가 되기 때문에 변수에 할당해야 함.
plus_ten2 = lambda x: x + 10
# lambda 식 내에서는 새로운 변수를 만들 수 없음, 단 바깥에 있었던 변수는 가능
# a = lambda x : y = 10 ; x + y  ERROR
y = 10
(lambda x: x + y)(1) # 가능

# 활용
list(map(plus_ten2, [1, 2, 3]))

# lambda 매개변수들: 식1 if 조건식 else // 식2 if 조건식2 else // 식3  //로 쉽게 구분함
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(map(lambda x: str(x) if x % 3 == 0 else x, a)) # a에서 x 가 3의 배수면 string 형태로 출력, 아니면 그대로 출력

# lambda filter 리스트에 들어있는 원소들을 함수에 적용시켜서 결과가 참인 값들 반환
list(filter(lambda x: x > 5, range(10)))
list(lambda x: x > 5, range(10)) # error list 조건 충족 x 때문

#lambda reduce 반복 가능한 객체의 각 요소를 지정된 함수로 처리한 뒤 이전 결과와 누적해서 반환하는 함수
from functools import reduce
reduce(lambda x, y: x + y, [0, 1, 2, 3, 4])
reduce(lambda x, y: y + x, 'abcde')


# .find 문자열에서 찾는게 있을 때 인덱스 반환, 없으면 -1 반환
print('abcde'.find('a'))



#unpacking, 가변인수 사용

def print_numbers(a, b, c):
    print(a)
    print(b)
    print(c)

x = [10, 20, 30]
y = (10, 20, 30)
z = {'a':10, 'b':20, 'c':30}

print_numbers(*x) # unpacking 하는 것
print(x)
print_numbers(*y) # tuple도 가능
print_numbers(**z) # dictionary는 **, *를 입력하면 key값이 나오기 때문, 단, 함수의 매개변수 이름과 dictionary의 key 이름이 같아야함!

sorted( df.columns ) # 파이썬 내장함수, 리스트, 딕셔너리 사용가능
list.sort() # list에 사용가능
dataframe.sort_values( by = '' ) # dataframe에 사용가능