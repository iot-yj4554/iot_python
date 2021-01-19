import sqlite3

con = sqlite3.connect('addr.db') # 세션 생성 / con ---> connection 약자
cursor = con.cursor() # 커서 객체 생성

cursor.execute('SELECT * FROM tblAddr')

# table = cursor.fetchall() # 전체 패치 (리스트형)

# for record in table: # record는 튜플
#     print(f'이름 : {record[0]}, 전화 : {record[1]}, 주소 : {record[2]}')

# for name, phone, addr in table:
#     print(f'이름 : {name}, 전화 : {phone}, 주소 : {addr}')

while True:
    record = cursor.fetchone() # 하나씩 패치 (튜플형)
    if record == None:
        break
    
    print(f'이름 : {record[0]}, 전화 : {record[1]}, 주소 : {record[2]}')


cursor.close()
con.close()
