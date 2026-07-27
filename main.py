def get_book_text(filepath: str) -> str:
    with open(filepath) as file:
        data = file.read()
    return data

def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    print(book_text)

main()