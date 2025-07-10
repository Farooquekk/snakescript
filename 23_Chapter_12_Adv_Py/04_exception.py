try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except ValueError as v:
    print("Bhai Value Error ha Input Sahi se de...")
    print(v)
    
except Exception as e:
    print(e) 

print("Thank You")