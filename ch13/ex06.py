# assert 조건, 메세지 (단정문)
# 조건이 True이면 통과
# False이면 메세지를 가지는 예외 발생
# "이 조건이 맞는지 지금 당장 확인하라"

score = 128
assert score <= 100, '점수는 100 이하여야 합니다.'
print(score)
