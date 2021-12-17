from netmiko import ConnectHandler
import re
from getpass import getpass

##1 sposob logowania
# device = ConnectHandler(device_type='linux', host='172.20.10.3', username='pawel', password='pawel')

##2 sposob logowania - sprytniejszy

linux_router = {
    'device_type': 'linux',
    'host': '192.168.43.197',
    'username': 'pawel',
    'password': 'pawel',

}

net_connect = ConnectHandler(**linux_router)

out = net_connect.send_command("ifconfig")
# print(out)


from klasaIP import IP


def analiza_logow(out, pattern):
    findings = re.findall(pattern, out)

    return findings


# regex = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

regex1 = "(inet|inet6) \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

# regex6 = "((?:(inet|inet6)) \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"

regex7 = "inet \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} | inet6 "

lista_do_sprawdzenia = analiza_logow(out, regex7)

lista_do_sprawdzenia = [x for x in lista_do_sprawdzenia if x!=' inet6 ']
lista_do_sprawdzenia = [x.strip('inet ') for x in lista_do_sprawdzenia]



def polacz(adresy_do_sprawdzenia):
    for ip in adresy_do_sprawdzenia:
        try:
            net_connect = ConnectHandler(device_type='linux', host=ip,username='test', password='test', port='2222')
            return ip, "dziala"
        except Exception as blad:
            print("ip: "+ip+" zglasza problem: ", blad)







# napisac funckje, ktora bedzie sprawdzala z ktore ip i haslo daja sie zalogowac do systemu
# na przypadek braku dostepu, niech funckja rzuci wyjatek, "access denied"

# ip pobrac z analiza_logow(out, regex7), haslo niech bedzie stale, i sie rowna pawel;

# device = ConnectHandler(device_type='linux', host='172.20.10.3', username='pawel', password='pawel')

# zmienic regex tak, by pobiewal IP po slowe inet

# linux_router_hidden = {
#     'device_type': 'linux',
#     'host': '172.20.10.3',
#     'username': 'pawel',
#     'password': getpass(),
# }
#
# net_connect_hidden = ConnectHandler(**linux_router_hidden)


# out = device.send_command("ifconfig")

# prompt = device.find_prompt()

# device = ConnectHandler(device_type='cisco_ios', host='192.168.1.1', username='cisco', password='cisco')
# device = ConnectHandler(device_type='cisco_ios', host='169.254.106.104', username='cisco', password='cisco')


# cisco_router = {
#     'device_type': 'cisco_ios',
#     'host': '192.168.1.1',
#     'username': 'cisco',
#     'password': 'cisco',
# }


# sshCli = ConnectHandler(
#     device_type = 'cisco_ios',
#     host = '192.168.1.1',
#     port = 22,
#     username = 'cisco',
#     password = 'cisco'
#     )
# # net_connect = ConnectHandler(**cisco_router)

