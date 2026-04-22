
# Q.11: write a program in python to find the unique elements in a list.

# Take numeric input from user
elements = input("Enter numbers separated by commas: ")

# Convert to list of integers
num_list = list(map(int, elements.split(",")))

# Get unique numbers
unique_number = []
for num in num_list:
    if num not in unique_number:
        unique_number.append(num)

# Display
print("Unique numbers are:", unique_number)
