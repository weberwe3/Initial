def test_sum_up_to(ex):
    assert ex.sum_up_to(4) == 10
    assert ex.sum_up_to(100) == 5050
    assert ex.sum_up_to(0) == 0


def test_factorial(ex):
    assert ex.factorial(5) == 120
    assert ex.factorial(0) == 1, "factorial(0) is 1 by definition - start your accumulator at 1"
    assert ex.factorial(1) == 1


def test_count_vowels(ex):
    assert ex.count_vowels("Hello World") == 3
    assert ex.count_vowels("AEIOU aeiou") == 10
    assert ex.count_vowels("rhythm") == 0


def test_reverse_string(ex):
    assert ex.reverse_string("hello") == "olleh"
    assert ex.reverse_string("") == ""


def test_fizzbuzz(ex):
    assert ex.fizzbuzz(5) == "1 2 Fizz 4 Buzz", f"got {ex.fizzbuzz(5)!r}"
    assert ex.fizzbuzz(15).split()[-1] == "FizzBuzz"


def test_years_to_double(ex):
    assert ex.years_to_double(0.10) == 8
    assert ex.years_to_double(1.0) == 1


def test_digit_sum(ex):
    assert ex.digit_sum(1234) == 10
    assert ex.digit_sum(0) == 0
    assert ex.digit_sum(9999) == 36


def test_is_prime(ex):
    primes = [2, 3, 5, 7, 11, 13, 97]
    not_primes = [0, 1, 4, 9, 15, 100]
    for p in primes:
        assert ex.is_prime(p) is True, f"{p} is prime"
    for n in not_primes:
        assert ex.is_prime(n) is False, f"{n} is not prime"


def test_times_table(ex):
    got = ex.times_table(3)
    lines = got.split("\n")
    assert len(lines) == 10, f"expected 10 lines, got {len(lines)}"
    assert lines[0] == "1 x 3 = 3", f"first line was {lines[0]!r}"
    assert lines[-1] == "10 x 3 = 30", f"last line was {lines[-1]!r}"
