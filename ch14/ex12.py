import sqlite3

con = sqlite3.connect('addr.db') # 세션 생성 / con ---> connection 약자
cursor = con.cursor() # 커서 객체 생성

name = input('이름 : ')
phone = input('전화번호 : ')
addr = input('주소 : ')

cursor.execute(f"INSERT INTO tblAddr VALUES ('{name}', '{phone}', '{addr}')")
con.commit() # insert, update, delete 할 때 반드시 호출해야 실제 DB에 반영됨

cursor.close()
con.close()
