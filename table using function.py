
# Q.18: write a program in python to print a table of a given number declaration by the user function.

# Function to print table of a given number
def print_table(number):
    print(f"Table of {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Main program
num = int(input("Enter a number: "))
print_table(num)
