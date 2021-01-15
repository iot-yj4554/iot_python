import json

dic1 = {
    'file_name' : 'C:/iot_python/plus/network_programming/data.jpeg',
    'file_size' : 31978
}


# 사전 (파이썬 자료 구조 객체) ---> 문자열로 표현
msg = json.dumps(dic1)
print(type(msg))
print(msg)

# 문자열 msg를 수신
# 문자열 ---> 사전 객체로 복원
dic2 = json.loads(msg)
print(type(dic2))
print(dic2)

# 리스트도 가능
list1 = [dic1, dic1]

list_msg = json.dumps(list1)
print(type(list_msg))
print(list_msg)

list2 = json.loads(list_msg)
print(type(list2))
print(list2)


# .ini 파일은 구조화 시키기 어려움
# json 파일은 사전 뿐만 아니라 파이썬의 자료 구조 모두를 문자열로 표현 가능