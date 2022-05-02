# 변수
a = 'Hello'
print(a)
a = '3'
print(a)

# 변수명
val = 10
val2 = 20
# -val = 20  incorrect
# *val = 40  incorrect
chain_reaction = 20
val_ = 30
print(id(val)) # 주소 검색하기
print(id(val_))
# 대소문자 구분, 특수문자는 _만 허용, 숫자는 맨 앞에 사용불가, 띄어쓰기 불가


# tuple, list
a, b, c = 10, 20, 'python'
print(a, b, c) # 10, 20, python

a = 1, 2, 3 # tuple의 packing # tuple은 괄호, list는 대괄호를 사용 # list는 요소의 추가, 수정, 삭제가 가능하지만 tuple은 불가함.
x, y, z = a #unpacking
print(x, y, z)

d = [1, 2, 3] # list
print(d)

# 값 삭제
del a
print(a, b, c) # a 변수값이 사라져 ERROR

# 할당 연산자 - assign
a = 10
a += 20
print(a) # a +=20: a = a + 20