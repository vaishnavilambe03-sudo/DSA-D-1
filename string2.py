# name = "prashantjha"  #this is our string 
#     #012345678910
# print(name[0]) #p
# print(name[1]) #r
# print(name[-1]) #a
# #print(name[15]) string index out of range
# print(name[0:5]) #prash
# print(name[1:]) #rashantjha
# print(name[:5]) #prash
# print(name[:]) #prashantjha
# print(name[1:8:2]) #rsat   8-1=7
# print(name[::-1]) #rev of string ahjtnahsarp 

# s = "Python is High level Programming Language"
# print(s.lower()) #all lowercase
# print(s.upper()) #all uppercase
# print(s.swapcase()) #if upper then lower and vice versa 
# print(s.title()) #Upper each first word 
# print(s.capitalize()) #First place 

# name = "prashant"
# sal = 5000
# age = 28
# print("{} sal is {} age is {}".format(name,sal,age))
# print("{0} sal is {1} age is {2}". format(name,sal,age))
# print("{x} sal is {y} age is {z}".format(x=name,y=sal,z=age))
# A=1
# print(f"{A} is a good boy")

# name ="prashant"
# for i in name: 
#     print(i)

#i/p = prashant o/p= prashnt 
#WAP to remove duplicate 


# name = "prashant"
# newname =""
# for i in name: 
#     if i not in newname:
#         newname += i
# print(newname)
  
#rev this 
# name = "prashant"
# newname = ""
# N = len(name)
# for i in range(N-1,-1,-1):

#         newname += name[i]
# print(newname)
 
#pallindrome 
#sampleinput= racecar (same from both the ends)

#name = "racecar" Palindrome
# name = "Vaishnavi" # Not Palindrome
# print(name)
# print(name[::-1])
# if name ==name[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome") 

#vowels 
# vowels = ['a','e','i','o','u']
# name = "hello"
# cons = 0
# vow = 0
# for i in name:
#     if i in vowels:
#         vow +=1
#     else:
#         cons +=1
# print("consonent="cons),
# print("vowels="vow)

# name = "This is a sentence"
# count= 1
# for i in name:
#     if i == " ":
#         count += 1
# print(count)

# a=50
# b=30
# c=20
# d=10
# print((a+b)*c/d)
# print((a-b)*(c/d))
# print(a+(b*c)/d)

#count no. of special char 

# name = "gasgg54@#vscsd!s*"
# special = ['!','@',]

#Que 

# s = "This is a test"
# print(s.title())

# print('prasahantjha777'.isalnum())
# print('prasahantjha'.isalpha())
# print('777f'.isalnum())
# print('sdsdsdsdsd'.islower())
# print(''.islower())
# print('PRASHANTj'.isupper())
# print('My Name Is Prashant'.istitle())
# print(''.istitle())
# print(''.isspace())
# print("Hello".startswith("He"))
# print("Hello".endswith("lo"))

print("prashant".find("r"))
print("prashant".index("r"))
print("prashant".count("a"))