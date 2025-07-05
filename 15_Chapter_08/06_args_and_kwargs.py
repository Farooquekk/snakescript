#  ************* args *******************

# def sum_of(a,b):
#     return(a+b)

# print(sum_of(4,5)) # give 9
# print(sum_of(3,4,5)) # TypeError: sum_of() takes 2 positional arguments but 3 were given

# to solve above problem we will use args

# def sum_of(*args):
#     sum = 0
#     for x in args:
#         sum += x
#     return sum

# print(sum_of(4,4,5,6))


#  ************* kwargs *******************
# passing key-word arguments, and non-keyword var
def sum_of(**kwargs):
    sum = 0
    for k,v in kwargs.items():
        sum+=v
    return round(sum,2)


print(sum_of(coffee=2.99,cake=1.01,Biryani=4.2,milk_shake=2.1))