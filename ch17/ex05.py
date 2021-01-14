# 함수 데코레이터
# 이미 만들어진 함수에 동작을 추가하는 파이썬의 고급 기법
# 함수를 래핑 (Wrapping) 하여 함수의 앞 또는 뒤에 코드를 자동으로 추가
# 함수를 호출하면 추가된 앞, 뒤의 코드도 같이 실행됨

def inner():
    print('결과를 출력합니다')

def hello():
    print('안녕하세요')

def outer(func):
    print('-'*20)
    func()
    print('-'*20)

outer(inner)
outer(hello)
# 이렇게 하면 실제로는 inner를 실행시키는게 주목적인데, outer를 주목적으로 실행하는 것처럼 보임
