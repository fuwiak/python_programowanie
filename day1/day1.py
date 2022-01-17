"""
x = 4            # integer
x1 = x + 4       # dodawanie
x2 = x - 1       # odejmowanie
x3 = x * 3       # mnożenie
x4 = x / 2       # odejmowanie
x += 2           # x = x + 2
x -= 2           # x = x - 2
x *= 3           # x = x * 3
x /= 3           # x = x / 3
x5 = x           # przypisanie zmiennych
x6 = x % 4       # dzielenie modulo


"""

z = 3.14         # floating point
z1 = z + 2.0     # dodawanie
z2 = z - 2.0     # odejmowanie
z3 = z / 3.0     # dzielenie
z4 = z // 3.0    # dzielenie całkowite
z += 2.0         # z = z + 2
z -= 2.0         # z = z - 2
z *= 3.0         # z = z * 3
z /= 3.0         # z = z / 3
z5 = z ** 2      # z^2
z6 = z ** 0.5    # z^(1/2) == sqrt(z)
z7 = pow(z,2)    # z^2
z8 = round(z)    # zaokrąglenie do najbliższego integera
z9 = int(z)


#zad2 stworzyc zmienne, a, b,c i wypisac na ekran wartosci wyrazenia b do kwadratu odjac 4ac
# zmienne a b c maja byc zmiennymi z przecinkiem
#wypisac rezultat na ekran
"""

a = float(input("Podaj zmienna a "))
b = float(input("Podaj zmienna b "))
c = float(input("Podaj zmienna c "))
d = b**2-4*a*c



print("wartosc zmiennej d", d)

"""

# y1 = True
# y2 = True
#
# print("AND ", y1 and y2)       # logiczny AND
# print("OR ", y1 or y2)        # logiczny OR
# print("NOT ", y1 and not y2)   # logiczny NOT


import math


# print("pierwiastek z dwoch", 2**0.5)
# print("pierwiastek z dwoch", math.sqrt(2))

# x = 4
# print(math.sqrt(x))      # sqrt(4) = 2
# print(math.pow(x,2))     # 4**2 = 16
# print("exp", math.exp(x))       # exp(4) = 54.6
# print("log", math.log(x))       # ln(x)
# print(math.log(x,10))    # log_10(x)
# print(math.fabs(-4))     # wartość bezwzględna
# print(math.factorial(x)) # 4!

#help(math) #dluzsza podpowiedz
#dir(math) # bardzo lakoniczna


# round(math.exp(x),2)

x = 16

# instrukcja warunkowa if

# if x % 2 == 0: #jesli ten warunek jest prawdziwy(x%2==0)
#     print("Liczba parzysta") #wtedy wykonuj to dzialanie
# else: #jesli jednak warunek z if nie jest prawdziwy, to wykonaj to co znajduje sie po slowie else
#     print("Liczba nieparzysta") #


#zd3 uzywajac funkcji input, wprowadzic liczbe x do programu i jesli bedzie nieparzysta dac dac komunikat
#nieparzysta liczba, w przeciwnym przypadku dac komunikat "nie szukalem takiej liczby:

# x = int(input("podaj x "))
# if x % 2 !=0:
#     print("Liczba nieparzysta")
# else:
#     print("nie szukałem takiej liczby")

a, b, c = 7, 1, 1
# a=1
# b=2
# c=1
delta = b**2-4*a*c

print("delta", delta)
if delta>0:
    print("2 rozwiazania")
elif delta==0:
    print("1 rozwiazanie")
elif delta==2:
    print("delta rowna 2")
else:
    print("Brak rozwiazan")


#zad bmi
 waga = input()
 wzrost = input()


# bmi=waga/wzrost**2

# 16,0–16,99

#na postawie danych z wikipedii, wypisywac komunikaty w stulu - wychudzony, otyly itd
#zakresy bmi znajduja sie na wikipedii(link w czacie)


if bmi>=16 and bmi<16.99:
    print("wychudzenie")

