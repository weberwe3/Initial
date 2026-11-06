"""
Module A00 exercises: Tokens, context and cost.   Run:  python check.py A0

You'll build the back-of-the-envelope calculator every AI ambassador gets asked
for: "How much text can it take?" and "What will this cost us?"
"""

import math


def estimate_tokens(text):
    # TODO: estimate tokens as len(text) / 4, rounded UP to a whole number.
    # estimate_tokens("abcdefghij") -> 3 ; estimate_tokens("") -> 0
    raise NotImplementedError


def words_to_tokens(word_count):
    # TODO: a token is about 0.75 of a word, so tokens = words / 0.75.
    # Round UP.  words_to_tokens(750) -> 1000
    raise NotImplementedError


def fits_in_context(texts, context_limit, reserve_for_answer=1000):
    # TODO: texts is a list of strings you want to send together.
    # Return True if the estimated tokens of ALL texts plus reserve_for_answer
    # is <= context_limit. Use estimate_tokens.
    raise NotImplementedError


def request_cost(input_tokens, output_tokens, input_price_per_million, output_price_per_million):
    # TODO: return the dollar cost of one request, rounded to 6 decimals.
    # Prices are per 1,000,000 tokens.
    # request_cost(1000, 500, 3.0, 15.0) -> 0.0105
    raise NotImplementedError


def monthly_cost(requests_per_day, input_tokens, output_tokens,
                 input_price_per_million, output_price_per_million, working_days=22):
    # TODO: cost of one request x requests_per_day x working_days, rounded to 2 decimals.
    # Reuse request_cost.
    raise NotImplementedError


def cheapest_option(options, input_tokens, output_tokens):
    # TODO: options is a dict {model_name: (input_price, output_price)}.
    # Return the NAME of the model with the lowest request_cost for this request.
    raise NotImplementedError
