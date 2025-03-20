

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents



def get_character_count(text):
    characters = {}
    
    for doots in text:
        doots_lower = doots.lower()
        if doots_lower in  characters:
            characters[doots_lower] +=1
        else:
             characters[doots_lower] = 1 
    return(characters)

def sort_on(dict):
    return dict["count"]

def return_list(text):
    unsorted_list = []
    dict1 = get_character_count(text)
    for keys in dict1:
        if keys.isalpha():
            holding_bin = {}
            holding_bin["key"] = keys
            holding_bin["count"] = (dict1[keys])
            unsorted_list.append(holding_bin)
    
        unsorted_list.sort(reverse=True, key=sort_on)
    return unsorted_list




def get_word_count(text):
    
    counter = 0
    words = text.split()
    for word in words:
        counter += 1 
    return (f'Found {counter} total words')





