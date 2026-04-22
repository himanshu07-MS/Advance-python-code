
# Q.12: write a program in python to check whether the number is prime or not.

a = int(input("Enter a number: "))

count = 0
if a <= 1:
    print(a, "is not a prime number.")
else:
    for i in range(1, a + 1):
        if a % i == 0:
            count += 1
    if count == 2:
        print("Number is prime.")
    else:
        print("Number is not prime.")
