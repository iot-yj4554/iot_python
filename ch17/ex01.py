# 고급 문법
# 열거 가능 객체
# for 반복문의 순회 대상 객체
# 해당 객체의 __iter__() 메서드로 열거 가능 객체 획득
# - 열거 가능 개체는 __iter__() 메서드를 정의해야 함
# 매 루프마다 __next()__ 함수를 통해 다음 요소를 추출
# 더 이상 요소가 없는데 __next()__를 호출하는 경우
# StopIteration 예외가 발생하고 for 반복문을 끝냄

# for문의 내부 코드 모습임
# iter와 next가 가능한 개체만 사용 가능
nums = [11,22,33]

it = iter(nums)
while True:
    try:
        num = next(it)
    except StopIteration:
        break

    print(num)