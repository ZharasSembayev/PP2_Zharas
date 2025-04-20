import psycopg2

#HERE WE WILL CONNECTING ON DATABASE
conn = psycopg2.connect(
    dbname = 'sembayev',
    user = 'postgres',
    password = '12345678',
    host = 'localhost',
    port = '5432'
)

conn.autocommit = True
cur = conn.cursor()

#HERE WE WILL CREATE TABLE USERS
cur.execute("""
CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL
)
"""
)

print("Created succesfully or already exists!")

cur.execute("SELECT * FROM users") 
rows = cur.fetchall() # Получаем все строки результата
for row in rows:
    print(row)
cur.close()
conn.close()