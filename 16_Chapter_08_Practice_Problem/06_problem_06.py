# Inches to Centimeters Converter

inches = float(input("Enter the length in inches: "))
def iches_to_cm(inches):
    return 2.54*inches

cm = iches_to_cm(inches)
print(f"The length in centimeters is: {round(cm, 2)} cm")