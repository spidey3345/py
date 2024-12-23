#WAP to input the percentage and display the division
def percentage(a):
    if(a>=80):
        print("You secured Distinction")
    elif(a>=65):
        print("You secured First Division")
    elif(a>=55):
        print("You secured Second Division")
    elif(a>=40):
        print("You secured Third Division")
    else:
        print("You secured Failed")

a=float(input("Enter Your Percentage:"))
percentage(a)