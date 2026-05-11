#Q1

# name = input("Enter Your Name : ")
# print(f"Good Morning {name}")


#Q2 replace <name> and <date>
message = "Dear <name> your are selected <date>"
print(message.replace("<name>", "Ashamin").replace("<date>", "11-05-2026"))


#Q3 write a program to detect double space in a string
name  = "my name is ashamin   biswas"
print(name.find("  "))
print(name.replace("  ", " "))