# create user jan with encrypted password 'jan';

# create database test22;

# \l   ---> sprawdzanie listy dostepnych baz danych

# \du+ ---> lista dostepnych uzytkownikow

# grant all privileges on database test22 to jan;

import psycopg2

conn_data = {
    'user': 'jan',
    'host': '127.0.0.1',
    'port':"5432",
    'database': 'test22',
    'password': 'pawel123',
}

connection = psycopg2.connect(**conn_data)
