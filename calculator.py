def calculator():
    print("Simple Calculator")
    a = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    b = float(input("Enter second number: "))

    if op == '+':
        print("Result:", a + b)
    elif op == '-':
        print("Result:", a - b)
    elif op == '*':
        print("Result:", a * b)
    elif op == '/':
        print("Result:", a / b if b != 0 else "Cannot divide by zero.")
    else:
        print("Invalid operator")

calculator()
