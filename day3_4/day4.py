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
    print("Liczba roznych systemow", ile_systemow)


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
try:

    for x in lista:
        print(x/2)
except Exception as e:
    print(e)
finally:
    print("wszystkie elementy podzielone")



#zadanie wyciagnac dla kazdej linia IP z lowy_logt.txt i drukowac tylko wiersze zaczynajacde od ip 127
#dla ip ktore nie zaczynaja od 127, dac komunikat "access denied"

# def not127(linia):
#     if not linia[:3]=='127':
#         raise AssertionError("access denied")
#     return linia






