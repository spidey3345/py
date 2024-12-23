#WAP to enter the marks of 10 students and display it.
marks=[ 0 for i in range(10)]
for x in range(10):
    marks[x]=int(input("Enter the marks:"))

print("-------------------")

for i in range(10):
    print(f"Marks for Student no {i} is {marks[i]}")