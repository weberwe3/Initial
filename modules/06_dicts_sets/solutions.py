"""Module 06 solutions."""


def word_counts(text):
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def most_common_word(text):
    counts = {}
    best_word, best_count = None, 0
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
        if counts[word] > best_count:
            best_word, best_count = word, counts[word]
    return best_word


def totals_by_category(transactions):
    totals = {}
    for category, amount in transactions:
        totals[category] = totals.get(category, 0) + amount
    return totals


def invert(d):
    result = {}
    for key, value in d.items():
        result[value] = key
    return result


def lookup_price(prices, item):
    return prices.get(item, 0)


def cart_total(prices, cart):
    total = 0
    for item, qty in cart.items():
        total += prices.get(item, 0) * qty
    return round(total, 2)


def names_in_dept(people, dept):
    names = []
    for p in people:
        if p["dept"] == dept:
            names.append(p["name"])
    return names


def average_salary_by_dept(people):
    totals, counts = {}, {}
    for p in people:
        d = p["dept"]
        totals[d] = totals.get(d, 0) + p["salary"]
        counts[d] = counts.get(d, 0) + 1
    averages = {}
    for d in totals:
        averages[d] = totals[d] / counts[d]
    return averages


def unique_count(items):
    return len(set(items))


def missing_skills(my_skills, job_skills):
    return sorted(set(job_skills) - set(my_skills))


def group_by_first_letter(words):
    groups = {}
    for w in words:
        letter = w[0].lower()
        if letter not in groups:
            groups[letter] = []
        groups[letter].append(w)
    return groups
