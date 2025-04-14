import psycopg2

conn = psycopg2.connect(
    dbname = "postgres",
    user = "postgres",
    password = "12345678",
    host = "localhost",
    port = "5432"
)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INT
);
""")
 
cur.execute("""
INSERT INTO students (name,age)
VALUES
('Zharas', 18),
('Asan', 19);
""")

cur.execute("SELECT * FROM students;")
rows = cur.fetchall()
for row in rows:
    print(row)

conn.commit()
cur.close()
conn.close()