# age = 33
# pi= 3.14
# name = "Vaishnavi"
# result = True
# print(type(age))
# print(type(pi))
# print(type(name))
# print(type(result))
# # use to define the address 
# print(id(age))
# print(id(pi))
# print(id(name))
# print(id(result))
# #Why all fundamentals datatypes are imutable
# maths = 50
# chem  = 50 
# phy   = 50
# print(id(maths))
# print(id(chem))
# print(id(phy))
# # all address are same because it is using/giving same memory ref 

# #Simple-if

# print(2+2)
# print("2"+"2")
# a = int(input("Enter the first number:"))
# b = int(input("Enter the second number:"))
# print(a+b)

# a = int(input("Enter any single digit:"))
# if a > 0:
#     print("positive number")
# if a < 0:
#     print("Negative number")
# if a == 0:
#     print("Zero")

#if-else
# day = input(input("Enter any day:"))
# if day == "SATURDAY" or day =="saturday" or day == "SUNDAY" or day =="sunday":
#     print("Weekend")
# else:
#     print("Working day")

# per = 65
# if per >=65:
#     print("Grade A")
# elif per <=65 and per >=50:
#     print("Grade B")
# else:
#     print("Fail")

# chr = ord(input("Enter any one character :"))
# if chr >=65 and chr <=90:
#     print("upper case")
# elif chr >=97 and chr <=122:
#     print("lower case")
# elif chr >=48 and chr <=57:
#     print("digit")
# else: 
#     print("Special symbol")

#membership Operator
#in 
#not in 

# name = "help4code"
# print('p' not in name)
# print('p' in name)

#Identity Opeartor (for address compariosn) is , not is 
# math = 50
# chem = 50
# print(math is not chem)

# #FOR(intialization,condition,increment/decrement)
# for i in range(5):# i=0
#     print(i)

# for i in range(2,11,2):# i=0, where 2 is inistailization and 10 is condition then next 2 is increment 
#     print(i)

#decrement 

# for i in range(5,0,-1):# i=5
#     print(i)

#print 2 table 

for i in range (1,11):
    print(i*3,i*4)


