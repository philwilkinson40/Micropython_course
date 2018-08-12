 ### Micropython MeetUp - PDPD August 2018
![](https://docs.pycom.io/img/micropython.jpg)

<!--
MeetUp workshop to complete the use case introduced in the initial introduction session
-->

---

### Information Sources

- [micropython website ](https://micropython.org) and [forum](https://forum.micropython.org/)
- PDPD Micropython [Github repo](https://github.com/philwilkinson40/Micropython_course)
- Adafruit and Core electronics offer good online tutorials
- will anyone use a list of online resources?

---

### interacting with the esp8266 ###

1. REPL interaction via serial USB: [micropython.org](https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/repl.html)
2. file transfer to/from onboard
 - [RSHELL](https://github.com/dhylands/rshell) is a simple shell, developed in python; good support on [Micropython forum](https://forum.micropython.org/)  
 - [mpfshell](https://github.com/wendlers/mpfshell) following [these instructions](https://gist.github.com/hardye/657385210c5d613e69cb5ba95e8c57a7)
 - [AMPY](https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy) from Adafruit
 - [WEBREPL](https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/repl.html#webrepl-a-prompt-over-wifi) via wifi

---

### ISR Interupt Service Routines
defined as callback functions
triggered as a result of
- a timer
- a pin state change

can occur while the system is in idle/sleep

---

```python
##example of using irq and callback
import machine
import micropython

micropython.alloc_emergency_exception_buf(100)

interruptCounter = 0
totalInterruptsCounter = 0

def handleInterrupt(timer):
  global interruptCounter
  interruptCounter = interruptCounter+1

timer = machine.Timer(0)
timer.init(period=10000, mode=machine.Timer.PERIODIC, callback=handleInterrupt)

while True:
  if interruptCounter>0:
    state = machine.disable_irq()
    interruptCounter = interruptCounter-1
    machine.enable_irq(state)

    #do something here


    totalInterruptsCounter = totalInterruptsCounter+1
    print("Interrupt has occurred " + str(totalInterruptsCounter)+ ' times.')
    machine.idle() # also try machine.sleep()
```
+++

```python
import machine
import micropython
import dht12
from machine import I2C, Pin

micropython.alloc_emergency_exception_buf(100)

interruptCounter = 0
totalInterruptsCounter = 0

def handleInterrupt(timer):
  global interruptCounter
  interruptCounter = interruptCounter+1

timer = machine.Timer(0)
timer.init(period=10000, mode=machine.Timer.PERIODIC, callback=handleInterrupt)
i2c = I2C(scl=Pin(5), sda=Pin(4))
sensor = dht12.DHT12(i2c)


while True:
  if interruptCounter>0:
    state = machine.disable_irq()
    interruptCounter = interruptCounter-1
    machine.enable_irq(state)

    #do something here
    sensor.measure()
    print('temp is: ', sensor.temperature())

    totalInterruptsCounter = totalInterruptsCounter+1
    print("Interrupt has occurred " + str(totalInterruptsCounter)+ ' times.')
    machine.idle()
```

---

### ISR Guidance
- Keep the code as short and simple as possible
- Avoid memory allocation: no appending to lists or insertion into dictionaries, no floating point
- Where data is shared between the main program and an ISR, consider disabling interrupt prior to accessing the data in the main program and re-enabling them immediately afterwards
- Allocate an emergency exception buffer to get error messages

+++

### Interrupt Service Routines - Further Info
- [micropython.org](http://docs.micropython.org/en/v1.9.3/esp8266/reference/isr_rules.html)
- [Tim Head's talk](https://www.youtube.com/watch?v=D-5V7s0GflU&t=1657s) at 2017 Pycon

---

# micropython refresh

---

### buzzer shield MLT-8540 ###
![](https://wiki.wemos.cc/_media/products:d1_mini_shields:buzzer_v1.0.0_1_16x9.jpg)


+++
### using the buzzer shield
```python
from machine import Pin, PWM
import time

pwm = PWM(Pin(14), freq=440, duty=512)
time.sleep(1)
pwm.deinit()

```
- note: freq c: 262, 'd': 294, 'e': 330, 'f': 349, 'g': 392, 'a': 440,'b': 494,'C': 523,
- rhythm is achieved by gaps between tones



---
### Temperature/Humidity shield DHT12 ###
![](https://wiki.wemos.cc/_media/products:d1_mini_shields:dht_v3.0.0_1_16x9.jpg)

+++

### polling dht sensor ###

use [dht12 library](https://github.com/mcauser/micropython-dht12)
```python
import time
import dht12
from machine import I2C, Pin
i2c = I2C(scl=Pin(5), sda=Pin(4))
sensor = dht12.DHT12(i2c)

while True:
	sensor.measure()
	print('temp is: ', sensor.temperature())
	print('humidity is: ', sensor.humidity())
	time.sleep(10)
```
---
### uniquely identifing your D1 mini
```python
import network

wlan = network.WLAN()
wlan.config('mac')

#or for the value in hex
import ubinascii
ubinascii.hexlify(wlan.config('mac')).decode()
```

---
### network library ###
connecting to local wifi network
```python
 import network
 sta = network.WLAN(network.STA_IF)
 sta.active(True)
 sta.connect("network-name", "password")
```
at this point the d1 mini should be connected to the network

```python
sta.isconnected() #should return True
sta.ifconfig()    #should return your IP address
```

---

### MQTT publish using [uMQTT.simple](https://github.com/micropython/micropython-lib/tree/master/umqtt.simple)

```python
from umqtt.simple import MQTTClient

c=MQTTClient('my_sensor', 'iot.eclipse.org') #default port is 1883

c.connect()
c.publish('RIFF/kennel3/temperature', '24')
c.disconnect()
```

+++

so develop your own temperature/humidity node!

```python
import time
import dht12
from machine import I2C, Pin
from umqtt.simple import MQTTClient

i2c = I2C(scl=Pin(5), sda=Pin(4))
sensor = dht12.DHT12(i2c)
c=MQTTClient('phil_sensor', 'iot.eclipse.org')

while True:
    sensor.measure()
    print('temp is: ', sensor.temperature())
    print('humidity is: ', sensor.humidity())
    c.connect()
    c.publish('RIFF/kennel4/temperature',str(sensor.temperature()))
    c.publish('RIFF/kennel4/humidity',str(sensor.humidity()))
    c.disconnect()
    time.sleep(10)
```

---

if you want to download a simple MQTT client on your laptop, consider mosquitto

```python
sudo apt-get install mosquitto mosquitto-clients

mosquitto_sub -h 'iot.eclipse.org' -t RIFF/#

```
- a good simple phone MQTT client is [MQTT dashboard](https://play.google.com/store/apps/details?id=com.thn.iotmqttdashboard&hl=en_AU) for Android
- port 1883 (unencripted)

---

### Shenton Park Dogs' Refuge Home ###
![](http://www.dogshome.org.au/themes/blackcandy/images/dogs-home-perth.gif)

 <!--
 speaker notes -
lets transfer our knowledge on the d1 mini to a real use case
 -->


+++
![](https://static1.squarespace.com/static/55d675c5e4b0ea1246287574/561d31dae4b00e055e2dad4a/561d31f1e4b07930589695a8/1444753906476/pact-ShentonParkDogRefuge-001.JPG)

---

### Shenton Park Dogs' Refuge Home - use case ###
User Requirements; the system shall...
1. alert nearby workers when a particular kennel temp is too high
2. alarm nearby workers when a kennel temp and humidity is high
3. provide office workers with temperature and humidity readings; updated every 3 mins
4. provide audible and visual alerts in office when any kennel temp is high
5. log temperature and humidity readings into a file. Low memory, easy to extract, not likely to become obselete, etc,etc
6. facilitate remote alerts for temp/humidity alarms/alerts out of office hours
