print("Welcome to calculator.")

operation_type = input("Do you want to add or subtract?\n")
number1 = float(input("Enter the first number.\n"))
number2 = float(input("Enter the second number.\n"))
result = ""

match operation_type:
    case "add":
        result = number1 + number2
    case "subtract":
        result = number1 - number2
    case _:
        result = "Invalid operator"
 
print(f"Your output is: {result}")