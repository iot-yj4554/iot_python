# 연산자 메서드
# 연산자를 재정의 할 수 있는 함수
# 연산자 별로 함수명이 정해져 있음

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

kim = Human('김상형', 29)
sang = Human('김상형', 29)
moon = Human('문종민', 44)

print(kim == sang) # 왼쪽이(kim) self로, 오른쪽이(sang) other로 대입됨
print(kim == moon)