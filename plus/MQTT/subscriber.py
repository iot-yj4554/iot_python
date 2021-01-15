# paho 모듈

import paho.mqtt.client as mqtt
import time

# 브로커 접속 시도 결과 처리 콜백 함수
def on_connect(client, userdata, flags, rc):
    print('Connected with result code', rc)
    if rc == 0:
        client.subscribe('iot/#') # 연결 성공 시 토픽 구독 신청
    else:
        print('연결 실패 : ', rc)

# 관련 토픽 메세지 수신 콜백 함수
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

# 1. MQTT 클라이언트 객체 인스턴스화
client = mqtt.Client()

# 2. 관련 이벤트에 대한 콜백 함수 등록
client.on_connect = on_connect
client.on_message = on_message

try:
    # 3. 브로커 연결
    client.connect('localhost')

    # 4. 메세지 루프 - 이벤트 발생 시 해당 콜백 함수 호출됨
    client.loop_forever()

    # client.loop_start() # 데몬 스레드

except Exception as err:
    print('에러 : ', err)


# time.sleep(10) # 메인 스레드
# print('End')