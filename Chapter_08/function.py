
#function definition
def average():
    a = int(input("Enter number one : "))
    b = int(input("Enter number two : "))
    c = int(input("Enter number three : "))
    avg = (a+b+c)/3
    print(avg)

#function call
# average()


# def greet(buddy):
#     print("Good day", buddy)
#     return "done"
# a = greet("Ashamin")
# print(a)




# default parameter

# def goodDay(name, ending="thankyou"):
#     print("good day,", name)
#     print(ending)
# goodDay("Ashamin")


#recursion


def factorial(n) : 
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n = int(input("enter number : "))
print(f"factorial of {n} = {factorial(n)}")