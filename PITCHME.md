 ### Micropython MeetUp - PDPD August 2018 - Low Power Mode Options ESP8266
![](https://docs.pycom.io/img/micropython.jpg)

<!--
MeetUp workshop to discuss Deep-sleep mode and RTC.memory on ESP8266
-->

Big thanks to this event supporters

![](https://uploads-ssl.webflow.com/5a04456bb45010000164c58f/5ac6e8a1e4871de747635287_Screen%20Shot%202018-04-06%20at%2011.24.58%20am-p-500.png)


---

### PDPD Micropython News
- two sessions; ongoing workshop at Artisfactory
- good talks at [Pycon-AU] by Damien and ???
- also at Europython by ???
### Need links here ###
- [micropython website ](https://micropython.org) and [forum](https://forum.micropython.org/)
- PDPD Micropython [Github repo](https://github.com/philwilkinson40/Micropython_course)
- Adafruit and Core electronics offer good online tutorials

---

### interacting with the esp8266 ###

- refer to previous workshops Github
- DHT12 sensor and networking

---
### IOT based solutions
# graphic required
- low cost microcontrollers
- connected devices
- **low power**

<!-- the expected massive explosion in IOT devices relies on three legs.  We will investigate the final leg; Low Power -->

---
### use case - environmental sensor
# need photo here
- temperature and humidity readings
- reading every minute
- placed within wifi range
- no power available; batteries only

---

### Regular Mode
- ESP8266 on; wifi connected
- use time module to sleep between polls
 - or timer callback functions

---

![](flowcharts/basic_flow.gif)

---

---?code=code/boot.py&title=boot file

---?code=code/main_regularex.py&title=regular main.py file

<!-- example code for Regular 'always on' Node -->
---
![](flowcharts/regular_powerchart.gif)

- using a [18650 LiPo bought from Bunnings](https://www.bunnings.com.au/solar-magic-2200mah-lithium-ion-rechargeable-batteries-2-pack_p4352437)
- 3.7V x 2.2Ahr = 3.3V x 0.080A x battery life
- battery life = (3.7x2.2)/(3.3x0.08) max=31 hours
---

### Modem Sleep Mode
- from [Espressif ESP8266  datasheet](https://www.espressif.com/sites/default/files/documentation/0a-esp8266ex_datasheet_en.pdf)
![](flowcharts/ESP8266_blockdia.png)

---

![](flowcharts/modem_sleep.gif)

---
---?code=code/main_modemsleepex.py&title= using Modem Sleep  main_modemsleepex.py

<!-- code to switch off wifi when not in use
-->
---

![](flowcharts/modem_powerchart.gif)
- 5s in each minute to connect to wifi and publish
- LiPo life approx 153hrs (6.4 days)

<!-- calculation shows better performance but still unsuitable for IOT devices
-->
---

### deepsleep
- CPU
- RTC wakes CPU on Pin #


---
REPL
# check micropython docs
- machine.deepsleep()
- beware endless deepsleep loops
 - use machine.reset_cause() & constants

---
```
from machine import Pin, I2C
from dht12 import DHT12
from umqtt.simple import MQTTClient
import time
import network
import esp
import machine

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
    sta.connect("SSID", "password")
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

t, h = poll_sensor()
wifi_init()
publish(t, h)
machine.deepsleep(60)

```



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
