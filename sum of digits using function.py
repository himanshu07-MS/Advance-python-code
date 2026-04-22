
# Q.17: write a program in python to find the sum of digit of a number using function. 

# Function to find sum of digits
def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total

# Main program
num = int(input("Enter a number: "))
result = sum_of_digits(num)
print(f"Sum of digits of {num} is {result}")
