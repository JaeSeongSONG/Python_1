# 웹페이지 긁어오기

from urllib.request import Request, urlopen # 선언했지만 쓰지 않으면 희미해짐

req = Request('http://www.naver.com') # naver 요청
res = urlopen(req)  

print(res.status) # value가 200 이라면 성공적으로 찾은 것, 예를들어 404라면 못찾은 것

# 외부 request 패키지 추가 설치
# pip install requests

import requests 

url = 'http://www.naver.com'
res = requests.get(url)

print(res.status_code)
print(res.text)