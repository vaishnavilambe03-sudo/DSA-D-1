# def first_non_repeating_char(s):
#     for ch in s:
#         count = 0

#         for c in s:
#             if ch == c:
#                 count += 1

#         if count == 1:
#             return ch

#     return None


# text = "leetcode"

# print(first_non_repeating_char(text))

#Recursion 
#when we have to go for recursion ?  (uses stack memory)
#Factorial sol 

# def factorial(num):
#     if num <=1:
#         return 1
#     return num* factorial(num -1)

# print(factorial(4))

#Capitalizefirst sol using recursion

# def capitalizeFirst(arr):

#     result = []
#     if len(arr) == 0:
#         return result
#     result.append(arr[0][0].upper() + arr[0][1:])
#     return result + capitalizeFirst(arr[1:])

# print(capitalizeFirst(['car','banana','taco']))

# def power(base, exponent):
#     if exponent == 0:
#         return 1
#     return base * power(base,exponent-1)

# print(power(2,0))
# print(power(2,2))
# print(power(2,4))

# def productofArray(arr):
#     if len(arr) == 0:
#         return 1 
#     return arr[0] * productofArray(arr[1:])

# print(productofArray([4,2,3]))
# print(productofArray([8,2,3,10]))

# def reverse(strng):
#     if len(strng) <=1:
#         return strng
#     return strng[len(strng)-1] + reverse(strng[0: len(strng)-1])

# print(reverse('python'))
# print(reverse('vaishnavi'))

# def recursiveRange(num):
#     if num <= 0:
#         return 0
#     return num + recursiveRange(num -1)

# print(recursiveRange(6))

# def isPalindrome(strng):
#     if len(strng) == 0:
#         return True
#     if strng[0] != strng[len(strng) - 1]:
#         return False
#     return isPalindrome(strng[1 : -1])

# print(isPalindrome('awesome'))
# print(isPalindrome('racecar'))

def someRecursive(arr, cb):
    if len(arr) == 0:
        return False

    if not(cb(arr[0])):
        return someRecursive(arr[1:], cb)

    return True


def isOdd(num):
    if num % 2 == 0:
        return False
    else:
        return True


print(someRecursive([1,2,3,4], isOdd))   # true
print(someRecursive([4,6,8,9], isOdd))   # true
print(someRecursive([4,6,8], isOdd))     # false