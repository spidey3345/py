#WAP program to sum all the items in a list.
a=[1,2,3,4]
def sum(a):
    b=0
    for i in range(len(a)):
        b= b + a[i]
    return b

c = sum(a)
print(c)
