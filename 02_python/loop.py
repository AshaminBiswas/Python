# for i in range (0,5,2):print(i)
# n = 7
# for i in range (1,6) : print(n, "x", i, "=", n*i)



n=0
a = 7
# while n<=5 : 
#     print(n) 
#     n += 1


while n <= 10 :
    print(a, "x", n, "=", n*a)
    n += 1



while True :
    number1 = int(input("enter a number"))
    number2 = int(input("enter a another number"))
    print(number1 + number2)
    stop = input("do you want to stop the loop")
    if stop == "yes" : break