# module
# 모듈은 누군가 만들어놓은 파이썬 파일(.py)이며, 이를 모아둔 폴더를 패키지
# 모듈안에는 함수, 모듈, 클래스가 존재함
# 라이브러리는 파이썬 설치 시 기본으로 설치되는 파이썬 표준 라이브러리(Python Standard Library, PSL)와 외부 라이브러리로 나뉨.

import math
# from math import *
# from문으로 시작한 import는 사용할 때 패키지의 이름을 쓰지 않아도 됨 

print(math.pi) # 마우스 오른쪽 버튼 - 정의로 이동
# print(pi) # from으로 시작한 import를 썼을 때

from math import cos, sinh
print(sinh(10)) # import 한 모듈만 할 수 있음
# print(tan(10)) # error - tan은 import 하지 않았기 때문에

