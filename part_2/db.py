import sqlite3

connection = sqlite3.connect('champions.db')

cursor = connection.cursor()

result = cursor.execute("SELECT * FROM champions;")
print(result.fetchall())