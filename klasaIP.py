import random


# __init__, nazwe do ktorego bedziemy zapisywac wyniki, oraz IP, ktore chcemy stworzyc

#tworzyc losowe localhost
#tworzyc losowe non local
#f. ktora zapisuje rezultaty na dysk

#podpowiedz
# class prostokat:
#
#     #wlasciwosci
#     def __init__(self, bok_a, bok_b):
#         self.bok_a = bok_a
#         self.bok_b = bok_b
#
#     #metody
#     def pole_prostokat(self):
#         return self.bok_a*self.bok_b


# class IP:
#     def __init__(self, filename, ips_to_generate):
#         self.filename = filename
#         self.ips_to_generate = ips_to_generate
#
#     def generate_ips(self):
#         for i in range(self.ips_to_generate):
#             print(i)

def kw(x):
    """

    :param x: x
    :return: x**2
    """
    return x**2


# class IP:
#     def __init__(self, ip_address, filename):
#         self.ip_address = ip_address
#         self.filename = filename
#
#
#     def random_ip_nonlocal(self):
#         lista_ip_non_local = []
#         for i in range(self.ip_address):
#             ip = ""
#             for i in range(0, 4):
#                 losowa_liczba = random.randint(1, 255)
#                 ip += str(losowa_liczba)
#                 if i in range(0, 3):
#                     ip += "."
#             lista_ip_non_local.append(ip)
#         return lista_ip_non_local
#
#     def random_ip_local(self):
#         lista_ip_local = []
#         for i in range(self.ip_address):
#             ip = "192.168."
#             for i in range(0, 2):
#                 losowa_liczba = random.randint(1, 255)
#                 ip += str(losowa_liczba)
#                 if i in range(1):
#                     ip += "."
#             lista_ip_local.append(ip)
#         return lista_ip_local


from pprint import pprint

import random

class IP:
    def __init__(self,plik):
        self.ipset = []
        self.plik = plik

    def genprv(self):
        templist = []
        templist.append('10.' + str(random.randint(0,255)) + '.' + str(random.randint(0,255)) + '.' + str(random.randint(0,255)))
        templist.append('172.' + str(random.randint(16,33)) + '.' + str(random.randint(0,255)) + '.' + str(random.randint(0,255)))
        templist.append('192.168.' + str(random.randint(0,255)) + '.' + str(random.randint(0,255)))
        return templist[random.randint(0,2)]

    def genpub(self):
        ip = ''
        for i in range(4):
            if i == 0:
                oct = '10'
                while (oct == '10') or (oct == '172') or (oct == '192') or (oct > '223'):
                    oct = str(random.randint(1,255))
                ip = ip + oct
            else:
                ip = ip + str(random.randint(0,255))
            if i != 3:
                ip = ip + '.'
        return ip

    def genprvs(self,ile):
        self.ipset = []
        for i in range(ile):
            self.ipset.append(self.genprv())
        return self.ipset

    def genpubs(self,ile):
        self.ipset = []
        for i in range(ile):
            self.ipset.append(self.genpub())
        return self.ipset

    def zapisz(self):
        plik = open(self.plik,mode='w')
        for ip in self.ipset:
            plik.write(ip+'\n')
        plik.close()

adr1 = IP('adresy_prv.txt')

print(adr1.genprv())
print(adr1.genprvs(10))
adr1.zapisz()

adr2 = IP('adresy_pub.txt')

print(adr2.genpub())
print(adr2.genpubs(10))
adr2.zapisz()