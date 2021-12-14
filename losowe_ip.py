import random






#stworzyc 100 IP: localhostow od 192 i 100 nielokalhostow - i zapisac do do listy

lista_ip_non_local = []
for i in range(100):

    ip=""
    for i in range(0,4):
            losowa_liczba = random.randint(1, 255)
            ip+=str(losowa_liczba)
            if i in range(0,3):
                ip += "."
    lista_ip_non_local.append(ip)

# print(lista_ip_non_local)

lista_ip_local = []
for i in range(100):
    ip="192.168."
    for i in range(0,2):
            losowa_liczba = random.randint(1, 255)
            ip+=str(losowa_liczba)
            if i in range(1):
                ip += "."
    lista_ip_local.append(ip)
# print(lista_ip_local)

#tworzymy haslo do kazdego z IP
# od 65 do 125
#wygenerowac liste 200 hasel 8 znakow

lista_hasel = []
for j in range(200):
    password = ""
    for i in range(0,8):
        losowa_liczba = random.randint(65, 125)
        password+=chr(losowa_liczba)

    lista_hasel.append(password)

print(lista_hasel)