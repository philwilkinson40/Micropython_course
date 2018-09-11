import network
import time


sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect("Wilko Wireless", "WilkoN600")
if not sta.isconnected():
    time.sleep(0.5)
