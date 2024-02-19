// DELETE

import sqlite3
conn = sqlite3.connect("SQLITE.db")
inp_name = input("ENTER THE NAME:")
conn.execute("DELETE FROM student where st_name="+ inp_name)
conn.commit()
conn.close()

// INSERT

import sqlite3
conn = sqlite3.connect("SQLITE.db")

ins = '''
    insert into student (st_name,st_class,st_email) VALUES 
        ("rizwan","16","rizwan@gmail.com"),
        ("raghib","13","raghib@gmail.com")
'''
conn.execute(ins)
conn.commit()
conn.close()

ins = '''
    insert into FEES (st_fees) VALUES 
        (1000),
        (2000)
'''

conn.execute(ins)
conn.commit()
conn.close()

// JOIN

import sqlite3
conn = sqlite3.connect("SQLITE.db")
print("STUDENT ID","STUDENT NAME","STUDENT FEES")
data = conn.execute("SELECT * FROM student")
for a in data:
    print(a)
conn.close()

//LIMIT

import sqlite3
conn = sqlite3.connect("SQLITE.db")
data = conn.execute("SELECT * FROM student limit 0,2") # GIVES STARTING 2 RECORDS
for a in data:
    print(a)

// SEARCHING

import sqlite3
conn = sqlite3.connect("SQLITE.db")
data = conn.execute("SELECT * FROM student where st_name='raghib'")
for n in data:
    print(n)

//SELECTDATA

import sqlite3
conn = sqlite3.connect("SQLITE.db")
data = conn.execute("SELECT * FROM student")
print("st_name","st_class")
for n in data:
    print(n)
    print(n[1])

//UPDATE

import  sqlite3
conn = sqlite3.connect("SQLITE.db")
conn.execute('''
    update student set st_name='raghib',st_class='14' where st_name='raghib'
''')
conn.commit()
conn.close()

//CONNECT

# it is a light weight database

import sqlite3
conn = sqlite3.connect("SQLITE.db")

#CREATING TABLE
conn.execute('''
Create table student (
      st_id INT AUTO_INCREMENT PRIMARY KEY,
      st_name VARCHAR(50),
      st_class VARCHAR(10),
      st_email VARCHAR(30)
)
''')

conn.execute('''
create table FEES (
     st_id INT AUTO_INCREMENT PRIMARY KEY,
     st_fees VARCHAR(10)
)
''')
conn.commit()
conn.close()
