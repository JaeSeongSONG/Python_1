## 문자열 포맷팅

# % 포맷팅
# %d 정수  %f  실수  %s  문자열  
# N자리로 포맷팅할 때, 정수부 : 0Nd, 실수부 : 0.Nf

num = 26
s = 'my age is %d' % num
print(s)

names = ['kim', 'song', 'jeong']
for name in names:
    print('my name is %s' % name)

print('my age is %d , my name is %s' %(num, name))

#-------------------------------------------------------------------------

# format 함수

str1 = "I'm so happy {0} you".format(2) # 2를 {0}에 넣는다
print(str1)
str1 = "I'm so happy {0} you. are'nt {1}".format(2, 'you') # 2를 {0}에 you를 {1}에 넣는다
print(str1)
str1 = "I'm so happy {1} you. are'nt {0}".format(2, 'you')
print(str1)

s9 = 'this is {0:<10} | done {1:<5} |'.format('left', 'a') # 왼쪽 정렬
print(s9)
s10 = 'this is {0:>10} | done {1:>5} |'.format('right', 'b') # 오른쪽 정렬
print(s10)
s11 = 'this is {0:^10} | done {1:^5} |'.format('center', 'c') # 가운데 정렬
print(s11)

# 자릿수 표현
# {0:0.2f} - :은 자릿수 표현 시 사용
# {0:10.3f} - 10자리를 확보하고 소수점 이하 3자리 float 넣기

money = 1000000000
print(format(money, ' ,d')) 

full_name = 'Song Jae Seong'
age = 26
greeting = '''안녕하세요, 저는 {0}입니다. 
나이는 {1}살 입니다.'''.format(full_name, age)
print(greeting)

#-------------------------------------------------------------------------------

# f-string
# f'문자열 {변수} 문자열' 의 형태

import math
mypi = math.pi
print(mypi)
print('{0:0.2f}'.format(mypi))
# ->
print(f'{mypi:0.6f}')

a = 2
b = 'you'
str2 =f"I'm so happy {a} you. aren't {b}" # 객체 앞에 f를 붙인다.
print(str2)

s1 = 'mid'
print(f'{s1:^10}') # 10칸 부여 후 가운데 정렬

greeting = f'''안녕하세요, 저는 {full_name}입니다.
나이는 {age:0.4f}살 이구요'''
print(greeting)

vals = list(range(1, 11))
print(vals)
res = 0 
for i in vals:
    res += i
print(f'{vals[-1]} 까지의 총합은 {res} 입니다.') # vals 의 인덱스 -1을 출력
