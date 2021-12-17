from netmiko import Netmiko
import logging

devices = [{
   "device_type": "cisco_xe",
   "ip": "ios-xe-mgmt-latest.cisco.com",
   "username": "***",
   "password": "***",
   "port": "8181",
}]

for device in devices:
   net_connect = Netmiko(**device)
   output = net_connect.send_config_from_file('changes.txt')
   print(output)
   net_connect.disconnect()


# Changes.txt
# interface GigabitEthernet3
# description This is set via Netmiko and text file