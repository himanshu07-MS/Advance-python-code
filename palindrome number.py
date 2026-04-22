
# Q.13: write a program in python to check whether the number is palindrome number is or not.

# Take input
n = int(input("Enter a number: "))
original = n
reverse = 0

# Reverse the number
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

# Check
if original == reverse:
    print(f"{original} is a palindrome number.")
else:
    print(f"{original} is not a palindrome number.")
