# 정적 메서드
# 단순히 클래스 내에 정의되는 일반 함수
# - 클래스에 대한 어떠한 정보도 제공하지 않음
# - 첫 번째 인자가 정해져 있지 않음
# 비슷한 성격의 함수를 묶어서 관리하는 역할

class Car2:
    @staticmethod
    def hello():
        print('오늘도 안전 운행 합시다.')
    
    count = 0

    def __init__(self, name):
        self.name = name
        Car2.count += 1

    @classmethod
    def outcount(cls):
        print(cls.count)

Car2.hello()
