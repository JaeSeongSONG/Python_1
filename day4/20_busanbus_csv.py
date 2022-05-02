# 부산버스 노선별 이용건수
# csv 파일은 list 의 형태로 출력함!!

import csv

file_name = '부산버스정보.csv'
f = open(file_name, 'r', encoding = 'utf- 8')

reader = csv.reader(f, delimiter = ',') # delimeter 구분자, csv 파일이 ,로 구분되기 때문에
next(reader) # 헤더를 없애는 역할
for line in reader:
    print(line)

f.close()