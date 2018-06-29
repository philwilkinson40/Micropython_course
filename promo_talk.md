
### Perth Python and Django Meetup - May 2018###

![](https://docs.pycom.io/img/micropython.jpg)

<!--
Speaker Notes:
Short personal introduction
thanks for the opportunity to speak

short talk about Micropython,
..few demos
...and a plug for course

note that much of the tech info provided here is taken from micropython.org
the course will borrow heavily from Radomir's course for the WEMOS D1 mini
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


### Using micropython ###

#### Basic REPL interface ####

- basic operators
- input history, tab completion
- paste mode
- modules, functions, classes
- lists, tuples, dictionaries

<!--
speaker Notes
straight into a short demo
explain the basics of dev board, UART connection to pc
run through the basics of interacting with the REPL
-->

---

### why use micropython? ###

- microcontrollers
    - very low power; RasPi idle ~0.2A,  ESP8266 80mA-15uA  
    - interaction with environment with IO
    - able to run in the wild
- able to use your Python coding skill in a different context



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
