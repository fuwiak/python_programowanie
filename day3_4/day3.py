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

