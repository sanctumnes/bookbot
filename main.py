import os

def count_words(book_content):
    words = book_content.split(' ')
    return len(words)

def count_letters(book_content):
    book_content = book_content.lower()
    characters_dict = {}
    
    for ch in book_content:
        if not str(ch) in characters_dict:
            characters_dict[str(ch)] = 1
        else:
            characters_dict[str(ch)] = characters_dict[str(ch)] + 1
    
    return characters_dict

def printBookReport(book_name, number_of_words, characters_dict):
    print(f"~~~ Beginning of {book_name} Book Report ~~~\n")
    print(f"There is <{number_of_words}> Words in This Book\n")
    print("Listing Letters\' Frequencies Below:")

    alphabet_count_list = list(characters_dict.items())
    list_index = 0
    while list_index < len(alphabet_count_list):
        current_key = str(alphabet_count_list[list_index][0])
        if not current_key.isalpha():
            del alphabet_count_list[list_index]
            continue
        list_index += 1

    alphabet_count_list.sort(key=lambda x : x[1], reverse=True)
    
    for i in range(len(alphabet_count_list)):
        current_letter_item = alphabet_count_list[i]
        print(f"\tLetter <{current_letter_item[0]}> Appeared <{current_letter_item[1]}> Times")

    print(f"\n~~~ Ending of {book_name} Book Report ~~~\n")
    print("\n\n") 


######## Main Script ########

for filename in os.listdir(os.getcwd()+'/books'):
    with open(os.path.join(os.getcwd()+'/books', filename), 'r') as f:
        book_name = filename.split('.')[0]
        book_content = f.read()
        number_of_words = count_words(book_content)
        characters_dict = count_letters(book_content)
        printBookReport(book_name, number_of_words, characters_dict)
        
         