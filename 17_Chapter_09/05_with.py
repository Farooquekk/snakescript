# f = open('01_file.txt')
# data = f.read()
# print(data)
# f.close()

#  This can be written using the with Statement like this:

with open('01_file.txt') as f:
    print(f.read())

#  You don't have to explicitly close the file
