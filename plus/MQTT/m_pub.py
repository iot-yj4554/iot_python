import paho.mqtt.client as mqtt
import random
import time

# 1. MQTT 클라이언트 객체 인스턴스화
def publish(host, topic, sec):
    client = mqtt.Client()

    try:
        while True:
            # 2. 브로커 연결
            client.connect(host)

            # 3. 토픽 메세지 발행
            client.publish(topic, random.randrange(0,20))
            client.loop(2)
            time.sleep(sec)

    except Exception as err:
        print('에러 : ', err)