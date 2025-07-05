# scoping in python
# 4 types of scope --> together they are reffered as LEGB
# i)   Local Scope
# ii)  Enclosing Scope
# iii) Global Scope
# iv)  Built-in Scope


# Global Scope
my_global_var = 101
def my_func():
    enclosed_var = 100
    def my_func_2():
            local_var = 92
            print('Access to global : ',my_global_var)
            print('Access to enclosed : ' , enclosed_var)
    my_func_2()
# my_func()
# print('Cannot access local : ',local_var)
my_func()
# print(local_var) #can't
# print(enclosed_var) #can't

# Built-in scope includes built-in functions and objects (like print(), len(), etc.), but not reserved keywords (like def, for, if, etc.).
