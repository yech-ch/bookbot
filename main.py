

def main():
    path = "books/frankenstein.txt"
    book = get_path_to_book(path)
    words = get_words(book)
    char_dict = get_characters(book)
    print_a_report(path, words, char_dict)




def get_path_to_book(path):

    with open(path) as f:
        file_contents = f.read()
        return file_contents
    


def get_words(text):

    words = text.split()
    return (len(words))



def get_characters(text):

    book = text.lower()
    joined_text = "".join(book.split()) #getting rid of spces
    chars_dict = {}

    for letter in joined_text:
        
        if letter in chars_dict:
            
            chars_dict[letter] += 1
        else:
            chars_dict[letter] = 1
    
    return chars_dict
        

def print_a_report(path, words, char_dict):

    dict_list = converting_dictionary(char_dict)

    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document")
    print("")

    for dict in dict_list:
        if dict['char'].isalpha():
            print(f"The '{dict['char']}' character was found {dict['num']} times")

    print("")
    print("--- End rport ---")


def converting_dictionary(char_dict):

    dict_list = [{'char': char, 'num':num} for char, num in char_dict.items()]
    dict_list.sort(reverse=True, key=sort_on)

    return dict_list



def sort_on(char_dict):
    return char_dict["num"]



main()
