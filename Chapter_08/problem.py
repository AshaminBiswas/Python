# find the greatest of three numbers using functions

# def greater(num1, num2, num3):
#     if(num1 > num2 and num1 > num3):
#         return f"{num1} : is greater"
#     elif(num2 > num1 and num2 > num3):
#         return f"{num2} : is greater"
#     elif(num3 > num1 and num3 > num2):
#         return f"{num3} : is greater"



# num1 = int(input("Enter your number1 : "))
# num2 = int(input("Enter your number2 : "))
# num3 = int(input("Enter your number3 : "))


# print(greater(num1, num2, num3))




# write a program to convert celsius to fortnite 

# def Fahrenheit(celsius):
#     return (celsius * 1.8) + 32

# celsius = int(input("Enter celsius : "))
# print(Fahrenheit(celsius))



# write a recursive function to calculate the sum of n natural number

# def sum(n):
#     if(n==1):
#         return 1
#     return n + sum(n - 1)

# n = int(input("Enter number : "))

# print(sum(n))


# def pattern(n):
#     if(n==0):
#         return # its code stop
#     print("*" * n) 
#     pattern ( n - 1)

# n = int(input("Enter number"))
# print(pattern(n))





# def amp(l, word):
#     li = []
#     for item in l :
#         if not(item == word):
#             li.append(item.strip(word))
#     return li

# l = ["ashamin", "sunham", "am"]
# print(amp(l, "a"))