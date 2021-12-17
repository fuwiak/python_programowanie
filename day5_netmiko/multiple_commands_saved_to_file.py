from pprint import pprint
import yaml
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)


def send_show_command(device, commands):
    result = {}
    try:
        with ConnectHandler(**device) as ssh:
            # ssh.enable()
            for command in commands:
                output = ssh.send_command(command)
                result[command] = output
        return result
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)

lista_ouput = []


linux_router = {
    'device_type': 'linux',
    'host': '192.168.43.197',
    'username': 'pawel',
    'password': 'pawel',

}
result = send_show_command(linux_router, ["ifconfig", "ip a"])
pprint(result, width=120)
lista_ouput.append(result)

#zapisac wynik z lista_output do plik txt, uzywajac funck, jako argument to nazwa do pliku do ktorej
#bedziemy zapisywac output



def save_log_to_file(file_name, lista_ouput):
    for i in range(len(lista_ouput)):
        with open(str(i)+file_name, 'w' ) as plik:
            for klucz, wartosc in lista_ouput[i].items():
                wiersz = '{}={}\n'.format(klucz,wartosc)
                plik.write(wiersz)
        print("zapisano do pliku {}".format(file_name+str(i)))


save_log_to_file('log.txt', lista_ouput)