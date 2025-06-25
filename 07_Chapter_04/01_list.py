# List in Python
# A list is a collection of items in a particular order.

friends = ['Farooque','Talha','Arbab',54.33,122,False,'Parkash']
print(friends)
print(friends[0])
friends[0]='PineApple' # Unlike strings, lists are mutable, meaning you can change their content
print(friends)
print(friends[0])

print(friends[1:4])

# other ways of printing a list 
print('List : ',*friends)
print(friends,sep=" ")


