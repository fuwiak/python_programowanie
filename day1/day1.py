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
# delta = b**2-4*a*c
#
# print("delta", delta)
# if delta>0:
#     print("2 rozwiazania")
# elif delta==0:
#     print("1 rozwiazanie")
# elif delta==2:
#     print("delta rowna 2")
# else:
#     print("Brak rozwiazan")


#zad bmi
 # waga = input()
 # wzrost = input()


# bmi=waga/wzrost**2

# 16,0–16,99

#na postawie danych z wikipedii, wypisywac komunikaty w stulu - wychudzony, otyly itd
#zakresy bmi znajduja sie na wikipedii(link w czacie)

# waga = float(input("Wpisz swoja wage"))
# wzrost = float(input("Wpisz swoj wzrost w metrach"))
# bmi = waga/wzrost**2
#
# print("Twoje BMI wynosi", bmi, "Twoja kategoria bmi to:\n")
# if bmi < 16:
#     print("wyglodzenie")
# elif bmi >= 16 and bmi <16.99:
#     print("Wychudzenie")
# elif bmi >= 17 and bmi < 18.49:
#     print("Niedowaga")
# elif bmi >= 18.5 and bmi <24.99:
#     print("Pozadana masa ciala")
# else:
#     print("idz na silownie")




# for i in range(1,11): #wypisz wsystkie liczby z zakresu od 1 do 11(ale juz 11 nie uwzgledniaj)
#     print(i)



# for i in range(6, 100, 6): #start 2, end = 100(bez 100), krok = 5
    # print("Wartość iteratora to " + str(i))
    # print("Wartość iteratora to ", i)
    # print(i)

# powtarzanie czynnosci

path = "c;//pawel/logi/log"

#log1, log2, log3, ... log100

# for i in range(0,100):
#     new_path = path+str(i)
#
#     print(new_path)

#zad range(6, 100, 6): #start 2, end = 100(bez 100), krok = 5

# korzystajac z wyzej wymienionej konstrukcji oraz petli for wypisac liczby z zakresu od 200 do 950(bez 950)
# z krokiem co 4 elementy


# for i in range(200,950, 4):
#     print("Wartość iteratora to " + str(i))

# a = 200
#
# while(a<950):
#     print(a)
#     a+=4

# moja_liczba = 9
#
# while(moja_liczba>0):
#     print(moja_liczba)
#     moja_liczba = int(input("Podaj liczbe "))

a = 0

# while(a<20):
#     a+=1
#     if a%2==0: #jesli liczba jest parzysta, to przeskocz ta sytuacje
#         continue
#     print(a)



# while(a<20):
#     a+=1
#     if a%2==0: #jesli liczba jest parzysta, to koncz
#         break
#     print(a)


#uzywajac petli while, wypisac kwadraty liczby 2, zakres od 1 do 1024

# a = 200
#
# while(a<950):
#     print(a)
#     a+=4

# a=1
# while (a<=1024):
#     print(a)
#     a=a*2
#

s1 = "Ala ma kota"

# print(s1[1:]) # wypisujemy s1 od drugiego elementu(z indeksem numer1)

# print(s1[1:4]) # wypisujemy s1 od drugiego elementu(z indeksem numer1) do czwartego

# print(s1[-1]) #ostatni element

# print(s1[-2]) #przedostatni element

# print(s1[-3]) #3 od konca

# print(s1[-3]+" "+s1[-7]) konretnie 2 symbole(index=-3, oraz index=-7)

# print(s1[-3]) #3 od konca


# print(s1[3:7])

# print(s1[::-1]) #odwrocenie stringu


#pobieranie co ktoregos elementu

# print(s1[0::2]) #pobierz co drugi element, zaczynajac od indeksu 0

# print(s1[1::3]) #pobierz co trzeci element, zaczynajac od indeksu 1

#liczymy liczbe znakow w danym stringu
# print("liczba spacji w s1", s1.count(" "))

# print('liczba spacji w s1', s1.count(' '))

# print("liczba liter a w s1", s1.count("a"))

# print("liczba literek a w s1 bez wzgledu na wielkosc litery", s1.lower().count('a'))

# print("liczba liter a w s1", s1.count("a")+s1.count("A"))


# print("Wszystkie duze litery", s1.upper())


#laczenie slow(stringow)
# ala = ["Ala", "ma", "kota"]
# print("+".join(ala)) #laczymy slowa w pudelku ala za pomoca znaku +

#dzielenie stringa

# podzielony_string = s1.split(" ") #podzielony string wg spacji

# s2 = "Ala ma kota       "
# s3 = "       Ala ma kota"
#
# s2.strip()#golenie z dwoch stron
# s3.lstrip()#golenie z lewej strony
# s2.rstrip()#golenie z prawej strony

# s1.replace("A", "X")#podmiana litery A na litere X


