# 임포트 (보통 소스의 앞쪽에 작성)

# 1. 모듈 불러오기
import math
print(math.sqrt(2))

# 2. 모듈에서 원하는 함수만 불러오기
# (단 이름이 충돌될 경우에는 사용 불가)
# (콤마로 나열도 가능)
from math import sqrt, sin, cos
print(sqrt(2))

# 3. 별칭 사용하기
import math as mt
print(mt.sqrt(2))

# 4. 1~3 종합하기
from math import sqrt as sq
print(sq(2))