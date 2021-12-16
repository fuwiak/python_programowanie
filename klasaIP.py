import random


# __init__, nazwe do ktorego bedziemy zapisywac wyniki, oraz IP, ktore chcemy stworzyc

#tworzyc losowe localhost
#tworzyc losowe non local
#f. ktora zapisuje rezultaty na dysk(


#4
#pobiera linia po linii plik
# @staticmethod
#     def pole_prostokat2(dowolna_nawaz):
#         return x*y

#5 fukcja ktora sprawdzi, czy wczytany plik zaczyna jest od numeru IP, jesli to
# to mam dostac info "plik nie zaczyna sie od IP", assert

#funkcja, ktora wyciaga parametry typu data, ip, post czy get,
# def fun6(dane, regex)

#star wersja #############
#
#
#
# import random
#
# class IP:
#     def __init__(self,plik, ):
#         self.ipset = []
#         self.plik = plik
#
#     def genprv(self):
#         templist = []
#         templist.append('10.' + str(random.randint(0,255)) + '.' + str(random.randint(0,255)) + '.' + str(random.randint(0,255)))
#         templist.append('172.' + str(random.randint(16,33)) + '.' + str(random.randint(0,255)) + '.' + str(random.randint(0,255)))
#         templist.append('192.168.' + str(random.randint(0,255)) + '.' + str(random.randint(0,255)))
#         return templist[random.randint(0,2)]
#
#     def genpub(self):
#         ip = ''
#         for i in range(4):
#             if i == 0:
#                 oct = '10'
#                 while (oct == '10') or (oct == '172') or (oct == '192') or (oct > '223'):
#                     oct = str(random.randint(1,255))
#                 ip = ip + oct
#             else:
#                 ip = ip + str(random.randint(0,255))
#             if i != 3:
#                 ip = ip + '.'
#         return ip
#
#     def genprvs(self,ile):
#         self.ipset = []
#         for i in range(ile):
#             self.ipset.append(self.genprv())
#         return self.ipset
#
#     def genpubs(self,ile):
#         self.ipset = []
#         for i in range(ile):
#             self.ipset.append(self.genpub())
#         return self.ipset
#
#     def zapisz(self):
#         plik = open(self.plik,mode='w')
#         for ip in self.ipset:
#             plik.write(ip+'\n')
#         plik.close()
#
#     @staticmethod
#     def read_new_file(file_name):
#         dane = open(file_name, "r").readlines()
#         return dane
#
#
#
# adr1 = IP('adresy_prv.txt')
#
# print(adr1.genprv())
# print(adr1.genprvs(10))
# adr1.zapisz()
#
# adr2 = IP('adresy_pub.txt')
#
# print(adr2.genpub())
# print(adr2.genpubs(10))
# adr2.zapisz()
#
#
# #czytanie nowego pliku
#
# new_data = adr2.read_new_file("plik.txt")
import random

class IP:
    def __init__(self, ip_address, filename):
        '''

        :param ip_address: int, liczba ip do wygenerowania
        :param filename: str
        '''
        self.ip_address = ip_address
        self.filename = filename
        self.ipset = []


    def random_ip_nonlocal(self):
        lista_ip_non_local = []
        # self.ipset = []
        for i in range(self.ip_address):
            ip = ""
            for i in range(0, 4):
                losowa_liczba = random.randint(1, 255)
                ip += str(losowa_liczba)
                if i in range(0, 3):
                    ip += "."
            lista_ip_non_local.append(ip)
            return lista_ip_non_local


    def random_ip_local(self):
        lista_ip_local = []
        for i in range(self.ip_address):
            ip = "192.168."
            for i in range(0, 2):
                losowa_liczba = random.randint(1, 255)
                ip += str(losowa_liczba)
                if i in range(1):
                    ip += "."
            lista_ip_local.append(ip)
            return lista_ip_local


    def zapisz(self):

        l1 = self.random_ip_nonlocal()
        l2 = self.random_ip_local()
        all_lines = l1+l2
        plik = open(self.filename, mode='w')
        for ip in all_lines:

            plik.write(ip+'\n')
        plik.close()


    @staticmethod
    def read_new_file(file_name):
        dane = open(file_name, "r").readlines()
        return dane