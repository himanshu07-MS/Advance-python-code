

# Q.1 = write a program in python to make a calculator by using match case.

num1 = float(input("Enter first number: "))   #take user input for first number
num2 = float(input("Enter second number: "))  #take user input for second number
operators = input("Enter operators (+, -, *, /, %): ")  #user choose operators on the following

match operators:    #used match case for making calculator.
    case "+":
        print(f"Result: = {num1 + num2}")
    case "-":
        print(f"Result: = {num1 - num2}")
    case "*":
        print(f"Result: = {num1 * num2}")
    case "/":
        if num2 != 0:
            print(f"Result: = {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
    case "%":
        print(f"Result: = {num1 % num2}")
    case _:
        print("Invalid operators. Please enter one of +, -, *, /, %.")
