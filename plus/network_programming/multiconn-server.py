import socket
from _thread import *

# echo server
def threaded(client_socket, addr):
    print(f'Connected by {addr[0]} : {addr[1]}')

    while True:
        try:
            # 데이터가 수신되면 클라이언트에 다시 전송합니다.
            data = client_socket.recv(1024)
            if not data:
                print(f'Disconnected by {addr[0]} : {addr[1]}')
                break
            
            print(f'Received from {addr[0]} : {addr[1]}', data.decode())
            client_socket.sendall(data)

        except ConnectionResetError as e: # 비정상적인 종료가 발생하였을 때
            print(f'Disconnected by {addr[0]} : {addr[1]}')
            break

    client_socket.close()

HOST = '127.0.0.1'
PORT = 9999

server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST, PORT))
server_socket.listen()

print('server start')

while True:
    print('wait')
    client_socket, addr = server_socket.accept()
    start_new_thread(threaded, (client_socket, addr))

server.socket.close()