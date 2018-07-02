

![](https://www.perth.wa.gov.au/sites/default/files/styles/medium_rounded_corners/public/news/thumbnails/cop-logo-newsroom-thumbnail-new.jpg?itok=qZOGls4g)

![](https://uploads-ssl.webflow.com/5a04456bb45010000164c58f/5ac6e8a1e4871de747635287_Screen%20Shot%202018-04-06%20at%2011.24.58%20am-p-500.png)

Big thanks to this event supporters

### Micropython Intro - PDPD July 2018###
![](https://docs.pycom.io/img/micropython.jpg)

<!--
Speaker Notes:
Short personal introduction

short intro course in Micropython,

note that much of the tech info provided here is taken from micropython.org
the course borrows heavily from Radomir's course for the D1 mini
http://micropython-on-wemos-d1-mini.readthedocs.io/en/latest/index.html

-->

---

### [micropython](https://micropython.org) and [forum](https://forum.micropython.org/) ###

*Reinterpretation* of Python 3.4
optimised to run in *constrained environments*

specficially microcontrollers; limited RAM & flash

- PDPD [MeetUp talk by Adrian](https://www.meetup.com/en-AU/Perth-Django-Users-Group/events/237034592/) in 2017
- PDPD [MeetUp talk by Phil](https://www.meetup.com/en-AU/Perth-Django-Users-Group/events/250001244/) in May 2018
- PDPD [solder session](https://www.meetup.com/en-AU/Perth-Django-Users-Group/events/251611417/) - soldering and [flashing micropython firmware](https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html#getting-the-firmware)


  <!--
  speaker Notes
  why use Micropython instead of CPython?
  cannot use CPython on small, low power hardware
  Power consumption comparison
  ~80 mA during connection to WiFi
  ~15 uA during a deepsleep
  Raspberry Pi 3 in idle is 0.3A so cannot be run on batteries for a long time
  GPIO pins allow easy interaction by using modules that provide abstraction
  Opportunity for Python developers to extend into IOT solutions

  Reinterpretation of Cpython means with respect to language syntax, and most of the features of MicroPython are identical to those described by the “Language Reference” documentation at docs.python.org."

  MicroPython aims to be as compatible with normal Python as possible to allow you to transfer code with ease from the desktop to a microcontroller or embedded system

  very limited RAM means 256k of code space and 16k of RAM (show Micro-bit)

  significant development in the language based on specific user needs
  similarities with Linux distros; same core kernel different implementations

  -->

---

### [D1 mini](https://wiki.wemos.cc/products:d1:d1_mini) ###

![](https://wiki.wemos.cc/_media/products:d1:d1_mini_v3.0.0_1_16x9.jpg)

<!--
speaker Notes
discuss UART, SPI, I2C, A0
pinout diagram

-->

+++

![](https://wiki.wemos.cc/_media/products:d1:d1_mini_v3.0.0_2_16x9.jpg)
---
### interacting with the esp8266 ###

<p style="text-align: left;"> LINUX / MAC [RSHELL](https://github.com/dhylands/rshell) </p>

- simple shell, developed in python good support on [Micropython forum](https://forum.micropython.org/)

```
sudo pip3 install rshell
```

<p style="text-align: left;"> WINDOWS install [mpfshell](https://github.com/wendlers/mpfshell) following [these instructions](https://gist.github.com/hardye/657385210c5d613e69cb5ba95e8c57a7) </p>

<p style="text-align: left;"> other options: </p>
- [WEBREPL](https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/repl.html#webrepl-a-prompt-over-wifi) via wifi
- [AMPY](https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy) from Adafruit
- [Mu editor](https://codewith.mu/) (not yet available for ESP)
- direct interaction with board: [micropython.org](https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/repl.html)

---

### using the SHELL ###

follow the RSHELL and MPFSHELL guides on the readme.md on the GITHUB pages

launch shell
```
rshell --buffer-size=30 -a -p /dev/ttyUSB0
```
list files on d1 mini, then copy a file to the board, then remove
```
ls /pyboard
cp Documents/main.py /pyboard
rm /pyboard/main.py
```
enter (repl) and leave (ctrl+x) the REPL is easy  

+++

<table>
  <tr>
    <th>command</th>
    <th>RSHELL</th>
    <th>mpfshell</th>
  </tr>
  <tr>
    <td> launch shell </td>
    <td> rshell --buffer-size=30 -a -p /dev/ttyUSB0 </td>
    <td> python {path to mpfshell.py} </br> open COM#  </td>
  </tr>
  <tr>
    <td> list files on d1 mini </td>
    <td> ls /pyboard </td>
    <td> ls  </td>
  </tr>  
  <tr>
    <td> copy file to d1 mini</td>
    <td> cp Documents/main.py /pyboard </td>
    <td> put main.py </br>(main.py must be in local folder) </td>
  </tr>
  <tr>
    <td> enter repl </td>
    <td> repl </td>
    <td> repl </td>
  </tr>
  <tr>
    <td> exit repl </td>
    <td> ctrl + x </td>
    <td> ctrl + Q </td>
  </tr>
</table>


---
### Using micropython ###

#### Basic REPL interface ####

- basic operators
- input history, tab completion
- paste mode (ctrl + e)
- modules, functions, classes
- lists, tuples, dictionaries

<!--
speaker Notes
participants should exit this slide being able to enter repl, execute code and return to shell
also be able to use a text editor and paste function in repl
-->

---

### basics - esp8266 modules ###

- esp8266 modules
 - esp, machine
- micropython modules
 - gc, uos, network, etc

<!--
speaker Notes
introduction to micropython specific modules
understand the 'u' prefix
get help at http://docs.micropython.org/en/v1.9.2/esp8266/index.html
-->
---
### 'hello world' of microcontrollers ###

D1 mini has its own LED connected to GPIO2 (D4)

```
from machine import Pin

led = Pin(2, Pin.OUT)
led (0)
led (1)

```

- TASK flash led 5 times
- TASK create function of visual indicators for fault finding
  - program running OK, fault in network connection, cannot read sensor
  - (use dict/list)
<!--
Speaker Notes
the onboard led is connected to GPIO2 which has a pull up resistor, so the led is on when the signal is pushed low
need to introduce time/utime module to achieve tasks
-->
---
### PWM - Pulse Width Modulation ###
![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGnyW8YUVyriZAFX--WLV2pevrSCiNkmzugyNtBCF8uUGxcKvM)

- use a digital signal in an 'analog fashion'
- Frequency (Hz)is how often a signal switches between low voltage and high voltage.
- Duty cycle is percent of time that the signal stays at high level (0->1023)

+++

### PWM control of on-board LED ###

```
from machine import Pin, PWM
import time

pwm = PWM(Pin(2)) #create PWM object

pwm.duty(0)       #led is always on
pwm.duty(1023)    #is always off

for i in range (1023):
  pwm.duty(i)
  time.sleep(0.01)

pwm.duty(512)     #set half way in between
pwm.freq(1)       #now set frequency at 1 hz

```


---

### buzzer shield MLT-8540 ###
![](https://wiki.wemos.cc/_media/products:d1_mini_shields:buzzer_v1.0.0_1_16x9.jpg)


+++
### using the buzzer shield
```
from machine import Pin, PWM
import time

pwm = PWM(Pin(14), freq=440, duty=512)
time.sleep(1)
pwm.deinit()

```
Freq; c: 262, 'd': 294, 'e': 330, 'f': 349, 'g': 392, 'a': 440,'b': 494,'C': 523,
- rhythm is achieved by gaps between tones
- max frequency available on the D1 mini is only 1000hz

- TASK develop a two tone alert
- TASK [RTTTL](https://en.wikipedia.org/wiki/Ring_Tone_Transfer_Language) use the [RTTTL library](https://github.com/dhylands/upy-rtttl) to perform a little 90's ringtone retro using the following string
'TakeOnMe:d=4,o=4,b=160:8f#5,8f#5,8f#5,8d5,8p,8b,8p,8e5,8p,8e5,8p,8e5,8g#5,8g#5,8a5,8b5,8a5,8a5,8a5,8e5,8p,8d5,8p,8f#5,8p,8f#5,8p,8f#5,8e5,8e5,8f#5,8e5,8f#5,8f#5,8f#5,8d5,8p,8b,8p,8e5,8p,8e5,8p,8e5,8g#5,8g#5,8a5,8b5,8a5,8a5,8a5,8e5,8p,8d5,8p,8f#5,8p,8f#5,8p,8f#5,8e5,8e5'

---
### Temperature/Humidity shield DHT12 ###
![](https://wiki.wemos.cc/_media/products:d1_mini_shields:dht_v3.0.0_1_16x9.jpg)

+++

### explaining I2C
![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBDoOJjIWX1Yc7QI97_i544-kCm9f78YChK2cItpyyYCXf-JgKlg)

+++

### polling sensor ###

use [dht12 library](https://github.com/mcauser/micropython-dht12)
```
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

TASK establish mean temperature across 2 mins polling every 20 seconds


---
### network module ###
connecting to local wifi network
```
 import network
 sta = network.WLAN(network.STA_IF)
 sta.active(True)
 sta.connect("network-name", "password")
```
at this point the d1 mini should be connected to the network

```
sta.isconnected() #should return True
sta.ifconfig()    #should return your IP address
```
+++

### [Star Wars Asciimation](https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/network_tcp.html?highlight=star) using sockets ###

```
import socket
addr_info = socket.getaddrinfo("towel.blinkenlights.nl", 23)
addr = addr_info[0][-1]
s = socket.socket()
s.connect(addr)
while True:
   data = s.recv(500)
   print(str(data, 'utf8'), end='')
```
---

### [MQTT](http://mqtt.org/) ###

- m2m lightweight messaging protocol
- publish / subscribe model
- for connections  where a small code footprint is required
-  and/or network bandwidth is at a premium.

+++
![](http://www.electronicwings.com/public/images/user_images/images/NodeMCU/NodeMCU%20Basics%20using%20ESPlorer%20IDE/NodeMCU%20MQTT%20Client/MQTT%20Broker%20nw.png)

+++
### MQTT publish using [uMQTT.simple](https://github.com/micropython/micropython-lib/tree/master/umqtt.simple)

```
from umqtt.simple import MQTTClient

c=MQTTClient('phil_sensor', 'iot.eclipse.org') #default port is 1883

c.connect()
c.publish('RIFF/phil/temperature', temp)
c.disconnect()
```

+++

if you want to download a simple MQTT client on your laptop, consider mosquitto

```
sudo apt-get install mosquitto mosquitto-clients

mosquitto_sub -h 'iot.eclipse.org' -t RIFF/#

```
a good simple phone MQTT client is [MQTT dashboard](https://play.google.com/store/apps/details?id=com.thn.iotmqttdashboard&hl=en_AU) for Android

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
- alert nearby workers when a kennel temp is high
- alarm nearby workers when a kennel temp and humidity is high
- provide office workers with 3 minute temperature and humidity readings
- give audible and visual alert in office when kennel temp is high
- provide phone alert if temp/humidity rises out of office hours
- write a python script for the office computer to record data over a (paho-mqtt library)
