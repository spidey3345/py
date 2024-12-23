#WAP to sort the list {5, 4, 11, 13, 51}
a=[5,4,13,11,51]
def sort(a):
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if(a[i]>a[j]):
                temp=a[i]
                a[i]=a[j]
                a[j]= temp

sort(a)
print(a)