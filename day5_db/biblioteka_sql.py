import psycopg2

dane_do_logowania = {
    'user': 'postgres',
    'host': '127.0.0.1',
    'port':"5432",
    'database': 'postgres',
    'password': 'pawel',
}

select_query ="""select * from mobile2"""


connection = psycopg2.connect(**dane_do_logowania)
cursor = connection.cursor()



def pobierz_z_tabeli(select_query):
    cursor.execute(select_query)
    dane = cursor.fetchall()
    return dane

# print(pobierz_z_tabeli(dane_do_logowania, select_query))



def stworz_tabele(query):
    cursor.execute(query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")


create_table_query = '''CREATE TABLE mobile3
          (ID INT PRIMARY KEY     NOT NULL,
          MODEL           TEXT    NOT NULL,
          PRICE         FLOAT); '''

# stworz_tabele(create_table_query)


def aktualizuj_rekord(id, nazwa_kolumny, nowa_wartosc, nazwa_tabeli):
    cursor.execute("UPDATE {} SET {} = '{}' WHERE ID = {}".format(nazwa_tabeli,nazwa_kolumny,nowa_wartosc,id))
    connection.commit()
    print("Zaktualizowano wiersz nr{}".format(id))


# aktualizuj_rekord(1, 'price', 9999999, 'mobile2')


 # Executing a SQL query to delete table

def usun_rekord(id, nazwa_tabeli):
    cursor.execute("Delete from {} WHERE ID = {}".format(nazwa_tabeli,id))
    connection.commit()
    print("Usunieto wiersz nr {}".format(id))

# usun_rekord(1, 'mobile2')
# usun_rekord(5, 'mobile2')








