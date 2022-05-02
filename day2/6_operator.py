# 연산자_사칙연산

a = 10
b = 4

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)


# 문자열 연산
stat1 = 'Hello'
stat2 = 'World'
len(stat1) # 문자열의 개수
print(stat1, stat2) # 출력
print(stat1 + stat2) # 붙여서 출력
print(stat1 - stat2) # 문자열 연산에서 - 는 없음
print(stat1 * 5)
print(stat1 / stat2) # 문자영 연산에서 / 는 없음


# 문자열 길이
print(len(stat1))
stat3 = '안녕하세요'
print(len(stat3))


# 문자열 인덱스, 리스트와 동일한 작업 
print(stat3[0])
print(stat3[1])
print(stat3[2])
print(stat3[3])
print(stat3[4])

print(stat3[-1])
print(stat3[-2])
print(stat3[-3])
print(stat3[-4])
print(stat3[-5])


# slicing
date = '2022-01-17 14:39:25'
print(date[0:4] + '년')
print(date[0:10])
print(date[-2:]) # 25
print(date[len(date) - 1]) # 5
print(date[0:8:3]) # 0부터 7까지 3씩 건너뛰어서
print(date[10::-1]) # 10부터 역으로 모두 출력

list_a = [1, 2, 3, 4, 5]
list_a[1] = 19
print(list_a) # 숫자형 list의 변환은 가능하지만 문자열의 변환은 불가능함
b = 'Hello'
print('h' + b[1:]) # 문자열 list의 변환

full_name = 'Song Jae seong'

# split
part_name = full_name.split() # list 형태로 반환
print(part_name)
print(type(part_name))

test = 'Hey, guys'
print(test.split(','))


# replace
full_name.replace('Jae', '재')


# strip 특정 문자열이나 빈공간 제거
aaa = '      aaa     '
print(aaa)
print(aaa.lstrip())
print(aaa.rstrip())
print(aaa.strip())

name = 'James'
print(name.lstrip('J'))


# index
print(full_name.index('J')) # J를 찾아서 위치를 반환함
print(full_name.index('a'))


# find
print(full_name.index('J')) 
print(full_name.find('J')) # 찾는 값이 없을 때 -1을 반환


# join 
'-'.join(full_name) # 특정 문자열 및 문자를 문자열 양 옆에 추가


# upper(), lower()
print(full_name.upper())
print(full_name.lower())


#count()
print(full_name.count('S'))