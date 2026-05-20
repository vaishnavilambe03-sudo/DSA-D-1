#'''INSTANCE VARIABLE'''
# 
# class New:
#     def __init__(self):
#         self.a = 10

# Obj1 = New()
# Obj2 = New()
# Obj3 = New()
# Obj1.a = 20
# print(Obj1.a)
# print(Obj2.a)
# print(Obj3.a)

# class New:
#     a = 10
#     def __init__(self):
#         self.name = "prashant"
# Obj1 = New()
# Obj2 = New()
# Obj3 = New()
# New.a = 50
# print(Obj1.a)
# print(Obj2.a)
# print(Obj3.a)
      
#for every object a seperate copy of instance variable is created but in case of static 
#variable only one copy will be created and it is accessible for every object of the class 


# class College:
#     collegename = "Modern College"   # static variable (1 memory)

#     def __init__(self):
#         self.studentname = "prashant"   # instance variable (3 separate memory)


# principal = College()    # object creation
# teacher = College()
# accountant = College()

# print("principal=", principal.collegename, ":", principal.studentname)
# print("teacher =", teacher.collegename, ":", teacher.studentname)
# print("accountant=", accountant.collegename, ":", accountant.studentname)

# College.collegename = "HBD"   # second way to add static variable

# principal.studentname = "prashant jha"

# print("principal=", principal.collegename, ":", principal.studentname)
# print("teacher =", teacher.collegename, ":", teacher.studentname)
# print("accountant=", accountant.collegename, ":", accountant.studentname)

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class Linkedlist:
#     def __init__(self):
#         self.head = None 
# linkedlist = Linkedlist()

# linkedlist.head = Node(5)
# second          = Node(10)
# third           = Node(15)
# fourth          = Node(20)

# #connecting nodes 
# linkedlist.head.next = second 
# second.next = third 
# third.next = fourth 

# #display linkedlist 
# while linkedlist.head != None:
#     print(linkedlist.head.data,"|","->",end=" ")
#     linkedlist.head = linkedlist.head.next 

#To create a dynamic node 

class Node:
    def __init__(self, data):
        self.data = data #instance variable
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self,value):
        self.node = Node(value)
        if self.head is None:
            self.head = self.node
            self.tail = self.node

        else:
            self.tail.next = self.node
            self.tail      = self.node


    def addNodeInBeg(self,value):
        print("Add node at begining")
        self.node = Node(value)
        if self.head is None:
            self.head = self.node
            self.tail = self.node
        else:
            self.node.next = self.head
            self.head = self.node

    def addNodeBetween(self, index, value):  
        node = Node(value)  
        if self.head is None:  
            self.head = node  
            self.tail = node  
        elif index ==0:  
            node.next = self.head  
            self.head = node  
        else:  
            temp = self.head  
            for _ in range(index-1):  
                temp = temp.next  
            node.next = temp.next  
            temp.next = node

    def display(self,value):
        while self.head is not None:
            print(self.head.data,"|","->",end=" ")
            self.head = self.head.next
        print()


if __name__ == '__main__': #memory is assign to main function first than other functions
    object = Linkedlist()

    while True:
        print("1. Add node Linked List :")
        print("2. Add node in Beginning :")
        print("3. Add node in Between :")
        print("4. Add node in end :")
        print("5. Display Linked List :")
        print("6. Exit :")

        ch = int(input(" Enter your choice"))
        if ch ==1:
            value = int(input(" Enter value for node"))
            object.addNode(value)
            print("Node added successfully in single linkedlist")

        elif ch == 2:
            value = int(input(" Enter value for node"))
            object.addNodeInBeg(value)
            print("Node added successfully in single linkedlist")

    
        elif ch ==3:  
            value = int(input('Enter value and add node in Between:'))  
            index = int(input('Enter position after that you have to insert:'))  
            object.addNodeBetween(index, value)  
            print('Node added successfully in Between:')  

        elif ch == 5:
            object.display(value)

        