
#write a program in python to check the number is armstrong or not.

num = int(input("Enter a 3-digit number: "))

a = num // 100              
b = (num // 10) % 10       
c = num % 10                

armstrong_sum = a**3 + b**3 + c**3

if armstrong_sum == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
