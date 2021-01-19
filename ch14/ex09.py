import sqlite3

con = sqlite3.connect('addr.db') # 세션 생성 / con ---> connection 약자
cursor = con.cursor() # 커서 객체 생성

cursor.execute('DROP TABLE IF EXISTS tblAddr')

cursor.execute('''
    CREATE TABLE tblAddr(
        name CHAR(16) PRIMARY KEY,
        phone CHAR(16),
        addr TEXT
    )
''')

cursor.execute("INSERT INTO tblAddr VALUES ('김상형', '123-4567', '오산')")
cursor.execute("INSERT INTO tblAddr VALUES ('한경은', '555-1004', '수원')")
cursor.execute("INSERT INTO tblAddr VALUES ('한주완', '444-1092', '대전')")

con.commit()

cursor.close()
con.close()
