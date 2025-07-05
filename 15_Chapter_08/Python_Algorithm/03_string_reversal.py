
# 1) simple way to reverse a string using slice funcion
# str[start:stop:step]
print('\nReverse using Slice function')
trail = 'Dogesh'
new_trail = trail[::-1]
print(f'trail : {trail}')
print(f'new_trail : {new_trail}')

# 2) recurison method
print('\nReverse using Recurison')
def str_reverse(str):
    if len(str) == 0:
        return str
    else:
        return str_reverse(str[1:] )+ str[0]
    
str = 'Dogesh'
reverse_str = str_reverse(str)
print(str)
print(reverse_str)

# name = 'Dogesh'
# print(name[1:])
# print(name[0])