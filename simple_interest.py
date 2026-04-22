
# Q.4: write a program in python to calculate the simple interest. 

principle = float(input("Enter the value of principle: "))
rate = float(input("Enter the value of rate: "))
time = float(input("Enter the value of time: "))

simple_interest = (principle * rate * time)/100

print(f"{simple_interest}")
