import sqlite3

conn = sqlite3.connect('example.db')
print("successfully connected")

conn.execute("INSERT INTO Employee VALUES(1,'Mark','Mugo',45,120000.00,'Manager')")
conn.execute("INSERT INTO Employee VALUES(2,'Martha','Mercy',32,14030.00,'Admin')")
conn.execute("INSERT INTO Employee VALUES(3,'Marbel','Njoroge',67,130000.00,'HR')")
conn.execute("INSERT INTO Employee VALUES(4,'Mike','Miugo',98,113477.00,'Receptionist')")
conn.execute("INSERT INTO Employee VALUES(5,'Maurice','Ruto',38,170000.00,'Marketer')")
conn.execute("INSERT INTO Employee VALUES(6,'Miriam','Arwa',92,300000.00,'Consultant')")

conn.commit()
print("Successfully inserted values into employee table")