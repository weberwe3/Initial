"""Project 1A reference solution: number-guessing game (with replay + best score)."""

import random


def play_round(low=1, high=100):
    secret = random.randint(low, high)
    guesses = 0
    print(f"\nI'm thinking of a number between {low} and {high}.")
    while True:
        text = input("Your guess: ").strip()
        if not text.isdigit():
            print("Please type a whole number.")
            continue
        guess = int(text)
        guesses += 1
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"🎉 Got it in {guesses} guesses!")
            return guesses


def main():
    best = None
    while True:
        score = play_round()
        if best is None or score < best:
            best = score
            print("New best score!")
        print(f"Best so far: {best} guesses")
        if input("Play again? (y/n) ").strip().lower() != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
