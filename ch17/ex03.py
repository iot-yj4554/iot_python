# 제너레이터
# 객체로 순회 가능한 객체를 만드는 것은 다소 귀찮은 작업
# 제너레이터 함수로 대체 가능
# 함수에서 데이터를 연속해서 리턴 (yield)
# 함수가 끝나면 (또는 return 실행) StopIteration 예외 발생
# 함수를 호출하면 함수가 실행되는 것이 아니고 순회 가능 리턴
# 순회 가능 객체로 순회할 때 실제 함수가 실행됨

def seqgen(data):
    for index in range(0, len(data), 2): # __next__ 메서드를 의미
        yield data[index:index+2] # 값은 주되, 로직 유지 / StopIteration 이 발생하면 종료됨

solarterm = seqgen('입춘우수경칩춘분청명곡우입하소만망종하지소서대서')
print(solarterm) # generator 객체로 출력
print(dir(solarterm)) # __iter__와 __next__ 가 존재함

for k in solarterm:
    print(k, end=',')