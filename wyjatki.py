# log = open("logi.txt").readlines()

# def too_long(linia):
#     if not len(linia)>173:
#         raise AssertionError("Zbyt dlugi log")
#     return linia
#
#
# for i in range(len(log)):
#
#     try:
#         #nasz caly kod, ktory ma byc niezawodny
#         print(too_long(log[i]))
#     except Exception as e:
#         #czynnosci, ktore wykonujemy w razie awarii
#         print(e)

#zadanie wyciagnac dla kazdej linia IP, i drukowac tylko wiersze zaczynajacde od ip 127
#dla ip ktore nie zaczynaja od 127, dac komunikat "access denied", regex i wykj

# def not127(linia):
#     if not linia[:3]=='127':
#         raise AssertionError("access denied")
#     return linia
#
#
#
# data = open("sample_log.txt").readlines()
#
# for ind, line in enumerate(data):
#
#     try:
#         #nasz caly kod, ktory ma byc niezawodny
#         print(not127(line))
#     except Exception as e:
#         #czynnosci, ktore wykonujemy w razie awarii
#         print(e)



#kolejne zadanko
# pokazac tylko, gdzie jest polaczenie https, jesli nie, to dac komunikat(rzucamu wyjatkiem) "niebezpieczne polaczenie"
def notsafe(linia):
    if "https" not in linia:
        raise AssertionError("niebezpieczne połączenie")
    return linia



data = open("sample_log.txt").readlines()

for ind, line in enumerate(data):

    try:
        #nasz caly kod, ktory ma byc niezawodny
        print(notsafe(line))
    except Exception as e:
        #czynnosci, ktore wykonujemy w razie awarii
        print(e)



