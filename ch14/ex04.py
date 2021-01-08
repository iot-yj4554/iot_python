# 파일 읽기
# 앞의 예제를 더 쉽게 쓰기
# f.readlines() 사용

print('*** 간단한 방법 ***')
try:
    with open('live.txt', 'rt', encoding='utf-8') as f:
        rows = f.readlines()
        for line_num, row in enumerate(rows):
            print(f'{line_num+1} : {row}', end='')
        print()
except Exception as e:
    print('예외 발생 :', e)

# 더 간단한 방법 : text파일에 한하여 readlines를 사용하지 않아도 가능
print('*** 더 간단한 방법 ***')
try:
    with open('live.txt', 'rt', encoding='utf-8') as f:
        for num,line in enumerate(f,1):
            print(f'{num} : {line}', end='')
        print()
except Exception as e:
    print('예외 발생 :', e)