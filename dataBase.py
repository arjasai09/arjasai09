import sqlite3

conn = sqlite3.connect("customers.db")


c = conn.cursor()


# c.execute("""CREATE TABLE customers(
#     Name TEXT,
#     Branch TEXT,
#     Roll No INTEGER
# )""")


lst = [
    ("Sai", "Automobile", 321),
    ("Vamsi", "Automobile", 337),
    ("Trinadh", "Automobile", 334)
]

c.executemany("INSERT INTO customers VALUES(?, ?, ?)", (lst))

# c.execute("DELETE FROM customers")

c.execute("SELECT * FROM customers")

print(c.fetchmany(3))

conn.commit()

conn.close()