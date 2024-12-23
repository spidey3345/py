#WAP program to get the largest number from a list
def largest(a):
    l = a[0]
    for i in range(len(a)):
        if l<a[1]:
            l=a[1]
    return l

c = int(input("Enter the Total number of numbers"))
a=[ 0 for i in range(c)]
for x in range(c):
    a[x]=int(input("Enter the number:"))

b = largest(a)
print("The Largest number is",b)
