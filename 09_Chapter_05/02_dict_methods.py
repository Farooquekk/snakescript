marks = {
    "Farooque" :91,
    "Arbab":93,
    "Talha":95,
    "Ada Dogesh":100,
    0:"Zero",  # This is a valid key-value pair
}

#  Items method
print(marks.items())
#  Keys method
# print(marks.keys())
#  Values method
# print(marks.values())
#  Update method
# marks.update({"Farooque":99,"Arbab":98,"Rohal":97}) # update and add new key-value pairs
# print(marks)

# Get method
# print(marks.get('Monkey'))
# print(marks.get('Ada Dogesh')) # If not found, it returns None by default
# print(marks['Ada Dogesh']) # If not found, it raises a KeyError

# Pop method
print(marks.pop('Farooque')) # Removes the key 'Farooque' and returns its value
print(marks)

# Pop item method
print(marks.popitem()) # Removes the last inserted key-value pair and returns it
print(marks)