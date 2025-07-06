class Employee:
    language = '' 
    salary = 0
    name = ''

    def __init__(self,namee,sal,lan): # dunder method which is automatically called
        self.name=namee
        self.language=lan
        self.salary=sal
        print('I am creating an Obj...')
    
    def getInfo(self):
        print(f'Language : {self.language}, salary : {self.salary}')

    @staticmethod
    def greet():
        print('Good Evening')

farooque = Employee("Farooque ",120000,"Python and TS")
farooque.greet()
farooque.getInfo()

# arbab =Employee()

