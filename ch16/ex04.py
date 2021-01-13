# 패키지
# 모듈들을 모아 놓은 디렉토리
# 반드시 __init__.py 가 존재하야 함
# - 일반적으로 내용은 없음

# from <패키지.디렉토리> import <모듈>

from mypack.calc import add
import sys

add.outadd(1,2)
print(sys.builtin_module_names) # 어떤 모듈들이 있는지 보여줌
