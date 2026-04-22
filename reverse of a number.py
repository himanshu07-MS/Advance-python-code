
# Q.14: write a program in python to print reverse of the number. 

# Reverse of a number program

# Step 1: User se number input lena
num = int(input("Enter a number: "))

# Step 2: Reverse find karna
reverse = 0
temp = num  # original number safe rakhne ke liye

while temp > 0:
    digit = temp % 10       # last digit nikalna
    reverse = reverse * 10 + digit  # reverse me add karna
    temp //= 10             # last digit remove karna

# Step 3: Output print karna
print("Reverse of", num, "is", reverse)
