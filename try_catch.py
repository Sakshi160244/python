# def calculator(a, b, choice):
#     if choice == 1:
#         return a + b
#     elif choice == 2:
#         return a - b
#     elif choice == 3:
#         return a * b
#     elif choice == 4:
#         return a / b
#     else:
#         return "Invalid Choice"

# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     choice = int(input("1.Add 2.Subtract 3.Multiply 4.Divide: "))

#     print("Result:", calculator(a, b, choice))

# except ValueError:
#     print("Please enter numbers only.")
#def calculator(a, b, choice):
#     if choice == 1:
#         return a + b
#     elif choice == 2:
#         return a - b
#     elif choice == 3:
#         return a * b
#     elif choice == 4:
#         return a / b
#     else:
#         return "Invalid Choice"

# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     choice = int(input("1.Add 2.Subtract 3.Multiply 4.Divide: "))

#     print("Result:", calculator(a, b, choice))

# except ValueError:
#     print("Please enter numbers only.")

# except ZeroDivisionError:
#     print("Cannot divide by zero.")

# finally:
#     print("Program Ended.")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")

# finally:
#     print("Program Ended.")


# def grading(marks):
#     if marks >= 90:
#         return "Grade A"
#     elif marks >= 75:
#         return "Grade B"
#     elif marks >= 60:
#         return "Grade C"
#     elif marks >= 40:
#         return "Grade D"
#     else:
#         return "Fail"

# try:
#     marks = int(input("Enter your marks: "))

#     if marks < 0 or marks > 100:
#         print("Marks should be between 0 and 100.")
#     else:
#         print(grading(marks))

# except :
#     print("Invalid input! Please enter numbers only.")

# finally:
#     print("Program End.")


# menu = {
#     "pizza": 200,
#     "burger": 100,
#     "coffee": 80
# }

# try:
#     item = input("Enter item name: ").lower()

#     print("Price:", menu[item])

# except :
#     print("Item is not available in the menu.")

# finally:
#     print("Thank you! Visit Again.")

import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
