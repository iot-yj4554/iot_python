# 지역 함수
# 함수 안에 함수를 정의해서 사용
# - 함수가 정의된 함수 내에서만 사용 가능 (함수의 이름 충돌 방지)
# - 함수를 리턴한 경우 함수 밖에서도 사용 가능

def calcsum(n):
    def add(a,b):
        return a+b
    
    total = 0
    for i in range(n+1):
        total = add(total,i)

    return total

print('~10 = ', calcsum(10))

# ex2
def makeHello(message):
    def hello(name):
        print(f'{message}, {name}')
    
    return hello # hello 함수의 참조값 리턴

enghello = makeHello('Good Morning')
kohello = makeHello('안녕하세요')

enghello('Mr kim')
kohello('홍길동')
