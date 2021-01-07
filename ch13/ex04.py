# 예외 처리
# raise : 개발자에 의해 임의로 예외를 발생시킴

# n이 입력되었을 때 1부터 n까지의 합을 리턴하는 함수
# 양수가 아닌 음수가 입력되었을때 강제로 예외 발생시킴

def calcsum(n):
    if n <= 0:
        raise ValueError # 예외 발생 시킴

    total = 0
    for i in range(n+1):
        total += i
    
    return total

try:
    print('1부터 10까지의 합 = ', calcsum(10))
    print('1부터 -5까지의 합 = ', calcsum(-5))
except ValueError:
    print('입력값이 잘못되었습니다.')