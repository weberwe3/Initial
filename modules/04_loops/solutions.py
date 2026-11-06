"""Module 04 solutions."""


def sum_up_to(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count


def reverse_string(text):
    result = ""
    for ch in text:
        result = ch + result   # put each new character at the FRONT
    return result


def fizzbuzz(n):
    words = ""
    for i in range(1, n + 1):
        if i % 15 == 0:
            word = "FizzBuzz"
        elif i % 3 == 0:
            word = "Fizz"
        elif i % 5 == 0:
            word = "Buzz"
        else:
            word = str(i)
        words += word + " "
    return words.strip()


def years_to_double(rate):
    value = 1.0
    years = 0
    while value < 2.0:
        value *= 1 + rate
        years += 1
    return years


def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10   # last digit
        n //= 10          # drop the last digit
    return total


def is_prime(n):
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True


def times_table(n):
    text = ""
    for i in range(1, 11):
        text += f"{i} x {n} = {i * n}\n"
    return text.rstrip("\n")
