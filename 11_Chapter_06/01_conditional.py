
a = int(input("Enter Your Age : "))

    # IF ELIF ELSE LADDER
if a < 0:
    print('Invalid Age')
elif a == 0:
    print('You entered 0, which is not a valid age')
elif a < 18:
    print('You are a minor')
    print('You cannot vote')
else:
    print('You are above 18 and can vote')

print("End of Program")
