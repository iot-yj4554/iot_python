# DAO : Data Access Object

import math
from models import AddressBookEntry

class Pagination:
    def __init__(self, total_count, total_page, datas):
        self.total_count = total_count
        self.total_page = total_page
        self.datas = datas


# Addressbook 의 db 처리 담당 ---> SQL 처리
class AddressBookDao:
    def __init__(self, cursor):
        self.cursor = cursor

    def get_total_count(self):
        query = f'select count(*) from addressbook'
        self.cursor.execute(query)
        return self.cursor.fetchone()[0] # fetchone()은 튜플 리턴이므로 첫번째 값만 리턴

    def get_list(self, start, perpage): # 페이지
        query = f"select * from addressbook order by name limit {start},{perpage}"
        self.cursor.execute(query)
        rows = self.cursor.fetchall() # 튜플의 튜플 또는 빈 튜플 리턴
        return (AddressBookEntry(*row) for row in rows) # 컴프리핸션을 이용한 변환

    def get_page(self, page, perpage):
        start = (page-1) * perpage
        total_count = self.get_total_count()
        total_page = math.ceil(total_count/perpage)
        rows = self.get_list(start,perpage)

        return Pagination(total_count, total_page, rows)

    def get(self,num): # 한 개
        query = f'select * from addressbook where num = {num}'
        self.cursor.execute(query)
        row = self.cursor.fetchone() # 튜플 또는 None 리턴
        if row:
            return AddressBookEntry(*row)
        else:
            return None

    def search(self, keyword):
        keyword = keyword.lower()
        query = f'select * from addressbook where lower(name) like "%{keyword}%" '
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return (AddressBookEntry(*row) for row in rows)

    def add(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass