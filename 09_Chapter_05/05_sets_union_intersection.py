s1 = {1,45,6,78}
s2 = {7,8,1,78}

# Union of two sets
print(s1.union(s2))
print(s1.intersection(s2))
print(s1 | s2)  # Another way to perform union
print(s1 & s2)  # Another way to perform intersection
# Difference of two sets
print(s1.difference(s2))
print(s2.difference(s1))
# Symmetric difference of two sets
print(s1.symmetric_difference(s2))
print(s1 ^ s2)  # Another way to perform symmetric difference