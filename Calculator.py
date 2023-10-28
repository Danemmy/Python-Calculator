#Declared a Variable to ask the user for the first number  
num1 = int(input("Type the first number: "))
# Declared a variable to ask the user to select an operand 
Calculation = input("please select an operator, +, -, /, *: ")
# Declared a variable to ask the user to input a second number 
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
