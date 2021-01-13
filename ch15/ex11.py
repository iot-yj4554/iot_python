# 액세서
# 프라이빗 멤버 변수 : 멤버 변수 앞에 __을 붙이면 외부에서 바로 접근 불가

class Date2:
    def __init__(self, month):
        self.__month = month

    def getmonth(self):
        return self.__month

    def setmonth(self, month):
        if 1 <= month <= 12:
            self.__month = month

    month = property(getmonth, setmonth)

today = Date2(8)
today.month = 15

print(today.month)
print(today.__month) # 예외 발생