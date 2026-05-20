'''16. Reverse Each Word in a String

Question:
Write a program to reverse each word in a string.

Logic:
Split the string into words, reverse each word, and join them back together.

Sample Input:
"Hello world"

Expected Output:
"olleH dlrow"'''
# text = "Hello world"

# words = text.split()

# reversed_words = []

# for word in words:
#     reversed_words.append(word[::-1])

# result = " ".join(reversed_words)

# print(result)

#Insertion Sort 
# arr = [5,3,8,6,2]
# for i in range(1,len(arr)):
#     key = arr[i]
#     j = i-1
#     while j >=0 and arr[j]>key: 
#         arr[j+1] = arr[j]
#         j = j-1
#         arr[j+1] = key
# print(arr)

#Selection sort 

# arr = [20,12,10,15,2]
# for i in range(len(arr)):
#     min = i
#     j = i + 1

#     while j < len(arr):
#         if arr[j] < arr[min]:
#             min = j
#         j = j + 1
#     arr[i], arr[min] = arr[min], arr[i]
# print(arr)

'''30. Find All Duplicates in a List

Question:
Write a function to find all the elements that appear more than once in a list.
Logic:
Use a loop and a dictionary to count occurrences.
Sample Input: [4, 3, 2, 7, 8, 2, 1, 5, 5]
Expected Output: [2, 5]'''

# def find_duplicates(lst):
#     count = {}
#     duplicates = []

#     for item in lst:
#         if item in count:
#             count[item] += 1
#         else:
#             count[item] = 1

#     for key in count:
#         if count[key] > 1:
#             duplicates.append(key)

#     return duplicates


# data = [4, 3, 2, 7, 8, 2, 1, 5, 5]

# print(find_duplicates(data))

#'''INSTANCE VARIABLE'''

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

class New:
    a = 10
    def __init__(self):
        self.name = "prashant"
Obj1 = New()
Obj2 = New()
Obj3 = New()
New.a = 50
print(Obj1.a)
print(Obj2.a)
print(Obj3.a)
      
