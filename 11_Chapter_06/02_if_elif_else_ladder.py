

age = int(input("Enter Your Age : "))

# IF-ELSE LADDER
if age < 0:
    print('Invalid Age, Negative age!')
elif age == 0:
    print('You entered 0, which is not a valid age')
elif age >= 18:
    print('You are above 18 and can vote')
    print('You can also drive')
else:
    print('You are below 18 and cannot vote')

print("End of Program")

# 

age =int(input('Enter your age: '))
if(age>=18):
    print('yes')
else:
    print("no")