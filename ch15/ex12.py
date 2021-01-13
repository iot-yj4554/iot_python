# 클래스 메서드

# 일반적인 메서드는 인스턴스 메서드
# - 반드시 인스턴스를 만든 후에 사용 가능
# - 첫 번째 인자는 항상 인스턴스에 대한 참조 (self)

# 클래스 메서드는 인스턴스와 무관하게 존재
# - 인스턴스 없이도 클래스명을 통해 접근 가능
# - 첫 번째 인자는 클래스에 대한 참조 (cls)
# - @classmethod 로 정의

# 클래스 멤버 변수
# - class 안에서 self와 무관하게 정의되는 멤버 변수
# - 인스턴스와 무관하게 존재하며 모든 인스턴스가 공유하는 정보

class Car:
    count = 0 # 클래스 멤버 변수

    def __init__(self, name):
        self.name = name
        Car.count += 1
    
    @classmethod
    def outcount(cls):
        print(cls.count)


pride = Car('프라이드')
korando = Car('코란도')
morning = Car('모닝')

pride.outcount()
Car.outcount()