import sqlite3
conn = sqlite3.connect("student74.db")

cursor = conn.cursor()

cursor.execute("""
        create table if not Exists student74(RollNo int, S_name text, age int)
    """)
print("Table created.")
cursor.execute("insert into student74 values(3,'nishant',20)")
cursor.execute("insert into student74 values(4,'jaimin',22)")
cursor.execute("insert into student74 values(5,'jemis',20)")
cursor.execute("insert into student74 values(6,'jainil',21)")
conn.commit()
print("Record inserted succesfully")

print("\n Student records.")
cursor.execute("select * from student74")

rows = cursor.fetchall();
for row in rows:
    print(row)
cursor.execute("""
        update student74 set age = 24 where RollNo = 3
    """)
conn.commit()
print("\n\n Data updated.")

print("\n\n updated Student records.")
cursor.execute("select * from student74")

rows = cursor.fetchall();
for row in rows:
    print(row)

cursor.execute("""
        delete from student74 where RollNo = 5
    """)
conn.commit()
print("\n\n Data deleted.")
print("\n\n deleted Student records.")
cursor.execute("select * from student74")

rows = cursor.fetchall();
for row in rows:
    print(row)

conn.close()
print("Data cnnection closed.")
