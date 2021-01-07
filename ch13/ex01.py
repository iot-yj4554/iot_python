# 예외 처리 : try ~ except 구문
# 이를 처리하지 않으면 default로 프로그램이 종료됨
# 아래 코드는 에러가 나면 에러 메세지만 내보내고 프로그램이 종료됨

str = '89점'
try:
    score = int(str)
    print(score)
except:
    print('예외가 발생하였습니다.')

print('작업 완료')