def test_greet(ex):
    assert ex.greet("Ada") == "Hello, Ada!", f"got {ex.greet('Ada')!r}"


def test_format_price(ex):
    assert ex.format_price(1234.5) == "$1,234.50", f"got {ex.format_price(1234.5)!r}"
    assert ex.format_price(3) == "$3.00", f"got {ex.format_price(3)!r}"


def test_initials(ex):
    assert ex.initials("ada lovelace") == "A.L.", f"got {ex.initials('ada lovelace')!r}"
    assert ex.initials("Grace Hopper") == "G.H."


def test_clean_email(ex):
    assert ex.clean_email("  Bob@Mail.COM ") == "bob@mail.com"


def test_email_domain(ex):
    assert ex.email_domain("a@b.com") == "b.com"
    assert ex.email_domain("someone@company.co.uk") == "company.co.uk"


def test_is_palindrome(ex):
    assert ex.is_palindrome("Level") is True, "'Level' is a palindrome (ignore case)"
    assert ex.is_palindrome("Python") is False
    assert ex.is_palindrome("racecar") is True


def test_file_extension(ex):
    assert ex.file_extension("Report.Final.PDF") == "pdf"
    assert ex.file_extension("photo.jpg") == "jpg"


def test_mask_card(ex):
    assert ex.mask_card("1234567812345678") == "************5678"
    assert ex.mask_card("98765") == "*8765"


def test_snake_case(ex):
    assert ex.snake_case("Monthly Rent Total") == "monthly_rent_total"
    assert ex.snake_case("  Hello   World ") == "hello_world", "extra spaces shouldn't make extra underscores - try split()"
