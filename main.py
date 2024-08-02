def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    num_words = get_num_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")

    chars_dict = get_chars_dict(text)
    
    sorted_char_list = dict_to_sorted_list(chars_dict)

    for item in sorted_char_list:
        char = item["character"]
        num = item["num"]
        # Ensure you only print letters
        if char.isalpha():
            print(f"The '{char}' character was found {num} times")

    print("--- End report ---")
def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def dict_to_sorted_list(chars_dict):
    # Convert dictionary to a list of dictionaries
    char_count_list = []
    for char, count in chars_dict.items():
        char_count_list.append({"character": char, "num": count})
    
    # Sort the list by the 'num' field using the built-in sorted function
    char_count_list = sorted(char_count_list, key=lambda x: x["num"], reverse=True)
    
    return char_count_list

if __name__ == "__main__":
    main()