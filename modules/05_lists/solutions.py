"""Module 05 solutions."""


def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def only_passing(scores, pass_mark=60):
    result = []
    for s in scores:
        if s >= pass_mark:
            result.append(s)
    return result


def add_tax_to_all(prices, rate):
    result = []
    for p in prices:
        result.append(round(p * (1 + rate), 2))
    return result


def second_largest(numbers):
    biggest = max(numbers)
    rest = []
    for n in numbers:
        if n != biggest:
            rest.append(n)
    return max(rest)


def remove_duplicates(items):
    seen = []
    for item in items:
        if item not in seen:
            seen.append(item)
    return seen


def total_expenses(expenses):
    total = 0
    for _category, amount in expenses:
        total += amount
    return total


def biggest_expense(expenses):
    best_name, best_amount = expenses[0]
    for name, amount in expenses:
        if amount > best_amount:
            best_name, best_amount = name, amount
    return best_name


def numbered_list(items):
    result = []
    for i, item in enumerate(items, start=1):
        result.append(f"{i}. {item}")
    return result


def chunk(items, size):
    result = []
    for start in range(0, len(items), size):
        result.append(items[start:start + size])
    return result


def column(grid, index):
    result = []
    for row in grid:
        result.append(row[index])
    return result
