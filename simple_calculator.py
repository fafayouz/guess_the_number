def calculator():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            operator = input("Enter the operator (+, -, *, /) or 'q' to quit: ").strip()
            
            if operator == 'q':
                print("Exiting calculator. Goodbye!")
                break
            
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Error: Cannot divide by zero!")
                    continue
                result = num1 / num2
            else:
                print("Invalid operator! Please enter one of +, -, *, /.")
                continue
            
            print(f"The result is: {result}\n")
        
        except ValueError:
            print("Invalid input! Please enter numeric values only.\n")


# Call the calculator function
calculator()
