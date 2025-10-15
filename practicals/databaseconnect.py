import sqlite3

conn = sqlite3.connect('student.db')

cursor=conn.cursor()

cursor.execute('''
create table if not exists student(
               prn varchar(10) primary key,
               name varchar(50),
               branch varchar(100),
               age int

               )
''')

prn=input("enter prn ")
name=input("Enter the name ")
age=int(input("Enter age "))
branch = input("Enter branch name ")

cursor.execute('''insert into student(prn,name,branch,age) values (?,?,?,?)''',(prn,name,branch,age))

cursor.execute('select * from student')
rows=cursor.fetchall()
for row in rows:
    print(row)

prn2=input("enter prn to update ")

branch2=input("enter the updated branch ")


cursor.execute('update student set branch = ? where prn = ?',(branch2,prn2))

conn.commit()
conn.close()