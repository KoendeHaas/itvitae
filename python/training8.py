def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def fraction(number1, number2):
    return number1 / number2
    
print("Welcome to calculator.")

state = None

while state != "exit":

    operation_type = input("Do you want to +, -, * or /?\n")
    number1 = float(input("Enter the first number.\n"))
    number2 = float(input("Enter the second number.\n"))
    result = ""

    match operation_type:
        case "+":
            result = add(number1, number2)
        case "-":
            result = subtract(number1, number2)
        case "/":
            result = fraction(number1, number2)
        case "*":
            result = multiply(number1, number2)
        case _:
            result = "Invalid operator"

    print(f"{number1} {operation_type} {number2} = {result}")

    input = input("Do you want to exit? y/n ")
    if input == "y":
        state = "exit"