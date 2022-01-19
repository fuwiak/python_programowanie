import random

#chce pobrac pierwszy elemt items
dane=open("plik.txt", "r").readlines()
lista_ip=[]
lista_hasla=[]
linia2 =[]
for linia in dane:
    linia = linia.strip("\n")
    linia = linia.split("=")
    linia2 = [linia[0], linia[1], len(linia[1])]
    lista_ip.append(linia2[0])
    lista_hasla.append(linia2[1])
#
for i, haslo in enumerate(lista_hasla):
    liczba_dodanych=random.randint(3,5)
    for j in range(liczba_dodanych):
        string = chr(random.randint(33,126))
        haslo=haslo+string
    lista_hasla[i]=haslo


# with open("hasla.txt", "w") as f:
#     for element in lista_hasla:
#         f.write(str(element)+'\n') #kazdy element listy w nowym wierszu


#ponownie skleic za pomoca znaku = lista_ip z lista_hasla, mozna uzyc petli for, oraz wynik do nowej listy
# lista_ip[0]+"="+lista_hasla[0]

lista_sklejona =[]

for i in range(len(lista_hasla)):
    pomocniczy=(lista_ip[i]+'='+lista_hasla[i]) #rownowaznie "=".join([lista_ip[0],lista_hasla[0]])


    lista_sklejona.append(pomocniczy)

with open("hasla2.txt", "w") as f:
    for element in lista_sklejona:
        f.write(str(element) + "\n")





#slowniki powtorka

wiersz_baza_danych = {}

wiersz_baza_danych["numer_telefonu"]=888111222

wiersz_baza_danych["miasta"] = "Sosnowiec", "Grojec"

#zmienmy wartosc grojec na radom

wiersz_baza_danych["miasta"] =wiersz_baza_danych["miasta"][0], "Radom"

wiersz_baza_danych["stanowisko"]="programista"

# wiersz_baza_danych["narodowosc"]="polska"


# nazwa_kolumny = input("Nazwa kolumny ")
# narodowosc = input("Podaj narodowosc ")
#
# wiersz_baza_danych[nazwa_kolumny]=narodowosc



baza_danych = []
baza_danych.append(wiersz_baza_danych)


wiersz_baza_danych2 = {}
nazwy_kolumn = ["numer_telefonu", "miasto", "fujarka"]
wartosci = [9999, "radom", 20]


#tworzymy linie w bazie(po prostu to jest slownik, natomiast baza danych to wiele slownikow w liscie
def add_row(nazwy_kolumn,wartosci):
    wiersz_baza_danych2 = {}
    for ind, col in enumerate(nazwy_kolumn):
        wiersz_baza_danych2[col] = wartosci[ind]
    return wiersz_baza_danych2

for i in range(10):
    nazwy_kolumn = ["numer_telefonu", "miasto", "fujarka"]
    wartosci = [random.randint(1000000, 20000000), "radom"+str(i), 20+random.randint(9, 22)]
    row = add_row(nazwy_kolumn,wartosci)
    baza_danych.append(row)

# print(baza_danych)


#pokazywanie rezulatu funkcji, pobierajac "x" od uzytkownika

# def foo(x):

#     return 2*x
#
# x = int(input("Podaj liczbe"))
#
# foo(x)


#lista vs krotka vs zbior vs slownik
lista = [1,2,3,4]
krotka = (1,2,3,4)
zbior = {1,2,3,4}
slownik = {"ip":1, "passw":2,"xyz": 3, "abc":4}


#uzywam funkcji print_new_line z pliku biblioteka

from biblioteka import print_new_line, proste_statystyki1, proste_statystyki2

# print_new_line(lista)


#przeniesc fukcje proste_statyski i proste_statyki do pliku biblioteka
#a nasteonie wydrukowac ich rezulaty dla listy = [1,2,3,4]


# lista = [1,2,3,4]
# print(proste_statystyki1(lista))
# print(proste_statystyki2(lista))


#sposoby podawania danych do funkcji


def foo1(*x): #podajemy dane po przecinku
    """
    esli chcesz podac po prostu do funkcji liczb przedzielajac je przecinkiem
    zrob nastepujaco foo1(1,2,3)
    """
    return x
# foo1(1,2,3)

def foo2(x):
    """
       esli chcesz podac [liste] lub (krotke) o zrob nastepujaco
       foo2([1,2,3])
       foo2((1,2,3))

    """
    return x

# foo2([1,2,3])

def foo3(**x):
    """
    jesli chcesz przekazac slownik, zrob nastepujaco

    #1 sposob
    slownik = {"pawel":1, "maja":2}
    foo3(**slownik)

    #2 sposob
    foo3(pawel=1, maja=2, kamil=3)

    """


    return x

#sposob1
slownik = {"pawel":1, "maja":2}

#sposob2
# foo3(pawel=1, maja=2, kamil=3)


foo3(**slownik)

# parsowanie(wyciaganie danych z pliku)

path = "C:\\Users\\stasi\\Documents\\GitHub\\python_programowanie\\dane\\sample_log.txt"

dane_logi = open(path, "r").readlines()


#pobbrac z kazdej linii ip, oraz slowo home lub away, mozna rodzielic elementy za pomoca funlcki split
#rezulata zapisac do nowej listy


#pobrac z każdej linii IP, oraz słowo HOME/AWAY, można rozdzielić elementy za pomoca funkcji split
#rezultat zapisać do nowej listy
dane_po_obrobce=[]
for linia in dane_logi:
    linia=linia.strip("\n")
    linia=linia.split(" ")
    # print(linia)
    linia2=(linia[0]+" "+linia[1])
    # print(linia2)
    dane_po_obrobce.append(linia2)

# print_new_line(dane_po_obrobce)


separate_ip_network = [linia.split(" ") for linia in dane_po_obrobce]


nazwy_kolumn = ["row1", "row2"]
wartosci = separate_ip_network
def add_row(nazwy_kolumn,wartosci):
    wiersz_baza_danych2 = {}
    for ind, col in enumerate(nazwy_kolumn):
        wiersz_baza_danych2[col] = wartosci[ind]
    return wiersz_baza_danych2


# add_row(nazwy_kolumn,wartosci)

#zadanie bojowe, wyciagnac takie dane jak: data w formacie dzien/miesiac/rok oraz slowo get
#rezulat zapisac do slownika

data_str = "[01/Feb/1998:01:08:39 -0800"
# data_str.split("/")[1]
# ata_str.split("/")[2][:4] pobranie pierwszych czerech elementow



#tym sposobem wyluskujemy date i get z pliku
dane_po_obrobce2=[]
for linia in dane_logi:
    linia=linia.strip("\n")
    linia=linia.split(" ")
    linia2=((str(linia[3])[1:12])+" "+(str(linia[5])[1:5]))
    dane_po_obrobce2.append(linia2)
# print_new_line(dane_po_obrobce2)

#tutaj zapiszemy rezultat do slownika
separate_date_location = [linia.split(" ") for linia in dane_po_obrobce2]
nazwy_kolumn1 = ["row1", "row2"]
wartosci=separate_date_location

def add_row(nazwy_kolumn1,wartosci):
    wiersze_baza_danych2 = {}
    for ind, col in enumerate(nazwy_kolumn1):
        wiersze_baza_danych2[col]=wartosci[ind]
    return wiersze_baza_danych2

# baza= add_row(nazwy_kolumn1,wartosci)

# print("zapisana baza", baza)


# \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} znajdujemy IP

# \d{2}/\w{3}/\d{4} znajdujemy date

import re

pierwszy_wiersz = dane_logi[0]

ip = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", pierwszy_wiersz)

# print("Znalezione IP", ip)

#pokaz wszystkie ip z listy dane logi

# for wiersz in dane_logi:
#     ip = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", wiersz)
#     print("znalezione IP", ip)


#uzywajac regexow, zapisac do listy list - date oraz slowo GET z listy dane_logi

# print(dane_logi)
dane_logi2 = []
for wiersz in dane_logi:
    get = re.findall("GET", wiersz)
    # print("Znalezione IP", get)
    data = re.findall("\d{2}\/\w{3}\/\d{4}", wiersz)
    # print("Znaleziona data", data)
    dane_logi2.append(data+get)

# print_new_line(dane_logi2)

#bardziej kompaktowa wersja kodu

def extract_patterns(text, regex):
    matches = re.findall(regex, text)
    return matches


# print("znalezione wyrazenia", extract_patterns(wiersz, "\d{2}\/\w{3}\/\d{4}|GET"))

def for_all_lines(logi):
    """
    znajdz dla calego logu/pliku
    """
    all_rows = []
    for line in logi:
        row = str(line)
        row = extract_patterns(row, "\d{2}\/\w{3}\/\d{4}|GET")
        all_rows.append(row)
    return all_rows


print_new_line(for_all_lines(dane_logi2))





