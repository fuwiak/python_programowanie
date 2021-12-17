import psycopg2
#funkcja pierwsze ma przyjmowac parametry
# slownik z danymi do logowania
# select, ktorym bedziemy wyciagac dane z tabeli
# rezulat ma byc zapisany do listy


#podpowiedz
# select_query = """SELECT id, model from mobile2"""
# cursor.execute(select_query)
# dane=cursor.fetchall()

dane_do_logowania= {
    "user":"postgres",
    "password"="pawel",
host"="127.0.0.1",


}




connection = psycopg2.connect(user="postgres",
                                  password="pawel",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")




def pobierz_z_tabeli(dane_do_logowania, select_query):
    global connection
    connection = psycopg2.connect(**dane_do_logowania)
    cursor = connection.cursor()
    cursor.execute(select_query)

    dane = cursor.fetchall()
    return dane

#napisac funckje, ktora tworzy tabele, ma byc na konciu komunikat, tabela stworzona
#podpowiedz
#create table
# cursor = connection.cursor()
# create_table_query = '''CREATE TABLE mobile2
#           (ID INT PRIMARY KEY     NOT NULL,
#           MODEL           TEXT    NOT NULL,
#           PRICE         FLOAT); '''
# # Execute a command: this creates a new table
# cursor.execute(create_table_query)
# connection.commit()
# print("Table created successfully in PostgreSQL ")




def stworz_tabele(dane_do_logowania, query):












