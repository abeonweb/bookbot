from stats import get_word_count, get_characters_count,sorted_characters
import sys
def get_book_text(file_path):
    contents = ""
    with open(file_path) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_count = get_characters_count(text)
    sorted_chars = sorted_characters(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(word_count)
    print("--------- Character Count -------")
    for i in range(0, len(sorted_chars)):
        if sorted_chars[i]["char"].isalpha():
            print(f"{sorted_chars[i]['char']}: {sorted_chars[i]['num']}")
    print("============= END ===============")


main()