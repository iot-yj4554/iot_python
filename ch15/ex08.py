# 클래스 상속
# 기존 클래스 정의를 그대로 자신의 것으로 취하는 방법
# class 자식클래스명(부모클래스명):
#   # 자식클래스 정의 ...
# 부모 클래스 == 수퍼 클래스
# 자식 클래스 == 서브 클래스
# 다중 상속은 가급적 쓰지 않는게 좋음

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f'{self.age}살 {self.name} 입니다.')


class Gender:
    def __init__(self, gender):
        self.gender = gender
    


class Student(Human, Gender): # 다중 상속
    def __init__(self, name, age, gender, stunum):
        # super().__init__(name, age) # 부모의 멤버 변수 초기화 / super(). ---> 부모 클래스의 참조 / init 함수를 직접 호출함 (특수한 경우임)
        Human.__init__(self, name, age) # 이렇게도 가능 / 다만 self를 직접 넣어주어야 함 / 다중 상속 시, 이런 방법으로 써야 함 (super로 호출 못함)
        Gender.__init__(self, gender)
        self.stunum = stunum
    
    def intro(self):
        super().intro() # override 오버라이드 ---> 덮어 쓴다라는 의미
        # Human.intro(self) # 다중 상속시 이것도 마찬가지로 self 넣어주어야 함
        print(f'학번 : {self.stunum}')

    def study(self):
        print('하늘 천, 따 지, 검을 현, 누를 황')

kim = Human(29, '김상형')
kim.intro()

lee = Student(34, '이승우', '남', 930011)
lee.intro()
lee.study()

# 오버라이드도 하지 않고 super().<method>도 쓰지 않겠다 ---> 부모의 메서드를 사용하지 않겠다 (하지만 때에 따라 쓸 수는 있음)
# 오버라이드는 하지만 super().<method>를 쓰지 않겠다 ---> 내가 부모와 완전히 다른 새로운 기능을 쓰겠다
# 오버라이드도 하고 super().<method>도 쓰겠다 ---> 부모의 메서드에 내가 기능을 추가해서 쓰겠다

