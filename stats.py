def word_count(text: str) -> int:
    words = text.split()
    return len(words)

def char_count(text: str) -> dict[str, int]:
    char_totals = {}
    chars = list(text.lower())

    for c in chars:
        if c not in char_totals:
            char_totals[c] = 1
        else:
            char_totals[c] += 1

    return char_totals