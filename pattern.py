# i=1, j=1 (i,j=1,1)
# for i in range(1,4): #outer loop -> rows
#     for j in range(1,4): #inner loop -> columns
#         print(i,end =" ")
#     print()

# n=int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i),end= " ")
#     print()

# n=int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,n+i):
#         print("*",end= " ")
#     print()

# n=int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(chr(64+j),end= " ")
#     print()

import time 
n= int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        time.sleep(3)
        print("*",end=" ")
    print()