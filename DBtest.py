import mysql.connector

connection = mysql.connector.connect(
                               host='192.168.1.184',
                               database='employees',
                               user='oracle',
                               password='kickstart')

cursor = connection.cursor()

mySQLQuery = ("""
              SELECT `first_name`,`last_name` FROM `employees` WHERE birth_date > 1960 
""")

print(mySQLQuery)

cursor.execute(mySQLQuery)

result = cursor.fetchall()
print(result)
for line in result:
    print(line)

