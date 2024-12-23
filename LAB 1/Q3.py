#WAP to calculate sum, diff, product and quotient between two input numbers using a single function.
def simplify(a,b):
    add=a+b
    diff=a-b
    product=a*b
    quotient=a/b
    return(add,diff,product,quotient)

a=float(input("Enter First Number"))
b=float(input("Enter Secong Number"))

a,d,p,q=simplify(a,b)

print("sum = ",a)
print("Difference = ",d)
print("Product", p)
print("Quotient",q)
