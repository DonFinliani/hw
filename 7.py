import random
count=0
for i in range(1000000000):
    x=random.uniform(0,1)
    y=random.uniform(0,1)
    if(x**2+y**2<1):
        count+=1
print(count/1000000000*4)

k=-1
n=3.0
result=1;resultnew=1
while(abs(result-resultnew)>0.0000000001 or n==3.0):
    result=resultnew
    resultnew+=k*(1/n)
    k=0-k
    n+=2
print(resultnew*4)

from cmath import sqrt
import math
n=2.0
result=1;resultnew=1
while(abs(result-resultnew)>0.0000000001 or n==2.0):
    result=resultnew
    resultnew+=1/(n**2)
    n+=1
print(sqrt(resultnew*6))
