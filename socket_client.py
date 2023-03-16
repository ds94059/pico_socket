import sys
import os
import time
import network
import socket

ssid = 'WIFI_SSID'
password = 'PASSWORD'
serverAddr = "192.168.1.111"
serverPort = 8000

# To know WLAN status
# It's helpflul in learning and debugging
def understandWLAN(wwlan):
    print("------------------------------")
    print("Information to understand wlan")
    print(wwlan)
    #print(dir(wwlan))
    print("active(): ", wwlan.active())
    print("isconnected(): ", wwlan.isconnected())
    s = wwlan.status()
    print("status() =", s)
    if s == network.STAT_IDLE:
        print("STAT_IDLE – no connection and no activity")
    elif s == network.STAT_CONNECTING:
        print("STAT_CONNECTING – connecting in progress")
    elif s == network.STAT_WRONG_PASSWORD:
        print("STAT_WRONG_PASSWORD – failed due to incorrect password")
    elif s == network.STAT_NO_AP_FOUND:
        print("STAT_NO_AP_FOUND – failed because no access point replied")
    elif s == network.STAT_CONNECT_FAIL:
        print("STAT_CONNECT_FAIL – failed due to other problems")
    elif s == network.STAT_GOT_IP:
        print("STAT_GOT_IP – connection successful")
    else:
        print("- unknown status!!!")
    
    print("------------------------------")

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected():
    print("Waiting to connect:", end='*\r')
    time.sleep(0.5)
    print("Waiting to connect:", end='-\r')
    time.sleep(0.5)

print("wlan connected")

# print(wlan.ifconfig())
print("my IP:", wlan.ifconfig()[0])
addr = (serverAddr, serverPort)
print('host:',addr)

s = socket.socket()
s.connect(addr)
s.send(b"\nHello from Pico W at " + wlan.ifconfig()[0])
rx = s.recv(512)
print(rx)