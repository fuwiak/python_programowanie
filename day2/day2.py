lista = [1, 5, 2, 4, 3]

# print(lista[1:]) # pobieramy wszystko od elementu od indeksu nr 1

# print(lista[::-1]) #lista odwrotnie

# print("suma listy", sum(lista))
# print("max listy", max(lista))
# print("min listy", min(lista))

lista1 = ['a', 2,1, 9, 0] #sprawdze co z tymi ujemnymi

# suma = 0
# for liczba in lista1:
#     if str(liczba).isdigit()==True: #jesli element listy jest cyfra, to dodaj
#         print(liczba)

# len(lista1) liczba elementow listy

# print("suma", suma)

#dla zadanej listy, lista2 = ['a', 'b', 'c', 1,2,3]
#policzyc srednia arytmetyczna danej listy nie uwzgledniajac liter
#wynik ma wyniesc dwa, mozemy uzyc petli i licznikow


lista2 = ['a', 'b', 'c', 1, 2, 3]

# suma=0
# licznik=0
# for liczba in lista2:
#     if str(liczba).isdigit()==True: #jeśli element listy jest cyfrą, to dodaj, jest to równoznaczne z if str(liczba).isdigit()
#         suma = suma+liczba
#         licznik+=1
#
# print("średnia =", suma/licznik)



#dodawanie elementow do listy

# lista3 = []
#
# lista3.append(4)
#
# print(lista3)
#
# lista3.append(9)
#
# print(lista3)
#
#
# lista3.append(11)
#
# # print(lista3.append(77)) #czesty blad poczatkujacych
#
# print(lista3)


import random


# lista_losowa = []
#
# for i in range(10): # dziesiec razy bedzie losowana liczba
#     losowa_liczba = random.randint(21, 37) #losowanie liczby
#     lista_losowa.append(losowa_liczba)
#
# print("losowa lista", lista_losowa)


#lsoujmy 20 liczb z zakresu od 100 do 200, dodajmy te elementy do listy a nastepnie policzmy srednia
#arytmetyczna z liczb tylko parzystych
#przyklad

#[101, 104, 106, 109]
# (104+106) / 2 = 105


lista_losowa = []
for i in range(20):                           # 20 razy losuje liczbę
    losowa_liczba = random.randint(100, 200)  # losowanie liczby
    lista_losowa.append(losowa_liczba)

# print("losowa lista ", lista_losowa)
# licznik = 0
# suma = 0
# for i in range(20):
#     if lista_losowa[i]%2==0:
#         suma+=lista_losowa[i]
#         licznik+=1

# for x in lista_losowa:
#     if x%2==0:
#         suma+=x
#         licznik+=1




# srednia=suma/licznik
#
# print("suma liczb parzystych =", suma)
# print("srednia z liczb parzystych ", srednia)


# for ind, element in enumerate(lista_losowa):
#     print("index", ind, "element", element)

#usuwanie elementu z listy

# lista4 = [1,2,3,4]
#
# lista4.remove(4)
# print(lista4)
#
# lista4.remove(3)
# print(lista4)


# lista4.remove(3)
# print(lista4)

# print(lista4.remove(1))

#podmiana dowolnego elementu uzywajac indeksow
lista5 = [9,2,7,8]

# lista5[1]='aaa'
#
# print(lista5)
#
# lista5[-1]='bbb'
#
# print(lista5)


#sprawdzenie czy dany element znajduje sie w liscie
# szukany_element = 7
#
# for element in lista5:
#     if szukany_element in lista5:
#         print("znalezlismy szukany element")
#         break
#
#




#szkukamy liczb parzystych w zakresie 0, 100

# a=0
#
# while(a<100):
#     a+=1
#     if a%2==1: #jesli liczba jest nieparzysta, to przeskocz ta sytuacje
#         continue
#     print(a)

# listy vs stringi

# napis = "Hello"
# # napis[0]="XXXX" tak nie mozna podmnieniac elementow stringa
# napis = list(napis) #zamieniamy string ma liste, by moc podmniec np pierwszy element napisu
# napis[0]="XXXX" # modifikacja listy
#
# napis= "".join(napis) #powrot zmodyfikowanej listy do stringa


lista6 = [1,2,3]
lista7 = [4,5,6]

# print(lista6+lista7) #sklejanie listy
#
# lista6.extend(lista7) #sklejanie listy(rozszerenie listy 6)
# print(lista6)

#zagniezdzanie petli

# for x in lista6:
#     for y in lista7: #zanim przeszkocznym do nastepnego elementu x, musza przejsc wszystkie y
#         print(x*y,end=" ")
#
#
# for kolumna in excel
#     for wiersz in kolumna:
#         print(wiersz)


#wygerowac liste 20 liczb losowych, dodac je do listy, nastepnie podac indeksy liczb nieparzsych z tej listy
#enumerate

# lista_losowa = []
# for i in range(20):                           # 20 razy losuje liczbę
#     losowa_liczba = random.randint(0, 1000)  # losowanie liczby
#     lista_losowa.append(losowa_liczba)
#
# for ind, element in enumerate(lista_losowa):
#     if element % 2 == 1:
#        print ("index", ind, "element", element)


#listy skladane(list comprehensions)

# lista_losowa = [random.randint(0, 1000) for i in range(20)]
# print(lista_losowa)

#filtrowanie listy

lista8 = [-1,0,-8,99,100, -8, 77] #podac z danej lsity tylko liczby dodatnie
only_pos  = []

for liczba in lista8:
    if liczba>0:
        only_pos.append(liczba)

# print(only_pos)

#nowy sposob

only_pos2 = [x for x in lista8 if x>0]
# print(only_pos2)


#uzywajac list comprehension, zostac w liscie8 tylko liczby parzyste

lista8 = [x for x in lista8 if x%2==0]

# print(lista8)

#zagniedzone listy, list of list

big_lista = [[1,2,3], [4,9,8], [9,1,2]]

# print(big_lista[0][-1]) #ostatni elemnt pierwszej listy
#
# print(big_lista[1][-1]) #ostatni elemnt drugiej listy


# gniazdo_list = [[1, [7,8,,9] 3], [2,3,4], [1,[8,1,2]]]


# print(gniazdo_list[0][1][0]) #pobieramy pierwsza liste. nastepnie z wybranej listy pobieramy
#drugi element, a nastepnie pierwszy z brzegu

#zeby dobrac do 8 [1,[8,1,2]] trzeba uzyc indeksu [2][1][0]


#zadanko zagniezdzone listy, uzywaja zagniezdzonej petli for lub list comprehension
#podac sume zagniezgdzonek listy: big_lista
# big_lista = [[1,2,3], [4,9,8], [9,1,2]]
#
# #1 sposob
# suma1 = 0
# for lista in big_lista:
#     temp_sum = sum(lista)
#     suma1+=temp_sum
#
#
# #sposob 2
# suma2 = 0
# for lista in big_lista:
#     temp_sum = 0
#     for element in lista: #sum w sposobie numer1
#         temp_sum+=element
#     suma2+=temp_sum
#
#
# print("suma", suma1)
# print("suma", suma2)

# zerkniesz na to: ?
# big_lista = [[1,2,3], [4,9,8], [9,1,2]]
#
# suma =0
# for lista in big_lista:
#     temp_sum=0
#     temp_sum=sum(lista)
#     suma+=temp_sum
# print(suma)


#praca z plikami

#wersja - czytamy w ktorym jednoczesnie znajduje sie nasz kod

# dane1 = open("plik.txt", "r").readlines() #wczytujemy plik do listy
# # print(dane1)
#
# dane2 = open("plik.txt", "r").read() # wczytujemy plik do stringa
# # print(dane2)

#ostroznie z sciezkami bezwglednymi, czasami nalezy dopisac \\
path = "C:\\Users\\stasi\\Dropbox\\Komputer\\Downloads\\plik.txt"

dane3 = open(path, "r").readlines()

#zadanie bojowe

#wczytac plik.txt do listy, nastepnie rozdzielic ip od hasla(split) i jednoczesnie podac komunikat
#ile liter ma dane haslo(len(lista[9]), zeby wyczysci znak \n, uzyc konstrukcji strip('\n')
#przyklad
#188.168.91.121=AKAMdkPs

#[188.168.91.121, AKAMdkPs, 8]

data = open("plik.txt", "r").readlines() #wczytujemy plik do listy
# print(data)

# for linia in data:
#     linia=linia.strip('\n')
#
#     linia=linia.split("=")
#     linia2=[linia[0], linia[1], len(linia[1])]
#     print(linia2)

#zapisywanie danych do pliku

lista = [3,3,3,3]

#sposob 1
# with open("new_file1.txt", "w") as f:
#     print(lista, file=f)

#sposob 2

with open("new_file3.txt", "w") as f:
    for element in lista:
        f.write(str(element)+'\n') #kazdy element listy w nowym wierszu


#aktualizacja plik.txt
#kazdego z hasel dodac od 3 do 5 nowych znakow
#plik.txt ma byc zaktualizowany nowymi haslami


#zamiana cyfry na znak 33-126
#random.randint(65, 126)

# print(chr(102))

# "pawelsahbdhjs"+"x"+"y"+"z"

# path = "plik.txt"
# dane = open(path,"r").readlines()
# lista_ip = []
# lista_hasla = []
# linia2 = []
# for linia in dane:
#     linia = linia.strip("\n")
#     linia = linia.split("=")
#     linia2 = [linia[0], linia[1], len(linia[1])]
#     lista_ip.append(linia2[0])
#     lista_hasla.append(linia2[1])
#
# with open("nowe_hasla.txt", "w") as f:
#     for haslo in lista_hasla:
#         liczba_dodanych = random.randint(3,5)
#         for i in range(liczba_dodanych):
#             string = chr(random.randint(66,126))
#             haslo=haslo+string
#         f.write(str(haslo)+"\n")

# for linia in data:
#     extra_znaki=""
#     linia=linia.strip('\n')
#     linia=linia.split("=")
#     n=random.randint(3, 5)
#     for i in range(n):
#         extra_znaki+=(chr(random.randint(65,126)))
#     linia2=[linia[0], linia[1]+extra_znaki]
#     print(linia2)


#krotki

a = [1,4,5]
b = (1,5,8)

#zamiana tupli na liste

b = list(b)

#zamian listy na tuple

b = tuple(b)
#slowniki

miasta = {}                     # nowy słownik
# miasta['id'] = {name, surname, salary}
miasta['WAR'] = "Warszawa" #klucz, wartosc
miasta['KRA'] = "Kraków"
miasta['WRO'] = "Wrocław"
miasta["RAD"] = "Radom"
miasta["XYZ"] = "Sosnowiec", "Grojec"
miasta[123]="Polska"

miasta[(1236)]="Germany"




# print("Wszystkie skroty", miasta.keys())
# print("Wszystkie miasta", miasta.values())
# print("Slownik do listy krotek", miasta.items())
#
# print("Wszystkie skroty", list(miasta.keys()))
# print("Wszystkie miasta", list(miasta.values()))
# print("Slownik do listy krotek", list(miasta.items()))


# miasta["XYZ"]="Posen" modyfikacja wartosi pod kluczem XYZ

lista = ['pawel',123,'jozef',666,'jaroslaw',8888,'user1'] #klucz, wartosc, klucz, wartosc, klucz, wartosc

#zamienic liste na slownik, co drugi element z listy pobieramy za pomoca lista[::2], lista[1::2]
#lista = lista[:-1] lista bez ostatniego elementu

lista = lista[:-1]
klucze = lista[::2]
wartosci = lista[1::2]

slownik = {}

for i in range(len(klucze)):
    slownik[klucze[i]]=wartosci[i]


#zbiory(zestawy, set)

# A = {1:1,2:2,3:3}
# slownik = {}


lista = [2,2,3,5,2]

zbiorA = set(lista) #jesli chcesz miec unikalne wartosci w danej kolekcji, uzyj zbioru(setu)

A = {1,2,3,4}
B = {3,4,5,6}

A = set(lista)

print("suma dwoch zbiorow", A.union(B))
print("czesc wspolna dwoch zbiorow", A.intersection(B))
print("roznica dwoch dwoch zbiorow A-B", A.difference(B))
print("roznica dwoch dwoch zbiorow B-A", B.difference(A))


# slownik["klucz"]="wartosc"


#wygenerowac dwie listy po 20 elementow(losowo), a zakres od 10 do 20, za pomoca setu wziac z jednej i drugie unikalne wartosci,
#i pdac sumie, czesc, i roznice symetryczna pomiedzy zbiorami, A-B, B-A

# lista_losowa = [random.randint(0, 1000) for i in range(20)]
# print(lista_losowa)

lista1 = [random.randint(10,20) for i in range(20)]
lista2 = [random.randint(10,20) for i in range(20)]

l1 = set(lista1)
l2 = set(lista2)

print("l1",l1)
print("l2", l2)

print("Suma dwoch zbiorów", l1.union(l2))
print("Czesc wspólna", l1.intersection(l2))
print("Roznica l1-l2", l1.difference(l2))
print("Roznica l2-l1", l2.difference(l1))
print("Różnica dwóch zbiorów B-A", l2.symmetric_difference(l1))
print("Różnica dwóch zbiorów A-B", l1.symmetric_difference(l2))














#
#
# #chce pobrac pierwszy elemt items
# dane=open("plik.txt", "r").readlines()
# lista_ip=[]
# lista_hasla=[]
# linia2 =[]
# for linia in dane:
#     linia = linia.strip("\n")
#     linia = linia.split("=")
#     linia2 = [linia[0], linia[1], len(linia[1])]
#     lista_ip.append(linia2[0])
#     lista_hasla.append(linia2[1])
#
# with open("nowe_hasla.txt", "w") as f:
#     for haslo in lista_hasla:
#         liczba_dodanych=random.randint(3,5)
#         for i in range(liczba_dodanych):
#             string = chr(random.randint(33,126))
#             haslo=haslo+string
#
#             string = ""
#         print(haslo)
