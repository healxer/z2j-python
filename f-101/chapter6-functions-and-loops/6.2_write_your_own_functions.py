# 1. Write a function called cube() with one number parameter and returns the value of that number raised to the third power. Test the function by displaying the result of calling your cube() function ona few different numbers.

def cube(num):
    cube_result = num ** 3
    return cube_result

print(f"2 cubed is {cube(2)}")
print(f"3 cubed is {cube(3)}")

# 2. Write a function called greet() that takes one string parameter called name and displays the text "Hello <name>!", where <name> is replaced with the value of the name parameter.

def greet(name):
    print(f"Hello {name}!")

greet("Thanh")