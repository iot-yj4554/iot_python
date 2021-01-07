# .argv : 명령행 인수
# 그래픽 기반이 아닌 서버나 IoT 환경에서 명령어 뒤에 정보를 입력함
# 예제 : 달력 출력
# 인수 0개 : 현재 달의 달력을 보여줌 / 인수 1개 : 년도 / 인수 2개 : 년도&월

import calendar
import time
import sys

# 인수 0개 (파일명이 디폴트로 있기에 인수를 안넣어주면 len == 1임)
if len(sys.argv) == 1:
    t = time.time()
    tm = time.localtime(t)
    calendar.prmonth(tm.tm_year, tm.tm_mon)

# 인수 1개
elif len(sys.argv) == 2:
    print(calendar.calendar(int(sys.argv[1])))

# 인수 2개
elif len(sys.argv) == 3:
    calendar.prmonth(int(sys.argv[1]), int(sys.argv[2]))

# 인수 3개 이상
elif len(sys.argv) == 4:
    print('인수는 2개 이하여야 합니다.')
