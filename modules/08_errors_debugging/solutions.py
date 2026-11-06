"""Module 08 solutions."""


def safe_int(text, default=0):
    try:
        return int(text)
    except ValueError:
        return default


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


def get_setting(settings, key, default=None):
    try:
        return settings[key]
    except KeyError:
        return default


def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if amount > balance:
        raise ValueError(f"Insufficient funds: balance is {balance}")
    return balance - amount


def parse_age(text):
    age = int(text)          # raises ValueError by itself for non-numbers
    if not 0 <= age <= 130:
        raise ValueError(f"Age out of range: {age}")
    return age


def sum_valid_numbers(items):
    total = 0
    for item in items:
        try:
            total += float(item)
        except ValueError:
            continue
    return total


def buggy_total(numbers):
    total = 0
    for n in numbers:
        total += n
    return total            # fixed: return after the loop, not inside it


def buggy_count_to(n):
    result = []
    for i in range(1, n + 1):   # fixed: range stops before its end value
        result.append(i)
    return result


def buggy_shout(text):
    text = text.strip()      # fixed: store the new string
    return text.upper()


def buggy_largest(numbers):
    largest = numbers[0]     # fixed: start from a real value, not 0
    for n in numbers:
        if n > largest:
            largest = n
    return largest


def buggy_describe(name, age):
    return name + " is " + str(age) + " years old"   # or an f-string
