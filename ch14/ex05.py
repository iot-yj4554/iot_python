# 파일 입출력 위치
# seek(위치, 기준)
# 위치(offset) : 기준으로부터 얼마나 떨어진 곳인지 바이트 단위로 지정
# 한글에서는 주의 필요 -> 따라서 binary 코드에서 사용
# 기준
# 0: 파일의 처음 위치
# 1: 현재 위치
# 2: 파일의 끝 위치

try:
    with open('live.txt', 'rt', encoding='utf-8') as f:
        # f.seek(12,0) # 한글이 깨져서 오류남
        f.seek(13,0)
        # f.seek(0,2) # 맨 뒤로 이동
        # f.seek(0,0) # 맨 앞으로 이동
        text = f.read()
        print(text)
except Exception as e:
    print('예외 발생 :', e)
