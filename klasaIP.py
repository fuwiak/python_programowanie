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
class IP:
    def __init__(self, ip_address, filename):
        self.ip_address = ip_address
        self.filename = filename


    def random_ip_nonlocal(self):
        lista_ip_non_local = []
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


from pprint import pprint