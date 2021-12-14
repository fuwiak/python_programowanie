import random


#czytanie plikow

dane = open("plik.txt", "r")
# print(dane)

# out = dane.read() #wczytujemy plik do stringa

# dane_lista = dane.readlines()
# print(dane_lista)


#usunac znaki konca linii z dane lista i zapisac do nowej zmiennej, strip i petli

dane_lista = dane.readlines()
# nowa_lista=[]
# for i in dane_lista:
#     nowa_lista.append(i.rstrip('\n'))
# print(nowa_lista)

#list_comprehensions
nowa_lista = [i.rstrip('\n') for i in dane_lista]
# print(nowa_lista)

#dolozyc sol do kazdego z elementow = dodatkowe znaki do hasla, od 3 do 6 elementow
# password+sol   hxksjkakjsa+moja_sol

# solona_lista = []
# for line in nowa_lista:
#     ip, password = line.split("=")
#
#     dlugosc_soli = random.randint(3, 8)
#     sol = ""
#     for i in range(dlugosc_soli):
#         lso += chr(random.randint(65, 125))
#     solone_haslo = password+"+"sol

import random

# czytanie plikow

dane = open("plik.txt", "r")
# print(dane)

# out = dane.read() #wczytujemy plik do stringa

# dane_lista = dane.readlines()
# print(dane_lista)


# usunac znaki konca linii z dane lista i zapisac do nowej zmiennej, strip i petli

dane_lista = dane.readlines()
# nowa_lista=[]
# for i in dane_lista:
#     nowa_lista.append(i.rstrip('\n'))
# print(nowa_lista)

# list_comprehensions
nowa_lista = [i.rstrip('\n') for i in dane_lista]
# print(nowa_lista)

# dolozyc sol do kazdego z elementow = dodatkowe znaki do hasla, od 3 do 6 elementow
# password+sol   hxksjkakjsa+moja_sol

solona_lista = []
for line in nowa_lista:
    # ip, password = line.split("=")
    args = line.split("=")

    print(*args)


    # dlugosc_soli = random.randint(3, 8)
    # sol = ""
    # for i in range(dlugosc_soli):
    #     sol += chr(random.randint(65, 125))
    # solone_haslo = password + "+"+sol
    # # solona_lista.append([ip, password, solone_haslo])
    # solona_lista.append([ip, password, solone_haslo])

# dla windows
# path = "C:\\Desktop\\szkolenie\\plik.txt"
# dane_windows = open(path, 'r')




#dla windows
# path = "C:\\Desktop\\szkolenie\\plik.txt"
# dane_windows = open(path, 'r')