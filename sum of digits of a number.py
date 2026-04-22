
# Q.16: write a program in python to find the sum of digits of a number.

# Sum of digits of a number program

# Step 1: User se number input lena
num = int(input("Enter a number: "))

# Step 2: Sum nikalne ke liye variables
sum_digits = 0
temp = num

while temp > 0:
    digit = temp % 10      # last digit lena
    sum_digits += digit    # sum me add karna
    temp //= 10            # last digit remove karna

# Step 3: Output
print(f"Sum of digits of {num} is {sum_digits}")
