try:
    # Code that may raise an exception
    num1 = int(input("Enter a numerator: "))
    num2 = int(input("Enter a denominator: "))
    result = num1 / num2
    print("Result:", result)

except ValueError:
    print("Invalid input! Please enter valid integers.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

finally:
    print("Execution complete. Thank you!")
