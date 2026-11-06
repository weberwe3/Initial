"""Module 01 solutions. Try the exercises first!"""


def add_tax(price):
    return price * 1.2


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def minutes_to_hours_and_minutes(total_minutes):
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return hours, minutes


def is_even(n):
    return n % 2 == 0


def split_bill(total, people):
    return round(total / people, 2)


def text_to_number_sum(a, b):
    return int(a) + int(b)


def average_of_three(a, b, c):
    # Parentheses matter: without them only c would be divided by 3.
    return (a + b + c) / 3
