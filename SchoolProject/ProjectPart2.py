#Start

import mysql.connector as sqlconn

myconn = sqlconn.connect(
    host="localhost",
    user="root",
    password="********",  
    database="uwu"
)

if myconn.is_connected():
    print("Connection successful")
else:
    print("Connection not successful")

mycursor = myconn.cursor()

def insStudent():
    try:
        i = int(input("Enter student ID: "))
        nm = input("Enter student name: ")
        st = input("Enter stream: ")
        sql = "INSERT INTO student (id, name, stream) VALUES (%s, %s, %s)"
        mycursor.execute(sql, (i, nm, st))
        myconn.commit()
        print("Student inserted successfully!")
    except Exception as e:
        print("Error inserting student:", e)

def showStudents():
    mycursor.execute("SELECT * FROM student")
    data = mycursor.fetchall()
    print("\n--- Students Table ---")
    if data:
        for row in data:
            print(row)
    else:
        print("No students found.")

def delStudent():
    try:
        d = int(input("Enter student ID to delete: "))
        sql = "DELETE FROM student WHERE id = %s"
        mycursor.execute(sql, (d,))
        myconn.commit()
        print("Student deleted successfully!")
    except Exception as e:
        print("Error deleting student:", e)

def updStudent():
    try:
        o = int(input("Enter student ID to update: "))
        print("Which field do you wish to change?")
        print("1. ID\n2. Name\n3. Stream")
        g = int(input("Enter choice: "))
        if g == 1:
            s = "id"
        elif g == 2:
            s = "name"
        elif g == 3:
            s = "stream"
        else:
            print("Invalid choice")
            return
        n = input("Enter new value: ")
        sql = f"UPDATE student SET {s} = %s WHERE id = %s"
        mycursor.execute(sql, (n, o))
        myconn.commit()
        print("Student updated successfully!")
    except Exception as e:
        print("Error updating student:", e)

def insSubject():
    try:
        sid = int(input("Enter subject ID: "))
        sname = input("Enter subject name: ")
        sql = "INSERT INTO subjects (subj_id, subj_name) VALUES (%s, %s)"
        mycursor.execute(sql, (sid, sname))
        myconn.commit()
        print("Subject inserted successfully!")
    except Exception as e:
        print("Error inserting subject:", e)

def showSubjects():
    mycursor.execute("SELECT * FROM subjects")
    data = mycursor.fetchall()
    print("\n--- Subjects Table ---")
    if data:
        for row in data:
            print(row)
    else:
        print("No subjects found.")

def insMarks():
    try:
        sid = int(input("Enter student ID: "))
        subj_id = int(input("Enter subject ID: "))
        e1 = int(input("Enter marks for Exam 1: "))
        e2 = int(input("Enter marks for Exam 2: "))
        e3 = int(input("Enter marks for Exam 3: "))
        e4 = int(input("Enter marks for Exam 4: "))
        sql = """INSERT INTO marks (student_id, subj_id, exam1, exam2, exam3, exam4)
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        mycursor.execute(sql, (sid, subj_id, e1, e2, e3, e4))
        myconn.commit()
        print("Marks inserted successfully!")
    except Exception as e:
        print("Error inserting marks:", e)

def showMarksForStudent():
    sid = int(input("Enter student ID: "))
    sql = """SELECT s.name, sub.subj_name, m.exam1, m.exam2, m.exam3, m.exam4
             FROM student s
             JOIN marks m ON s.id = m.student_id
             JOIN subjects sub ON m.subj_id = sub.subj_id
             WHERE s.id = %s"""
    mycursor.execute(sql, (sid,))
    data = mycursor.fetchall()
    if data:
        print(f"\n--- Marks for Student ID {sid} ---")
        for row in data:
            print(f"Name: {row[0]}, Subject: {row[1]}, Exams: {row[2]}, {row[3]}, {row[4]}, {row[5]}")
    else:
        print("No marks found for this student.")

def updMarks():
    try:
        sid = int(input("Enter student ID: "))
        subj_id = int(input("Enter subject ID: "))
        exam_no = int(input("Which exam do you want to update? (1–4): "))
        new_marks = int(input("Enter new marks: "))
        sql = f"UPDATE marks SET exam{exam_no} = %s WHERE student_id = %s AND subj_id = %s"
        mycursor.execute(sql, (new_marks, sid, subj_id))
        myconn.commit()
        if mycursor.rowcount > 0:
            print("Marks updated successfully!")
        else:
            print("No matching record found.")
    except Exception as e:
        print("Error updating marks:", e)

def delMarks():
    try:
        sid = int(input("Enter student ID: "))
        subj_id = int(input("Enter subject ID: "))
        sql = "DELETE FROM marks WHERE student_id = %s AND subj_id = %s"
        mycursor.execute(sql, (sid, subj_id))
        myconn.commit()
        if mycursor.rowcount > 0:
            print("Marks deleted successfully!")
        else:
            print("No matching record found.")
    except Exception as e:
        print("Error deleting marks:", e)

#Main Menu
while True:
    print("\n--- Main Menu ---")
    print("1. Insert Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. Show Students")
    print("5. Insert Subject")
    print("6. Show Subjects")
    print("7. Insert Marks")
    print("8. Show Marks for a Student")
    print("9. Update Marks")
    print("10. Delete Marks")
    print("11. Exit")

    try:
        m = int(input("Enter choice: "))
        if m == 1:
            insStudent()
        elif m == 2:
            delStudent()
        elif m == 3:
            updStudent()
        elif m == 4:
            showStudents()
        elif m == 5:
            insSubject()
        elif m == 6:
            showSubjects()
        elif m == 7:
            insMarks()
        elif m == 8:
            showMarksForStudent()
        elif m == 9:
            updMarks()
        elif m == 10:
            delMarks()
        elif m == 11:
            print("Thank you for using this app!")
            break
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")


#end
