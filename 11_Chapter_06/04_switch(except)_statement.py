# Python did not traditionally have a switch-case statement like many other programming languages like c++, java etc.

#  This feature uses the match and case keywords to provide functionality similar to a switch-case statement, offering a more concise and readable way to handle multiple conditions.

n = int(input('Enter an integer number : '))

match n:
    case 0:
        print('off')
    case 1:
        print('on')
    case default:
        print('Invalid input signal!')

# -----------------------------------------------------------------------------       

# an edge case not related to above code

# a = isinstance(str,"aa")
# print(a)
# a = isinstance('aa',str)
# print(a)

# -----------------------------------------------------------------------------

# edge cases of input method

# input("") # working correctly 
# "" = input("My name is :" + name) # name is not defines
# "" = input("My name is :") # will give error cannot assign to literal

# input() # working correctly

