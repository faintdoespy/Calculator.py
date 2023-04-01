from time import sleep as wait
from colorama import Fore
import os

def clear():
    os.system('cls')

def calculator():
    clear()
    while True:
        print(Fore.LIGHTMAGENTA_EX)
        wait(1)
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
