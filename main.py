from time import sleep as wait
import os

def clear():
    os.system('cls')

def calculator():
    wait(1)
    clear()
    num1 = int(input(f'Number 1: '))
    num2 = int(input(f'Number 2: '))
    operation = input(f'+, -, /, or %: ')
    if operation == str('+'):
        print(f'{str(num1+num2)}')
    if operation == str('-'):
        print(f'{str(num1-num2)}')
    if operation == str('/'):
        print(f'{str(num1/num2)}')
    if operation == str('%'):
        print(f'{str(num1%num2)}')

calculator()