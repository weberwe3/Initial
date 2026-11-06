"""
Module 03 exercises: Decisions.   Run:  python check.py 3
"""


def grade(score):
    # TODO: 90+ -> "A", 80-89 -> "B", 70-79 -> "C", 60-69 -> "D", below 60 -> "F"
    raise NotImplementedError


def fizzbuzz_word(n):
    # TODO: return "FizzBuzz" if n divides by 3 AND 5, "Fizz" if by 3,
    # "Buzz" if by 5, otherwise the number as a string.
    # fizzbuzz_word(15) -> "FizzBuzz", fizzbuzz_word(7) -> "7"
    raise NotImplementedError


def can_vote(age, is_citizen):
    # TODO: True only if age is 18 or over AND is_citizen is True.
    raise NotImplementedError


def is_weekend(day):
    # TODO: True if day is "saturday" or "sunday", in ANY case ("Sunday", "SUNDAY").
    raise NotImplementedError


def shipping_cost(total, country):
    # TODO: rules:
    #   country "US": free if total >= 50, otherwise 5.99
    #   country "CA" or "MX": 12.0
    #   anything else: 25.0
    raise NotImplementedError


def bmi_category(weight_kg, height_m):
    # TODO: BMI = weight / height squared.
    # below 18.5 -> "underweight", below 25 -> "normal",
    # below 30 -> "overweight", otherwise "obese"
    raise NotImplementedError


def is_leap_year(year):
    # TODO: A year is a leap year if divisible by 4,
    # EXCEPT years divisible by 100, which are NOT,
    # EXCEPT years divisible by 400, which ARE.
    # 2024 -> True, 1900 -> False, 2000 -> True, 2023 -> False
    raise NotImplementedError


def password_strength(password):
    # TODO: return "weak" if shorter than 8 characters,
    # "medium" if 8+ characters but it is all letters or all digits,
    # otherwise "strong".
    # Hint: str.isalpha() and str.isdigit()
    raise NotImplementedError
