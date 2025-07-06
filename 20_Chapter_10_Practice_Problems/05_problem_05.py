from random import randint
class Train:
    
    def __init__(self,trainNo):
        self.trainNo = trainNo
        
    def book(self,fro,to):
        print(f'Ticket is booked in Train no :  {self.trainNo} from {fro} to {to}')
        
    def getStatus(self):
        print(f'The train with Train Number :{self.trainNo} is running on time')
    def getFare(self,fro,to):
        print(f'Ticket is booked in Train no :  {self.trainNo} from {fro} to {to} is {randint(222,55555)}')


t = Train(123)
t.book("MPK","HYD")
t.getFare("MPK","HYD")
t.getStatus()