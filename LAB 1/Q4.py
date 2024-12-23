#WAP to display prime numbers from 1 to 100
a=[]
def prime(n):
    divisible=0
    for x in range(1,n):
        if(n%x)==0:
            divisible=divisible+1
    if divisible<=2:
            a.append(n)

for i in range(1,101):
    prime(i)

print(a)