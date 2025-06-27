s = {1,32,5,4,0,54,5,5,5,"Farooque"}
# print(s)
# print(type(s))

# Set methods

# 1. add() - Adds an element to the set
s.add(10000)
print(s,type(s))
# 2. Len() - Returns the number of elements in the set
print(len(s))
# 3. remove() - Removes an element from the set, raises KeyError if not found
s.remove(10000)
print(s)