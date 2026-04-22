
# Q.15: write a program in python to print table of a given number.

# Table of a given number program

# Step 1: User se number input lena
num = int(input("Enter a number: "))

# Step 2: Loop se table print karna
print(f"Table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
