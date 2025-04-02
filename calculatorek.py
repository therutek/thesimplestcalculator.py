print("Welcome to the Calculatorek!")

while True:
    operation = input("Type operation (e.g. 3+2-1*4/2): ")

    try:
        result = eval(operation, {"__builtins__": None}, {})  # Ograniczamy eval, by był bezpieczny
        print("Result:", result)
    except Exception:
        print("Error! Type correct mathematical operation.")
        if operation != "*/0":
            print("Can't divide by zero.")

    next = input("Do you wish to proceed with further calculations? (yes/no): ")
    if next.lower() != "yes" and next.lower() != "y": 
        break

print("Thank you for using Calculatorek!")
# Kalkulator w Pythonie
