# Write a script called exponent.py that receives two numbers from the user and displays the first number raised to the power of the second number.

base = float(input("Enter a base: "))
exponent = float(input("Enter an exponent: "))
exponentiation = base**exponent

result = f"{base} to the power of {exponent} = {exponentiation}"

print(result)
