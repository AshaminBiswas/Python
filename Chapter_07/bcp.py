#break ==> when the given condition is meet its brake your loop or logic

for i in range(100):
    if (i == 30):
        break
    print(i)

#continue ==> when meets the condition its skip this particular iteration 
for i in range(100):
    if (i == 30):
        continue
    print(i)



#Pass ==>  when we use the pass keyword then skip the whole program and jump into the next program
for i in range(100):
    pass
i= 0
while(i<6):
    print(i)
    i+=1