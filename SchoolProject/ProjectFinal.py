#start

import mysql.connector as sqlconn

myconn = sqlconn.connect(
    host="sql12.freesqldatabase.com",
    user="sql12793853",
    password="yE93h6nSmP",
    database="sql12793853"
)
if myconn.is_connected():
    print("Connection succesful")
else:
    print("Connection not succesful")

mycursor = myconn.cursor()


def createTab():
    try:
        sql = "CREATE TABLE marks (id int,name varchar(20),physics int,chemistry int,maths int,english int,computer int)"
        mycursor.execute(sql)
        print("Table created succesfully")
    except:
        print("Table already exists")
        

def showTab():
    mycursor.execute("SELECT * FROM marks")
    data = mycursor.fetchall()
    count = mycursor.rowcount
    for row in data:
        print(row)
    print("total no. of rows:",count)
        

def insTab():
    def newRec():
        sql = "INSERT INTO marks (id,name,physics,chemistry,maths,english,computer) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        i = int(input("Enter student id: "))
        nm = input("Enter student name: ")
        ph = int(input("Enter physics marks: "))
        ch = int(input("Enter chemistry marks: "))
        mat = int(input("Enter maths marks: "))
        eng = int(input("Enter english marks: "))
        cs = int(input("Enter computer marks: "))
        val = (i,nm,ph,ch,mat,eng,cs)
        mycursor.execute(sql,val)
        myconn.commit()
        showTab()
        b = int(input("Do you wish to input any more records? Press 1 for yes, 2 for no: "))
        if b == 1:
            newRec()
    newRec()
    

def delTab():
    def delRec():
        d = int(input("Enter id of the student whose record you wish to delete: "))
        sql = "DELETE FROM marks WHERE id = %s"
        val = (d,)
        mycursor.execute(sql,val)
        myconn.commit()
        showTab()
        b = int(input("Do you wish to delete any more records? Press 1 for yes, 2 for no: "))
        if b == 1:
            delRec()
    delRec()
    

def updTab():
    def updRec():
        o = int(input("Enter id of the student whose marks you wish to update: "))
        def updSpec():
            global s
            g = int(input("Marks of which subject do you wish to change?\nPress 1 for physics\nPress 2 for chemistry\nPress 3 for maths\nPress 4 for english\nPress 5 for computer: "))
            if g == 1:
                s = "physics"
            elif g == 2:
                s = "chemistry"
            elif g == 3:
                s = "maths"
            elif g == 4:
                s = "english"
            elif g == 5:
                s = "computer"
            else:
                print("Invalid choice")
                updSpec()
        updSpec()
        n = input("Enter updated value: ")
        sql = f"UPDATE marks SET {s} = %s WHERE id = %s"
        val = (s,n,o)
        mycursor.execute(sql,val)
        myconn.commit()
        showTab()
        b = int(input("Do you wish to update any more records? Press 1 for yes, 2 for no: "))
        if b == 1:
            updRec()
    updRec()
    

showTab()

while True:
    m = int(input("Press 1 to create table for marks\nPress 2 to insert any new records\nPress 3 to delete any existing records\nPress 4 to update any existing records\nPress 5 to access a specific record\nPress 6 to exit: "))
    if m == 1:
        createTab()
    elif m == 2:
        insTab()
    elif m == 3:
        delTab()
    elif m == 4:
        updTab()
    elif m == 5:
        accTab()
    elif m == 6:
        print("Thank you for using this app!")
        break
    else:
        print("Invalid choice")

#end

