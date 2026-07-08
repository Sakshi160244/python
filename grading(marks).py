def grading(marks):
    if marks >= 90:
        return "Grade A"
    elif marks >= 75:
        return "Grade B"
    elif marks >= 60:
        return "Grade C"
    elif marks >= 40:
        return "Grade D"
    else:
        return "Fail"

try:
    marks = int(input("Enter your marks: "))

    if marks < 0 or marks > 100:
        print("Marks should be between 0 and 100.")
    else:
        print(grading(marks))

except :
    print("Invalid input! Please enter numbers only.")

finally:
    print("Program End.")

