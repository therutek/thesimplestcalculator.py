print("Welcome to The Simplest Calculator!")

number1 = float(input("Enter the first number: "))                 # Float konwertuje tekst na liczbę zmiennoprzecinkową, np. 3, 14.2, 1.24 itd.
number2 = float(input("Enter the second number: "))
operation = input("Select operation (+, -, *, /): ")

if operation == "+":
    result = number1 + number2
elif operation == "-":
    result = number1 - number2
elif operation == "*":
    result = number1 * number2
elif operation == "/":
    if number2 != 0:
        result = number1 / number2
    else:
        result = "Error! Can't divide by zero."
else:
    result = "Operation unknown!"

print("Result:", result)

next = input("Do you wish to perform further calculations? (yes/no): ")
while next == "yes":           # Pętla "while" pozwala na wielokrotne wykonywanie tego samego kodu
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    operation = input("Select operation (+, -, *, /): ")

    if operation == "+":
        result = number1 + number2
    elif operation == "-":
        result = number1 - number2
    elif operation == "*":
        result = number1 * number2
    elif operation == "/":
        if number2 != 0:
            result = number1 / number2
        else:
            result = "Error! Can't divide by zero."
    else:
        result = "Operation unknown!"

    print("Result:", result)
    next = input("Do you wish to perform further calculations? (yes/no): ")
