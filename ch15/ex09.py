# 엑세서
# 파이썬은 기본적으로 정보 은폐 기능을 지원하지 않음
# getter / setter로 정보 (프로퍼티) 보호

class Date:
    def __init__(self, month):
        self.inner_month = month
    
    @property # getter와 setter로 접근 가능하다는 의미
    def month(self):
        return self.inner_month

    @month.setter # setter : property.setter 형식
    def month(self, month):
        if 1 <= month <= 12:
            self.inner_month = month

today = Date(8)
today.month = 15

print(today.month)
