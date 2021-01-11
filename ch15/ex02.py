class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.gender = None
        # self의 멤버 변수는 언제든지 추가할 수 있음

    def intro(self):
        print(f'{str(self.age)} 살 {self.name}  ({self.gender}) 입니다.')

    def change(self,gender):
        self.gender = gender

    # 멤버 변수들의 값을 보고 싶을 때 / print 함수에 쓰임 / 단독으로 쓰였을 때
    def __str__(self):
        return f'<Human {self.name}, {self.age}, {self.gender}>'

    # 핵심만 보고 싶을 때 / print 함수에 쓰임 / 컬랙션에 포함되어 단독이 아닐 때
    def __repr__(self):
        return f'<Human {self.name}>'


kim = Human('김상형', 29)
print(kim.name)
kim.name = '홍길동'
print(kim.name)
kim.gender = '남'
kim.intro()

print(kim)

# del kim.name
# kim.intro()

lee = Human('이승우', 45)
lee.intro()

# 멤버 변수들의 값을 보고 싶을 때 -> __str__
print(lee)

list1 = [kim, lee]

# 멤버 변수들의 값을 보고 싶을 때 -> __repr__
print(list1)


# AttributeError 는 없는 멤버 변수를 사용하였을 때 발생함