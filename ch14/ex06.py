# 파일을 읽어서 내가 원하는 형식으로 리턴하는 함수
# ex) csv 파일을 읽어서 dictionary 형식으로 리턴하기

# pickle : 파이썬 자료형 / 반드시 binary 모드로 오픈해야 함 / 다른 언어와 호환성은 없음
# 저장하기 : pickle.dump(data, file) -> 파일은 'wb'로 오픈한 파일 객체 (binary)
# 불러오기 : pickle.load(file) -> 파일은 'rb'로 오픈한 파일 객체 (binary)
import pickle

# 파일을 열어 라인으로 리턴하는 함수
def load(fpath):
    with open(fpath, 'rt', encoding='utf-8') as f:
        return f.readlines() # 라인의 리스트 형식
        
# 학생 이름 : key, 성적 리스트 : value --> 사전으로 만드는 함수
def convert(lines):
    data = {} # data 변수는 stack에, 빈 사전은 heap에 저장됨
    for line in lines[1:]:
        line = line.replace('\n', '') # 개행문자 삭제
        name = line.split(',')[0] # 학생 이름
        scores = line.split(',')[1:] # 성적들
        data[name] = list(map(int,scores)) # int로 변경 후 사전으로 등록
        
        # TIP: map함수를 이용하여 개행문자가 포함된 문자를 int로 변환하여도 영향을 미치지 않음
        # 이를 white 문자라고 함 (공백, 엔터, 탭 ...)
    
    return data # heap에 있는 사전의 참조값을 리턴

# load 함수에서 예외 처리를 하면, 아래 load 라인은 괜찮지만 print 라인이 또 다시 오류 발생        

# 저장 함수
def save(fpath, data):
    with open(fpath, 'wb') as f:
        pickle.dump(data,f)

# 흐름 제어 함수
def main():
    try:
        lines = load('data.csv')
        # fpath = input('파일명 : ') # 파일명을 받아서 열 수도 있음
        # lines = load(fpath)
        data = convert(lines)
        # print(data) # 확인용
        save('data.dat',data)

    except Exception as e:
        print('예외 발생 : ', e)

main()

# print(data) -> 이는 오류 발생 / main 함수에서 data를 리턴하지 않았기 때문

# \u : 유니코드
# feff : 어떤 문자열로 코딩되었는지 일종의 식별자