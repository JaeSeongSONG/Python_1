# 예외처리
# 가장 중요!
# try except가 중복되서 예외가 발생하면 처리속도가 매우 느려짐

list = []

def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def multi(a, b):
    return a * b


def divide(a, b):
    return int(a / b)

print('사칙연산 시작')
a, b = 4, 1 # 예외 발생, 실행한 이후 찾아낼 수 있음 : division by zero
numbers = [3, 6, 9]

try:
    print(f'나누기 결과 : {divide(a, b)}') # 예외가 발생할 것 같은 코드
    res = int(numbers[2]) * 8
    print(res)
    num = int(input('수를 입력하세요.'))
    print(f'곱하기 결과 : { multi(a, b)}') # try에서 error가 나면 바로 중지하고 IndexError로 점프해서 넘어가기 떄문에 이하 구문들을 실행하지 않음.
    print(f'  빼기 결과 : { minus(a, b)}') # 따라서 예외가 발생할 곳만 입력하고, 아닌 것들은 넣지 않는게 좋음.
    print(f'더하기 결과 : {   add(a, b)}')

except ZeroDivisionError as e: # 정확히 어떤 에러인지 표시 - 최상위인 Exception을 사용해도 되지만 구체적인 정보를 위해 사용
    print(f'나누기 예외발생 {e}') # 발생시 처리 방법 : 예외발생 출력 후 어떤 에러인지 표시

except IndexError as e: 
    print(f'인덱스 예외발생 {e}')

except Exception as e: 
    print(f'알 수 없는 예외발생 {e}')

except ValueError as e:
    print(f'값 예외발생 {e}')

# finally:
    # print(f'곱하기 결과 : { multi(a, b)}') # 예외가 발생해도 무조건 실행, 없어도 되긴 함.
    # print(f'  빼기 결과 : { minus(a, b)}')
    # print(f'더하기 결과 : {   add(a, b)}')



print('사칙연산 종료')


### debuging
# break point를 걸어야함!! f9로 설정
# point 실행 전에 point에서 멈춤
# f5 시작
# f9 로 point 설정
# f10 한 줄 실행 
# f11 step into e.g.) def 함수 안으로 진입