# ex05를 변형한 코드

def inner():
    print('결과를 출력합니다.')

def outer(func):
    def wrapper():
        print('-'*20)
        func()
        print('-'*20)
    
    return wrapper

inner = outer(inner)
inner() # 함수 inner()를 호출한 것처럼 보이지만 사실은 wrapper()임
