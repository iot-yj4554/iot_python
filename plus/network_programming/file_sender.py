import os
import socket
import json

HOST = '127.0.0.1'
PORT = 6000
FILE_PATH = 'C:/iot_python/plus/network_programming/image.jpeg'

def file_read(file_path):
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                break

            yield data

def file_info(fpath):
    # file_name = fpath.split('/')[-1]
    file_name = os.path.split(fpath)[1] # 튜플 리턴 (directory path, file name)
    file_size = os.path.getsize(fpath)
    
    return {
        'file_name' : file_name,
        'file_size' : file_size
    }



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST,PORT))

        finfo = file_info(FILE_PATH)

        # 파일 크기 전송
        print('전송 파일 이름 : ', finfo.get('file_name'))
        print('전송 파일 크기 : ', finfo.get('file_size'))

        msg = json.dumps(finfo)
        s.sendall(msg.encode()) # 숫자를 그대로 전송하면, byte로 변환할 때, CPU 제조사 마다 다른 방식으로 변환하기 때문에 문자열로 바꾼 후 encoding함

        # 준비 상태 수신
        isready = s.recv(1024).decode()
        if isready == 'ready':
            # 파일 전송
            for data in file_read(FILE_PATH):
                s.sendall(data)
            
            print('전송 완료')

    except Exception as e:
        print(e)

# 파일 크기 뿐만 아니라 파일명 등 다양한 정보를 보내려면 어떻게?
# json(JavaScript Object Notation) 파일을 사용하자