from machine import Pin, I2C
from dht12 import DHT12
from umqtt.simple import MQTTClient
import time

def poll_sensor():
    i2c = I2C(scl = Pin(5), sda = Pin(4))
    sensor = DHT12(i2c)
    sensor.measure()
    t = sensor.temperature()
    h = sensor.humidity()
    return t, h

def publish(t, h):
    c=MQTTClient('my_sensor', 'iot.eclipse.org') #change my_sensor!!
    c.connect()
    c.publish('RIFF/phil/temperature', str(t)) # change the topic tree!
    c.publish('RIFF/phil/humidity', str(h)) # change the topic tree!
    c.disconnect()

while True:
    t, h = poll_sensor()
    publish(t, h)
    time.sleep(60)
