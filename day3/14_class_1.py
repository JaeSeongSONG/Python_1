# class

class Amazon:
    strength = 20          # 값 (객체 그 자체, 명사)
    dexterity = 25
    vitality = 20
    energy = 15

    def attack(self):      # 로직 (행위, 동작, 동사)
        return 'jab!!!'    # parameter가 없는 함수를 만들어도 self는 들어가야 함

    def exercise(self):
        self.strength += 2
        self.dexterity += 3
        self.vitality += 1


# cmd에서 열어보기

#-----import 14_class # class는 항상 import가 필수!!
#-----jane = 14_class.Amazon() # jane 이라는 객체 생성

jane.strength # 20


# 상속
# Amazom class를 만든 후 그 속성을 가진 다른 class를 만들 때

class Korean(Amazon):
    def study(self):
        print('열공')

james = Korean()
james.attack() # jab!!! 을 반환
james.study() # 열공 을 반환
