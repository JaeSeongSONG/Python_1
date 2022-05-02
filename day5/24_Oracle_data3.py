# bookrentalshop.py
# divtbl, membertbl

import cx_Oracle as ora

def myconn():
    dsn = ora.makedsn('localhost', 1521, service_name = 'orcl')
    conn = ora.connect(user = 'scott', password = 'tiger', dsn = dsn, encoding = 'utf-8')
    return conn

def GetAllDataFromDivtbl(conn):
    cur = conn.cursor()
    query = 'SELECT * FROM divtbl'
    for row in cur.execute(query):
        print(row)

def SetDataIntoDivtbl(conn, tup):
    cur = conn.cursor()
    query = 'INSERT INTO divtbl (division, names) VALUES (:1, :2)'
    cur.execute(query, tup)
    cur.close()
    conn.commit() # commit

def getSomeDataFromMembertbl(conn):
    cur = conn.cursor()
    query = '''SELECT names, levels, addr, mobile, email 
                FROM membertbl
                WHERE addr LIKE '서울%'
                AND UPPER(email) LIKE '%@NAVER.COM'
                ORDER BY idx DESC'''
    for row in cur.execute(query):
        print(row)

    cur.close()

def setNewMemberIntoMembertbl(conn, tup):
    cur = conn.cursor()

    query = '''SELECT ROWNUM, idx
                FROM (
                    SELECT idx FROM membertbl
                    ORDER BY idx DESC  
                        ) 
                WHERE ROWNUM = 1'''
    cur.execute(query)
    idx = cur.fetchone()[1] 
    if idx is None:
        idx = 0
    else:
        idx = idx[1]

    intup = (idx + 1, tup[0], tup[1], tup[2], tup[3])

    query = '''INSERT INTO membertbl (idx, names, levels, userid, password)
               VALUES (:1, :2, :3, :4, :5)'''

    cur.execute(query, intup)
    conn.commit()

def setChangeMemberFromMembertbl(conn, tup):
    cur = conn.cursor()
    query = '''UPDATE membertbl
                SET names = :1
                , addr = :2
                , mobile = :3
                , email = :4
                WHERE idx = :5'''
    cur.execute(query, tup)
    cur.close()
    conn.commit()

def deleteDivision(conn, division):
    cur = conn.cursor()
    query = 'DELETE FROM divtbl WHERE division = :1'
    cur.execute(query, (division,)) # 데이터가 하나면 튜플로 변경하면서 (ㅇ,) 쉼표를 넣어줘야 한다.
    conn.commit()

if __name__ == '__main__':
    
    print('책대여점 프로그램 시작')
    scott_con = myconn()

    # 1. divtbl에서 데이터 조회
    
    print('책 장르 조회')
    GetAllDataFromDivtbl(scott_con)

    # 2. divtbl에 새로운 데이터 입력
    
    print('책 장르 정보 입력')
    division = input('구분코드 임력: ')
    names = input('장르명 입력: ')
    tup = (division, names)
    SetDataIntoDivtbl(scott_con, tup)
    print('정보 입력 성공')

    # 3. membertbl에서 데이터 조회

    getSomeDataFromMembertbl(scott_con)

    # 4. membertbl에 새 데이터 입력

    print('신규 회원 입력: ')
    names = input('이름입력: ')
    levels = input('레벨입력(A_D): ')
    userid = input('아이디 입력(최대 20자): ')
    password = input('패스워드 입력: ')
    tup = (names, levels, userid, password)
    setNewMemberIntoMembertbl(scott_con, tup)
    print('신규회원 저장성공')

    # 5. membertbl의 데이터를 수정
    
    print('기존회원 수정')
    idx = input('변경회원번호 입력: ') # key를 중심으로 바꾸는 것이 중요
    names = input('이름 입력: ')
    addr = input('주소 입력: ')
    mobile = input('전화번호 입력 ( - 포함): ')
    email = input('이메일 입력: ')
    tup = (names, addr, mobile, email, idx) # 순서변경 : WHERE 조건이 들어가서 순서가 변했기 때문
    setChangeMemberFromMembertbl(scott_con, tup)
    print('기존회원 수정완료')

    # 6. divtbl의 임의 데이터 삭제
    
    print('삭제할 책 정보 입력')
    division = input('삭제할 장르코드 입력: ')
    deleteDivision(scott_con, division)
    print('삭제 성공')