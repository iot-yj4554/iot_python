import socket
from _thread import *
import json

HOST = '127.0.0.1'
PORT = 6000
# FILE_PATH = 'C:/iot_python/plus/network_programming/data.jpeg'

def receive_thread(client_socket, addr):
    try:
        # 파일 크기 수신
        # size = client_socket.recv(1024)
        # size = int(size.decode())
        # print('수신할 파일 크기 : ', size)

        # json 문자열 수신
        msg = client_socket.recv(1024).decode()
        finfo = json.loads(msg)
        print(f'파일명 : {finfo.get("file_name")}, 파일 크기 : {finfo.get("file_size")}')

        name, extension = finfo.get('file_name').split('.')
        copy_name = name + '_copy.' + extension

        fpath = 'C:/iot_python/plus/network_programming/' + copy_name

        # 준비 상태 전송
        client_socket.send('ready'.encode())

        # 파일 수신
        total_size = 0
        with open(fpath, 'wb') as f:
            while True:
                data = client_socket.recv(1024) # socket.SOCKSTREM 때문에 보낸 크기와 받는 크기가 달라도 데이터 모두 다 받음
                f.write(data)
                total_size += len(data)

                if total_size >= finfo.get('file_size'):
                    break

            print(f'수신 완료 : {total_size} bytes')

    except Exception as e:
        print(e)
    
    finally:
        client_socket.close()


with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
    try:
        s.bind((HOST,PORT))
        s.listen(1)

        while True:
            client_socket, addr = s.accept() # 접속 대기
            start_new_thread(receive_thread, (client_socket,addr))

    except Exception as e:
        print(e)
