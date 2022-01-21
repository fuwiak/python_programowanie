mport psycopg2
import random

from my_functions import bulkInsert, deleteData, updateTable

from psycopg2 import Error

# create user janusz with encrypted password 'janusz';
# grant all privileges on database sample_db to user_name;

#\du+

# \create database test3;


#Polacz sie z baza danych
# conn_data = {
#     'user': 'postgres',
#     'host': '127.0.0.1',
#     'port':"5432",
#     'database': 'postgres',
#     'password': 'pawel123',
# }


conn_data = {
    'user': 'jan',
    'host': '127.0.0.1',
    'port':"5432",
    'database': 'test22',
    'password': 'jan',
}


connection = psycopg2.connect(**conn_data)

#
#create table(C)
cursor = connection.cursor()
create_table_query = '''CREATE TABLE IF NOT EXISTS mobile3
          (ID INT PRIMARY KEY     NOT NULL,
          MODEL           TEXT    NOT NULL,
          PRICE         FLOAT); '''
# # Execute a command: this creates a new table
cursor.execute(create_table_query)
connection.commit()

print("Potwierdzenie, ze prawidlowo polaczylismy sie z baza danych")
print("Table created successfully in PostgreSQL ")
