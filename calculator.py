def calculator(a, b, choice):
    if choice == 1:
        return a + b
    elif choice == 2:
        return a - b
    elif choice == 3:
        return a * b
    elif choice == 4:
        return a / b
    else:
        return "Invalid Choice"

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    choice = int(input("1.Add 2.Subtract 3.Multiply 4.Divide: "))

    print("Result:", calculator(a, b, choice))

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Program Ended.")