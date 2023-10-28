num1 = int(input("Type the first number: "))
Calculation = input("please select an operator, +, -, /, *: ")
num2 = int(input("Type your second number: "))


if Calculation == ('+', '-', '/', '*'):
    if Calculation == '+':
        print(num1 + num2)
elif Calculation == '-':
    print(num1 - num2)
elif Calculation == '*':
    print(num1 * num2)
elif Calculation == '/':
    print(num1 / num2)


else:
    print("select a number")
