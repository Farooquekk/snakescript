class Employee:
    def __init__(self,name,last) -> None:
        self.name = name
        self.last = last

class Supervisor(Employee):
    def __init__(self, name, last,password):
        super().__init__(name, last)
        self.password = password

class Chefs(Employee):
    def leave_request(self,days):
        return "May I take a leave for " + str(days) + "days"
    

farooque = Supervisor('Farooque','F','fruit')
talha = Chefs('Talha','T')
arbab = Chefs('Arbab','A')

print(talha.leave_request(3))
print(farooque.password)
print(talha.name)