import time
import dht12
from machine import I2C, Pin
from umqtt.simple import MQTTClient

i2c = I2C(scl=Pin(5), sda = Pin(4))
sensor = dht12.DHT12(i2c)

c=MQTTClient('phil_sensor1', 'iot.eclipse.org')

while True:
    sensor.measure()
    temp = sensor.temperature()
    humidity = sensor.humidity()
    print('temp is: ', temp)
    print('humidity is : ', humidity)
    c.connect()
    c.publish('RIFF/philip/temperature', str(temp))
    c.publish('RIFF/philip/humidity', str(humidity))
    c.disconnect()
    time.sleep(10)
