

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

print(uczen1.name)
print(uczen2.name)


print(uczen1.show_full_name())
print(uczen2.show_full_name())