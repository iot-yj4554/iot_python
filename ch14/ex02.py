# 파일 읽기
# f.read() -> 파일 전체 내용
# f.read(n) -> n개의 내용 (binary 파일일 때만 씀 / 텍스트 파일은 잘 안씀)
# f.readline() -> 한 줄
# f.readlines() -> 전체 라인 리스트 
# (각 라인 끝에 개행 문자 들어 있음)

# I/O 작업은 예외 처리를 꼭 해주는게 좋음
# 파일이 있을수도 없을수도 있기 때문임

try:
    # f = open('live.txt', 'rt', encoding='utf-8') # 좋지 못한 코드
    with open('live.txt', 'rt', encoding='utf-8') as f: # with : 파일 진입을 하고 with를 벗어날 때 자동으로 .close()를 해줌
        text = f.read()
        print(text)
except Exception as e: # Exception : 에러 종류에 상관 없이 모두 처리해줌
    print(e)

# open과 close를 짝으로 사용 할 때 with를 쓴다.
# with는 예외 발생 시 벗어나게 되며 자동으로 close를 호출함