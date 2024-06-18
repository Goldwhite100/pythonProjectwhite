# A simple calculator
num1 = int(input("Enter first number:"))
sign = input("Enter sign:")
num2 = int(input("Enter second number:"))
if sign == "+" :
        print("Result:", num1 + num2)
elif sign == "-" :
        print("Result:", num1 - num2)
elif sign == "*" :
        print("Result:", num1 * num2)
elif sign == "/" :
    if num2 != 0:
        result = num1 / num2
    else:
        result = "math error"
        print("Result:", result)
else:
    print("Invalid input")
