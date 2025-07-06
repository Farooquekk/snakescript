class Employee:
    # name='Farooque'
    lang = 'PY and TS' # this is the class attribute
    salary = 1200000

farooque = Employee()


farooque.lang='Js'
print(farooque.lang) # this is instance attr
print(farooque.salary)

# Instance attr takes prefrences over class attr during assignment and retrievel.
