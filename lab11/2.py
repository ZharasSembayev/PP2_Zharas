import psycopg2

def add_or_update_user(name, phone):
    with psycopg2.connect(host="localhost", database="postgres", user="postgres", password="12345678") as conn:
        with conn.cursor() as cur:
            cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
            print(f"User '{name}' processed with phone '{phone}'")

add_or_update_user("Bauka", "87088889999")