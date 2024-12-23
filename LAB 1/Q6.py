#WAP to calculate the factorial of an input number.
def factorial(a):
    if(a<2):
        return 1
    else:
        return a * factorial(a-1)

a=int(input("Enter a number:"))

f= factorial(a)
print("The factorial is:",f)