# try:
#    a= int(input("enter first number"))
#    b=int(input("enter second number"))
#    print(a/b)
# except ZeroDivisionError:
#    print("can't devide by zero")
# except ValueError:
#    print("Enter only integer value:")
# except:                                  #default block
#    print("ABC")   

# # we can take multiple except block in single except block
# #except(ZeroDivisionError, ValueError) as msg:
#    #print(msg)

# import logging

# logging.basicConfig(filename="newfile.txt", level=logging.DEBUG)

# try:
#     a = int(input("enter first integer no"))
#     b = int(input("enter second integer no"))

#     print(a / b)

# except (ZeroDivisionError, ValueError) as message:
#     print(message)
#     logging.exception(message)

# print("Logging Level is set up. Check 'newfile.txt' for log details.")

# import csv
# f = open("employee.csv",'a')           #f: File pointer  a: append
# a = csv.writer(f)
# #a.writerow(["EmpID","Emp Name","Emp Age"])

# empid = int(input("Enter you Empid:"))
# empName = (input("Enter you employee name:"))
# empAge = int(input("Enter you employee age:"))
# a.writerow([empid,empName,empAge])
# print("file has created")

import csv
f = open("student.csv", 'a')
a = csv.writer(f)
# a.writerow(["studID", "studName", "phy", "chem", "maths", "total", "percentage"])
studID = int(input("Enter the studID :"))
studName = input("Enter the studname :")
phy = int(input("Enter the phy :"))
chem = int(input("Enter the chem :"))
maths = int(input("Enter the maths :"))
total = phy+chem+maths
percent = (total/300)*100
a.writerow([studID,studName,phy,chem,maths,total,percent])
print("File has been created")