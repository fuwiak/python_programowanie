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

def proste_statystyki1(liczby):
    maxi = max(liczby)
    mini = min(liczby)
    suma = sum(liczby)
    srednia = suma/len(liczby)
    return maxi, mini, suma, srednia


def print_new_line(lista):
    for line in lista:
        print(line)

#zadanie bojowe, przerobic funkcje proste statystki, zeby wzracala slownik
#klucze: max, min, suma, srednia
#slownik = {}
#slownik["max"]


def proste_statystyki2(liczby):
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
