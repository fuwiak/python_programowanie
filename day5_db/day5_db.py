# create user jan with encrypted password 'jan';

# create database test22;

# \l   ---> sprawdzanie listy dostepnych baz danych

# \du+ ---> lista dostepnych uzytkownikow

# grant all privileges on database test22 to jan;

import psycopg2

#dane do logowania
conn_data = {
    'user': 'jan',
    'host': '127.0.0.1',
    'port':"5432",
    'database': 'test22',
    'password': 'pawel123',
}

connection = psycopg2.connect(**conn_data)

#create table(C)
cursor = connection.cursor()
create_table_query = '''CREATE TABLE IF NOT EXISTS mobile2
          (ID INT PRIMARY KEY     NOT NULL,
          MODEL           TEXT    NOT NULL,
          PRICE         FLOAT); '''
