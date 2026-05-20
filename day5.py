'''input = 8
[79, 77, 54,81,48,34,25,16]
output = 3'''

# import math

# n = 8
# arr = [79, 77, 54, 81, 48, 34, 25, 16]

# stack = []
# count = 0

# # push elements into stack
# for i in arr:
#     stack.append(i)

# # pop elements and check perfect square
# while stack:
#     num = stack.pop()

#     if math.isqrt(num) * math.isqrt(num) == num:
#         count += 1

# print(count)

# def func(value, values):
#     var = 1
#     values[0] = 44
# t = 3
# v = [1,2,3]
# func(t,v)
# print(t,v[0])

# def f(i, values = []):
#     values.append(i)
#     print(values)
#     #return values
# f(1) #calling function
# f(2)
# f(3)


'''QUEUE 
'''

# import sys
# class Queue:
#     def __init__(self,size):
#         self.myQueue = [] #creating stack /* FIFO */
#         self.queueSize = size

#     def isFull(self):
#         if len(self.myQueue) == size:
#             return True
#         else:
#             return False
        
#     def enqueue(self, value):
#         if self.isFull():
#             print("Queue is Full. ")
#         else:
#             self.myQueue.append(value)

#     def display(self,value):
#         print(self.myQueue) 

#     def isEmpty(self):
#         if self.myQueue == []:
#             return True 
#         else:
#             return False
        
#     def deQueue(self):
#         if self.isEmpty():
#            print("Queue is empty")
#         else:
#             self.myQueue.pop(0)

#     def peek(self):
#          if self.isEmpty():
#              print("Queue is empty")
#          else:
#              print(self.myQueue[0])

#     def delete(self):


#         self.myQueue = None


# size = int(input("Enter the size of the queue : "))
# obj = Queue(size)
# print("Stack has created :")

# while True:   #range is not fixed and to run access loop  multiple times
#     print("1. Enque Operation :")
#     print("2. Display Queue :")
#     print("3. deQueue Operation :")
#     print("4. Peek Operation :")
#     print("5. Delete Queue :")
#     print("6. Exit :")

#     choice = int(input("Enter the valid number : "))

#     if choice == 1:
#         value=int(input("Enter element to add in queue : "))
#         obj.enqueue(value)
#     elif choice ==2:
#         obj.display(value)
#     elif choice ==3:
#         obj.deQueue()
#     elif choice == 4:
#          obj.peek()
#     elif choice == 5:
#         obj.delete()
#     else:
#          sys.exit()

# fruit = {}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
# addone('Apple')
# addone('Banana')
# addone('apple')
# print(len(fruit)) 

# #Write a program to accept students name and marks from the keyboard and create a dictionary. 
# # Also display student marks by taking student name.

# n =int(input("Enter the number of student :"))
# d = {}
# for i in range(n):
#     name = input("Enter Student Name:")
#     marks = input("Enter Student Marks:")
#     d[name] = marks
# while True:
#     name = input("Enter Student Name to get Marks :")
#     marks = d.get(name,-1)
#     if marks ==-1:
#         print("Student Not Found")
#     else:
#         print("The arks of" ,name,"are",marks)
#     option=input("Do you want to find another student marks[Yes|No]")
#     if option == "No":
#         break
#     print("Thanks for using our application ")

#write a program to access each vharacter of string  in forward and backward direction by 
# using while loop 

s = "Learning Python is very easy"
n = len(s)
i = 0 
print("Forward direction ")
while i < n:
    print(s[i],end= ' ')
    i +=1
print("Backward Direction")
i = -1
while i >= -n:
    print(s[i],end = ' ')
    i = i-1


# stringSent = "abcdfgerj"
# stringRec = "abcdfger"


# for ch in stringSent:
#     if stringSent.count(ch) != stringRec.count(ch):
#         print("Missing character is:", ch)
#         break

# v = ['a','e','i','o','u']
# w = input("Enter the word where we will search the vowels:")
# found = []
# for i in w:
#     if i in v:
#         if i not in found:
#             found.append(i)
# print('Found vowels =', found)
# print('Unique vowels',len(found), 'from the given word =',w)

# x,y,z = map(int,input().split())
# mylist = []
# for i in range (x):
#     a = int(input())
#     mylist.append(a)

# for j in mylist:
#     if j >= y and j<=z:
#         print(j,end= '')

# import datetime 

# #daretime formatting 
# date = datetime.datetime.now()
# print("It's now: {:%d%m%y %H:%M:%S}".format(date))

# x= ['A','B','C']
# y= ['A', 'B', 'C']
# z= [1,2,3,4]
# print(x==y)
# print(x==z)
# print(x != z)

# s = [1,4,9,16,25,36,49,64,81,100]
# val = [2**i for i in range(1,6)] #left calculation , loop on right 
# print(val)

# #Dictionary Comprehension:

# squares  = {x: x*x for x in range(1,6)}
# print(squares)

# doubles = {x: 2*x for x in range(1,6)}
# print(doubles)

# a,b = [int(x) for x in input("Enter 2 numbers :").split()]
# print("Product is :", a*b)

# a,b,c = [float(x) for x in input("Enter 3 float numbers :").split()]
# print("Sum is :", a+b+c)

#using else block 

# mycart = [10,20,800,60,70]
# for item in mycart:
#     if item > 400:
#         print("This is noty in my budget")
#         continue 
#     print(item)
# else:
#     print("you have purchased everything")

username = "admin"
password = "admin"



