import random
def f(x):
    return x**3+x**2
count=0
for i in range(1000000):
    x=random.uniform(0,1)
    y=random.uniform(0,2)
    if(y<f(x)):
        count+=1
print(count/1000000*2)