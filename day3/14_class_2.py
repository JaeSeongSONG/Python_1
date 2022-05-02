# Person.py
# Person class

class Person:
    name = '무명' # Defaule 값 생성
    age = 0
    height = 0 
    gender = ''
    feetsize = ''
    bloodtype = ''

    def eat(self, food):
        print(f'{self.name}이(가) {food}을(를) 먹는다.')
    
    def work(self, drink):
        print(f'{self.name}이(가) {drink}를 마신다.') # 누가 동작의 주체인지 나타내기 위해 self를 이용

    def introduce(self):
        greeting = f'''안녕하세요, 저는 {self.name}입니다.
        저는 {self.gender}구요. 혈액형은 {self.bloodtype} 입니다.'''
        print(greeting)

    # 생성자
    # __OO__ 매직 매서드
    def __init__(self, name, age) -> None: # Person() 값을 넣고 초기화 initialization
        self.name = name
        self.age = age
        print('Person이 생성되었습니다.')



if __name__ == '__main__':

    # p1 = Person() # p 라는  Person 객체 생성
    # print(type(p1)) 
    # print(id(p1)) # id 값
    
    # p2 = Person()
    # print(type(p2)) 
    # print(id(p2)) # id 값
    
    sjs = Person('송재성', 14) # == __init__ (self, name, age)
    # sjs.name = 'Song Jae Seong'
    # sjs.age = 26
    # sjs.height = 172.5
    # sjs.gender = 'male'
    # sjs.feetsize = 270
    # sjs.bloodtype = 'O'
    
    sjs.introduce() # name 과 age 값만을 넣었기 떄문에 null 값이 존재한다.
    sjs.eat('cereal') # self를 빼는것은 안되지만 함수 입력시 self를 입력하지는 않는다
    sjs.work('Orange Juice')


    
   