# 두 글자씩 슬라이싱하여 for문 돌기

# 파이썬의 모든 class는 최상위 객체인 object를 자동으로 상속받음
class Seq:
    def __init__(self, data):
        self.data = data
        self.index = -2

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 2
        if self.index >= len(self.data):
            self.index = -2
            raise StopIteration

        return self.data[self.index:self.index+2]

    def __eq__(self, other): # object의 __eq__ 메서드를 오버라이드함
        return self.data == other

solarterm1 = Seq('입춘우수경칩춘분청명곡우입하소만망종하지소서대서')
solarterm2 = Seq('입춘우수경칩춘분청명곡우입하소만망종하지소서대서')

# for k in solarterm1:
#     print(k, end=',')

# print()

# for k in solarterm1:
#     print(k, end=',')

# print()

# # print(dir(solarterm1)) # object 객체로부터 상속받은 것들이 같이 들어있음
# print(solarterm1 == solarterm2) # object 객체의 __eq__ 메서드는 참조값을 기준으로 판정하기에 False임 / 따라서 따로 오버라이드 해줌

print(solarterm1.__dict__) # 개발자가 정의한 멤버 변수를 보여줌 / __dict__도 멤버 변수지만, 개발자가 직접 추가한 것이 아니므로 나오지 않음
print(solarterm1.__dir__()) # = print(dir(solarterm1))