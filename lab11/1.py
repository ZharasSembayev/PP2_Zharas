import psycopg2
def search_phonebook(pattern):
    with psycopg2.connect(host="localhost", database="postgres", user="postgres", password="12345678") as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM search_phonebook(%s)", (pattern,))
            print("Search results:")
            for row in cur.fetchall():
                print(row)

search_phonebook("B")