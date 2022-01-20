from biblioteka import print_new_line

path_old = r"""C:\Users\stasi\Dropbox\Komputer\Downloads\nowy_log.txt"""

def change_path_to_windows(path):
    new_path = path.replace("\\", "\\")
    return new_path

path = change_path_to_windows(path_old)
# dane = open(path, "r").readlines()
# print_new_line(dane)

list_of_list = [['127.222.333.123'], ['127.222.333.123'], ['111.222.333.123']]

#stuczka jak splaszczyc liste list

fiatten = sum(list_of_list, [])
unique = set(fiatten)


#znalez unikalne IP w pliku nowy_log.txt
#do znalezenia IP, uzyjmy regexa ze wczoraj, znalezione regexy beda znajdowaly sie liscie
#zeby znalezc unikalne IP, zamien liste na zbior(set)
#na koniec rezulat zapisz do pliku o nazwie unikalne_ip.txt

# help(set)
# dir(set)

def parse_log(regex, input_file_name, output_name):
    pass


# dane = open(path, "r").readlines()'



path = r"""C:\\Users\\stasi\\Dropbox\\Komputer\\Downloads\\nowy_log.txt"""

dane = open(path, "r").readlines()
print_new_line(dane)


#znalez unikalne IP w pliku nowy_log.txt
#do znalezenia IP, uzyjmy regexa ze wczoraj, znalezione regexy beda znajdowaly sie liscie
#zeby znalezc unikalne IP, zamien liste na zbior(set)
#na koniec rezulat zapisz do pliku o nazwie unikalne_ip.txt

#dir(set)
#help(set)

def foo(regex, input_file_name, output_name):










# dane = open(path, "r").readlines()
