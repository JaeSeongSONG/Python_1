# 리스트 연산

arr = list(range(5))
print(arr)

arr = list(range(0, 5))
print(arr)

print(arr[0] + arr[4])


# 2차원 배열 (list)

arr2 = [1, 2, ['HI', 'My', 'Friend']]
print(arr2[0])
print(arr2[2])
print(arr2[2][1])
print(arr2[2][1][0])

arr3 = list(range(1, 4))
print(arr3)
print(arr3 * 3)
print(arr3 + 3) # error list에는 list만 더할 수 있음


# list 함수

del arr3[3] # del 해당 인덱스에 있는 값을 제거
print(arr3)

arr3.remove(2) # remove 해당 값인 것을 제거, 최초의 값만 지우고 나머지는 남겨둠
print(arr3)

arr4 = [4, 2, 6, 9, 12, 16, 7, 1, 3, 3, 5]
arr4.remove(3)
del arr4[8] 
print(arr4)
set(arr4)


# sort, reverse 정렬

arr4.sort() # 순차적
print(arr4)

arr4.reverse() # 역순
print(arr4)

# insert(인덱스, 값)
arr4.insert(1, 10) 
print(arr4)

# append 맨 마지막에 추가
print(arr3.append(4)) 
print(arr3)

#tuple # 인덱스, 값 모두 변환불가
tup1 = tuple(range(1, 10))
print(tup1)
print(tup1[0])


# dictionary

dict1 = dict(health = 90, mana = 334, melee = 550) # dicionary 생성
print(dict1)
dict2 = dict(zip(['health', 'mana', 'melee'], [90, 334, 550]))
print(dict2)

dic1 = {1 : 'a'}
dic1[2] = 'b' # 2 값에 b를 넣음
print(dic1)
dict1['armor'] = 18.72 # 새로운 key 생성 후 값 부여
print(dict1)

'health' in dict1 # True

dic1['name'] = 'JaeSeong' # 새로운 key 생성 후 값 부여
print(dic1)

print(dic1.keys()) # 왼쪽 값
print(dic1.values()) # 오른쪽 값
print(dic1.items()) # 함께 출력


# list tuple 변환

arr10 = list(range(10))
print(arr10)

tup1 = tuple(arr10)
print(tup1)

arr11 = list(tup1) # tuple 을 list 로 변환한뒤 10을 append하고 다시 tuple로 변환
print(arr11)
arr11.append(10)
print(arr11)
tup2 = tuple(arr11)
print(tup2)
