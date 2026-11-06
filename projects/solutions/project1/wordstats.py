"""Project 1C reference solution: word statistics."""


def clean_words(text):
    kept = ""
    for ch in text.lower():
        if ch.isalpha() or ch == " " or ch == "'":
            kept += ch
        else:
            kept += " "
    return kept.split()


def main():
    text = input("Paste a paragraph:\n")
    words = clean_words(text)
    if not words:
        print("No words found!")
        return

    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1

    # sort the (word, count) pairs by count, biggest first
    ranked = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)

    longest = ""
    total_letters = 0
    for w in words:
        total_letters += len(w)
        if len(w) > len(longest):
            longest = w

    print(f"\nWords: {len(words)}   Characters: {len(text)}")
    print(f"Longest word: {longest}")
    print(f"Average word length: {total_letters / len(words):.1f}")
    print("Most common words:")
    for word, count in ranked[:5]:
        print(f"  {word:<15} {count}")


if __name__ == "__main__":
    main()
