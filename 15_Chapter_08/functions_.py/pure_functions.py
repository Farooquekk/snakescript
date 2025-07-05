my_list = [1,2,3]

# def add_to_list(item):
#     return my_list.append(item)
# add_to_list(4)
# print(my_list)


# def add_to_list(item):
#     my_list.append(item)
#     return my_list

# my_new_list = add_to_list(4)
# print(my_list)
# print(my_new_list)

# def add_to_list(lst,item):
#     print('Traditional Function')
#     lst.append(item)
#     return lst
# my_new_list = add_to_list(my_list,4)
# print(my_list)
# print(my_new_list) 

#  the above function(s) is not a pure function because data at the globla state of the function is changed.
# A pure function is a function that does not change or have any effect on a variable, data, list, or sets beyond its own scope.

# let's make the above function to a pure function
def add_to_list(lst,item):
    print('Pure Function')
    nl = lst.copy()
    nl.append(item)
    return nl
my_new_list = add_to_list(my_list,4)
print(my_list)
print(my_new_list)