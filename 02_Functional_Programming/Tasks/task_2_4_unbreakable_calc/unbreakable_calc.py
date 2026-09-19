
try:
    x = float(input("Enter a number: "))
    y = float(input("Enter another number: "))
    result = x / y
    print(f"The result of {x} divided by {y} is: {result}")
except ValueError:
    print("Error: Please enter numbers only.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print(f"Success! The result is {result}")
finally:
    print("Calculation attempt complete.")
          