from stats import word_count

def get_book_text(filepath: str) -> str:
    with open(filepath) as file:
        data = file.read()
    return data

def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    print(f"Found {word_count(book_text)} total words")

main()