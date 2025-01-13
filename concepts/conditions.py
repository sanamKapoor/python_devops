day_of_week = input("Enter the day of the week: ").lower()

if day_of_week in ["saturday", "sunday"]:
    print("It's the weekend!")
elif day_of_week == "monday":
    print("It's Monday - start of the work week")
elif day_of_week == "friday":
    print("It's Friday - almost weekend!")
else:
    print("It's a regular weekday")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

match operator:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero!"
    case _:
        result = "Error: Invalid operator!"

print(f"Result: {result}")