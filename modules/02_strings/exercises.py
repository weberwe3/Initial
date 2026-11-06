"""
Module 02 exercises: Strings.   Run:  python check.py 2
"""


def greet(name):
    # TODO: return "Hello, <name>!"   greet("Ada") -> "Hello, Ada!"
    raise NotImplementedError


def format_price(amount):
    # TODO: return the amount as money with 2 decimals and a $ sign,
    # with thousands separators.  format_price(1234.5) -> "$1,234.50"
    raise NotImplementedError


def initials(full_name):
    # TODO: full_name is "first last" in any case. Return the initials
    # in uppercase with dots.  initials("ada lovelace") -> "A.L."
    raise NotImplementedError


def clean_email(raw):
    # TODO: remove surrounding whitespace and make it lowercase.
    # clean_email("  Bob@Mail.COM ") -> "bob@mail.com"
    raise NotImplementedError


def email_domain(email):
    # TODO: return the part after the "@".  email_domain("a@b.com") -> "b.com"
    raise NotImplementedError


def is_palindrome(word):
    # TODO: return True if the word reads the same backwards, ignoring case.
    # is_palindrome("Level") -> True ; is_palindrome("Python") -> False
    raise NotImplementedError


def file_extension(filename):
    # TODO: return the extension without the dot, lowercase.
    # file_extension("Report.Final.PDF") -> "pdf"
    # Hint: split on "." and take the LAST piece (index -1).
    raise NotImplementedError


def mask_card(card_number):
    # TODO: card_number is a string of digits. Replace all but the last 4
    # with "*".  mask_card("1234567812345678") -> "************5678"
    raise NotImplementedError


def snake_case(phrase):
    # TODO: turn "Monthly Rent Total" into "monthly_rent_total".
    # Extra spaces should not create extra underscores:
    # snake_case("  Hello   World ") -> "hello_world"
    raise NotImplementedError
