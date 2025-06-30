marks =  int(input('Enter Your marks : '))

if(marks<=100 and marks >= 90):
    print('You have got A+')
elif(marks<90 and marks >=80):
    print('You have got A')
elif(marks<80 and marks>=70):
    print('You have got B+')
elif(marks<70 and marks>=60):
    print('You have got B')
elif(marks<60 and marks>=50):
    print('You have got C+')
else:
    print('You failed the exam')

