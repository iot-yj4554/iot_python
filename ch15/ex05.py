# 모델 객체 ---> 주로 데이터만 관리하는 용도로 사용하는 객체

import sys

# 설정 정보 담당
class Configuration:
    def __init__(self):
        config = self.load() # 중요함
        self.fname = config['FNAME']
        self.encoding = config['ENCODING']

    def load(self):
        config = {}
        with open('config.ini', 'rt') as f:
            entries = f.readlines()
            for entry in entries:
                key, value = entry.split('=')
                config[key.strip()] = value.strip()
        return config

    def __str__(self):
        return f'<Configuration fname : {self.fname} / Encoding : {self.encoding}>'

# 한 사람 주소 정보 담당
class AddressBookEntry():
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    # def make_book(self, name, phone, email, address):
    #     pass
    
    # def __str__(self):
    #     return f'<{self.name}, {self.phone}, {self.email}, {self.email}>'

    # def __repr__(self):
    #     return f'<{self.name}>'


""" # 단위 테스트 (unit test)

config = Configuration()
print(config)

entry = AddressBookEntry('홍길동', '010-1234-1234', 'hong@gmail.com', '서울')
print(entry) # __str__
print([entry]) # __repr__ """


# 여러개의 entry를 관라하는 클래스 ---> book list 관리
class AddressBook:
    def __init__(self):
        self.book = []

    def load(self, config):
        with open(config.fname, 'rt', encoding=config.encoding) as f:
            lines = f.readlines()[1:]
            for line in lines:
                if line == '\n':
                    continue
                else:
                    name, phone, email, addr = line.replace('\n','').split(',')
                    entry = AddressBookEntry(name, phone, email, addr)
                    self.book.append(entry)
        
        # 정렬을 하지만 key 값을 주지 않으면'참조값'으로 정렬됨
        self.book.sort(key=lambda a: a.name)

    # def add(self, name, phone, email, addr):
    #     pass

    # def delete(self, name):
    #     pass

    # def update(self, name, phone, email, addr):
    #     pass

    # def __str__(self):
    #     return f'<{self.book}>'

# config = Configuration()
# book = AddressBook()
# book.load(config)
# print(book)

# 최상위 계층 ---> 어플리케이션 운영 및 관리
class Application:
    def __init__(self):
        self.config = Configuration()
        self.addressbook = AddressBook()
        self.addressbook.load(self.config)

    def select_menu(self):
        print()
        print('1)목록  2)상세보기  3)추가  4)수정  5)삭제  6)종료')
        menu = int(input('입력 : '))
        print()
        return menu

    def run(self, menu):
        if menu == 1:  # 목록
            self.print_book()
        elif menu == 2: # 상세보기
            self.print_detail()
        elif menu == 3: # 추가
            self.add()
        elif menu == 4: # 수정
            self.update()
        elif menu == 5: #삭제
            self.delete()
        elif menu == 6: # 종료
            self.exit()
        else:
            print('잘못 선택하였습니다. 다시 선택해 주세요.')
    
    def print_book(self):
        print('='*50)
        print('주소록')
        print('='*50)
        for ix, entry in enumerate(self.addressbook.book):
            print(f'{ix+1:02d}. {entry.name} : {entry.phone}, {entry.email}, {entry.address}')

    def print_detail(self):
        pass
        # find_name = input('찾는 사람의 이름을 입력하세요 : ') # 완전 일치 검색
        # if find_name in self.addressbook.book.name:
        #     print(f'*** {self.addressbook.book.name} : {self.addressbook.book.phone}, {self.addressbook.book.email}, {self.addressbook.book.address} ***')
        # else:
        #     print(f'{find_name} 님은 목록에 없습니다.')
        # print()

    def add(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def exit(self):
        sys.exit(0)

# main 함수
def main():
    app = Application()
    while True:
        menu = app.select_menu()
        app.run(menu)

main()

# config = Configuration()
# book = AddressBook()
# book.load(config)
# print(book)

# 기존 방법 : 절차 중심 ---> Top down (main부터 만듬)
# OOP : 객체 중심 ---> Bottom up (main을 가장 나중에 만듬)

# Application
#     Configuration
#     AddressBook
#         AddressBookEntry