# 파일 입출력


# 파일 출력

# f = open('newfile.txt', 'w')
# f.close() # close는 필수
# r 읽기모드 w 쓰기모드 a 추가모드

f = open('C:/Sources/sample/text.txt', 'w')
f.close()
print('파일이 생성되었습니다.')

# ascii (영어만 처리)와 cp949(한글처리), utf-8
# newfile.txt 읽어오기

n_file = ''

f = open('newfile.txt', 'r', encoding = 'utf-8')
while 1: 
    line = f.readline() # readline 파일의 한 줄을 가져와 문자열로 반환 , readlines 파일 내용 전체를 가져와 리스트로 반환
    if not line: # 값이 있으면 True를 반환
        break
    n_file = n_file + line.strip() + '\n'
f.close()
print(n_file)


f = open('newfile.txt', 'r', encoding = 'utf-8')
lines = f.readlines() 
print(lines)
for line in lines: # for 을 사용해서 한줄이 더 띄어짐
    print(line)
f.close()


f = open('newfile.txt', 'r', encoding = 'utf-8')
for line in f:
    print(line.replace('\n',''))
f.close()


# 내용 쓰기 
# w 는 데이터가 새로 쓰이므로 주의

f = open('writefile.txt', 'w', encoding = 'utf8')
f.write('저는 한국사람입니다.')
texts = ['저는 미국인입니다.', '저는 프랑스인입니다.']
f.writelines(texts)
f.close()


# 내용 추가

f = open('writefile.txt', 'a', encoding = 'utf8')
f.write('\n내용 추가합니다.')
f.close()