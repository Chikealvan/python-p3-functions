#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}")

def greet_with_default(name="programmer"):
    greeting = f"Hello {name}"
    print(greeting)

def add(num1, num2):
    result = num1 + num2
    return result

def halve(number):
    if not isinstance(number, (int, float)):
        return None

    return number / 2
