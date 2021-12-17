


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


czy_local(lista)


#uzywajac kodu z funkcji czy_lokal, sprawdzic w pliku plik.txt, ktory z ip jest lokalny badz nie
#usun haslo z linii, i zastap je komunikatem tak lub nie



# 127.0.0.1, "tak"
# 192.168.136.83, "nie"

