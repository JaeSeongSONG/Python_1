# 줄 바꿈. tab
print(1, 2, 3, sep = '\n')
print('1\n2\n3') # \n
print('1\t2\t3') # \t
print('1\\3') # \\: \를 그대로 출력하고 싶을 때

# triple quote
bruce_eckel = '''Life is short
You need python.
i need it'''
print(bruce_eckel)




# 자료형

print(None) # 빈 값 지정
print(type(None))

print(0 == None)
a = None
print(a)
print(type(a))


# 숫자형
금액 = 12_345_345 # 천단위 표시
print(금액)


# 문자열
bruce_eckel = 'Life is short,\nYou need python'
print(bruce_eckel)


# boolean type
val_sum = 1000
print(val_sum == 1000) # 참거짓을 판단
print(val_sum == 100) # False
print(val_sum = 10) # ERROR
print(val_sum is 1000) # False

bl_true = True # boolean 타입도 할당이 가능
bl_False = False
print(bl_true)
print(bl_False)
print(bl_true == 1) # True
print(bl_true is True) # True
print(bl_true is None) # False  # ==과 is의 차이: ==는 값이 같을 때, is는 오브젝트가 같을 떄

print(bool(1))
print(bool(0)) # bool에는 bool(0), bool(0,0), bool('')을 제외한 어떤 것을 넣어도 True가 나옴


# (list)
b = [1, 2, 'James', True]
print(b)

b = [i for i in range(1,100)]
print(b)

arr2 = ['Life', 'is', 'short', 'You', 'need', 'Python', 3]
print(arr2)

arr3 = [['1, 2, 3'], ['4, 5, 6']] # 2차원 배열 alike 행렬
print(arr3)

a = list('Hello') # 한 음절씩 분리해서 리스트 형태로 저장
print(a)

arr4 = list() # 빈 list 만들기
arr5 = []
print(arr4, arr5)

list(range(0, 10, 3)) # range(시작, 끝, 증가폭)
list(range(10, 0, -3)) # range(끝, 시작, 감소폭)


# (tuple)
a = (1, 2, 3, 4)
print(a)
a = (1,) # 만약 튜플의 값이 1개일 경우


# {dictionary} 모든 키에 대한 값이 쌍으로 항상 존재하는 형태, list와 tuple은 순차적이지만 dictionary는 비순차적 
spiderman = {'name' : 'peter parker', 'age' : 18, 'weapon' : 'webshooter'}
print(spiderman)


# ([set])
set1 = set([1, 2, 3, 4, 5, 6, 3, 2])
print(set1) # 중복된 값을 제거함











