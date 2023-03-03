print('if elif else - Exercise\n')
print("Create a calculator\n")
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f



math = input('Enter math operation(+,-,*,/) or f for Celsius to Fahrenheit conversion: ')
num1 = float(input('Enter first number: '))
if math.lower() == 'f':
    print(f'{num1} Celsius is equivalent to {(num1*9/5)+32 } fahrenheit')
else:
    num2 = float(input('Enter second number: '))

    if math == 'f':
        print(f'Answer is: {num1 + num2}')
    elif math == '+':
        print(f'Answer is: {num1 + num2}')
    elif math == '-':
        print(f'Answer is: {num1 - num2}')
    elif math == '*':
        print(f'Answer is: {num1 * num2}')
    elif math == '/':
        print(f'Answer is: {num1 / num2}')
    else:
        print('Input error!')
        print("Please use math operation(+,-,*,/) or f for Celsius to Fahrenheit conversion:")