# datetime 모듈
# 이것도 참조형임 (숫자, bool 만 기본형)
import datetime

now = datetime.datetime.now()
print(f'{now.year}년 {now.month}월 {now.day}일')
print(f'{now.hour}시 {now.minute}분 {now.second}초')