
from functools import reduce

menu = ["espreeso","mocha","latte","cappuccino","cortado","americano"]
price = [12.1,12.2,11]

def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee

# map function
map_coffee = map(find_coffee,menu)
print(map_coffee)

for c in map_coffee:
    print(c)

# filter function
filter_coffee = filter(find_coffee,menu)
# print(filter_coffee)
for c in filter_coffee:
    print(c)

# # reduce function
sum_of_price = reduce(lambda x,y : x+y,price)
print(sum_of_price)
