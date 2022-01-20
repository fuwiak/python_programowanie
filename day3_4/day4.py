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
    with open(output_name, "w") as f:

        f.write(str(out))


parse_log(regex, path, "unikalne_ip.txt")
