# salary = int(input('Enter your salary :'))
# rating = int(input('Enter your performance appraisal rating :'))
# increment = 0 
# if rating >=1 and rating<=3:
#     increment = salary*10/100
# elif rating >=3.1 and rating <=4:
#     increment = salary*30/100
# elif rating >=4.1 and rating <=5:
#     increment = salary*40/100
# else:
#     print('Invalid rating')
# print('Incremented salary: ' ,increment+salary)


# basicSalary = 20000
# GrossSalary = 0

# HRA = basicSalary *(20/100)
# TA = basicSalary *(30/100)
# DA = basicSalary *(45/100)
# GrossSalary = basicSalary-(HRA+TA+DA)
# print("GrossSalary:", GrossSalary)

# '''Binary Search'''

# def binarySearch(array,target):
#     low = 0 
#     high= len(array)-1
#     while low <= high:
#         mid = (low+high)//2
#         if array[mid] == target:
#             return mid
         
#         elif array[mid] < target:
#             low = mid+1
#         else: 
#             high = mid-1
#     return -1 

# array = [2,4,5,9,11,13,14,15,19,20,22,23,27,30,32,39,42,44,45,49,51,53,54,55,59,60,62,63,67,70,72,79]
# target = 72
# result = binarySearch(array, target)
# if result == -1:
#     print("Element Not Found")
# else: 
#     print("Element found at", result)

# '''Bubble sort '''

# def bubbleSort(array):
#     for i in range(len(array)-1):
#         for j in range(len(array)-i-1):
#             if array[j] > array[j+1]:
#                 temp = array[j]
#                 array[j] = array[j+1]
#                 array[j+1] = temp
#             print(array)
#         print()

# array = [64,34,25,12,22,11,90]
# bubbleSort(array)

# '''WIPRO'''
# Input = 578378923
# output = 3 


# data = [5,7,8,3,7,8,9,2,3]

# count = 0

# for i in range(len(data)):
#     for j in range(i + 1, len(data)):
#         if data[i] == data[j]:
#             count += 1

# print(count)

# mylist=[5,7,8,3,7,8,9,2,3]
# newlist= []

# for i in range(len(mylist)):
#     count =0
#     key = mylist[i]
#     j= i+1     #j=3
#     while j<len(mylist):
#         if key == mylist[j]:
#             newlist.append(key)
#         j=j+1
# print(len(newlist))

''''DEFAULT CONSTRUCTOR 
stack implementation without size limit
 stack implementation with size limit 
There are two ways
1. List/Array
2. Linkedlist

Use of Class = 
Use of Object = 
Role of data member = means variable'''

# class Name:
#     age = 30 #data member
#     def display(self): #method 
#         print("Hello World")

# obj = Name()
# print(obj.age)
# obj.display()

# class Student:
#     def __init__(self):  #special method 
#         self.name = "prashant"
#         self.age =30 

#     def display(self):
#         print("Name=", self.name)
#         print("Age=", self.age)
        
# stuObj = Student()
# print(stuObj)

# class Message:
#     def __init__(self):
#         print("I am constructor")

#     def shows(self):
#         print("Class Program")

# obj = Message()
# obj.shows()
# obj2 = Message()
# #constructor gets call once for one object 

# '''PARAMETERIZED CONSTRUCTOR'''
# class StudentInfo:
#     def __init__(self, name, age,roll_no):
#         self.Name = name
#         self.Age = age 
#         self.roll_no = roll_no

#     def displayStudentInfo(self):
#         print("Name=", self.Name)
#         print("Age=", self.age)
       
# studentObj = StudentInfo("Prakash",34,101)
# studentObj.displayStudentInfo()

'''Stack Implementation without size limit'''

# push 
# pop
# peek
# is empty 
# is full 
# delete 
# display 

import sys
class Stack:
    def __init__(self):
        self.mystack = []

    def push(self, value):
        self.mystack.append(value)
        print("Element push")

    def display(self):
        print(self.mystack)

    def isEmpty(self):
        if self.mystack == []:
            return True
        else:
            return False
        
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print(self.mystack.pop())  # removes permanently

            #peek: removes the topmost element 
    
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print(self.mystack[-1])

obj = Stack()
print("Stack has created :")

while True:
    
    print("1. Push Operations :")
    print("2. Display Stack :")
    print("3. Pop operation :")
    print("4. Peek operation :")
    print("7. Exit")
    choice = int(input("Enter your choice :"))
    if choice ==1:
        value = int(input("Enter your value to push in stack: "))
        obj.push(value)
    elif choice == 2:
        obj.display()
    elif choice == 3:
        obj.pop()
    elif choice == 4:
        obj.peek()
    else:
        sys.exit()