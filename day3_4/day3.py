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


#funkcje

def kwadrat(x):
    x = x**2

    return x

def kwadrat2(x):
    x = x**2


def delta(a,b,c):
    d = b**2-4*a*c
    if d>=0:
        return "co najmniej jedno rozwiazanie"
    else:
        return "brak rozwiazan"

# a,b,c = 1,2,1
# print(delta(a,b,c))


def powieksz_o_jeden(a,b,c):
    a+=1
    b+=1
    c+=1
    return a,b,c



#zad1 napisac funkcje, ktora znaduje wieksza z dwoch podanych argumentow

def maksi(a,b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "sa rowne"



#zad2, to samo, tylko dla 3 argumentow

#to samo dla 3 argumentów
# def wieksza_z_3 (a,b,c):
#     if a>b:
#         if a>c:
#             return a
#         elif c>a:
#             return c
#         else:
#             return "a i c są równe"
#     elif b>a:
#         if b>c:
#             return b
#         elif c>b:
#             return c
#         else:
#             return "b i c są równe"
#     else:
#         return "sa równe"


def maks3(a,b,c):

    if (a>b) and (a>c):
        maxi = a
    elif (b>a) and (b>c):
        maxi = b

    elif (a==b) and (a==c) and (b==c):
        print("Rowne")
        maxi = a
    else:
        maxi = c

    return maxi


#mozna nieokreslona na poczatku liczbe parametrow


def suma_elemntow(*x): #przyjmij nieskonczona liczbe parametrow
    return sum(x) # odpakuj elementy z listy i je zsumuj

# suma_elemntow([1,2])

def pokaz_argumenty(*x):
    return x #zwroc argumenty, ktore zostaly podane

# pokaz_argumenty(9,1,2)

def proste_statystyki(*liczby):
    maxi = max(liczby)
    mini = min(liczby)
    suma = sum(liczby)
    srednia = suma/len(liczby)
    return maxi, mini, suma, srednia

#zadanie bojowe, przerobic funkcje proste statystki, zeby wzracala slownik
#klucze: max, min, suma, srednia
#slownik = {}
#slownik["max"]


def proste_statystyki2(*liczby):
    maxi=max(liczby)
    mini=min(liczby)
    suma=sum(liczby)
    srednia=suma/len(liczby)

    slownik = {}
    slownik['maxi'] = maxi
    slownik['mini'] = mini
    slownik['suma'] = suma
    slownik['srednia'] = srednia

    return slownik

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

from biblioteka import print_new_line

print_new_line(lista)




















