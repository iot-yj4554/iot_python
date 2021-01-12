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


# 한 사람 주소 정보 담당
class AddressBookEntry():
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


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
        
        self.book.sort(key=lambda a: a.name)

    def add(self, name, phone, email, addr):
        entry = AddressBookEntry(name, phone, email, addr)
        self.book.append(entry)
        self.book.sort(key=lambda a: a.name)

    def delete(self, index):
        del self.book[index]

    def update(self, index, name, phone, email, addr):
        self.book[index].name = name
        self.book[index].phone = phone
        self.book[index].email = email
        self.book[index].addr = addr

        self.book.sort(key=lambda a: a.name)


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
        index = int(input('대상 선택 (번호): '))
        entry = self.addressbook.book[index-1]
        print()
        print(f'이름 : {entry.name}')
        print(f'전화번호 : {entry.phone}')
        print(f'이메일 : {entry.email}')
        print(f'주소 : {entry.addr}')
        # 이름으로 찾는것도 해보기

    def add(self):
        print('새 주소록 항목 추가')
        name = input('이름 : ')
        phone = input('전화번호 : ')
        email = input('이메일 : ')
        addr = input('주소 : ')
        self.addressbook.add(name, phone, email, addr)
        print('등록이 완료되었습니다.')

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

    def exit(self):
        sys.exit(0)


# main 함수
def main():
    app = Application()
    while True:
        menu = app.select_menu()
        app.run(menu)

main()
