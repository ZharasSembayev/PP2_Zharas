import psycopg2

conn = psycopg2.connect(
    dbname='snake',
    user='postgres',
    password='12345678',
    host='localhost',
    port='5432'
)
cur = conn.cursor()

# Таблица пользователей
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL
    )
""")

# Таблица очков
cur.execute("""
    CREATE TABLE IF NOT EXISTS user_score (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        score INTEGER,
        level INTEGER,
        saved_at TIMESTAMP
    )
""")

conn.commit()
cur.close()
conn.close()

print("✅ Таблицы успешно созданы в базе Snake.")