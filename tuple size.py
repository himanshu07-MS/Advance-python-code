

# Q.9: write a program in python to find the size of a tuple.

# Take input from user as comma-separated values
elements = input("Enter tuple elements : ")

# Convert to tuple
my_tuple = tuple(elements.split(","))

# Find size
size = len(my_tuple)

# Display
print(f"The size of the tuple is: {size}")
