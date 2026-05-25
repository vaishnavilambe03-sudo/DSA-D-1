# import re   # re module for performing all the regular expression based operation

# count = 0   # to count the number of matching found

# pattern = re.compile("function")   # string converts into bytecode

# # print(pattern)

# matcher = pattern.finditer(
#     "A function in python is defined by a def statement. python The general syntax looks like this: def function-name(Parameter list): statements, i.e. the function body. The parameter python list consists of none or more parameters."
# )

# # print(matcher)

# for i in matcher:
#     count += 1
#     print(i.start(), "...", i.end(), "...", i.group())

# print("The number of occurrences: ", count)

# import re

# count = 0

# matcher = re.finditer("Hi", "HiHiHiHi")

# # print(matcher)

# for i in matcher:   # loop 4 times execute HiHiHiHi
#     count += 1
#     print(i.start(), "...", i.end(), "...", i.group())

# print("The number of occurrences: ", count)

# 

# import re

# a = input("enter string to perform match operation:")

# mtch = re.match(a, "python is very important language")

# print(mtch)

# if mtch != None:
#     print("match found at begining level")
#     print(mtch.start(), " ", mtch.end())

# else:
#     print("there is no matching at begining level")

# import re
# a= input("enter string to perform match operation:")
# match = re.fullmatch(a,"pythonisveryimportantlanguage")
# print(match)                #if it doesnt match the full sting then its get none
# if match != None:
#     print('match found ')
#     print(match.start()," ",match.end())
# else:
#     print("there is no matching ")

# import re
# s = input("Enter mail id : ")
# m = re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com", s)
# if m != None:
#     print("Vaild mail id")
# else:
#     print("Invalid mail id")

# search() function

# import re

# a = input("enter string to perform match operation : ")

# mtch = re.search(a, "python sss dynamic lannn")

# print(mtch)

# if mtch != None:
#     print(mtch.start(), " ", mtch.end(), " ", mtch.group())

# else:
#     print("there is no matching anywhere")

# sub() function   3245 XXXX XXXX XXXX 

# import re
# a= input("Enter a word to perform search operation : ")
# f1 = open("para.txt", "r")
# data = f1.read()
# mtch = re.search(a, data)
# print(mtch)
# if mtch != None:
#     print(mtch.start(), " ", mtch.end(), " ", mtch.group())
# else:
#     print("There is no matching anywhere")

#Program to print the number of lines, words and characters present in the

#given file?


#Program to print the number of lines, words and characters present in the

#given file?

import os, sys

fname=input("Enter File Name: ")

if os.path.isfile(fname):

    print("File exists:", fname)

    f=open(fname, "r")

else:

    print("File does not exist:", fname)

    sys.exit(0)

lcount=wcount=ccount=0

for line in f:

    lcount=lcount+1

    ccount=ccount+len(line)

    words=line.split()

    wcount=wcount+len(words)

print("The number of Lines:", lcount)

print("The number of Words:", wcount)

print("The number of Characters:", ccount)