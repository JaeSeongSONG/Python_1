# 함수 선언 및 사용
# function call

def add(a, b): # def 함수(parameter): return
    """이 함수는 a와 b를 더하는 함수입니다. """ # 함수의 주석
    res = a + b
    return res

mid_val = add(234, 45)
print(mid_val)
print(mid_val * 3)

print(add(6)) # error, parameter가 하나 부족


# return의 빠져나오는 기능

def not_ten(a):
    if a == 0:
        return
    print(a, '입니다', sep = '')

not_ten(10) # 10을 출력하지 않는다. return 뒤에 none이 있기 때문

# parameter가 없는 상태
 
def hello():
    return 'hello'
hello()
Hel = hello()
print(Hel.replace('h', 'H'))


# 결과값이 없는 형태

def hello():
    print('hello')
    # return None이 숨겨져 있는 것. 단, none을 return하기 때문에 출력되어 보이지 않는 것. 
hello()


# 둘 다 없는 경우

def say_goodbye():
    print('Bye Bye')
    #return None

say_goodbye()


#매개변수 개수가 가변적일 때

def plus(*a): # 개수가 가변적이면 *문자를 사용
    res = 0

    for i in a:
        res += 1

    return res

print(plus(1,2,3,4,5))
print(plus(1,2,3,4,5,6,6,7,8,8))


# 결과값이 여러 개일 떄

def add(a, b):
    return a + b, a - b

print(add(10, 30)) # 결과값이 여러 개일 때 결과 값을 tuple로 변환함!!
(val1, val2) = add(10, 30)
print(val1 ,val2)


# 사칙연산

def  arith(x, y):
    return x + y, x - y, x * y, x / y

res1, res2, res3, res4 = arith(10, 20)
print(res1, res2, res3, res4)
print(type(arith(10, 20))) # tuple