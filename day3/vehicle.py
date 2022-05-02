class Car:
    number = '' # Set Default
    color = ''
    maker = ''
    fuel = ''
    year = ''
    level = ''
    

    # Magic Method

    def __init__(self, number, color) -> None: # 리턴값 없음
        self.number = number
        self.color = color

    def __str__(self) -> str: # 문자열 리턴 parameter 쓸 필요 없음
        return f'제 차는 {self.year} 년에 만들어진 {self.fuel} 차량 입니다.'


    # __ : Private | def에서 선언한 함수에서만 접근이 가능하지만, 밖에서는 접근이 안되도록 만든 것 eg) __fuel 보안상의 이유로 막음


    def goForward(self, level):
        print(f'{self.color} 색 차가 {level} 단으로 Go Forward')

    def goBackward(self):
        print(f'{self.color} 색 차가 Go Backward')

    def goLeft(self):
        print(f'{self.color} 색 차가 Go Left')

    def goRight(self):
        print(f'{self.color} 색 차가 Go Right')

    def stop(self):
        print(f'{self.color} 색 차가 Go Stop')

class airplane:
    pass