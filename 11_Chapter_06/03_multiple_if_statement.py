a = int(input("Enter Your Age : "))
# If statement one
if (a % 2 == 0):
    print('You entered an even number')
# End of If statement one

# If statement two
if a < 0:
    print('Invalid Age')
elif a == 0:
    print('You entered 0, which is not a valid age')
elif a < 18:
    print('You are a minor')
    print('You cannot vote')
else:
    print('You are above 18 and can vote')
# End of If statement two

print("End of Program")