# 클래스가 다른곳에서 중복되지는 않지만 나누어서 편하게 파일 관리하기 위해 만듬

# 한 사람 주소 정보 담당
class AddressBookEntry:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.addr = address


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
        
        # 정렬할 때 key 값을 주지 않으면'참조값'으로 정렬됨
        self.book.sort(key=lambda a: a.name)

    def save(self, config):
        with open(config.fname, 'wt', encoding=config.encoding) as f:
            f.write('이름,전화번호,email,주소\n')
            for entry in self.book:
                f.write(f'{entry.name},{entry.phone},{entry.email},{entry.addr}\n')

    def search(self, keyword):
        return list(filter(lambda entry: entry.name.find(keyword) != -1, self.book))

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