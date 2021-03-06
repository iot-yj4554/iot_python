# 모듈
# 변수와 함수를 모두 한 파일에 정의하면 관리가 힘들어짐
# - 비슷한 성격의 변수, 함수들을 파일 별로 나눠 정의
# - 이렇게 정의한 파일을 모듈이라고 함
# - 파일명이 모듈명이 됨

# 모듈 테스트
# __name__ 변수에 모듈명이 저장됨
# 단독으로 실행된 경우 (모듈로 사용된 것이 아님)
# - '__main__' 으로 지정됨
# 모듈로 사용된 경우(import에 의해 실행된 경우)
# - 파일명이 지정됨
# 모듈 개발시 모듈로 쓰였는지 테스트 할 수 있도록 지원

import m1

if __name__ == '__main__':
    print(m1.calcsum(10))

print('ex01.py', __name__)
