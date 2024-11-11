# Wi-Fi scanner using network library 
import network 

print("Scanning for Wi-Fi networks, please wait...", "") 

sta_if = network.WLAN(network.STA_IF) 
sta_if.active(True) 
authmodes = ['Open', 'WEP', 'WPA-PSK' 'WPA2-PSK4', 'WPA/WPA2-PSK'] 
for (ssid, bssid, channel, RSSI, authmode, hidden) in sta_if.scan(): 
  print("* {:s}".format(ssid)) 
  print("   - Channel: {}".format(channel)) 
  print("   - RSSI: {}".format(RSSI)) 
  print("   - BSSID:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}".format(*bssid)) 
  print() 
