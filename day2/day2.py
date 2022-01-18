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


lista_losowa = []

for i in range(10): # dziesiec razy bedzie losowana liczba
    losowa_liczba = random.randint(21, 37) #losowanie liczby
    lista_losowa.append(losowa_liczba)

print("losowa lista", lista_losowa)


#lsoujmy 20 liczb z zakresu od 100 do 200, dodajmy te elementy do listy a nastepnie policzmy srednia
#arytmetyczna z liczb tylko parzystych
#przyklad

#[101, 104, 106, 109]
# (104+106) / 2 = 105












