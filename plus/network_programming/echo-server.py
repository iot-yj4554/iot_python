import socket

HOST = '127.0.0.1' # 특수 주소 : 자기 자신의 주소임
PORT = 9999

# 주소 체계 (address family): IPv4, 소캣 타입: TCP
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 이 인자는 디폴트이므로 생략할 수 있음
server_socket = socket.socket()

# 이미 열린 포트 충돌 시 재 사용 옵션 설정
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST,PORT))
server_socket.listen()


# accept 함수에서 대기, 클라이언트 접속 시 새로운 소켓을 리턴
client_socket, addr = server_socket.accept()

# 접속한 클라이언트의 주소 출력
print('Connected by ', addr)

while True:
    # 메시지 수신 대기
    data = client_socket.recv(1024) # 데이터 크기를 1024(1K) 로 버퍼의 크기를 정함
    if not data:
        break
    
    # data (byte array)를 문자열로 변환하여 출력
    print(f'Received from {addr} : {data.decode()}')

    # 받은 문자열을 다시 클라이언트로 전송 (에코)
    client_socket.sendall(data)

client_socket.close()
server_socket.close()