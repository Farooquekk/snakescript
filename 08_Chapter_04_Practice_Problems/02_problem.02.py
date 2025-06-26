# Write a Program to accept the marks of the 5 students and sort them in ascending order.

marks=[]
f1 = float(input("Enter Marks of Student 1 : "))
marks.append(f1)
f2 = float(input("Enter Marks of Student 2 : "))
marks.append(f2)
f3 = float(input("Enter Marks of Student 3 : "))
marks.append(f3)
f4 = float(input("Enter Marks of Student 4 : "))
marks.append(f4)
f5 = float(input("Enter Marks of Student 5 : "))
marks.append(f5)
f6 = float(input("Enter Marks of Student 6 : "))
marks.append(f6)
f7 = float(input("Enter Marks of Student 7 : "))
marks.append(f7)

print("Your marks List is : " , marks)
# Sort the marks in ascending order
marks.sort()
print("Your sorted marks List is : " , marks)

# Note :- Need to convert this to int or float before sorting