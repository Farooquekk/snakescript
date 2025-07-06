class Employee:
    
    lang = 'PY and TS' 
    salary = 1200000
    def getInfo(self):
        print(f'Language : {self.lang}, salary : {self.salary}')

    @staticmethod
    def greet():
        print('Good Evening')

farooque = Employee()

print(farooque.lang) 
print(farooque.salary)
# farooque.getInfo() # Employee.getInfo(farooque)
farooque.getInfo()
farooque.greet()

# Employee.getInfo(farooque)
# Employee.greet(farooque)