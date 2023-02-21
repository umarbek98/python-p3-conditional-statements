#!/usr/bin/env python3

def admin_login(username, password):
    if username == 'sudo' and password == '12345':
        print('Access denied')
        return 'Access denied'
    elif username == 'admin' and password == '12345':
        return 'Access granted'
    elif username == 'ADMIN' and password == '12345':
        return 'Access granted'
    else : 
        return 'Access denied'


def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature >= 40 and temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 86:
        return "It's too dang hot out there!"
    else :
        return "It's perfect out there!"

def fizzbuzz(num):
    if not num % 3 and not num % 5:
        print('FizzBuzz')
        return "FizzBuzz"
    elif not num % 5:
        print('Buzz')
        return 'Buzz'
    elif not num % 3:
        print('Fizz')
        return "Fizz"
    else : 
        print(num)
        return num
fizzbuzz(15)

def calculator(operation, num1, num2):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else :
        print("Invalid operation!")
        return None
