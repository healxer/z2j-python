name = "Zaphod"
heads = 2
arms = 2
print(f"{name} has {heads} heads and {arms} arms")

print("{} has {} heads and {} arms".format(name, heads, arms))

# 1. Create a float object named weight with the value 0.2, and create a string object named animal with the value "newt". Then use these objects to print the following string using only string concatenation: 0.2kg is the weight of newt.

weight = 0.2
animal = "newt"
print(str(weight) + " kg is the weight of the " + animal + ".")

# 2. Display the same string by using the .format() method and empty {} place-holders.

print("{} kg is the weight of the {}.".format(weight, animal))

# 3. Display the same string using an f-string.

print(f"{weight} kg is the weight of the {animal}.")