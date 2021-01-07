# random 모듈
import random

# .random() : 0~1 사이의 난수 리턴 (1은 미포함)
for i in range(5):
    print(random.random())

# 0 ~ n 사이의 난수를 리턴하고 싶을 때 : random.random() * n 
# n ~ n+m 사이의 난수를 리턴하고 싶을 때 : n + (random.random() * m)

# .randint(begin, end) : begin ~ end 사이의 '정수' 난수 리턴 (end 포함)
# .randrange(begin, end) : begin ~ end 사이의 '정수' 난수 리턴 (end 미포함)
# .uniform(begin, end) : begin ~ end 사이의 '실수' 난수 리턴 (end 미포함)

# .choice(시퀀스) : 시퀀스에서 랜덤하게 요소 선택하여 리턴
food = ['짜장면','짬뽕','탕수육','군만두']
print(random.choice(food))

# 인덱스를 랜덤으로 추출하여 동일한 작업 가능
i = random.randrange(len(food))
print(food[i])

# .shuffle(시퀀스) : 시퀀스의 내용을 랜덤하게 섞음
# 리턴값이 없으므로 변수에 저장 안됨 (list.sort()와 같음)
food = ['짜장면','짬뽕','탕수육','군만두']
print(food)
random.shuffle(food)
print(food)

# .sample(시퀀스, count) : 시퀀스에서 랜덤하게 count개의 요소 리턴
food = ['짜장면','짬뽕','탕수육','군만두']
print(random.sample(food,2))

# 로또 번호 추출해보기
nums = random.sample(range(1,46), 6)
nums.sort()
print(nums)

