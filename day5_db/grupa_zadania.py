import psycopg2
from psycopg2 import Error



connection = psycopg2.connect(user="postgres",
                                  password="pawel",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")


cursor = connection.cursor()
create_table_query = '''CREATE TABLE mobile2
          (ID INT PRIMARY KEY     NOT NULL,
          MODEL           TEXT    NOT NULL,
          PRICE         REAL); '''
# Execute a command: this creates a new table
cursor.execute(create_table_query)
connection.commit()
print("Table created successfully in PostgreSQL ")


# Executing a SQL query to insert data into  table
insert_query = """ INSERT INTO mobile2 (ID, MODEL, PRICE) VALUES (1, 'Iphone12', 1100)"""
cursor.execute(insert_query)
connection.commit()

cursor.close()
connection.close()