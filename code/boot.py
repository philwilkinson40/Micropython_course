import network
import time


sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect("SSID", "password")
if not sta.isconnected():
    time.sleep(0.5)
