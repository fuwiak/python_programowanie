import psycopg2
import random
from psycopg2 import Error



connection = psycopg2.connect(user="postgres",
                                  password="pawel",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")

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
#
#
# # Executing a SQL query to insert data into  table
#
#
# for i in range(5):
#     id, model, price = i, "xiaomi"+str(i), 1000+20*i
#     insert_query = """ INSERT INTO mobile2 (ID, MODEL, PRICE) VALUES ({}, {}, {})""".format(id, model, price)
#     cursor.execute(insert_query)
#     connection.commit()
#
# cursor.close()
# connection.close()
#


#zadanie bojowe, uzywajac np petli, dodac do bazy mobile2 5 rzonych modeli telefonow oraz losowe ceny
#random xiami

#lukasz
# connection = psycopg2.connect(**conn_data)
cursor = connection.cursor()
# create_table_query = '''CREATE TABLE IF NOT EXISTS mobile2
#           (ID INT PRIMARY KEY     NOT NULL,
#           MODEL           TEXT    NOT NULL,
#           PRICE         REAL); '''
#
# cursor.execute(create_table_query)
# connection.commit()
# print("Table created successfully in PostgreSQL ")
#
# mobilki=["LDŻ","Szajsung","Hujej","japko","alcatel"]
#
#
# # Executing a SQL query to insert data into  table
# i = 16
# for element in mobilki:
#     insert_query = """INSERT INTO mobile2 (ID, MODEL, PRICE) VALUES (%s,%s,%s)"""
#     insert_v = (i, element, random.randint(1000,5000))
#     i += 1
#     print(insert_v)
#     cursor.execute(insert_query, insert_v)
# connection.commit()
#
#
# #dopisac do tabeli mobile2 20 modeli telefonow, w taki sposb, zeby do kazdej nazwy po 3 cyfry
# # np LG1223 xiaomo 888
#
# #podpowiedz
# #haslo = 'pawel.' + str(random.randint(0,255)) + '.' + str(random.randint(0,255))+ str(random.randint(0,255))
#
#
# #update bazy
#
#
#
#
# #zmienic ceny modeli od id=3 do id=6 i dac im cene 10000
#
# # update_query = """Update mobile2 set price = 1000 where id = 3"""
# #
# # #pod1
# # """Update mobile2 set price = 10000 where id = {}""".format(id)
# #
# #
# # cursor.execute(update_query)
#
# #pod2
# # for i in range(5):
# #     id, model, price = i, "xiaomi"+str(i), 1000+20*i
# #     insert_query = """ INSERT INTO mobile2 (ID, MODEL, PRICE) VALUES ({}, {}, {})""".format(id, model, price)
# #     cursor.execute(insert_query)
# #     connection.commit()
# #
# # cursor.close()
# # connection.close()
#
# for i in range(2,5):
#     update_query = "Update mobile2 set price = 12500 where id = {}".format(i)
#     cursor.execute(update_query)
# connection.commit()
#
#
# #zadanie z selectem
# #wyciagnac dwie koiumny z tabeli i zapisac je slownika, jesli komus do to listy
#
# # query = """select id, model from mobile2"""
# # cursor.execute(update_query)


select_query = """SELECT id, model from mobile2"""
cursor.execute(select_query)
dane=cursor.fetchall()


