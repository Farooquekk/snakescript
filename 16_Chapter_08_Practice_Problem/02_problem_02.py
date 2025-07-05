#  Celcius to Fahrenheit conversion

#  c/5 = (f-32)/9

# f = float(input("Enter temperature in Fahrenheit: "))
# c= 5*(f-32)/9
# print(f"Temperature in Celsius: {c:.2f}")

f = float(input("Enter temperature in Fahrenheit: "))
def f_to_c(f):
    return 5*(f-32)/9

c = f_to_c(f)
print(f"Temperature in Celsius: {round(c,2)}")