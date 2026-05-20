# #List Collection data type 

# mylist = ["prashnat","Ashish","Komal","ankush","Ashish",77,"sandip",60.52,"Prashant"]

# # print(mylist)
# # print(type(mylist))#<List>
# # print(mylist[0]) #Prashant
# # print(mylist[1]) #Ashish
# # print(mylist[2]) #Komal
# # print(mylist[-1]) #Prashant
# # print(mylist[2:5]) #n=5,n-1=4 .. komal,ankush,ashish
# # print(mylist[:5]) #n=5,n-1=4.. prashant
# # print(mylist[1:]) #n=8, n-1=7 
# # print(mylist[1:8:2])

# # mylist[2]="Akshay"
# # print(mylist)
# # print(mylist[0]) 
# # print(mylist[1])
# # print(mylist[2])
# # print(mylist[3])
# # print(mylist[4])
# # print(mylist[5])

# # if "ankush" in mylist:
# #     print("yes ankush is available")
# # else:
# #     print("not available")
# #append the value to the right and adds it to the top 
# # mylist.append("harsh")
# # mylist.append("laxman")
# # print(mylist)

# #to add an item toa specific position 

# # mylist.insert(3,"sanket")
# # print(mylist)

# # mylist.remove("sandip")
# # print(mylist)

# #to make a clone of the list 

# newlist = mylist.copy()
# print(newlist)

# mylist = [['prashant','jha'],['85.26'],[440022,"yyy"]]
# print("example of multidimensional list: ")
# print (mylist)
# #print(mylist[row][col])
# print(mylist[0][0]) #prashant
# print(mylist[0][1]) #jha
# print(mylist[1][0])  # 85.26
# print(mylist[2][0])  #440022
# print(mylist[2][1])  #yyy

# list2 =[50,25.50,'prashant']
# del list2[2]
# #del list2
# print(list2)

# list2 =[50,25.50,'prashant']
# del list2[2]  first comment this 
# #del list2 second comment 
# print(list2)

# list2 =[50,25.50,'prashant']
# list2.clear()
# print(list2)

# name="prashant" #['p', 'r', 'a', 's', 'h', 'a', 'n', 't']
# print(name)
# myname=list(name) #typecasting
# print(myname)  # we have used list constructor 

#sorting example

# mylist=[44,22,77,0,9,88]
# mylist.sort()
# #mylist.sort(reverse=True) for decending order
# print(mylist)
# '''default sorting order for number is ascending order, default sorting order for string is alphabetical order we should know that list should conatin homogenous'''

#alising means assigninhg one variable ref to another 
#variable 
# mylist=[44,22,77,0,9,88]
# newlist = mylist
# print(id(mylist))
# print(id(newlist))

# mylist=[44,22,77,0,9,88]
# for i in mylist:
#     print(i)

# que i/p =[0,1,4,0,2,5]  o/p= [1,4,2,5,0,0]

# list1=[0,1,4,0,2,5]
# for i in list1:
#     if i==0:
#         list1.remove(i)
#         list1.append(i)
# print(list1)

# mylist=[7,3,9,2,8]
# mylist.sort()
# #mylist.sort(reverse=True) #for decending order
# print(mylist[-2])

mylist = []
N =int(input("Enter the value of N:"))
for i in range(N):
    val = int(input("Enter the value:"))
    mylist.append(val)
#print(mylist)
sum =0
for i in range(len(mylist)-1):
    if i+1 in range(len(mylist)):
        sum += abs(mylist[i]-mylist[i+1])
print(sum)

