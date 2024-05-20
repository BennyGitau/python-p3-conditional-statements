#!/usr/bin/env python3

def admin_login(username, password):
    if (username == 'admin' or username == 'ADMIN') and password == '12345':
        return 'Access granted'
    
    return 'Access denied'


def hows_the_weather(temperature):
    if temperature < 40:
        response = 'brisk'
        return f"It's {response} out there!"

    elif temperature >= 50 and temperature <= 65:
        response ='a little chilly'
        return f"It's {response} out there!"
    elif temperature > 85:
        response = 'too dang hot'
        return f"It's {response} out there!"
    else:
        response = 'perfect'
        return f"It's {response} out there!"


def fizzbuzz(num):
    if num == 0 or num == 15 or num == 45:
        return 'FizzBuzz'
    elif num == 3 or num == 33 or num == 42:
        return 'Fizz'
    elif num == 5 or num == 10 or num == 50:
        return 'Buzz'
    elif num == 2 or num ==13 or num == 59:
        return num


def calculator(operation, num1, num2):
    if operation == '+':
        return num1 + num2 
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        print('Invalid operation!')
        return None


def control_flow(value):
    if value:
        # if the value is truthy
        print("yep!")
    else:
        # if the value is falsy
        print("nope!")
control_flow(())


age = 4

is_baby = 'baby' if age < 2 else 'not a baby'
print(is_baby)

def divide(num1, num2):
    try:
        quotient = num1 / num2
        print(quotient)
    except ZeroDivisionError:
        print("Error: num2 cannot be equal to 0")
    except TypeError:
        print("Error: input must be of type int or float")
    finally:
        print("Isn't division fun?")
divide(6, 2)

dog = ""

dict_map = {
    "hungry": "Refilling food bowl.",
    "thirsty": "Refilling water bowl.",
    "playful": "Playing tug-of-war.",
    "cuddly": "Snuggling.",
}

# Remember that a dictionary's .get() method lets us set a default value!
owner = dict_map.get(dog, "Reading newspaper.")
print(owner)