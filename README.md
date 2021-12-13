
name = "Adam        "
names = ["Adam", "Kamil", "Dawid"]

liczby  = range(21, 40, 2)

jumper = "Janne Ahonen na nastepnych zawodach Cie pokonam"
# jumper[0:10]
# jumper[0::2]

# list(liczby)[2:-2] od elementu o indeksie 2 do indeksu -2(ale -2 nie bierzemy pod uwage)

# names[0] pierwszy element
# names[-1] ostatni element
# names[-2] przedostatni element
# list(liczby)[0::3] co trzeci element zaczynajac od indeksu zerowego
# list(liczby)[1::3] co trzeci element zaczynajac od indeksu pierwszego


# print(len(name))
# name=name.strip()
# print(name)
# "Adam".strip("A") #sluzy do odcinanania na brzegach
#replace = zamiana w dowolnym miejscu

# "AJAX".strip("A")

# named = name.replace("d", "x")
# print(named)

# comma_IP = "196,121,1,1"
# comma_IP_without_commas = comma_IP.replace(",", ".")
# print(comma_IP_without_commas)


# print(comma_IP_without_commas.split("."))

numbers_str = ["101", "200", "300", "400", "501"]
# numbers_int = [100, 200, 300]

suma = 0
for digit in numbers_str:
    suma = suma+int(digit) #suma=100, suma=300, suma=600
# print("suma ", suma)
# print("numbers str ", numbers_str)

#suma liczb parzystych z numbers_str
suma = 0
for digit in numbers_str:
    if int(digit)%2==1:
        suma = suma+int(digit)

print("suma nieparzystych", suma)


comma_IP = "196,122,1,1"

#wyciagnc z IP liczby parzyste, i podac ich sume
comma_IP = "192,168,1,1"

sortowanie = comma_IP.split(",")
print(sortowanie)
suma = 0
for i in sortowanie:
    if int(i)%2==0:
        suma = suma+int(i)
print(suma)

lista1 = [2,1,37]
krotka1 = (1,4,88)

#key: value
hasla = {"pawel": "haslo_maslo",
         "kamil": "1234",
         "ziutek": "twoja_stara_deska_do_krojenia"}

# list(hasla.items()) wszystkie elementy

# list(hasla.keys()) wszystkie klucze
# list(hasla.values()) wszystkie wartosci

#mam wczytana z pliku liste
# lista = ["pawel", 123, "jozef", 666, "jaroslaw", 8888, "user1"]
#zeby pobrac hasla czy loginy lista[::2]
# [-1]
#trzeba nie brac pod uwage "user1", poniewaz nie ma hasla

# slownik["key"]="wartosc"




