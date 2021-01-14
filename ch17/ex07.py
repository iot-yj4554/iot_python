# ex06을 파이썬의 데코레이터로 사용하여 간단하게 만듬

def outer(func):
    def wrapper():
        print('-'*20)
        func()
        print('-'*20)
    
    return wrapper

@outer # inner = outer(inner) 와 같음
def inner():
    print('결과를 출력합니다.')


inner()