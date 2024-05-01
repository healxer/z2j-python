# 1. In one line of code, display the result of trying to .find() the substring "a" in the string "AAA". The result should be -1.

print("AAA".find("a"))

# 2. Replace every occurrence pf the character "s" with "x" in the string "Somebody said something to Samantha".

phrase = "Somebody said something to Samantha"
print(phrase.replace("s", "x"))

# 3. Write and test a script that accepts user input using the input() function and displays the result of trying to .find() a particular letter in that input.

name = input("What is your name?\n")
print(name.find("a"))