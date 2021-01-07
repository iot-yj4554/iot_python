# sys 모듈 : 시스템 정보

import sys

print('버전 :', sys.version)
print('플랫폼 :', sys.platform)

# .exit() : 프로그램 종료 명령
# 매개변수 숫자에는 의미가 있음
# 1: 메모리 부족, 2: 데이터 오류 ....
# 개발자가 정하는 것
# 0: 정상적인 종료  => 이는 관례로 쓰임
while True:
    ans = input('명령 >> ')
    if ans == 'quit':
        sys.exit(0)

    print(ans)