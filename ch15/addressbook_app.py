# 모델 객체 ---> 주로 데이터만 관리하는 용도로 사용하는 객체

from app_base import Application
from models import AddressBook

# 최상위 계층 ---> 어플리케이션 운영 및 관리
class AddressBookApp(Application):
    def __init__(self):
        super().__init__()
        self.addressbook = AddressBook()
        self.addressbook.load(self.config)
        
    def create_menu(self, menu):
        self.menu.add('목록', self.print_book) # print_book() 이라고 쓰면 이 메서드의 리턴값을 넘겨주기 때문에 괄호를 쓰면 안됨
        self.menu.add('상세보기', self.print_detail)
        self.menu.add('검색', self.search)
        self.menu.add('추가', self.add)
        self.menu.add('수정', self.update)
        self.menu.add('삭제', self.delete)
        self.menu.add('종료', self.exit)
    
    def print_book(self):
        print('='*50)
        print('주소록')
        print('='*50)
        for ix, entry in enumerate(self.addressbook.book):
            print(f'{ix+1:02d}. {entry.name} : {entry.phone}, {entry.email}, {entry.addr}')

    def print_detail(self):
        index = int(input('대상 선택 (번호): '))
        entry = self.addressbook.book[index-1]
        print()
        print(f'이름 : {entry.name}')
        print(f'전화번호 : {entry.phone}')
        print(f'이메일 : {entry.email}')
        print(f'주소 : {entry.addr}')

    def search(self): # 부분 일치 검색 (키워드 검색)
        keyword = input('검색어 : ')
        result = self.addressbook.search(keyword)
        print('='*50)
        print(f'검색 결과 ({len(result)}건)')
        print('='*50)
        for index, entry in enumerate(result):
            print(f'{index+1:02d}) {entry.name} : {entry.phone}, {entry.email}, {entry.addr}')

    def add(self):
        print('\n<새 주소록 항목 추가>\n')
        name = input('이름 : ')
        phone = input('전화번호 : ')
        email = input('이메일 : ')
        addr = input('주소 : ')
        self.addressbook.add(name, phone, email, addr)
        print('\n등록이 완료되었습니다.')

    def update(self):
        index = int(input('대상 선택 (번호): '))
        entry = self.addressbook.book[index-1]
        print('주소록 항목 수정')

        name = input(f'이름({entry.name}) -> ')
        if name.strip() == '':
            name = entry.name
        phone = input(f'전화번호({entry.phone}) -> ')
        if phone.strip() == '':
            phone = entry.phone
        email = input(f'이메일({entry.email}) -> ')
        if email.strip() == '':
            email = entry.email
        addr = input(f'주소({entry.addr}) -> ')
        if addr.strip() == '':
            addr = entry.addr
        
        self.addressbook.update(index-1, name, phone, email, addr)
        
    def delete(self):
        index = int(input('대상 선택 (번호): '))
        entry = self.addressbook.book[index-1]
        if input(f'{entry.name}님을 정말로 삭제할까요? (y/n) ') == 'y':
            self.addressbook.delete(index-1)

    def destroyed(self):
        self.addressbook.save(self.config)


# main 함수
def main():
    app = AddressBookApp()
    app.run()

main()



# 기존 방법 : 절차 중심 ---> Top down (main부터 만듬)
# OOP : 객체 중심 ---> Bottom up (main을 가장 나중에 만듬)

# 객체 지향 설계 원칙
# 1) SRP (Single Responsibility Principle) : 단일 책임의 원칙
# 2) OCP (Open Close Principle) : 확장에는 열려있고 (기능), 변화에는 닫혀있음을 의미


# <주소록의 설계 구조>
# Application (부모)
#     AddressBookApp
#     Configuration (부모)
#     Menu (부모)
#         MenuItem
#     AddressBook
#         AddressBookEntry


# <일기장의 설계 구조>
# Application ---> (부모 / 일부만 사용)
#     DiaryApp
#     Configuration (부모)
#     Menu (부모)
