from stats import count_words, get_chars_dict, get_sorted_list
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    count = count_words(text)
    chars_dict = get_chars_dict(text)
    sorted_list = get_sorted_list(chars_dict)

    # print output
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print(    "----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        print(f"{item['char']} : {item['num']}")
    print("============= END ===============")
    

def get_book_text(path):
    with open(path) as f:
        return f.read() 
    

main()
