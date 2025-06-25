# friends = ['Farooque','Talha','Arbab',54.33,122,False,'Parkash']
# print(friends)
# friends.append('Rohal')
# print(friends)

# # Sort the list
# l1 = [1,-1,-9,0,200,4,3,-100]
# print(l1)
# l1.sort()
# print(l1)

# # Reverse the list
# print(l1)
# l1.reverse()
# print(l1)

# # Insert item in the list
# print(l1)
# l1.insert(3,333333)  # insert 333333 at index 3 in the list 
# print(l1)


# # Remove item from the list at an index
# print(l1)
# print(l1.pop(2))
# print(l1)

# # Remove item from the list by value
# print(l1)
# value = l1.remove(333333)
# print(value)
# print(l1)



list1 = [1,2,3,4,5]
print(list1,sep=" ")
list1.insert(len(list1),6)
print(list1,sep=" ")
list1.append(7)
print(list1,sep=" ")
list1.extend([8,9,10])
print(list1,sep=" ")
list1.pop(9)
print(list1,sep=" ")
del list1[2]
print(list1,sep=" ")
# printing all the values using loop

for x in list1:
    print("value : " ,x)