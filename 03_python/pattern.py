# 1
# 12
# 123
# 1234
# 12345

#write a program to find this pattern

# for i in range(1,6) :
#     for j in range(1,i+1) :
#         print(j, end=" ")
        
#     print()


#1
#22
#333
#4444
#55555

# for i in range(1,6) : 
#     for j in range(1, i+1):
#         print(i, end=" ")
#     print()




#11111
#2222
#333
#44
#5

for i in range(1, 6) :
    for j in range(6, i, -1) :
        print(i, end="")
    print()