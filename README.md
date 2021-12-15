```
mail poczta130@gmail.com

name = "Adam        "
names = ["Adam", "Kamil", "Dawid"]

liczby  = range(21, 40, 2)

jumper = "Janne Ahonen na nastepnych zawodach Cie pokonam"
# jumper[0:10]
# jumper[0::2]

# list(liczby)[2:-2] od elementu o indeksie 2 do indeksu -2(ale -2 nie bierzemy pod uwage)

# names[0] pierwszy element
# names[-1] ostatni element
# names[-2] przedostatni element
# list(liczby)[0::3] co trzeci element zaczynajac od indeksu zerowego
# list(liczby)[1::3] co trzeci element zaczynajac od indeksu pierwszego


# print(len(name))
# name=name.strip()
# print(name)
# "Adam".strip("A") #sluzy do odcinanania na brzegach
#replace = zamiana w dowolnym miejscu

# "AJAX".strip("A")

# named = name.replace("d", "x")
# print(named)

# comma_IP = "196,121,1,1"
# colog = """111.222.333.123 HOME - [01/Feb/1998:01:08:39 -0800] "GET /bannerad/ad.htm HTTP/1.0" 200 198"""

all_ip=re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",log)
print("znalezione IP", all_ip.group())

#napisac funkcje, ktora wyciaga z kazdej linii IP, uzywajac regexa wyzejmma_IP_without_commas = comma_IP.replace(",", ".")
# print(comma_IP_without_commas)


# print(comma_IP_without_commas.split("."))

numbers_str = ["101", "200", "300", "400", "501"]
# numbers_int = [100, 200, 300]

suma = 0
for digit in numbers_str:
    suma = suma+int(digit) #suma=100, suma=300, suma=600
# print("suma ", suma)
# print("numbers str ", numbers_str)

#suma liczb parzystych z numbers_str
suma = 0
for digit in numbers_str:
    if int(digit)%2==1:
        suma = suma+int(digit)

print("suma nieparzystych", suma)


comma_IP = "196,122,1,1"

#wyciagnc z IP liczby parzyste, i podac ich sume
comma_IP = "192,168,1,1"

sortowanie = comma_IP.split(",")
print(sortowanie)
suma = 0
for i in sortowanie:
    if int(i)%2==0:
        suma = suma+int(i)
print(suma)

lista1 = [2,1,37]
krotka1 = (1,4,88)

#key: value
hasla = {"pawel": "haslo_maslo",
         "kamil": "1234",
         "ziutek": "twoja_stara_deska_do_krojenia"}

# list(hasla.items()) wszystkie elementy

# list(hasla.keys()) wszystkie klucze
# list(hasla.values()) wszystkie wartosci

#mam wczytana z pliku liste
# lista = ["pawel", 123, "jozef", 666, "jaroslaw", 8888, "user1"]
#zeby pobrac hasla czy loginy lista[::2]
# [-1]
#trzeba nie brac pod uwage "user1", poniewaz nie ma hasla

# slownik["key"]="wartosc"


lista = ['pawel',123,'jozef',666,'jaroslaw',8888,'user1']
if len(lista)%2!=0:
    lista = lista[:-1]

keys = lista[::2]
values = lista[1::2]
slownik = {}
for i in range(len(keys)):
    slownik[keys[i]] = values[i]

# print(slownik)

#set - zbiorem - zestaw

lista1 = [2,2,1,1,1,3]

zbior = set(lista1)
zbior1 = {}
print("zbior ", set(lista1))

set1 = set([1,2,3,4])
set2 = set([3,4, 5, 6])
# set1.union(set2) suma zbiorw
# set1.difference(set2) set1 - set2
# set2.difference(set1) set2 - set1
#list(set2.difference(set1)) #zamiana roznicy dwoch zbiorw na liste



# i = 0
# while i <= len(lista):
#     if i+1 < len(lista):
#         slownik[lista[i]] = lista[i+1]
#     i += 2


#polaczyc liste, usunac duplikaty, oraz podac ile razy powtorzyl sie pawel w dwoch listach
#resultat do slownika

lista1 = ['pawel',123,'jozef',666,'jaroslaw',8888,'pawel',999, "jozef", 888, "janne", 2222]
lista2 = ['pawel',123,'jozef',666,'krzaklewski',8888,'hans',999, "jozef", 888, "janne", 2222]

import random


ip=""
for i in range(16):
    if i%4==0 and i!=0:
        ip+="."
    else:
        losowa_cyfra = random.randint(0, 9)
        ip+=str(losowa_cyfra)





print("losowe ip", ip)

#stworzyc 100 IP: localhostow od 192 i 100 nielokalhostow - i zapisac do do listy







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


with open('myfile.txt', 'w') as f: #write, 'r' - czytanie, 'a' - dodajemy linie do pliku
    print(slownik, file=f)


with open(r'plik.txt', 'w' ) as plik:
    for klucz, wartosc in slownik.items():
        wiersz = '{}={}\n'.format(klucz,wartosc)
        plik.write(wiersz)
        
        
    


def kwadrat(x): #x wejscie
    return x**2 # return wyjscie

# print(kwadrat(3))


def suma_liczb(x,y):
    return x+y

print("suma liczb x,y=", suma_liczb(3,4))


result = []
for i in range(1, 11):
    result.append(kwadrat(i))

# print(result)

#napisac funkcje, ktora odwraca podana liste, [1,2,0,7] ---> [7, 0, 2, 1], lista[::-1], list.sort(), sorted(list)
# lista[::-1]

def odwroc_liste(x):
    return x[::-1], y, z

lista = [1,6,1,2, 7, -9, -100, 21]

# print("oryginalna lista", lista)
# # print(odwroc_liste(lista))
#
# print("sortowanie malejaco", sorted(lista, reverse=True))
# print("sortowanie rosnaco", sorted(lista, reverse=False))
# print(lista)

#napisac funkcje, ktora przyjmuje liste jako argument, i printuje originalna liste, potem posortowna rosnaco,
#a nastepnie malejaco

# def sorts(lista):
#     return lista, sorted(lista, reverse=False), sorted(lista, reverse=True)
#
# li = [1,2,0,7,5,1,8,2,9]
#
# lior, liasc, lides = sorts(li)
#
# print('Original   =',lior)
# print('Ascending  =',liasc)
# print('Descending =',lides)


# lista =[3,5,6,7,9,34]
# def lista_org(x):
#     # print("oryginalna lista", x)
#     # print("sortowanie malejąco", sorted(x, reverse=True))
#     # print("sortowanie rosnąco", sorted(x, reverse=False))
#     return x, sorted(x, reverse=True), sorted(x, reverse=False)


# wynik = lista_org(lista)

lista = [1,2,8,6,5,7,4]

#dowolna liczba parametrow

# def suma_liczb(*x):
#     return sum(x)

def show_arg(*x):
    return x

#napisz funckej, ktora ma jako argument *args, i podaje sume dla kazdej z micj, a = [2,1], b = [1,2,3], c = [3,4,5,2]

# a, b, c = [2,1], [1,2,3], [3,4,5,2]
#
# big_list = [a,b,c]
#
# def suma_liczb(*x):
#     return sum(x)
#
# for lista in big_list:
#     print(lista, suma_liczb(*lista))


#sortowanie
# words = {"python": 2, "blah": 4, "alice": 3}
# print(dict(sorted(words.items(), key=lambda x: x[1])))
#
# words = {"python": 2, "blah": 4, "alice": 3}
# print(dict(sorted(words.items(), key=lambda x: x[0])))
#
# #
# words = {"python": 2, "blah": 4, "alice": 3}
# print(dict(sorted(words.items(), key=lambda x: x[0], reverse=True)))


#napisac funkcje, ktora sprawdzi czy dane ip z listy to localhost, zalozmy ze takie od sekwencji 127  - napis[0:3]

def czy_local(lista_ip):
    for line in lista_ip:
        if line[0:3]=="127":
            print(line, "tak")
        else:
            print(line, "nie")


lista = ["127.0.0.1", "192.168.136.83", "127.1.1.1", "888.222.111.1"]





def kwadrat(x): #x wejscie
    return x**2 # return wyjscie

# print(kwadrat(3))


def suma_liczb(x,y):
    return x+y

print("suma liczb x,y=", suma_liczb(3,4))


result = []
for i in range(1, 11):
    result.append(kwadrat(i))

# print(result)

#napisac funkcje, ktora odwraca podana liste, [1,2,0,7] ---> [7, 0, 2, 1], lista[::-1], list.sort(), sorted(list)
# lista[::-1]

def odwroc_liste(x):
    return x[::-1], y, z

lista = [1,6,1,2, 7, -9, -100, 21]

# print("oryginalna lista", lista)
# # print(odwroc_liste(lista))
#
# print("sortowanie malejaco", sorted(lista, reverse=True))
# print("sortowanie rosnaco", sorted(lista, reverse=False))
# print(lista)

#napisac funkcje, ktora przyjmuje liste jako argument, i printuje originalna liste, potem posortowna rosnaco,
#a nastepnie malejaco

# def sorts(lista):
#     return lista, sorted(lista, reverse=False), sorted(lista, reverse=True)
#
# li = [1,2,0,7,5,1,8,2,9]
#
# lior, liasc, lides = sorts(li)
#
# print('Original   =',lior)
# print('Ascending  =',liasc)
# print('Descending =',lides)


# lista =[3,5,6,7,9,34]
# def lista_org(x):
#     # print("oryginalna lista", x)
#     # print("sortowanie malejąco", sorted(x, reverse=True))
#     # print("sortowanie rosnąco", sorted(x, reverse=False))
#     return x, sorted(x, reverse=True), sorted(x, reverse=False)


# wynik = lista_org(lista)

lista = [1,2,8,6,5,7,4]

#dowolna liczba parametrow

# def suma_liczb(*x):
#     return sum(x)

def show_arg(*x):
    return x

#napisz funckej, ktora ma jako argument *args, i podaje sume dla kazdej z micj, a = [2,1], b = [1,2,3], c = [3,4,5,2]

# a, b, c = [2,1], [1,2,3], [3,4,5,2]
#
# big_list = [a,b,c]
#
# def suma_liczb(*x):
#     return sum(x)
#
# for lista in big_list:
#     print(lista, suma_liczb(*lista))


#sortowanie
# words = {"python": 2, "blah": 4, "alice": 3}
# print(dict(sorted(words.items(), key=lambda x: x[1])))
#
# words = {"python": 2, "blah": 4, "alice": 3}
# print(dict(sorted(words.items(), key=lambda x: x[0])))
#
# #
# words = {"python": 2, "blah": 4, "alice": 3}
# print(dict(sorted(words.items(), key=lambda x: x[0], reverse=True)))

#napisac funkcje, ktora sprawdzi czy dane ip z listy to localhost, zalozmy ze takie od sekwencji 127  - napis[0:3]

# def czy_local(lista_ip):
#     for line in lista_ip:
#         if line[0:3]=="127":
#             print(line, "tak")
#         else:
#             print(line, "nie")


lista = ["127.0.0.1", "192.168.136.83", "127.1.1.1", "888.222.111.1"]


# czy_local(lista)


#uzywajac kodu z funkcji czy_lokal, sprawdzic w pliku plik.txt, ktory z ip jest lokalny badz nie
#usun haslo z linii, i zastap je komunikatem tak lub nie



# 127.0.0.1, "tak"
# 192.168.136.83, "nie"

dane = open("plik.txt", "r")
dane_w_lista = dane.readlines()
nowa_lista = []



# for i in dane_w_lista:
#     nowa_lista.append(i.split("=")[0])
#
#
#
# def fukcja_dla_ip(list_ip):
#     for line in list_ip:
#         if line[:3]=="127":
#             print(line, "Tak")
#         else:
#             print(line, "nie")
#
# print(fukcja_dla_ip(nowa_lista))


# def localhost(x):
#     for i in x:
#         if i[0:3] == "127":
#             print (i,"jest localhostem")
#         else:
#             print(i,"nie jest localhostem")
#
# dane = open("plik.txt", "r")
# dane_lista = dane.readlines()
# nowa_lista2 = [i.rstrip('\n') for i in dane_lista]  # list comprehension?
#
# ipki=[]
# for i in nowa_lista2:
#     ipki.append(i.split(":")[0])
#
# localhost(ipki)

dane = open("plik.txt","r")


dane_lista = dane.readlines()
nowa_lista=[]


for i in dane_lista:
    nowa_lista.append(i.split('=')[0])

# nowa_lista = [i.strip('password') for i in dane_lista]

nowa_lista = [i.split("=")[0] for i in dane_lista]

def local_host(dane):
    for line in dane:
        if line[:3]=="127":
            print(line, "Tak")
        else:
            print(line, "Nie")
# print(local_host(nowa_lista))



# lista = ["tak", "nie", "tak", "tak"]
#
# licznik = 0
# for x in lista:
#     if x=="tak":
#         licznik+=1

# lista.count("tak")



#wyznaczyc statystyki pliku(mamy funkcje, w ktorej jako argument dajemy nazwe pliku), podac liczbe wszyskich ip, podac liczbe local, podac liczne non local, podac unikalnych ip(set),
#podac procent elementow unikalny 150 / 200 = 75%
# def localhost(x):
#     jest=0
#     niejest=0
#     for i in x:
#         if i[0:3] == "127":
#             print (i,"jest localhostem")
#             jest += 1
#         else:
#             print(i,"nie jest localhostem")
#             niejest += 1
#     print("localhost",jest)
#     print("inne",niejest)
#     uniq=len(set(x))
#     all=len(x)
#     print("procent unikalnych",round(uniq/all*100,2),"%")
#
# dane = open("plik_updated.txt", "r")
# dane_lista = dane.readlines()
# nowa_lista2 = [i.rstrip('\n') for i in dane_lista]
#
# ipki=[]
# for i in nowa_lista2:
#     ipki.append(i.split(":")[0])
# localhost(ipki)


def localhost(file_name):
    dane = open(file_name, "r")
    dane_lista = dane.readlines()
    nowa_lista2 = [i.rstrip('\n') for i in dane_lista]  # list comprehension?
    ipki = []
    for i in nowa_lista2:
        ipki.append(i.split("=")[0])  # dodaj tylko pierwszą kolumnę
    # print(ipki)
    jest=0
    niejest=0
    for i in ipki:
        if i[0:3] == "127":
            # print (i,"jest localhostem")
            jest += 1
        else:
            # print(i,"nie jest localhostem")
            niejest += 1
    print("localhost",jest)
    print("inne",niejest)
    uniq=len(set(ipki))
    all=len(ipki)
    print("procent unikalnych",round(uniq/all*100,2),"%")

# localhost("plik_updated.txt")
# localhost("plik.txt")

#podac liczbe hostow dla danego IP, ustalic sobie maske wg uznania,
#def liczba_hosto(maska)
#maska

# IP = "127.168.91.121"
#liczba hostow 256

def hosty(prefix):
    bity=32-prefix
    print("liczba hostow:",2**bity-2)
hosty(24)

#napisac funckje, ktora tworzy liste krotek gdzie (cidr, liczba_hostow)), mozna uzyc list comprehension

# [(1, liczba), (2, liczba_hosto2)]


log = """111.222.333.123 HOME - [01/Feb/1998:01:08:39 -0800] "GET /bannerad/ad.htm HTTP/1.0" 200 198"""

all_ip=re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",log)
print("znalezione IP", all_ip.group())

#napisac funkcje, ktora wyciaga z kazdej linii IP, uzywajac regexa wyzej
result = []
find_words1 = re.findall(r"\w+",logi)
for word in find_words1:
    if word.isdigit()!=True:
        result.append(word)
print(result)
dlugosci=[]
for i in result:
    dlugosci.append(len(i))
slownik=(collections.Counter(dlugosci))

print("posortowany slownik", dict(sorted(slownik.items(), key=lambda x: x[0])))

```
