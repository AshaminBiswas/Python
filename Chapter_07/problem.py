# write a program to print the multiplication  table given number using for loop
# for i in range(1, 11) :
#     print(f"{5} x {i} = ", i * 5)

# i = 1
# while(i<11):
#     print(f"{5} x {i} = {5*i}")
#     i+=1


#greet the person whose name start with "S" 

# l = ["Ashamin", "soumen", "ushamin", "hasan"]

# for i in l: 
#     if(i.lower().startswith("s")):
#         print(f"Hello buddy : {i}")



# write a program to find a given number prime number or not
# number = int(input("Enter Your number"))

# for i in range (2, number):
#     if(number%2==0):
#         print(f"{number} : This is not a prime number")
#         break
#     else:print(f"{number} : is Prime number")


#find factorial

number = int(input("Enter Your number"))
i= 1
fact = 1
while(i<=number):
    fact*=i
    i+=1
print(fact)