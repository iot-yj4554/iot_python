import MySQLdb
from app_base import Application
from dao import AddressBookDao

class AddrBookApp(Application):
    def __init__(self):
        super().__init__()
        # print(self.config)
        self.db = MySQLdb.connect(
            db = self.config['DB'], 
            host = self.config['HOST'], 
            user = self.config['USER'], 
            passwd = self.config['PASSWD'],
            charset = self.config['CHARSET'],
            use_unicode = True
            )

        self.cursor = self.db.cursor()
        self.addressbook_dao = AddressBookDao(self.cursor)
        self.PERPAGE = 20 # 한 페이지 당 출력 건수

    def create_menu(self, menu):
        menu.add('목록',self.print_list)
        menu.add('상세보기',self.print_detail)
        menu.add('검색',self.search)
        menu.add('추가',self.add)
        menu.add('수정',self.update)
        menu.add('삭제',self.delete)
        menu.add('종료',self.exit)

    def print_list(self):
        page = int(input('페이지 : '))
        pagination = self.addressbook_dao.get_page(page, self.PERPAGE)
        
        print()
        if page > pagination.total_page:
            print('잘못된 입력입니다. (페이지 초과)')
            return
        
        print('='*100)
        print(' '*40,'주소록')
        print('='*100,'\n')
        for e in pagination.datas:
            print(f'{e.num:8d})   {e.name:25s} {e.phone:20s} {e.email:30s} {e.addr}')

        # 현재 페이지 / 전체 페이지 (총 데이터 건수)
        print(f'\npage : {page} / {pagination.total_page}  (총 {pagination.total_count}건)')


    def print_detail(self):
        num = int(input('번호 : '))
        row = self.addressbook_dao.get(num)
        print()
        if not row:
            print(f'{num}은 없습니다.')
            return

        print(f'num : {row.num}')
        print(f'이름 : {row.name}')
        print(f'전화번호 : {row.phone}')
        print(f'이메일 : {row.email}')
        print(f'주소 : {row.addr}')

    def search(self): # 부분 일치 검색
        keyword = input('검색어 : ')
        rows = self.addressbook_dao.search(keyword)
        
        print('='*100)
        print(' '*37,'검색 결과 ', len(rows), '건')
        print('='*100,'\n')
        for e in rows:
            print(f'{e.num:8d})   {e.name:25s} {e.phone:20s} {e.email:30s} {e.addr}')


    def add(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    # def exit(self):
    #     self.destroyed()
    #     sys.exit(0)

    def destroyed(self): # 부모클래스의 메서드 오버라이드
        self.cursor.close()
        self.db.close()





if __name__ == '__main__':
    app = AddrBookApp()
    app.run()

# ORM (Object Relationship Model)