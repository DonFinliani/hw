c=2
start=1
while(abs(c-start**2)>0.01):
    start+=0.001
print(start)

min=0;max=2
g=(min+max)/2
while(abs(g**2-c)>0.01):
    if(g**2<c):
        min=g
    if(g**2>c):
        max=g
    g=(min+max)/2
print(g)

def f(x):
     return x**2-2

start=1
while(abs(start**2-2)>0.01):
    start=1+start-start**2/2
print(start)