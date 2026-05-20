# arr = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1]

# count = 0
# maximum = 0

# for i in arr:
#     if i == 1:
#         count = count + 1
        
#         if count > maximum:
#             maximum = count
#     else:
#         count = 0

# print("Maximum consecutive 1s:", maximum)

# #Que count substring in a string  "abababab"

# s= "abababab"
# sub= "ab"


#While loop

# i = 1
# while i<=5:
#     print(i)
#     i +=1

# #Function 

# def hello():
#     print("hello world")

# hello () #calling function 
# hello()

# def arithmatic():
#     a = int(input("Enter value of a:"))
#     b = int(input("Enter value of b:"))
#     sum = a+b
#     sub = a-b
#     div = a/b
#     mul = a*b
#     return sum,sub,div,mul

# #print(arithmatic())

# result = arithmatic()
# print("Arithmatic =",result)   #return multiple values 

#Que 
'''how many types of argumrnt we pass in function?
positional,keyword,default,variable length '''

# def arithmatic(a,b):
   
#     sum = a+b
#     sub = a-b
#     div = a/b
#     mul = a*b
#     return sum,sub,div,mul

# result = arithmatic(5,5) #positional argument 
# print("Arithmatic =",result)

#keyword argument 
# def crdential (username,password):
#     if username == password:
#         print("Login Successfully")
#     else:
#         print("invalid credentials")

# crdential(username = "admin", password="admin")#calling function 

#default arg 
# def cityName(city = "Pune"):
#     print(city)

# cityName("Nagpur")
# cityName("Mumbai")
# cityName()

#variable length 

# def cityName(*name):
#     print(name)

# cityName("Nagpur","delhi","Mumbai","pune")

#modularity approach in function 
# import sys
# def add():
#     a= int(input("Enter value of A:"))
#     b= int(input("Enter value of B"))
#     print(a+b)

# def sub():
#     a= int(input("Enter value of A:"))
#     b= int(input("Enter value of B"))
#     print(a-b)    

# def  mul():
#     a= int(input("Enter value of A:"))
#     b= int(input("Enter value of B"))
#     print(a*b)    

# def div():
#     a= int(input("Enter value of A: "))
#     b= int(input("Enter value of B: "))
#     print(a/b) 

# while True:
#     print("1.Addition")
#     print("2.Sub")
#     print("3.mul")
#     print("4.div")
#     print("5.Exit")
#     choice = int(input("Enter your choice"))
#     if choice ==1:
#         add()
#     elif choice ==2:
#         sub()
#     elif choice ==3:
#         mul()
#     elif choice ==4:
#         div()
#     elif choice ==5:
#         sys.exit()
    
# Que: Row wise max value 
# [100,198, 333, 323]
# [122,232, 333, 323]
# [223,565,245,764]

# oP:[[100,190,333,323],
#     [122,232,221,111],
#     [223,565,245,764]].


# mylist=[[100,190,333,323],
#          [122,232,221,111],
#         [223,565,245,764]]
# newlist=[]
# for i in range(3):
#     j=0
#     max = mylist[i][j] 
#     for j in range(4):
#         c_max = mylist[i][j]
#         if max < c_max:
#             max = c_max
#     newlist.append(max)
# print(newlist)

#input = prashant*is*a*good*programmer
#output = ***prashantisagoodprogrammer

# name = 'prashant*is*a*good*programmer'
# newname = ''
# val = ''
# for i in name:
#     if i !='*':
#         newname += i
#     else:
#         val +=i
# print(newname)
# print(str(val+newname))

# #aaabbbbccceeeee = output 
# a3b4c3e5 = output


name = "aaabbbbccceeeee"
newname = {}
for i in range (len(name)):
    key = name[i]
    count = 0
    for j in range (len(name)):
        if key == name[j]:
            count +=1
    newname[key] = count
#print(newname)
for i,j in newname.items():
    print(i,j,sep='' ,end= '')

