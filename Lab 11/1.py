import psycopg2
import csv
from tabulate import tabulate

# Подключение к БД
try:
    conn = psycopg2.connect(
        host="localhost",
        dbname="phonebook",
        user="postgres",
        password="Kbtu6720!",
        port=5432
    )
    cur = conn.cursor()
    print("[+] Connection to database successful.")
except Exception as e:
    print(f"[!] Error connecting to database: {e}")
    exit()

# Создание таблицы
try:
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            user_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            phone VARCHAR(255) NOT NULL,
            surname VARCHAR(255) NOT NULL
        )
    """)
    conn.commit()
    print("[+] Table created (if not exists).")
except Exception as e:
    print(f"[!] Error creating table: {e}")
    conn.close()
    exit()

def insert_data():
    print('Type "csv" or "con" to choose an option: upload a CSV file or input data from the console.')
    method = input().lower()
    if method == "con":
        name = input("Name: ")
        surname = input("Surname: ")
        phone = input("Phone: ")
        cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)", (name, surname, phone))
    elif method == "csv":
        filepath = input("Enter a file path with proper extension (e.g. data.csv): ")
        try:
            with open(filepath, 'r') as f:
                reader = csv.reader(f)
                next(reader)  # Пропустить заголовок
                for i, row in enumerate(reader, start=2):
                    if len(row) < 3:
                        print(f"[!] Skipping row {i}: not enough columns: {row}")
                        continue
                    name, surname, phone = row  # Меняем местами фамилию и телефон
                    cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)", (name.strip(), surname.strip(), phone.strip()))
            print("[+] Data inserted successfully from CSV.")
        except FileNotFoundError:
            print("[!] File not found. Please check the path.")
    conn.commit()

def update_data():
    column = input("Which column to update (name, surname, phone): ").strip()
    value = input(f"Enter the old {column} value to search: ").strip()
    new_value = input(f"Enter the new value for {column}: ").strip()
    if column not in ["name", "surname", "phone"]:
        print("[!] Invalid column name.")
        return
    try:
        cur.execute(f"UPDATE phonebook SET {column} = %s WHERE {column} = %s", (new_value, value))
        conn.commit()
        print("[+] Updated successfully.")
    except Exception as e:
        print(f"[!] Error updating data: {e}")

def delete_data():
    choice = input("Delete by (name/surname/phone): ").strip()
    value = input(f"Enter {choice}: ").strip()
    if choice not in ["name", "surname", "phone"]:
        print("[!] Invalid field.")
        return
    try:
        cur.execute(f"DELETE FROM phonebook WHERE {choice} = %s", (value,))
        conn.commit()
        print("[+] Deleted successfully.")
    except Exception as e:
        print(f"[!] Error deleting data: {e}")

def query_data():
    column = input("Search by column (name/surname/phone): ").strip().lower()
    value = input(f"Enter {column}: ").strip()
    
    if column not in ["name", "surname", "phone"]:
        print("[!] Invalid column.")
        return

    # ILIKE + wildcard %value% for partial, case-insensitive match
    try:
        cur.execute(f"SELECT * FROM phonebook WHERE {column} ILIKE %s", (f"%{value}%",))
        rows = cur.fetchall()

        if rows:
            print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))
        else:
            print("[!] No records found.")
    except Exception as e:
        print(f"[!] Error querying data: {e}")

def display_data():
    try:
        cur.execute("SELECT * FROM phonebook;")
        rows = cur.fetchall()
        print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))
    except Exception as e:
        print(f"[!] Error displaying data: {e}")

# Меню
while True:
    print("""
    === PhoneBook Commands ===
    1. Type "i" or "I" to INSERT data to the table.
    2. Type "u" or "U" to UPDATE data in the table.
    3. Type "q" or "Q" to make a specific QUERY in the table.
    4. Type "d" or "D" to DELETE data from the table.
    5. Type "s" or "S" to SHOW all values in the table.
    6. Type "f" or "F" to FINISH and close the program.
    """)
    command = input("Enter command: ").lower()

    if command == "i":
        insert_data()
    elif command == "u":
        update_data()
    elif command == "d":
        delete_data()
    elif command == "q":
        query_data()
    elif command == "s":
        display_data()
    elif command == "f":
        break
    else:
        print("[!] Unknown command.")

# Завершение
cur.close()
conn.close()
print("Goodbye!")
