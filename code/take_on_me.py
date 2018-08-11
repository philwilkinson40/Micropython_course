#90's ringtone retro 
#https://forum.micropython.org/viewtopic.php?f=16&t=2047&start=10


from rtttl import RTTTL
import time
from machine import Pin, PWM

buz_tim = PWM(Pin(14))

def play_tone(freq, msec):
    print('freq = {:6.1f} msec = {:6.1f}'.format(freq, msec))
    if freq > 0:
        buz_tim.freq(int(freq))
        buz_tim.duty(50)
    time.sleep_ms(int(msec * 0.9))
    buz_tim.duty(0)
    time.sleep_ms(int(msec * 0.1))


tune = RTTTL('TakeOnMe:d=4,o=4,b=160:8f#5,8f#5,8f#5,8d5,8p,8b,8p,8e5,8p,8e5,8p,8e5,8g#5,8g#5,8a5,8b5,8a5,8a5,8a5,8e5,8p,8d5,8p,8f#5,8p,8f#5,8p,8f#5,8e5,8e5,8f#5,8e5,8f#5,8f#5,8f#5,8d5,8p,8b,8p,8e5,8p,8e5,8p,8e5,8g#5,8g#5,8a5,8b5,8a5,8a5,8a5,8e5,8p,8d5,8p,8f#5,8p,8f#5,8p,8f#5,8e5,8e5')

for freq, msec in tune.notes():
    play_tone(freq, msec)
