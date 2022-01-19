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

#zad2, to samo, tylko dla 3 argumentow











