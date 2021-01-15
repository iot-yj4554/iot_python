from mqtt_sub import subscribe
import time

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

subscribe('localhost', 'iot/#', on_message, forever=False)

time.sleep(5)
print('End')