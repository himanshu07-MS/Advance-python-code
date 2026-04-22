
# Q.3: write a program in python to find the factorial a number.

num = int(input("Enter a number: "))

def factorial(n):      # Function define kiya
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
result = factorial(num)
print(f"The factorial of {num} is {result}.")
