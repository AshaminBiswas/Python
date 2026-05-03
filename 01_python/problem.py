

# number = int(input("Enter your number here : "))
# if a number is positive or not
# if number > 0 : print("this is a positive number")
# else : print("number is negative")


#even and odd number
# if number % 2 == 0 : print ("this is a even number")
# else : print("this is a odd number")


#Write a program to create a area calculator
# height = float(input("Enter height : "))
# width = float(input("Enter width : "))

geometry = int(input("Enter your number between 1 - 4 : "))

if  1 <= geometry <= 4 :
    if geometry == 1 : 
        print("calculating area of rectangle")
        height = float(input("Enter height : "))
        width = float(input("Enter Width : "))
        print("area of rectangle is : ", height * width)

    elif geometry == 2 :
        print("calculating area of square")
        length = float(input("Enter length : "))
        print("area of square is : ", length*length)

    elif geometry == 3 : 
        print("calculating area of triangle")
        length = float(input("Enter length : "))
        breath = float(input("Enter Breath : "))
        print("area of triangle is : ", (0.5 * (length * breath)))
    
    elif geometry == 4 :
        print("calculating area of square")
        radius = float(input("Enter length : "))
        print("area of circle is : ", (3.14 * (radius*radius)))
else:
    print("enter valid number")