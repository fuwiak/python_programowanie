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


#ConnectHandler - laczenie sie przez ssh, odpowiednik kursora w postgresie
net_connect = ConnectHandler(**linux_router)

out = net_connect.send_command("ifconfig")
# print(out)




#analiza logow za pomoca regexow
def analiza_logow(out, pattern):
    findings = re.findall(pattern, out)

    return findings


regex7 = "inet \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} | inet6 "

lista_do_sprawdzenia = analiza_logow(out, regex7)

lista_do_sprawdzenia = [x for x in lista_do_sprawdzenia if x!=' inet6 ']
lista_do_sprawdzenia = [x.strip('inet ') for x in lista_do_sprawdzenia]





#logowanie uzywajac wyjatkow
def polacz(adresy_do_sprawdzenia):
    for ip in adresy_do_sprawdzenia:
        try:
            net_connect = ConnectHandler(device_type='linux', host=ip,username='test', password='test', port='2222')
            return ip, "dziala"
        except Exception as blad:
            print("ip: "+ip+" zglasza problem: ", blad)


