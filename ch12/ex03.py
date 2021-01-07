# time 모듈 (굉장히 많이 쓰임)

import time

# 1970년 1월 1일 자정을 기준으로 경과한 시간을 초 단위로 표현 
# 에폭 (Epoch) 시간 또는 유닉스 시간 이라고 함
# Timezone : 영국 그리니치
print(time.time())

# 문자열 시간
print(time.ctime())

# 현지 시간 (운영체제에 설정되어있는 지역)
# 여러가지 요소를 리턴해줌
print(time.localtime())

# 원하는 포맷으로 시간 출력해보기
now = time.localtime()
print(f'현재 시각은 {now.tm_year}년 {now.tm_mon}월 {now.tm_mday}일 {now.tm_hour}시 {now.tm_min}분 {now.tm_sec}초 입니다.')

