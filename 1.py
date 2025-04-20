import psycopg2

conn = psycopg2.connect(
    dbname = "postgres",
    user = "postgres",
    password = "12345678",
    host = "localhost",
    port = "5432"
)

conn.autocommit = True
cur = conn.cursor()

#Here We will create table:
cur.execute("CREATE DATABASE Sembayev")
print("Database 'Sembayev' created succesfully!") 

cur.close()
conn.close()


