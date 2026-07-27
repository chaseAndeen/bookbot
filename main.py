def get_book_text(filepath: str) -> str:
    with open(filepath) as file:
        data = file.read()
    return data

def word_count(text: str) -> int:
    words = text.split()
    return len(words)

def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    print(f"Found {word_count(book_text)} total words")

main()