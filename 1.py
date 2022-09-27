result=1
for i in range(101):
    if(i%2!=0):
        print(i)
    if(i<50 and i%2!=0):
        result*=i
print(result)