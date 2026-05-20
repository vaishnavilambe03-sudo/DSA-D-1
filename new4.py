# '''
# now implement stack with size limit '''

# import sys
# class Stack:
#     def __init__(self, size):
#         self.myStack = []
#         self.stackSize = size 

#     def isFull(self):
#         if len(self.myStack) == self.stackSize:
#             return True 
#         else:
#             return False

#     def push(self, value):
#         if self.isFull():
#             print("Stack is full")
#         else:
#             self.myStack.append(value)
#             print("Element Push")

#     def display(self):
#         print(self.myStack) 

#     def isEmpty(self):
#         if self.myStack == []:
#             return True 
#         else:
#             return False 
        
#     def pop(self):
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             print(self.myStack.pop())

#     def peek(self):
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             print(self.myStack[-1])

#     def delete(self):
#         self.myStack = None

# size = int(input("Enter the size of the stack : "))
# obj = Stack(size)
# print("Stack has created : ")
# while True:
#     print("1. Push Operation")
#     print("2. Display Stack")
#     print("3. Pop Operation")
#     print("4. Peek Operation")
#     print("5.Delete Operation")
#     print("7. Exit ")
  
#     choice = int (input("Enter your choice : "))
#     if choice == 1:
#         value = int(input("Enter value to push in stack : "))
#         obj.push(value)
#     elif choice == 2:
#         obj.display()
#     elif choice == 3:
#         obj.pop()
#     elif choice == 4:
#         obj.peek()
#     elif choice == 5:
#         obj.delete()
#     else:
#         sys.exit()

# Another Method
mylist = [5,7,8,3,7,8,9,2,3,3]
newdict = {}
for i in range(len(mylist)):
    count = 0
    key = mylist[i]
    j = 1
    while j < len(mylist):
        if key == mylist[j]:
            count += 1
        j += 1
    if count > 1:
        newdict[key] = count
max = newdict
print(max)