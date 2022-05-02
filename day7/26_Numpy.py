a = [1, 2, 3, 4]
print(type(a))
print(len(a)) # 4

b = [[1,2], [2,3,4]]
print(len(b))  # 2


# list와 행렬의 차이점
# 행렬구조에 특화된 numpy 모듈에 대하여 먼저 학습
# 행렬은 반드시 행과 열의 갯수가 인덱싱마다 같아야하고, 연산이 가능함. 자료의 성격이 같아야함.

import numpy as np

x = [[1,2,3], [1,2,3]] # 2행 3열
x2 = np.array(x) + 2
np.shape(x) # 행렬 구조 확인
np.shape(x2) # x2는 배열로 변환되었기 때문에 shape로 사용
print(type(x), type(x2))

x2 = np.array(x)
x2 + 100 # x2+[[100,100,100],[100,100,100]]

# broadcast 기능

import numpy as np
from PIL import Image

img = Image.open('C:\pic\Bearbarnstar.jpg')
img.show()