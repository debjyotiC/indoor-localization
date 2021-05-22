import rssi

scan = rssi.rssi(interface='wlan0')

print(scan.getRawNetworkScan(sudo='False'))
