import sqlite3
conn = sqlite3.connect("student.db")
cursor =conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Student(
    id INTEGER PRIMARY KEY,
    name TEXT,
    course TEXT,
    marks INTEGER
)
""")
conn.commit()
while True:
    print("1.Add Student")
    print("2.View Students")
    print("3.Search Student")
    print("4.Update Student")
    print("5.Delete Student")
    print("6.Exit")

    choice = int(input("Enter Choice: "))
    if choice == 1:
        id=int(input("enter the id  "))
        name=input("enter the name  ")
        course=input("enter the course  ")
        marks=int(input("enter the mark  "))
        cursor.execute(
            "INSERT INTO Student VALUES (?, ?, ?, ?)",
            (id, name, course, marks)
        )
        conn.commit()
        print("added")
    elif choice ==2:
        cursor.execute("SELECT * FROM Student")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    elif choice ==3:
        sid=int(input("enter the id "))
        cursor.execute("SELECT * FROM Student WHERE id =?", (sid,))
        student = cursor.fetchone()

        print(student)
    elif choice ==4:
        sid = int(input("Enter ID: "))
        new_marks = int(input("Enter New Marks: "))
        cursor.execute("update Student set marks =? where id=?",(new_marks,sid))

        conn.commit()
        print("updated")
    elif choice==5:
        sid = int(input("enter the id "))

        cursor.execute(
            "DELETE FROM Student WHERE id=?",
            (sid,)
        )

        conn.commit()
        print("deleted")
    elif choice==6:
        break
conn.close()