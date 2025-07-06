
class Calculator:
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f'The Square is : {self.n*self.n}')
    def cube(self):
        print(f'The Cube is : {self.n*self.n*self.n}')
    def squareroot(self):
        print(f'The Sqyare Root is : {self.n**1/2}')

n = Calculator(4)
n.square()
n.cube()
n.squareroot()