# Basic Calculator (Week 2 Project)
"""
The goal of this project is to create a simple calculator to demonstrate my understanding of my module.
"""
# Create a Function(Parameters)
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

operation = input ("choose(+, -, *, /")

if operation == "+":
    print("Result:", num1 + num2)
    
elif operation == "-":
    print("Result:", num1 - num2)
    
elif operation == "*":
    print("Result:", num1 * num2)
 
elif operation == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
        
    else:
            print("Cannot divide by Zero!")
            
else:
    print("Invalid operation")