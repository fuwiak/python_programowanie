from klasaIP import IP
# from klasaIP import kw


# p = IP(10, 'dupa.txt')
# # print(p.random_ip_nonlocal())
#
# k = kw(8)
# print(k)
#z pliku main stworzyc wygodne menu
#bedziemy sample_log.txt/ logi.txt etc

# llista_regexow = ['r1', 'r2']
# for r in listare:
#     foo(r)

#wersja beta
def analiza_logow(plik):
    adresy = IP.szukaj(plik,"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
    daty = IP.szukaj(plik,"\d{2}/[A-za-z]{3}/\d{4}:\d{2}:\d{2}:\d{2}")
    przegladarka = IP.szukaj(plik,"(?i)(chrome|mozilla|firefox)")
    wynik = list(zip(adresy,daty,przegladarka))
    return wynik

from pprint import pprint

pprint(analiza_logow('sample_log.txt'))

# #Chrome|Firefox
# cala_robota("plik1")
# cala_robota("onet.yxt")
# #wyluskac z kazdej linii, dane takie jak IP, data i przegladarka
# # i te dane wrzucic do slownika
#
# # [ [ip1, dat1, brow1], [ip2, dat2, brow2], [ip3, dat3, brow3], ....]
#
# #{IP:[123.199.111, 9999.1111.999.11], data:[], przegladarka}
