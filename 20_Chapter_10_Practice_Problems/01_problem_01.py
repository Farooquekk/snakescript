class Programmer:
    company = 'MS '

    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin

f = Programmer('Farooque',1300000,321)
print(f.company,f.name,f.salary,f.pin)