from machine import Pin, I2C
from dht12 import DHT12
from umqtt.simple import MQTTClient
import time
import network
import esp

def poll_sensor():
    i2c = I2C(scl = Pin(5), sda = Pin(4))
    sensor = DHT12(i2c)
    sensor.measure()
    t = sensor.temperature()
    h = sensor.humidity()
    return t, h

def wifi_init():
    sta = network.WLAN(network.STA_IF)
    sta.active(True)
    sta.connect("Wilko Wireless", "WilkoN600")
    if not sta.isconnected():
        time.sleep(0.5)

def publish(t, h):
    c=MQTTClient('my_sensor', 'iot.eclipse.org') #change my_sensor!!
    c.connect()
    c.publish('RIFF/phil/temperature', str(t)) # change the topic tree!
    c.publish('RIFF/phil/humidity', str(h)) # change the topic tree!
    c.disconnect()

def wifi_deinit():
    sta = network.WLAN(network.STA_IF)
    sta.active(False)

esp.sleep_type(esp.SLEEP_MODEM) #all sleep is modem sleep
while True:
    t, h = poll_sensor()
    wifi_init()
    publish(t, h)
    wifi_deinit()
    time.sleep(60)
