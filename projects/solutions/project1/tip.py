"""Project 1B reference solution: bill splitter & tip calculator."""


def ask_positive_number(prompt, allow_zero=False):
    while True:
        try:
            value = float(input(prompt).replace("$", "").strip())
        except ValueError:
            print("That isn't a number - try again.")
            continue
        if value < 0 or (value == 0 and not allow_zero):
            print("Please enter a number above zero.")
            continue
        return value


def main():
    bill = ask_positive_number("Bill total: $")
    tip_percent = ask_positive_number("Tip percentage (15/18/20 or custom): ", allow_zero=True)
    while True:
        people = ask_positive_number("How many people? ")
        if people == int(people):
            people = int(people)
            break
        print("People come in whole numbers!")

    tip = bill * tip_percent / 100
    total = bill + tip
    print()
    print(f"{'Subtotal:':<18}${bill:>9.2f}")
    print(f"{f'Tip ({tip_percent:g}%):':<18}${tip:>9.2f}")
    print(f"{'Total:':<18}${total:>9.2f}")
    print(f"{'Each person pays:':<18}${total / people:>9.2f}")


if __name__ == "__main__":
    main()
