s=input()
count=1
max=0
for i in range(len(s)-1):
    if(s[i+1]==s[i]): 
        count+=1
    else:
        if(count>max):
            max=count
        count=1
print(max)