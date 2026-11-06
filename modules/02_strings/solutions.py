"""Module 02 solutions."""


def greet(name):
    return f"Hello, {name}!"


def format_price(amount):
    return f"${amount:,.2f}"


def initials(full_name):
    first, last = full_name.split()
    return f"{first[0]}.{last[0]}.".upper()


def clean_email(raw):
    return raw.strip().lower()


def email_domain(email):
    return email.split("@")[1]


def is_palindrome(word):
    w = word.lower()
    return w == w[::-1]


def file_extension(filename):
    return filename.split(".")[-1].lower()


def mask_card(card_number):
    return "*" * (len(card_number) - 4) + card_number[-4:]


def snake_case(phrase):
    # split() with no argument handles any amount of whitespace.
    return "_".join(phrase.lower().split())
