# publisher (센서)

from threading import Thread
import time
import random
import paho.mqtt.client as mqtt

HOST = 'localhost'

class Sensor(Thread):
    def __init__(self, interval, range, topic):
        super().__init__()
        self.interval = interval
        self.range = range
        self.topic = topic

        self.client = mqtt.Client()

    def run(self):
        self.client.connect(HOST)

        while True:
            time.sleep(self.interval)
            value = random.uniform(*self.range)
            print(self.topic, value)

            self.client.publish(self.topic, value)
            self.client.loop(2)


if __name__ == '__main__':
    temp_sensor = Sensor(5, (3,10), 'iot/user1/temp')
    temp_sensor.start()
