try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(f"The result is {result}")
except ZeroDivisionError:
    print("❌ Error: Cannot divide by zero.")
except ValueError:
    print("❌ Error: Please enter a valid number.")
# finally done
