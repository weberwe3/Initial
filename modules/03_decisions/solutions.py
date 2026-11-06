"""Module 03 solutions."""


def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def fizzbuzz_word(n):
    # Check the most specific case (both) first.
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    return str(n)


def can_vote(age, is_citizen):
    return age >= 18 and is_citizen


def is_weekend(day):
    return day.lower() in ("saturday", "sunday")


def shipping_cost(total, country):
    if country == "US":
        return 0 if total >= 50 else 5.99
    elif country in ("CA", "MX"):
        return 12.0
    return 25.0


def bmi_category(weight_kg, height_m):
    bmi = weight_kg / height_m ** 2
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    return "obese"


def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


def password_strength(password):
    if len(password) < 8:
        return "weak"
    if password.isalpha() or password.isdigit():
        return "medium"
    return "strong"
