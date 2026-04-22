
# Q.7: write a progra in python to calculate the electricity bill according to the following criteria.

unit = float(input("Enter your bill in unit: "))

if unit <= 100:
    bill = unit*5
    print("your bill anount is according to 5 rupees / units: ",bill)

elif unit>100 and unit <=200:
    bill = unit*10
    print("your bill amount is according to 10 rupees / units: ",bill)

elif unit>200:
    bill = unit*15
    print("your bill amount is according to 15 rupees /unit: ",bill)
    
