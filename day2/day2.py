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
big_lista = [[1,2,3], [4,9,8], [9,1,2]]

#1 sposob
suma1 = 0
for lista in big_lista:
    temp_sum = sum(lista)
    suma1+=temp_sum


#sposob 2
suma2 = 0
for lista in big_lista:
    temp_sum = 0
    for element in lista: #sum w sposobie numer1
        temp_sum+=element
    suma2+=temp_sum


print("suma", suma1)
print("suma", suma2)
