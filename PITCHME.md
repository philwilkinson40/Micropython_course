 ### Micropython MeetUp - PDPD August 2018 - Low Power Mode Options ESP8266
![](micropython_logo.png)

<!--
MeetUp workshop to discuss Deep-sleep mode and RTC.memory on ESP8266
-->

---
Big thanks to this event supporters

![](https://uploads-ssl.webflow.com/5a04456bb45010000164c58f/5ac6e8a1e4871de747635287_Screen%20Shot%202018-04-06%20at%2011.24.58%20am-p-500.png)


---

### PDPD Micropython News
- two sessions; ongoing maker workshop at Artisfactory and CBD Workshops
- good talks at [Pycon-AU] by Damien and ???
- also at Europython by ???

---

### interacting with the esp8266 ###

- refer to previous workshops Github
- DHT12 sensor and networking

---
### IOT based solutions
![](https://cdn-images-1.medium.com/max/1600/1*B90K6ApXTNvY6RQApeHZ1A.jpeg)
1. low cost microcontrollers
2. connected devices
3. **low power**

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
@[1-4](import libraries)
@[6-12](temperature and humidity)
@[14-19](publish via MQTT)
@[21-24]

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
@[16-21](wifi initiated in main script)
@[30-32](wifi deinit as soon as possible)
@[34-40]

<!-- flowchart and code: switch off wifi when not in use
-->
---

![](flowcharts/modem_powerchart.gif)
- 5s in each minute to connect to wifi and publish
- LiPo life approx 120.8hrs (5 days)

<!-- calculation shows better performance but still unsuitable for IOT devices
-->
---

### deepsleep
- wifi unit off, CPU off, RTC is on
- RTC wakes CPU - GPIO (D0 on Wemos D1 mini)


---
### REPL
- machine.deepsleep()
- beware endless deepsleep loops
 - use machine.reset_cause() & constants
 # add link to micropython docs here

---

![](flowcharts/deepsleep.gif)

---
---?code=code/main_deepsleepex.py&title= using Deepsleep  main_deepsleepex.py
@[31-32](allows user to Ctrl+C when not waking from deepsleep)
@[34-37]

<!-- flowchart and code: using Deepsleep function
-->
---

![](flowcharts/deepsleep_powerchart.gif)
- 5s in each minute to connect to wifi and publish
- LiPo life approx 342 hours (14 days)
---

### Deepsleep challenges
- all memory is lost on deepsleep
- using EEPROM wears out flash
- Espressif provided a useful option in RTC

---
### RTC.memory
- limited memory available in addition to the clock
- 256 bytes user memory available (in 4 byte 'units')

---
### REPL
- rtc = machine.RTC()
- rtc.memory(b'')
- rtc.memory().decode('utf-8')

---
---

![](flowcharts/rtcmem.gif)
- 1s every min to poll_sensor
- 5s every 10 mins connect to wifi and publish
- LiPo life approx 1987 hours (83 days)

---
---?code=code/main_rtcmemex.py&title= using RTC memory and Deepsleep  main_rtcmemex.py
@[]()
# need to complete the code and walkthrough

<!-- flowchart and code: using RTC.memory function
-->
---
