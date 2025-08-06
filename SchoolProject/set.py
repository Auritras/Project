#start
import mysql.connector as sqlconn

myconn = sqlconn.connect(
    host="localhost",
    user="root",
    password="*GodUssoopp123",
    database="Project"
)
if myconn.is_connected():
    print("Connection succesful")
else:
    print("Connection not succesful")

cursor=myconn.cursor()
cursor.execute("select * from f1_day1")
data=cursor.fetchall()
count=cursor.rowcount
print("total no. of rows:",count)
for row in data:
    print(row)

#end
