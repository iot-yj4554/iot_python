# Aggregation 집합

class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
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


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance 

    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        if self.balance < money:
            raise Exception('잔액이 부족합니다.') # 클래스 Exceptionn 인스턴스 생성
        
        self.balance -= money
        return money
        
    def inquire(self):
        print(f'{self.owner}님의 잔액은 {self.balance}원 입니다.')


hong = Human('홍길동', 20, '남')
account = Account(hong, 8000) # Account의 인스턴스 생성
account.inquire()

try:
    account.deposit(1000)
    account.inquire()

    money = account.withdraw(3000)
    account.inquire()

    account.withdraw(8000)
    account.inquire()
except Exception as e:
    print('예외 :', e)