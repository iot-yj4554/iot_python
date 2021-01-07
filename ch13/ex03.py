# 예외 처리
# 어떤 에러가 발생했는지 알려줌

# NameError : 초기화하지 않은 변수 발생
# ValueError : 타입은 맞지만 값의 형식이 잘못되었다.
# ZeroDivisionError : 0으로 나누었다.
# IndexError : 첨자의 범위를 벗어났다.
# TypeError : 타입이 맞지 않다.

# 예외는 2개가 동시에 발생하지 않는다.

str = '89'
try:
    score = int(str)
    print(score)
    a = str[2]
except ValueError:
    print('점수의 형식이 잘못되었습니다.')
except IndexError:
    print('첨자 범위를 벗어났습니다.')

print('작업 완료')

# A 또는 B 에러가 발생하였을 때 묶을 수 있음

str = '89'
try:
    score = int(str)
    print(score)
    a = str[2]
except (ValueError, IndexError):
    print('점수의 형식이나 첨자가 잘못되었습니다.')

print('작업 완료')

# 예외 객체 메세지를 print로 출력할 수도 있음

str = '89점'
try:
    score = int(str)
    print(score)
    a = str[2]
except ValueError as e:
    print(e)
except IndexError as e:
    print(e)

print('작업 완료')