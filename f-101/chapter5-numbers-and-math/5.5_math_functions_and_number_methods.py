# 1. Write a script that asks the user to input a number and then displays that number rounded to two decimal places.

num1 = float(input("Enter a number: "))
round_num1 = round(num1, 2)

print(f"{num1} rounded to 2 decimal places is {round_num1}")

# 2. Write a script that asks the user to input a number and then displays the absolute value of that number.

num2 = int(input("Enter a number: "))
abs_num2 = float(abs(num2))

print(f"The absolute value of {num2} is {abs_num2}")

# 3. Write a script that asks the user to input two numbers by using the input() function twice, then display whether or not the difference between those two number is an integer.

first_number = float(input("Enter a number: "))
second_number = float(input("Enter another number: "))
is_integer = (first_number - second_number).is_integer()

print(f"The difference between {first_number} and {second_number} is an integer! {is_integer}!")
