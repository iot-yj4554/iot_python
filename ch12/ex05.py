# 실행 시간 측정하기
import time

# ex) 1000번 루프를 돌며 출력하는 시간 측정
start = time.time()
for a in range(1000):
    print(a)
end = time.time()

print(end - start)

# ex) 1000번 루프를 돌며 계산하는 시간 측정
total = 0
start = time.time()
for a in range(1000):
    total += a
end = time.time()

print(end - start)