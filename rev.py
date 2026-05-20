# num = 123 # rev 321 
# a = num % 10 #a=3
# num = num//10 # num=12
# b = num % 10 #b=2
# c = num // 10 #c = 1
# rev = a*100+b*10+c*1
# print(rev)


#123456
# num = 123456
# a= num %10
# num= num//10 
# b= num % 10
# num = num//10
# c= num %10
# num= num//10 
# d= num %10
# num= num//10
# e= num %10
# f= num= num//10
# rev = a*100000+b*10000+c*1000+d*100+e*10+f*1
# print(rev)

Amount = int(input("Please Enter Amout to withdraw :"))
print("100 notes =",Amount//100)
print("50 notes =",(Amount % 100)//50)
print("20 notes =",((Amount % 100)%50)//20)
print("10 notes =",(((Amount % 100) %50)%20)//10)
print("5 notes =",((((Amount % 100) %50)%20)%10)//5)
print("2 notes =",(((((Amount % 100) %50)%20)%10)%5)//2)
print("1 notes =",((((((Amount % 100) %50)%20)%10)%5)%2)//1)





