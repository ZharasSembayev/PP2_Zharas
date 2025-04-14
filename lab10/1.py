import psycopg2
import csv


DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "12345678"

def get_connection():
    """Establish a connection to the database."""
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

def create_table():
    """Creates the PhoneBook table if it does not exist."""
    conn = get_connection()
    cur = conn.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS PhoneBook (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(100),
        phone VARCHAR(15)
    );
    """
    cur.execute(create_table_query)
    conn.commit()
    cur.close()
    conn.close()
    print("PhoneBook table created or already exists.")

def insert_from_csv(csv_file_path):
    """Inserts data from a CSV file.
    CSV must have a header and two columns: first_name, phone.
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                if len(row) >= 2:
                    cur.execute("INSERT INTO PhoneBook (first_name, phone) VALUES (%s, %s)", (row[0], row[1]))
        conn.commit()
        print(f"Data from file {csv_file_path} has been successfully inserted.")
    except Exception as e:
        print("Error while loading data from CSV:", e)
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def insert_from_console():
    """Inserts data entered by the user from the console."""
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO PhoneBook (first_name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()
        print("Data successfully added.")
    except Exception as e:
        print("Error while adding data:", e)
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def update_data():
    """
    Updates data in the PhoneBook table.
    The user chooses what to update: name or phone, and provides a filter (e.g., phone or name).
    """
    print("Select what you want to update:")
    print("1. Change name by phone number")
    print("2. Change phone number by name")
    choice = input("Your choice (1 or 2): ").strip()

    conn = get_connection()
    cur = conn.cursor()
    try:
        if choice == "1":
            phone_filter = input("Enter the phone number to find the record: ").strip()
            new_name = input("Enter the new name: ").strip()
            cur.execute("UPDATE PhoneBook SET first_name = %s WHERE phone = %s", (new_name, phone_filter))
        elif choice == "2":
            name_filter = input("Enter the name to find the record: ").strip()
            new_phone = input("Enter the new phone number: ").strip()
            cur.execute("UPDATE PhoneBook SET phone = %s WHERE first_name = %s", (new_phone, name_filter))
        else:
            print("Invalid choice. Update aborted.")
            return
        conn.commit()
        print("Record updated successfully.")
    except Exception as e:
        print("Error while updating data:", e)
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def query_data():
    """
    Executes queries from the PhoneBook table with optional filters.
    Examples: all records, filter by name, filter by part of phone number.
    """
    print("Select query type:")
    print("1. Select all records")
    print("2. Filter by name")
    print("3. Filter by part of phone number")
    choice = input("Your choice (1, 2, or 3): ").strip()

    conn = get_connection()
    cur = conn.cursor()
    try:
        if choice == "1":
            cur.execute("SELECT * FROM PhoneBook")
        elif choice == "2":
            name_filter = input("Enter the name to filter by: ").strip()
            cur.execute("SELECT * FROM PhoneBook WHERE first_name = %s", (name_filter,))
        elif choice == "3":
            phone_part = input("Enter part of the phone number to filter by: ").strip()
            cur.execute("SELECT * FROM PhoneBook WHERE phone LIKE %s", (f"%{phone_part}%",))
        else:
            print("Invalid choice.")
            return

        rows = cur.fetchall()
        if rows:
            print("Query results:")
            for row in rows:
                print(row)
        else:
            print("No records found matching the criteria.")
    except Exception as e:
        print("Error while querying data:", e)
    finally:
        cur.close()
        conn.close()

def delete_data():
    """
    Deletes data from the table based on name or phone number.
    The user selects the deletion criteria.
    """
    print("Select deletion method:")
    print("1. Delete by name")
    print("2. Delete by phone number")
    choice = input("Your choice (1 or 2): ").strip()

    conn = get_connection()
    cur = conn.cursor()
    try:
        if choice == "1":
            name_filter = input("Enter the name to delete: ").strip()
            cur.execute("DELETE FROM PhoneBook WHERE first_name = %s", (name_filter,))
        elif choice == "2":
            phone_filter = input("Enter the phone number to delete: ").strip()
            cur.execute("DELETE FROM PhoneBook WHERE phone = %s", (phone_filter,))
        else:
            print("Invalid choice. Deletion aborted.")
            return

        conn.commit()
        print("Record(s) deleted successfully.")
    except Exception as e:
        print("Error while deleting data:", e)
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def show_menu():
    """Main menu for the PhoneBook application."""
    while True:
        print("\n=== PhoneBook Menu ===")
        print("1. Create PhoneBook table")
        print("2. Insert data from CSV")
        print("3. Insert data from console")
        print("4. Update data")
        print("5. Query data")
        print("6. Delete data")
        print("7. Exit")
        choice = input("Select menu option: ").strip()

        if choice == "1":
            create_table()
        elif choice == "2":
            csv_path = input("Enter the path to the CSV file: ").strip()
            insert_from_csv(csv_path)
        elif choice == "3":
            insert_from_console()
        elif choice == "4":
            update_data()
        elif choice == "5":
            query_data()
        elif choice == "6":
            delete_data()
        elif choice == "7":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    show_menu()