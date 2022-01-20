from biblioteka import print_new_line
import re

path_old = r"""C:\Users\stasi\Dropbox\Komputer\Downloads\nowy_log.txt"""

def change_path_to_windows(path):
    new_path = path.replace("\\", "\\")
    return new_path

path = change_path_to_windows(path_old)

#znalez unikalne IP w pliku nowy_log.txt
#do znalezenia IP, uzyjmy regexa ze wczoraj, znalezione regexy beda znajdowaly sie liscie
#zeby znalezc unikalne IP, zamien liste na zbior(set)
#na koniec rezulat zapisz do pliku o nazwie unikalne_ip.txt

#dir(set)
#help(set)


regex = r"""\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"""

def parse_log(regex, input_file_name, output_name):
    list_out = []
    dane = open(input_file_name, "r").readlines()

    for row in dane:
        ip = re.findall(regex, row)
        list_out.extend(ip)
    out = list(set(list_out))

    ile_systemow = len(out)
    # print("Liczba roznych systemow", ile_systemow)


    # with open(output_name, "w") as f:
    #
    #     f.write(str(out))

    with open(output_name, "w") as f:
        for element in out:
            f.write(str(element)+'\n') #kazdy element listy w nowym wierszu


# parse_log(regex, path, "unikalne_ip.txt")


#uzywajac funkcji parse log, podac liczbe systemow uzuywanych w logu, rezulat zapisc kazdy w nowej linii,
#unikalne systemy



regex2 =r"""Ubuntu|Windows|Macintosh"""
parse_log(regex2, path, "unikalne_systemy.txt")

#wyjatki i assercje



#przyklad assercji

def podaj_mase1(masa):
    if not masa>0:
        raise AssertionError("masa musi byc dodatnia")
    return masa

# print(podaj_mase1(99)) #tutaj nie ma zadnego problemu
#
# print(podaj_mase1(-99)) #tutaj nie ma zadnego problemu


#wyjatki anty - przrzyklad- petla sie wykonuje do ppierwszego napotkanego problemu

lista = [2, 1, "pawel", 7, "lukasz"]

# for x in lista:
#     print(x/2)

# try:
#     for x in lista:
#         print(x/2)
# except:
#     pass
#

#jak przejsc przez wszystkie elementy? obsluzyc wyjatek - czyli wymyslec co zrobic w przypadku
#napotkanego bledu

# for x in lista:
#     try:
#         print(x / 2)
#     except:
#         print(x+" niestey nie mozemy dzielic tekstu przez liczbe")


#jak sprawdzic, jakiego typu blad w danej sytuacji?

# for x in lista:
#     try:
#         print(x / 2)
#     except Exception as e:
#         print(e)

#jesli byc pewni, ze wszystkie elementy podzielone(w ogolnosci zostal kod pomiedzy try a except i wykonane
#wszystkie sytuacje specjalne, uzyjmy do tego slowa kluczowego finally
# try:
#
#     for x in lista:
#         print(x/2)
# except Exception as e:
#     print(e)
# finally:
#     print("wszystkie elementy podzielone")



#zadanie wyciagnac dla kazdej linia IP z lowy_logt.txt i drukowac tylko wiersze zaczynajacde od ip 127
#dla ip ktore nie zaczynaja od 127, dac komunikat "access denied"


# def not127(linia):
#     if not linia[:3]=='127': # tu dzialanie jesli nastapi jakis blad/wyjatek
#         raise AssertionError("access denied")
#
#     #w nastepnych liniach mozemy zdefiniowac dzialania jakie wykonujemu, jesli bledy czy
#     #wyjatki nie nastapily
#
#     return linia

# dane = open(path,"r").readlines()
# for x in dane:
#     try:
#
#         print(not127(x))
#     except Exception as e:
#         print(e)
#         # print("Access denied")


#kolejne zadanko
# pokazac tylko, gdzie jest polaczenie https, jesli nie, to dac komunikat(rzucamu wyjatkiem) "niebezpieczne polaczenie"


# def notsafe(linia):
#     if "https" not in linia:
#         raise AssertionError("niebezpieczne połączenie")
#     return linia
#
# dane = open(path, "r").readlines()
# for x in dane:
#     try:
#         print(notsafe(x))
#     except Exception as e:
#         print(e)




#wstep do klas

class Uczen:
    def __init__(self, name, surname, level):
        self.name = name
        self.surname = surname
        self.level = level

    def przedstaw_sie(self):
        return "Nazywam sie {} {} i chodze do klasy nr {}".format(self.name, self.surname, self.level)

ania = Uczen("Ania", "Kowalska", 1)

bobek = Uczen("Robert", "Lewandowski", 99)

# print(ania.przedstaw_sie()) #pierwszy egzemplarz Ucznia
#
# print(bobek.przedstaw_sie()) #drugi egzemplarz Ucznia

# print("Imie ", ania.name)
# print("Nazwisko ", ania.surname)
# print("klasa ", ania.level)


#stworzmy klase prostokat, ktora przyjmuje 2 parametry, a i b
#nastepnie stworzyc 2 funkcje w klasie, pole_prostokata i obwod prostokata
#ktore zwracaja wartosci pola i jak obwodu
#stworzyc 2 instancje(wystapienia) klasy prostokat(prostiej stworz 2 prostokaty o roznych dlugosciach boku)

class Prostokat:
    #wlaściwości
    def __init__(self, bok_a, bok_b):
        self.bok_a = bok_a
        self.bok_b = bok_b

    def pole_prostokata(self):
        return "Pole prostokąta wynosi {}".format(self.bok_a * self.bok_b)
    def obwod_prostokata(self):
        return "Obwod prostokata wynosi {}".format(self.bok_a*2 + self.bok_b*2)



# print(prostokat1.pole_prostokata())
# print(prostokat1.obwod_prostokata())
# print(prostokat2.pole_prostokata())
# print(prostokat2.obwod_prostokata())
# print(prostokat3.pole_prostokata())
# print(prostokat3.obwod_prostokata())
#




class Prostokat:
    #wlaściwości

    #own special methods

    def __init__(self, bok_a, bok_b, nazwa_zmiennej):
        self.bok_a = bok_a
        self.bok_b = bok_b
        self.nazwa_zmiennej = nazwa_zmiennej

    def __add__(self, other):
        return self.bok_a*self.bok_b + other.bok_a*other.bok_b

    def __str__(self): #print ladnie wyswietlenie
        return "{} o bokach o dlugosci {} {}".format(self.nazwa_zmiennej, self.bok_a, self.bok_b)

    def __repr__(self): #ladnie wyswietlenie w konsoli
        return "{} o bokach o dlugosci {} {}".format(self.nazwa_zmiennej, self.bok_a, self.bok_b)



    def pole_prostokata(self):
        return "Pole prostokąta wynosi {}".format(self.bok_a * self.bok_b)
    def obwod_prostokata(self):
        return "Obwod prostokata wynosi {}".format(self.bok_a*2 + self.bok_b*2)

prostokat1 = Prostokat(10,20, "prostokat1")
prostokat2 = Prostokat(10,50, "prostokat2")
prostokat3 = Prostokat(30,45, "prostokat3")


# print("Dodaj do siebie dwa prostokaty", prostokat1+prostokat3)



# print(prostokat1)


#klasa wektor2d

import math



class wektor2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self): #print
        return "({} , {})".format(self.x, self.y)
    def __repr__(self): #widok w konsoli
        return "({} , {})".format(self.x, self.y)

    def __add__(self, other):
        return "Suma wektorów  ({},{})".format(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return "Różnica wektorów  ({},{})".format(self.x-other.x, self.y-other.y)

    def __mul__(self, other): #iloczyn x1*x2, y1*y2
        return "Iloczyn wektorow  {} {}".format(self.x*other.x, self.y*other.y)

    def __abs__(self):
        return "Wartość bezwzględna wektorów {}".format((self.x**2 + self.y**2)**0.5)

    def __eq__(self, other):
        if (self.x == other.x) and (self.y == other.y):
            return "Wektory są równe"
        else:
            return "Wektory nie są równe"


w1 = wektor2d(2, 5)
w2 = wektor2d(4, 8)
w3 = wektor2d(2, 5)


# print(w1)
# print(w2)
#print(abs(w1))

print("suma w1 oraz w2 " ,w1+w2)
print("roznica w1 oraz w2 ", w1-w2)
print("Iloczyn wektorow w1 oraz w2", w1*w2)
print("wartosc bezwzgledna w1", abs(w1))

print("czy w1==w3", w1==w3)
print("czy w1==w2", w1==w2)

#uzupelnic funkcjonalnosc klasy wektor o nastepujace szczegoly:


#reprezentacja tekstowa __repr__ ----> po wpisaniu w konsole w1, chce dostac komunikat wektor =(x,y)
##reprezentacja dla printa __str__ ----> po wpisaniu w konsole pringt(w1), chce dostac komunikat wektor =(x,y)

#dodawanie __add__
#odejmowanie __sub__
# mnozenie __mul__ suma(x1*x2+y1*y2) __mul__
# wartosc bezwzgledna __abs__ math.sqrt(x**2+y**2)


#znak rownosci, __eq__  w1==w2 --> True





