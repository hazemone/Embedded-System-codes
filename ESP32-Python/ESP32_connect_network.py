import network 
import time 

# Type the name and the passwork of your hotspot network
ssid = '' 
password = '' 
 
station = network.WLAN(network.STA_IF) 
station.active(True) 
station.connect(ssid, password) 
 
while not station.isconnected(): 
    time.sleep(1) 
    print('Connecting to Wi-Fi...') 
 
print('Connected to Wi-Fi') 
print('IP address:', station.ifconfig()[0]) 
 
print('The used IP addresses are : ' ) 
print(station.ifconfig()) 
