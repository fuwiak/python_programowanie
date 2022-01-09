
imie = "Adam"
nazwisko="Malysz"

IP = "192.168.0.1"

# liczba_kropek = IP.count(".")
# print("liczba cyfr w IP", len(IP))

#!=



#napisca program, ktory weryfikuje czy podane IP ma prawidlowa liczbe cyfr
#jesli ma wiecej nizn 12 lub mniej niz 4, to ma ma wyrzucic komunikat w stylu "podales bledne IP"

IP = "192.168.0.1"
liczby_w_ip = len(IP)
liczba_kropek = IP.count(".")
wynik_dzialania = liczby_w_ip - liczba_kropek
if wynik_dzialania < 4 or wynik_dzialania > 13:
    print("zly ip")
else:
    print("poprawny IP")

ip1=int(input("Podaj adres IP oktetami1 : ",))
ip2=int(input(" . ",))
ip3=int(input(" . ",))
ip4=int(input(" . ",))

# print(ip1,".",ip2,".",ip3,".",ip4)
# if ip1 <= 1 or ip1 > 256:
#     print("NIEPRAWIDLOWY ADRES PROBLEM W OKTECCIE PEIRWSZYM")
# elif ip2 <= 1 or ip2 > 256:
#     print("NIEPRAWIDLOWY ADRES PROBLEM W OKTECIE DRUGIM")
# elif ip2 <= 1 or ip2 > 256:
#     print("NIEPRAWIDLOWY ADRES PROBLEM W OKTECIE Trzecim")
# elif ip2 <= 1 or ip2 > 256:
#     print("NIEPRAWIDLOWY ADRES PROBLEM W OKTECIE Czwartym")
# else:
#     print("Adres prawidłowy")
