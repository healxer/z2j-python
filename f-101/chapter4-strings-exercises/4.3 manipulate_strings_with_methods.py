# 1. Write script that converts the following strings to lowercase: "Animals", "Badger", "Honey Bee", "Honeybadger". Print each lowercase string on separate line.

first_string = "Animals"
second_string = "Badger"
third_string = "Honey Bee"
fourth_string = "HoneyBadger"

print(first_string.lower())
print(second_string.lower())
print(third_string.lower())
print(fourth_string.lower())

# 2. Repeat Exercise 1, but convert each string to uppercase instead of lowercase.

print(first_string.upper())
print(second_string.upper())
print(third_string.upper())
print(fourth_string.upper())

# 3. Write a script that removes whitespace from the following strings. Print out the strings with the whitespace removed.

string1 = "   Filet Mignon"
string2 = "Brisket    "
string3 = "  Cheeseburger  "

print(string1.lstrip())
print(string2.rstrip())
print(string3.strip())

# 4. Write a script that prints out the result of .startswith("be") on each of the following strings:

string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = "  bEautiful"

print(string1.startswith("be"))
print(string2.startswith("be"))
print(string3.startswith("be"))
print(string4.startswith("be"))

# 5. Using the same four strings from Exercise 4, write a script that uses string methods to later each string so that .starstwith("be") returns True for all of them.

string1 = string1.lower()
string2 = "becomes"
string3 = string3.lower()
string4 = string4.lower().strip()

print(string1.startswith("be"))
print(string2.startswith("be"))
print(string3.startswith("be"))
print(string4.startswith("be"))
