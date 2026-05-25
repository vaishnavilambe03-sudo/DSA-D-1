# class Node:
#     def __init__(self, value = None):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def __iter__(self):
#         curNode = self.head
#         while curNode:
#             yield curNode
#             curNode = curNode.next 

# class Stack:
#     def __init__(self):
#         self.Linkedlist = LinkedList()

#     def __str__(self):
#         values = [str(x.value) for x in self.Linkedlist]
#         return '\n'.join(values)

#     def isEmpty(self):
#         if self.Linkedlist.head == None:
#             return True
#         else:
#             return False
#     def pop(self):
#         if self.isEmpty():
#           return "There is npo element in the stack"
    
#         else: 
#          nodeValue = self.Linkedlist.head.value
#          self.Linkedlist.head = self.Linkedlist.head.next
#          return nodeValue
        
#     def push(self,value):
#         node = Node(value)
#         node.next = self.Linkedlist.head
#         self.Linkedlist.head = node

#     def peek(self):
#         if self.isEmpty():
#             return "There is not any element in the stack"
#         else:
#             nodeValue = self.Linkedlist.head.value
#             return nodeValue
#     def delete(self):
#         self.LinkedList.head = None    

# customStack = Stack()
# customStack.push(1)
# customStack.push(2)
# customStack.push(3)
# print(customStack)
# print("Display Top value")
# print(customStack.peek())
# print("Pop Top Element")
# print(customStack.pop())
# print("Now check the stack again")
# print(customStack)
# print("Pop Top Element")
# print(customStack.pop())
# print("Now check the stack again")
# print(customStack)

class Node:
    def __init__(self, value=None):
        self.value = value 
        self.next = None
    
    def __str__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self):
       self.head = None
       self.tail = None

    def __iter__(self):
         curNode = self.head
         while curNode:
             yield curNode
             curNode = curNode.next 

class Queue:
     def __init__(self):
         self.LinkedList = LinkedList()

     def __str__(self):
         values = [str(x.value) for x in self.LinkedList]
         return ' '.join(values)
     
     def enqueue(self,value):
        newNode = Node(value)
        if self.LinkedList.head == None:
            self.LinkedList.head = newNode
        else:
            self.LinkedList.tail.next = newNode
            self.LinkedList.tail = newNode

     def isEmpty(self):
        if self.LinkedList.head == None:
             return True
        else:
             return False
        

     def dequeue(self):
        if self.isEmpty():
            return "There is not any node in the Queue"
        else:
            tempNode = self.LinkedList.head

            if self.LinkedList.head == self.LinkedList.tail:
                self.LinkedList.head = None
                self.LinkedList.tail = None

            else:
                self.LinkedList.head = self.LinkedList.head.next

            return tempNode
        
     def peek(self):
         if self.isEmpty():
             return "There is not any element in the stack"
         else:
             return self.LinkedList.head
         
     def delete(self):
        self.LinkedList.head= None
        self.LinkedList.tail= None
         
custQueue = Queue()
custQueue.enqueue(3)
print(custQueue)
print("Display top value :")
print(custQueue.peek())
print("Delete FIFO")
print(custQueue.dequeue())
print("display Queue again")
print(custQueue)
print("Delete FIFO")
print(custQueue.dequeue())
print("display Queue again")
print(custQueue)