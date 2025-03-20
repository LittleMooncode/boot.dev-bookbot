import sys
from stats import get_book_text, get_word_count, return_list

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]
book_text = get_book_text(book_path)

def print_function(list2):
    for i in list2:        
        print(f"{i['key']}: {i['count']}")
    return

print(f'''============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
{get_word_count(book_text)}
--------- Character Count -------''')
print_function(return_list(book_text))
print('''
============= END ===============''')

