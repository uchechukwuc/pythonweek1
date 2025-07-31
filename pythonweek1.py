# This program creates a simple calculator that performs basic arithmetic operations.

def calculator():
    """
    Performs a calculation based on user input for two numbers and an operation.
    """
    print("Welcome to the Basic Calculator Program!")

    while True:
        try:
            # Get the first number from the user
            num1 = float(input("Enter the first number: "))
            break # Exit loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        try:
            # Get the second number from the user
            num2 = float(input("Enter the second number: "))
            break # Exit loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        # Get the mathematical operation from the user
        operation = input("Enter the operation (+, -, *, /): ")

        # Perform the operation based on user input
        if operation == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
            break
        elif operation == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
            break
        elif operation == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
            break
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
                break
            else:
                print("Error: Division by zero is not allowed. Please enter a non-zero second number.")
                # If division by zero, ask for the second number again
                while True:
                    try:
                        num2 = float(input("Enter the second number (cannot be zero): "))
                        if num2 != 0:
                            break
                        else:
                            print("Invalid input. Please enter a non-zero number.")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
        else:
            print("Invalid operation. Please enter one of +, -, *, /.")

# Call the calculator function to run the program
calculator()