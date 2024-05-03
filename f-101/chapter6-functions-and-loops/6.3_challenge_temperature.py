# Write a script called temperature.py that defines two functions:

# 1. convert_cel_to_far() which takes one float parameter representing degrees Celsius and returns a float representing the same temperature in degrees Fahrenheit using the following formula: F = C * 9/5 + 32

def convert_cel_to_far(temperature_celsius):
    temperature_fahrenheit = temperature_celsius * (9/5) + 32
    return temperature_fahrenheit


# 2. convert_far_to_cel() which take one float parameter representing degrees Fahrenheit and returns a float representing the same temperature in degrees Celsius using the following formula: C = (F - 32) * 5/9

def convert_far_to_cel(temperature_fahrenheit):
    temperature_celsius = (temperature_fahrenheit - 32) * (5/9)
    return temperature_celsius

temperature_fahrenheit = input("Enter a temperature in degrees F: ")

temperature_celsius = convert_far_to_cel(float(temperature_fahrenheit))

print(f"{temperature_fahrenheit} degrees F = {temperature_celsius:.2f} degrees C")



temperature_celsius = input("Enter a temperature in degrees C: ")

temperature_fahrenheit = convert_cel_to_far(float(temperature_celsius))

print(f"{temperature_celsius} degrees C = {temperature_fahrenheit:.2f} degrees F")
