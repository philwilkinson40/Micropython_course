
### Micropython Intro - PDPD July 2018###

![](https://docs.pycom.io/img/micropython.jpg)

<!--
Speaker Notes:
Short personal introduction

short intro course in Micropython,

note that much of the tech info provided here is taken from micropython.org
the course borrows heavily from Radomir's course for the WEMOS D1 mini
http://micropython-on-wemos-d1-mini.readthedocs.io/en/latest/index.html


-->

---

### micropython ###

*Reinterpretation* of Python 3.4
optimised to run in *constrained environments*

specficially microcontrollers; limited RAM & flash

- PDPD [MeetUp talk by Adrian](https://www.meetup.com/en-AU/Perth-Django-Users-Group/events/237034592/) in 2017
- [micropython.org website](https://micropython.org) and [forum](https://forum.micropython.org/)
- important forks:
  * [MicroBit](http://microbit.org/) (education)
  * [Pycom](https://pycom.io/) (wireless communications)
  * [Adafruit's Circuitpython](https://learn.adafruit.com/welcome-to-circuitpython/what-is-circuitpython) (electronic makers)
  * (Pyboard), ESP8266, ESP32

  <!--
  Speaker Notes:
  This talk is not covering the background to Micropython, refer to previous talk

  Reinterpretation of Cpython means with respect to language syntax, and most of the features of MicroPython are identical to those described by the “Language Reference” documentation at docs.python.org."

  MicroPython aims to be as compatible with normal Python as possible to allow you to transfer code with ease from the desktop to a microcontroller or embedded system

  very limited RAM means 256k of code space and 16k of RAM (show Micro-bit)

  significant development in the language based on specific user needs
  similarities with Linux distros; same core kernel different implementations

  -->

---

### WEMOS D1 mini ###

![](https://wiki.wemos.cc/_media/products:d1:d1_mini_v3.0.0_1_16x9.jpg)

---

![](https://wiki.wemos.cc/_media/products:d1:d1_mini_v3.0.0_2_16x9.jpg)
---
### interacting with the esp8266 ###

<p style="text-align: left;"> LINUX / MAC [RSHELL](https://github.com/dhylands/rshell) </p>

- simple shell, developed in python good support on [Micropython forum](https://forum.micropython.org/)

```
sudo pip3 install rshell
```

<p style="text-align: left;"> WINDOWS install [mpfshell](https://github.com/wendlers/mpfshell) following [these instructions](https://gist.github.com/hardye/657385210c5d613e69cb5ba95e8c57a7) </p>

other options to interact with the board include:

- [WEBREPL](https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/repl.html#webrepl-a-prompt-over-wifi) via wifi
- [AMPY](https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy) from Adafruit
- [Mu editor](https://codewith.mu/) (not yet available for ESP)

fallback options for direct interaction with board at [micropython.org](https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/repl.html)

---

### using RSHELL ###

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
participants should exit this slide being able to enter repl execute code and return to shell
-->

---

### basics - GPIO Output ###

D1 mini has its own LED connected to GPIO2 (D4)

```
from machine import Pin

led = Pin(2, Pin.OUT)
led (0)
led (1)

```
TASK 1 - get the led to flash 5 times

---
###  Pulse Width Modulation ###
INSERT figure explaining PWM duty cycles and frequency
---

```
>>>from machine import Pin, PWM
>>>import time

>>>pwm = PWM(Pin(2)) #create PWM object

>>>pwm.duty(0) #the is always on
>>>pwm.duty(1023) # is always off

>>>for i in range (1023):
      pwm.duty(i)
      time.sleep(0.01)

>>>pwm.duty(512)  #set half way inbetween
>>>pwm.freq(1) now the frequency is set at 1 hz

```

---

---
### buzzer shield ###
-introduce shields for the WEMOS d1 Mini
-introduce the buzzer and datasheet
-
```
from machine import Pin, PWM

pwm = PWM(Pin(14), freq=440, duty=512)
```
- range of notes,
- rythum is achieved by gaps between tones
- unfortunately the maximium frequency available on the wemos is only 1000hz

Task 1 - develop a two tone alert
Stretch Task [RTTTL](https://en.wikipedia.org/wiki/Ring_Tone_Transfer_Language) - use the RTTTL library to perform a little 90's ringtone retro using the following string
'TakeOnMe:d=4,o=4,b=160:8f#5,8f#5,8f#5,8d5,8p,8b,8p,8e5,8p,8e5,8p,8e5,8g#5,8g#5,8a5,8b5,8a5,8a5,8a5,8e5,8p,8d5,8p,8f#5,8p,8f#5,8p,8f#5,8e5,8e5,8f#5,8e5,8f#5,8f#5,8f#5,8d5,8p,8b,8p,8e5,8p,8e5,8p,8e5,8g#5,8g#5,8a5,8b5,8a5,8a5,8a5,8e5,8p,8d5,8p,8f#5,8p,8f#5,8p,8f#5,8e5,8e5'

---

<!--
speaker Notes
why use Micropython instead of CPython?
cannot use CPython on small, low power hardware
Power consumption comparison
~80 mA during connection to WiFi
~15 uA during a deepsleep
Raspberry Pi 3 in idle is 0.3A
GPIO pins allow easy interaction by using modules that provide abstraction
Opportunity for Python developers to extend into IOT solutions
-->


---

![](http://micropython-on-wemos-d1-mini.readthedocs.io/en/latest/_images/board.png)


---

### basic IO interfacing ###

 - machine module
 - blink
 - temperature/humidity sensor
 - interrupts; ISR (event and timed)
 - network module

<!--
speaker Notes
live demo
use of the machine module on WEMOS D1 mini devboard
using a DH12 temp/humidity shield

from machine import Pin
import time
led = Pin(2, Pin.OUT)
led(1)
led(0)....

for i in range (10):
    led(0)
    time.sleep(0.2)
    led(1)
    time.sleep(0.2)


 ```
 example of GPIO and I2C using DHT12 shield
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
-->

---

![](https://www.postscapes.com/webhook-uploads/1469479748766/sensors.jpg)

<!--
useful reminder of possible sensors that can be used as environmental triggers for IOT devices.
Don't forget the actuators that could act.  Sometimes it is better to complete edge computing and simply report status changes to the network.

-->

<!--
### case study - Kings Park fauna boxes

![](https://www.fairfaxstatic.com.au/content/dam/images/g/r/h/1/k/n/image.related.articleLeadwide.620x349.grh1jp.png/1473980446152.jpg)

At the moment Kings Park staff have to physically visit every fauna box to check it is occupied.  
-->

---

### case study - WA Surf Lifesaving ###

![](http://www.westernaustralia-travellersguide.com/wp-content/uploads/2013/11/peasholm-street-dog-beach-perth.jpg)

<!--

speaker notes
WA surf lifesaving has no idea how many people are on beaches they do not patrol. They have to send people to the beach to estimate, wasting lifesaving resources.

If Surf lifesaving could understand the rough numbers of bathers on beaches they do not patrol, they would be able to allocate resources more efficiently.

Tough climate, no wifi, no power, low cost.

what about value add?  UV sensor and a LED matrix display or uSD card logger?

-->

---
### case study - perth bike counters
![](http://2.bp.blogspot.com/-Hi2dixJwxYM/UzLmmeKRbOI/AAAAAAAABB0/hsZhdQu39uY/s1600/DSC_3735.jpeg)

<!--

speaker notes
Western Australia aims to get more people cycling more often.  We have a perfact climate for cyclying however we have very low numbers of daily commuters.
In order to make effective data-driven design decisions that achieve the aim traffic planners need base data.

Perth has only 14 bicycle counters and theses are not actively streaming their data.

A report indicated that a single bicycle counter costs $15k-$5k !!
http://cdmresearch.com.au/files/reports/0030%20TMR%20Cyclist%20Counter%20Trials%20%28Final-2%29.pdf

-->

---

### micropython course ###

#### from zero to IOT solution ####

 - 4 week introduction course
 - WEMOS D1 Mini - ESP8266 microcontroller
 - aim is to run the course for a wider audience

 volunteers?
 <!--
 speaker Notes
 course will be based on
 aim is to learn Micropython by developing an IOT solution
 -->
