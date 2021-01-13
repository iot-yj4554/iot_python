# ex01이 모듈로 사용됨
# - ex01의 파일명이 출력됨

import ex01
import m1

print('ex02.py', __name__)
print(m1.calcsum(20))

if __name__ == '__main__':
    print('모듈이 아닙니다.')
else:
    print('모듈입니다.')

print(dir(m1)) # 모듈에 있는 함수들을 알려줌 (자주 쓰임)
print(m1.__file__)