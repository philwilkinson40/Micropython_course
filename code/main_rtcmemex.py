#simplified code to illustrate RTC.memory

from machine import Pin, I2C
from dht12 import DHT12
from umqtt.simple import MQTTClient
import time
import network
import machine

def poll_sensor():
    i2c = I2C(scl = Pin(5), sda = Pin(4))
    sensor = DHT12(i2c)
    sensor.measure()
    t = sensor.temperature()
    return t

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

if machine.reset_cause()!= machine.DEEPSLEEP_RESET:
    time.sleep(20) #allows time to ctrl+C
    rtc.memory('')

mem = rtc.memory().decode('utf-8')
mem = mem.split(',') #allows list manipulation

mem.append(poll_sensor())

if len(mem)>=12:
    wifi_init()
    c=MQTTClient(config.client_id, config.MQTT_server)
    c.connect()
    mem=','.join([str(i) for i in mem])
    c.publish('RIFF/datadump', mem)
    c.disconnect()
    rtc.memory('')
else:
    mem.append(new_data)
    mem=','.join([str(i) for i in mem])
    rtc.memory(mem)
