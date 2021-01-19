import sqlite3

con = sqlite3.connect('addr.db')
cursor = con.cursor()

name = input('검색할 이름을 입력하세요 : ')
cursor.execute(f'SELECT addr FROM tblAddr WHERE name = "{name}"')

record = cursor.fetchone() # 튜플 리턴
print(type(record), record)

if record:
    print(f'{name} 님은 {record[0]}에 살고 있습니다.')
else:
    print(f'{name} 님은 없는 이름입니다.')


cursor.close()
con.close()