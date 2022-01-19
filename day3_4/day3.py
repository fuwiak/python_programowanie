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


lista = [1,2,3,4]
print(proste_statystyki1(lista))
print(proste_statystyki2(lista))



