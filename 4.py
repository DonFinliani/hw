s=input()
s=s+" "
news=""
i=0
j=0
for i in range(len(s)):
    if(s[i]==' '):
        news+=s[j:i]
        j=i+1
print(news)