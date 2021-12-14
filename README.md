```
import random

iplist = []
for private in range(100):
    ip = '192.168.' + str(random.randint(0,255)) + '.' + str(random.randint(0,255))
    iplist.append(ip)
for public in range(100):
    ip = ''
    for i in range(4):
        if i == 0:
            ip = ip + str(random.randint(1,255))
        else:
            ip = ip + str(random.randint(0,255))
        if i != 3:
            ip = ip + '.'
    iplist.append(ip)

print('Adresy:', iplist)

# Tworzymy 8-znakowe haslo do kazdego ip (chr od 65 do 125)

passlist = []
for passes in range(200):
    passwd = ''
    for i in range(8):
        passwd += chr(random.randint(65,125))
    passlist.append(passwd)

print('Passla:', passlist)

slownik = {}
for i in range(len(iplist)):
    slownik[iplist[i]] = passlist[i]

print('Wszystko w slowniku:', slownik)



#zapisywanie do pliku txt
import json

#zapis do pliku

a_file = open("data.json", "w")
json.dump(slownik, a_file)
a_file.close()
```
