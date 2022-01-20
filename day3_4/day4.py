
from biblioteka import print_new_line
# #c
#
# path = r"""C:\Users\stasi\Dropbox\Komputer\Downloads"""
# path.replace(r"\", r"\\")
#
#
# # def change_path_to_windows(path):
# #     temp = path.split("\")
# #     connected_path = "\\".join(temp)
# #     return connected_path
# #
# # new_path = change_path_to_windows(path)
# # print("new path", new_path)


path = r"""C:\\Users\\stasi\\Dropbox\\Komputer\\Downloads\\nowy_log.txt"""

dane = open(path, "r").readlines()
print_new_line(dane)


#znalez unikalne IP w pliku nowy_log.txt
#do znalezenia IP, uzyjmy regexa ze wczoraj, znalezione regexy beda znajdowaly sie liscie
#zeby znalezc unikalne IP, zamien liste na zbior(set)
#na koniec rezulat zapisz do pliku o nazwie unikalne_ip.txt

def foo(regex, input_file_name, output_name):
    









# dane = open(path, "r").readlines()
