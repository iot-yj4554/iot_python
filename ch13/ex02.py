# 예외 처리
# while 문을 사용하여 예외가 발생하지 않을 때까지 루프 반복 실행
# 예외가 발생하지 않을 때에는 마지막에 break로 탈출

while True:
    str = input('점수를 입력하세요 : ')
    try:
        score = int(str)
        print('입력한 점수 :', score)
        break
    except:
        print('점수 형식이 잘못되었습니다.')

print('작업완료')
