marks1 = int(input('Enter marks for subject 1:'))
marks2= int(input('Enter marks for subject 2:'))
marks3 = int(input('Enter marks for subject 3:'))
marks4 = int(input('Enter marks for subject 4:'))

# Check for total percentage
total_marks  = marks1+marks2+marks3+marks4
total_percentage = (total_marks/400)*100
if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33 and marks4>=33):
    print('You have passed the exam with a percentage of : ', total_percentage)
else:
    print('You have failed the exam : ', total_percentage) 