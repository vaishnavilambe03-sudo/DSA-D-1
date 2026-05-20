# #find biggest number 
# def findbiggestNumber(sampleArray):
#     biggestNumber = sampleArray[0]
#     for index in range(1,len(sampleArray)):
#         if sampleArray[index]> biggestNumber:
#             biggestNumber = sampleArray[index]
#     print(biggestNumber)

# sampleArray = [5,7,9,2,3,4]
# findbiggestNumber(sampleArray)


#Linear Search 

# def linearSearch(array, target):
#     for i in range(0, len(array)):
#         if array[i]== target:
#             return
        
# array = [1,2,3,4,8,9]
# target = 7
# linearSearch(array,target)
# result = linearSearch
# if result == -1:
#     print("Target value not found ")
# else:
#      print("Target value found at index",result)

#Removing spaces from the string 
#1. rstrip = to remove spaces at right hand side 
#2. lstrip = to remove spaces at left hand side 
#3. strip = to remove spaces from both sides

city=input("Enter your city Name:")
scity=city.strip()
if scity=="Hyderabad":
    print("Hello Hyderabadi..Adab")
elif scity=="Chennai":
     print("Hello Madrasi..Vanakkam")
elif scity=="Bangalore":
     print("Hello Kannadiga..Shubhodaya")
else:
     print("Your entered City is invalid")
    