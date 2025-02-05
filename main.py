def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char = get_num_char(text)
    book_report = get_book_report(num_char)
    srt_book_report = dict(sorted(book_report.items(), key=lambda item: item[1], reverse=True))
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words were found in the document")
    print("")
    for key,value in srt_book_report.items():
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")

def get_num_char(text):
     lowered_string = text.lower()
     dictionary = {}
     for char in lowered_string:
         if char in dictionary:
             dictionary[char] += 1
         else:
             dictionary[char] = 1
     return dictionary
 
def get_book_report(dict_object):
    is_alpha_char = {}
    for char in dict_object:
        if char.isalpha():
            is_alpha_char[char] = dict_object[char]
    return is_alpha_char

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()