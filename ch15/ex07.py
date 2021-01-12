class Human:
    def __init__(self):
        self.name = '홍길동'

    def info(self):
        print(self.name)


def test3(func):
    func()

hong = Human() # 생성자 함수 호출 ---> 이름이 홍길동인 인스턴스를 참조
test3(hong.info)

hong = Human # 실제 클래스가 '정의'되어 있는 곳 참조 ---> 잘못된 것
# hong.info() # self가 없다는 오류 발생
h1 = hong() # 이처럼 두단계를 거치면 쓸 수 있음
h1.info() # 오류 안남

# UML 기법 ---> OOP에서 매우 필요한 기법
# 설계 시 그림으로 표현함
# 클래스는 네모 박스로 표현
# 상속은 화살표로 표현함 / 자식이 부모를 가리킴 [child] ---(세모) [parent]