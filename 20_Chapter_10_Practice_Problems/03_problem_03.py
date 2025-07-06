class Demo:
    a=4
o=Demo()
print(o.a) # prints class attr b/c instance attr is not present
print(Demo.a)
o.a = 0 # instance attr is set
print(Demo.a) # prints the class attr
print(o.a) # prints the instance attr b/c it is present