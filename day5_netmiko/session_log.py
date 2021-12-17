#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass


#zapisywanie wszystkiego co sie dzieje po polaczeniu


linux_router1 = {
    'device_type': 'linux',
    'host': '192.168.43.197',
    'username': 'pawel',
    'password': 'pawel',
    'session_log': "sesja.txt"

}

# Show command that we execute
command = "ifconfig"
with ConnectHandler(**linux_router1) as net_connect:
    output = net_connect.send_command(command)
