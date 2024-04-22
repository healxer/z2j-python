# 1. Create a string containing an integer, then convert that string into an actual integer object using int(). Test that your new object is a number by multiplying it by another number and displaying the result.

num1 = "18"
int_num = int(num1)
print(int_num * 3)

# 2. Repeat the previous exercise, but use a floating-point number and float.

num2 = "22.34"
float_num = float(num2)
print(float_num * 2)

# 3. Create a string object and an integer object, then display them side-by-side with a single print statement by using the str()function.

statement = "Eaten apples: "
apples_eaten = 4
print(statement + str(apples_eaten))

# 4. Write a script that gets two numbers from the user using the input() function twice, multiplies the numbers together, and displays the result. If the user enters 2 and 4, your program should print the following text: The product of 2 and 4 is 8.0.

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
multiply_nums = float(num1) * float(num2)
print("The product of " + num1 + " and " + num2 + " is " + str(multiply_nums) + ".")
