import psycopg2
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
# create_table_query = '''CREATE TABLE IF NOT EXISTS mobile4
#           (ID INT PRIMARY KEY     NOT NULL,
#           MODEL           TEXT    NOT NULL,
#           PRICE         FLOAT); '''
# # # Execute a command: this creates a new table
# cursor.execute(create_table_query)
# connection.commit()
#
# print("Potwierdzenie, ze prawidlowo polaczylismy sie z baza danych", connection)
# print("Table created successfully in PostgreSQL ")

#\dt - podejrzenie jaka stworzylismy tabele
#
#
# # # Executing a SQL query to insert data into  table mobile2
# model_list = ["Xiaomi", "Iphone", "Motorola", "Nokia"]
#
#
# #insert one line

# insert_query = """ INSERT INTO mobile2 (ID, MODEL, PRICE) VALUES (1, 'Iphone12', 1100)"""
# cursor.execute(insert_query)
# connection.commit()

insert_query = """ INSERT INTO mobile2 (ID, MODEL, PRICE) VALUES (2, 'Iphone1333', 99999)"""
cursor.execute(insert_query)
connection.commit()


#select * from mobile2; --> sprawdzic w tabeli mobile2

#
#
insert many lines

# list of rows to be inserted
values = [(17, 'szajomi', 67), (18, 'szajsung', 79), (19, 'majphone', 95)]

# executing the sql statement
cursor.executemany("INSERT INTO mobile2 (ID, MODEL, PRICE) VALUES(%s,%s,%s)", values)
connection.commit()
#
#
# #by function
#
# values = [(17, 'szajomi', 67), (18, 'szajsung', 79), (19, 'majphone', 95)]
#
# bulkInsert(values, connection)
#
#
#
# #generate new_lines
#
# # for i in range(1,5):
# #     id, model, price = i, random.choice(model_list), random.randint(2000,5000)
# #     insert_query = """INSERT INTO mobile2 (ID, MODEL, PRICE) VALUES ({}, '{}', {})""".format(id, str(model), price)
# #     cursor.execute(insert_query)
# #     connection.commit()
# #     print(insert_query)
#
#
#
# #zrzuc rezultat do listy
# # cursor.execute("SELECT * from mobile2")
# # print("Result ", cursor.fetchall())
#
#
#
#
#
# #update line
#
# # update_query = """Update mobile2 set price = 1000 where id = 3"""
# # cursor.execute(update_query)
#
#
# #by function
#
# connection = psycopg2.connect(**conn_data)
# updateTable(19, 9999, connection)
#
#
# #update from list
#
#
# #deleltion by id
#
# # connection = psycopg2.connect(**conn_data)
# # deleteData(17, connection)
#
#
#
#
#
#
#
#
#
#
#
