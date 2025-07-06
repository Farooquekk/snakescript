# payment_info.py

class Payslips:
    def __init__(self, name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment = "yes"

    def status(self):
        if self.payment == "yes":
            return self.name + " is paid " + str(self.amount)
        else:
            return self.name + " is not paid yet"

farooque = Payslips("Farooque", "no", 1000)
talha = Payslips("Talha","no",2000)

print('Befor Payment')
print(farooque.status(),"\n",talha.status())
print('After Payment')
farooque.pay()
print(farooque.status(),"\n",talha.status())
