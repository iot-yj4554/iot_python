# ex06.py에서 pickle.dump한 파일을 불러오기
# 명령 뒤에 파일명을 같이 입력하여 sys.argv 사용하기

import pickle
import sys

def load(fpath):
    with open(fpath,'rb') as f:
        return pickle.load(f)

def main(): 
    try:
        if len(sys.argv) != 2: # 파일명을 입력하지 않았을 때
            print('에러 : 파일명을 입력하세요')
            print('ex) python ex08.py <filename>')
            sys.exit(0)

        fname = sys.argv[1] # sys.argv[0] 는 현재 실행하는 파일임 
        data = load(fname)
        print(f'이진 데이터 파일을 불러옵니다.')
        print(data)
    except Exception as e:
        print('예외 발생 : ', e)

main()