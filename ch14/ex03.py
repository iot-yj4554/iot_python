# 파일 읽기
# 한 줄씩 읽어서 문장 번호를 앞에 출력해주기

try:
    with open('live.txt', 'rt', encoding='utf-8') as f:
        text = ''
        line = 1
        while True:
            row = f.readline()
            if not row:
                break
            text += str(line) + ':' + row
            line += 1
except Exception as e:
    print('예외 발생 :', e)

print(text)