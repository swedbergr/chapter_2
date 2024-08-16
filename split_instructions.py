time = input("Give me a time ")

# Separate everything on each side of the : into a list
list_name = time.split(":")

# Reference every element in the list by a separate variable
hour = list_name[0]
min = list_name[1]

# Print output
print("Hours are", hour, "and minutes are ", min)