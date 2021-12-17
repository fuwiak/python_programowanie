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


#jedna linia do aktulaizacji
def wprowadz_nowy_rekord(id, nowa_wartosc, nazwa_tabeli):
    pass













