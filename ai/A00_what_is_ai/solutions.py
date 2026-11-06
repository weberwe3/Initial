"""Module A00 solutions."""

import math


def estimate_tokens(text):
    return math.ceil(len(text) / 4)


def words_to_tokens(word_count):
    return math.ceil(word_count / 0.75)


def fits_in_context(texts, context_limit, reserve_for_answer=1000):
    total = sum(estimate_tokens(t) for t in texts)
    return total + reserve_for_answer <= context_limit


def request_cost(input_tokens, output_tokens, input_price_per_million, output_price_per_million):
    cost = input_tokens / 1_000_000 * input_price_per_million + output_tokens / 1_000_000 * output_price_per_million
    return round(cost, 6)


def monthly_cost(requests_per_day, input_tokens, output_tokens,
                 input_price_per_million, output_price_per_million, working_days=22):
    one = request_cost(input_tokens, output_tokens, input_price_per_million, output_price_per_million)
    return round(one * requests_per_day * working_days, 2)


def cheapest_option(options, input_tokens, output_tokens):
    return min(options, key=lambda name: request_cost(input_tokens, output_tokens, *options[name]))
