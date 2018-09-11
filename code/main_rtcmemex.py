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
    sta.connect("SSID", "password")
    if not sta.isconnected():
        time.sleep(0.5)

def publish(t, h):
    c=MQTTClient('my_sensor', 'iot.eclipse.org') #change my_sensor!!
    c.connect()
    c.publish('RIFF/phil/temperature', str(t)) # change the topic tree!
    c.publish('RIFF/phil/humidity', str(h)) # change the topic tree!
    c.disconnect()

def goto_sleep():
    rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)
    rtc.alarm(rtc.ALARM0, (10000))
    machine.deepsleep()

rtc = machine.RTC()

if machine.reset_cause()!= machine.DEEPSLEEP_RESET:
    print('not woken from ds')
    time.sleep(20) #allows time to ctrl+C
    data = poll_sensor()
    rtc.memory(str(data))
    print(rtc.memory())
    goto_sleep()

else:
    mem = rtc.memory().decode('utf-8')
    mem = mem.split(',')
    data=poll_sensor()
    mem.append(str(data))
    if len(mem)>=5:
        print('data collection complete: ', mem)
        publish(mem, 'h')
    else:
        mem=','.join([str(i) for i in mem])
        rtc.memory(mem)
        print(rtc.memory())
        goto_sleep()
