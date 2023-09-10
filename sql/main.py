import sqlite3 as sq
# database = sq.connect(r'E:\qa_test.db')
# cursor = database.cursor()
# cursor.execute("""SELECT * FROM AUTO""")
# print(type(cursor.fetchall()))
db = sq.connect('qatest.db')
cu = db.cursor()
# cu.execute("""CREATE TABLE IF NOT EXISTS Students( StudentsID INTEGER PRIMARY KEY,
# First_Name TEXT NOT NULL,
# Last_Name TEXT NOT NULL);""")
# db.commit()
"""Небезопасно"""
# cu.execute("""INSERT INTO Students(First_Name,Last_Name) VALUES ("1","2")""")
# db.commit()
# cu.execute("""SELECT * FROM Students""")
# print(cu.fetchall())
"""Безопасно"""
data = ('asd', 'asd2')
cu.execute("""INSERT INTO Students(First_Name,Last_Name) VALUES (?,?);""", data)
db.commit()