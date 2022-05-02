# cursor에 접근하는 코드를 함수로 작성

import cx_Oracle as ora

def myconn(): # def선언은 if __name__ == '__main__' 위에 써주는 것이 좋다
    """이 함수는 Oracle과 connection하는 함수 입니다"""
    # makedsn ('호스트명', port number, service_name = '서비스명')
    dsn = ora.makedsn('localhost', 1521, service_name = 'orcl')
    # conn = connect(user = 'username', password = 'tiger', dsn = dsn, encoding = 'utf-8')
    conn = ora.connect(user = 'scott', password = 'tiger', dsn = dsn, encoding = 'utf-8')
    return conn


def getalldata(conn): # conn 객체를 parameter로 받아서 뭐리 실행
    cur = conn.cursor() # 커서생성
    query = 'SELECT * FROM emp' 
    for row in cur.execute(query): # emp 테이블의 최상단에 커서가 위치하여 모든 데이터를 한줄씩 출력
        print(row)


def getNamesAndJobData(conn):
    cur = conn.cursor()
    query = 'SELECT ename, job FROM emp'
    cur.execute(query)
    while True:
        row = cur.fetchone() # 한 record 읽기
        if not row:
            break
        else:
            print(row)


def getdeptName(conn, no, loc):
    cur = conn.cursor()
    query = f'SELECT * FROM dept WHERE deptno = {no} AND loc = \'{loc}\'' 
    cur.execute(query)
    row = cur.fetchone()
    print(row)
    


def getdeptName2(conn, tup): # tuple을 사용하여 여러 변수 입력 가능
    cur = conn.cursor()
    # query = f'SELECT * FROM dept WHERE deptno = {tup[0]} AND loc = \'{tup[1]}\''  # 문자는 '' 표시가 필수
    # cur.execute(query)
    query = 'SELECT * FROM dept WHERE deptno = :1 AND loc = :2' # 참고 - 동적으로 parameter를 바꿀 수 있게 하는 문법, oracle은 1로 시작하기 떄문에 1부터 시작
    cur.execute(query, tup)
    row = cur.fetchone()
    print(row)
    


if __name__ == '__main__': # 해당 모듈이 임포트된 경우가 아니라 인터프리터에서 직접 실행된 경우에만, if문 이하의 코드를 돌리라는 명령, 코드의 시작부분
    print('Program start')

    print('emp table 전체 조회')
    scott_con = myconn() # dsn, connect() 후 접속객체 conn 리턴
    getalldata(scott_con)

    print('\nemp 이름과 직업 전체 조회')
    getNamesAndJobData(scott_con)

    no = input('1. 부서번호 입력하세요: ')
    loc = input('2. 위치를 입력하세요: ').upper()
    tup = (no, loc)
    print(f'부서번호: {no}, 지역: {loc}')
    getdeptName(scott_con, no, loc)
    getdeptName2(scott_con, tup)

    print('Program end')