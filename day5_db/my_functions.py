import psycopg2

def bulkInsert(records, connection):
    try:
        # connection = {
        #     'user': 'postgres',
        #     'host': '127.0.0.1',
        #     'port': "5432",
        #     'database': 'postgres',
        #     'password': 'pawel123',
        # }
        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO mobile2 (id, model, price) 
                           VALUES (%s,%s,%s) """

        # executemany() to insert multiple rows
        result = cursor.executemany(sql_insert_query, records)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error:
        print("Failed inserting record into mobile table {}".format(error))

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

# records_to_insert = [(4, 'LG', 800), (5, 'One Plus 6', 950)]
# bulkInsert(records_to_insert)

def deleteData(mobileId, connection):
    try:

        cursor = connection.cursor()

        # Update single record now
        sql_delete_query = """Delete from mobile2 where id = %s"""
        cursor.execute(sql_delete_query, (mobileId,))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully ")

    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

# id4 = 4
# id5 = 5
# deleteData(id4)
# deleteData(id5)

def updateTable(mobileId, price,connection):
    try:

        cursor = connection.cursor()

        print("Table Before updating record ")
        sql_select_query = """select * from mobile2 where id = %s"""
        cursor.execute(sql_select_query, (mobileId,))
        record = cursor.fetchone()
        print(record)

        # Update single record now
        sql_update_query = """Update mobile2 set price = %s where id = %s"""
        cursor.execute(sql_update_query, (price, mobileId))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")

        print("Table After updating record ")
        sql_select_query = """select * from mobile2 where id = %s"""
        cursor.execute(sql_select_query, (mobileId,))
        record = cursor.fetchone()
        print(record)

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

# id = 3
# price = 970
# updateTable(id, price)

