#write a program to find of all even number upto 50

# sum = 0
# for i in range(1,51) : 
#     if i % 2 == 0 :
#         sum += i
# print(sum)



#write a program to write first 20 numbers and their squired numbers

# for i in range(1,21) :
#     print("number is : ", i, "Squire is : ", i**2)



#write a program to find sum of odd number  upto 10
# sum = 0
# n = 1
# while n <= 20 :
#     if n % 2 == 1 :
#      sum+=n
#     n+=1
# print(sum)



#write a program to check if a number is divisible by 8 and 12 upto 100

# for i in range(1,101) : 
#     if i % 8 == 0 and i % 12 == 0 :
#         print(i)


# write a billing system at supermarket

while True :
    total = 0
    while True : 
         quantity = int(input("Enter Quantity"))
         amount = int(input("Enter amount"))
         total += quantity * amount
         repeat = input("Do you want to perches more then type yes else no")
         if repeat == "no" :break
    billName = input("enter bill name : ")
    print(total)
    repeat = input("Do you want to perches more then type yes else no")
    if repeat == "no" :break

