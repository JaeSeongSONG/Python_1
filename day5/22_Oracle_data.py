# Oracle data
# cx_oracle 설치: pip install cx_oracle

import cx_Oracle

# 접속
# makedsn ('호스트명', port number, service_name = '서비스명')
dsn = cx_Oracle.makedsn('localhost', 1521, service_name = 'orcl') # 접속 주소
# conn = connect(user = 'username', password = 'tiger', dsn = dsn, encoding = 'utf-8')
conn = cx_Oracle.connect(user = 'scott', password = 'tiger', dsn = dsn, encoding = 'utf-8')

cur = conn.cursor() # 실행결과 데이터를 담을 메모리 객체
                    # 마우스 커서와 비슷한 의미, 명령어대로 커서를 옮김
                    # DB는 0이 아니라 1부터 시작함을 명심


try: 
    for row in cur.execute('SELECT * FROM emp'): # row 별로 row 를 가져옴, 단 csv 파일과 다르게 튜플의 형태로 가져옴
        print(row)
    # cur.execute('SELECT COUNT(*) FROM emp')
    # result = cur.fetchone() # fetchone : 한번 호출에 하나의 Row 만을 가져올 때 사용
    # print(result)
except cx_Oracle.DatabaseError as e:
    print(f'쿼리문이 잘못되었습니다. 확인부탁드립니다 : {e}') # 예외처리

finally:
    cur.close() # 커서 닫고
    conn.close() # 접속 닫음
