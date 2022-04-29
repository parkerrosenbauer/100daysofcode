# Day 10 of 100 Days of Code Challenge
# Calculator
import os
from calculator_art import logo


def clear():
    """Clears the terminal"""
    os.system('cls')


def calculator(n1, n2, calc_type):
    """Takes two numbers and an operator to perform the mathmatical operation"""
    if calc_type == '+':
        return n1 + n2
    elif calc_type == '-':
        return n1 - n2
    elif calc_type == '*':
        return n1 * n2
    elif calc_type == '/':
        return n1 / n2


run = 'm'

while run != 'n':
    if run == 'y':
        first_num = output
        print(f"The first number is {first_num}")
    else:
        clear()
        print(logo)
        first_num = float(input("What's the first number?: "))
    print("+\n-\n*\n/")
    operator = input("Pick an operation: ")
    second_num = float(input("What's the next number?: "))
    output = calculator(first_num, second_num, operator)
    print(f"{first_num} {operator} {second_num} = {output}")
    run = input(
        f"Type 'y' to continue calculating with {output}, type 'm' to start a new calculation, or type 'n' to end the calculator: ")
