# threading 모듈
# Thread 클래스
# 스레드 운영 방법
# 1) Thread 에게 작업 함수를 전달해서 실행
# 2) Thread 클래스를 상속 받아 재정의
#   - run() 메서드 재정의
# 스레드의 기동
# - start() 호출

# threading.Thread() 함수를 호출하여 Thread 객체 생성
# - 생성자에 실행 함수와 인자를 전달
# Thread 객체의 start() 메서드 호출

import threading

count = 2 # 운영할 스레드의 개수

def sum(low, high):
    global count
    total = 0
    
    for i in range(low, high):
        total += i

    print('Subthread', total)
    count -= 1 # 스레드가 종료할 때 1 감소

t = threading.Thread(target=sum, args=(1,100000)) # 키워드 전달 방식
# target에는 실행할 함수 / args는 실행할 함수의 매개 변수 (1은 sum의 low, 100000은 sum의 high)

t.start() # thread 기동 / 반드시 해주어야 함

t2 = threading.Thread(target=sum, args=(1,100000)) 
t2.start()

while count != 0: # 운영되는 작업스레드가 모두 끝날 때 메인 스레드를 실행시키겠다는 의미
    pass

print('Main Thread') # main thread (작업 스레드보다 양이 적기 때문에 먼저 종료됨)