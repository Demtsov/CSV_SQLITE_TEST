import sqlite3
import csv

conn = sqlite3.connect("users.db")
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        email TEXT
    )
''')


with open('users.csv', 'r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        cursor.execute('''
            INSERT INTO users (username, email)
            VALUES (?, ?)
        ''', (row['username'], row['email']))


conn.commit()


cursor.execute("SELECT * FROM users")
print("Все пользователи:")
print(cursor.fetchall())

cursor.execute("SELECT * FROM users WHERE username LIKE 'user%'")
print("\nПользователи с именем, начинающимся на 'user':")
print(cursor.fetchall())

conn.close()
