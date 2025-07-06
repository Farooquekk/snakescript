class Employee:
    # name='Farooque'
    lang = 'PY and TS' # this is the class attribute
    salary = 1200000

farooque = Employee()

# print(farooque.name)
farooque.name='Farooque Sajjad' # this is the Obj/instance attribute
print(farooque.name)
print(farooque.lang)
print(farooque.salary)

arbab = Employee()
arbab.name = "Arbab Hussain"
print(arbab.name)
print(arbab.salary)
print(arbab.lang)

# Here name is Obj/instance attribute and salary and language are class attributes as they directly belongs to the class