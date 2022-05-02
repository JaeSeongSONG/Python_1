# mycar.py

from vehicle import Car


if __name__ == '__main__':
    mycar = Car('98 가 1234', 'White')
    # mycar.number = '98 가 1234'
    # mycar.color = 'White'
    # mycar.fuel = 'Gasoline'
    # mycar.maker = 'Kia'
    # mycar.year = '2021'
    # 여기에 변수하나를 새롭게 생성해도 추가가 가능함

    mycar.goForward(7)
    mycar.goBackward()
    mycar.goLeft()
    mycar.goRight()
    mycar.stop()

    print(mycar)
    