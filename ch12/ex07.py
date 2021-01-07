# time.strftime 문자열로 표현해주는 함수

import time

timestr1 = time.strftime('%Y-%m-%d', time.localtime())
print(timestr1)

timestr2 = time.strftime('%H:%M:%S', time.localtime())
print(timestr2)

# Y : 4자리 년도
# y : 2자리 년도
# m : 월
# d : 일
# H : 시간 (24시간)
# I : 시간 (12시간)
# M : 분
# S : 초