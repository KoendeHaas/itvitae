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
    
    sum = input("Please enter your sum (syntax: 1 + 1)\n").split(" ")
    operation_type = sum[1]
    number1 = float(sum[0])
    number2 = float(sum[2])
    
    # operation_type = input("Do you want to +, -, * or /?\n")
    # number1 = float(input("Enter the first number.\n"))
    # number2 = float(input("Enter the second number.\n"))
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

    exit = input("Do you want to exit? y/n\n")
    if exit == "y":
        state = "exit"