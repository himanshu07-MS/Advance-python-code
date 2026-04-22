
# Q.10: write a program in python to find sum of tuple elements.

# Take input from user
elements = input("Enter elements of tuples in commas : ")

# Convert input string to tuple of integers
my_tuple = tuple(map(int, elements.split(",")))

# Calculate sum
total = sum(my_tuple)

# Display result
print(f"The sum of tuple elements is: {total}")
