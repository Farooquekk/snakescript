# a = (1,2,3,4)
# print(type(a))
# b=() # empty tuple
# print(type(b))
# c=(1) # this is not a tuple, it is an int
# print(type(c))
# d=(1,) # this is a tuple with one element
# print(type(d))

# n1 = (1,2,"Farooque",True,3.14,"Farooque",2,"Farooque")
# print(n1)
# print(type(n1))
# # Tuples are immutable, meaning they cannot be changed after creation
# # print(n1[0])
# # n1[0]=1000

# # Tuple Methods
# # count() method returns the number of occurrences of a value in the tuple
# num = n1.count("Farooque")
# print(num)

# # index() method returns the index of the first occurrence of a value in the tuple
# index_of_farooque = n1.index("Farooque")
# print(index_of_farooque)

# another way of creating a tuple

# my_tuple_01 = (1,2,'strings',1.5,False)
my_tuple_02 = 2,'strings_',1.8,False

# printing values of tuple using loop

for x in my_tuple_02:
    print("value : " ,x)
    