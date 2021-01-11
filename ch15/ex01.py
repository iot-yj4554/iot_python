# class -> 객체 (object)
# 생성자 이름은 대문자로 쓰기, 복합문자는 이어서 대문자로 쓰기 -> 파스칼 표기법
# 클래스에서 함수는 메서드, 변수는 인스턴스 라고 표현함
# 사용하기 위해서는 인스턴스를 생성한 후 사용
# 특정 인스턴스의 상태를 저장하기 위해 사용하는 것 -> 멤버변수(필드) -> self.()

class Account:
    def __init__(self, balance): # 생성자 함수 (constructor)
        self.balance = balance # self 는 handling 할 인스턴스의 참조 변수 / 파이썬에서는 항상 첫번째에 붙여주어야함
        # self.balance는 heap에, balance는 스택에 있는 데이터임
        # heap에 self.balance라는 필드를 만들어 주기 위해 쓰는 것
    def deposit(self, money):
        self.balance += money

    def inquire(self):
        print(f'잔액은 {self.balance}원 입니다.')

account = Account(8000) # Account의 인스턴스 생성
account.deposit(1000)
account.inquire()
# print(account) # self 값을 나타냄 / 즉 인스턴스의 참조값

shinhan = Account(8000)
shinhan.deposit(1000)
shinhan.inquire()

nonghyup = Account(1200000)
nonghyup.inquire()

# 여러개의 인스턴스를 생성한다고 해서 여러개의 동일한 메서드를 저장하는 것이 아님
# 클래스의 메서드는 한번만 메모리에 올라옴
# 컨트롤 누른 채로 메서드를 마우스 클릭하면 해당 함수로 스크롤해줌