

#funkcja, ktora przyjmuje jako parametr x
# class Ania:
#     # def __init__(self, x):
#     #     self.x = x
#
#     # def kwadrat(self):
#     #     return self.x**2
#     def kwadrat(self, x):
#         return x**2
#
#
# klasa1 = Ania(8)
#
#
# def kwadrat(x):
#     return x**2
#
# print("kwadrat z klasy", klasa1.kwadrat(7))
# print("kwadrat z fun", kwadrat(8))


class Uczen:
    #wlasciwosci
    def __init__(self, name, surname, level):
        self.name = name
        self.surname = surname
        self.level = level

    #metody
    def show_full_name(self):
        return self.name+" "+self.surname

uczen1 = Uczen("Ania", "Do", 8)
uczen2 = Uczen("Kamil", "Uch", 7)

# print(uczen1.name)
# print(uczen2.name)
#
#
# print(uczen1.show_full_name())
# print(uczen2.show_full_name())


#stworzyc klase prostokat, ktory w inicie bedzie dwa parametry, dlugosci i szerokosc oraz metoda pole,
# ktora wzraca pole prostokata, i na koncu stworzyc

class prostokat:

    #wlasciwosci
    def __init__(self, bok_a, bok_b):
        self.bok_a = bok_a
        self.bok_b = bok_b

    #metody
    def pole_prostokat(self):
        return self.bok_a*self.bok_b

    @staticmethod
    def pole_prostokat2(x, y):
        return x*y

    #magic/special functions
    def __str__(self):
        return "To jest prostokat o bokach dlugosci a={}, b={}".format(self.bok_a, self.bok_b)

    def __add__(self, other):
        return self.bok_a+other.bok_a, self.bok_b+other.bok_b


p1 = prostokat(2,7)
print(p1)

p2 = prostokat(8,9)
print(p2)

p3 = prostokat(8,9)
print(p2)

# prostokat.pole_prostokat2(7,8)

