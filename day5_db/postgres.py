import psycopg2
from psycopg2 import Error


#Polacz sie z baza danych
conn_data = {
    'user': 'postgres',
    'host': '127.0.0.1',
    'port':"5432",
    'database': 'postgres',
    'password': 'pawel',
}
connection = psycopg2.connect(**conn_data)
