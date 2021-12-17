from netmiko import Netmiko
import logging

#wysylanie tych samych ustawien(zapisanych w pliku changes.txt) do wielu ruterow/OS/eetc


linux_router1 = {
    'device_type': 'linux',
    'host': '192.168.43.197',
    'username': 'pawel',
    'password': 'pawel',

}

linux_router2 = {
    'device_type': 'linux',
    'host': '192.168.43.197',
    'username': 'pawel',
    'password': 'pawel',

}




devices = [linux_router1, linux_router2]

for device in devices:
   net_connect = Netmiko(**device)
   output = net_connect.send_config_from_file('changes.txt')
   print(output)
   net_connect.disconnect()


# Changes.txt
# interface GigabitEthernet3
# description This is set via Netmiko and text file