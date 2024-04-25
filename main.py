#Bookbot App
#Functionality: word Count, letter count, sorted character count report

#Main function
def main():
    #declaring our variables for use:
    book_file = './books/frankenstein.txt'
    book = get_text(book_file)
    word_count = num_words(book)
    total_letters = count_char(book)
    sorted_letter_list = sorted_dic_letters(total_letters)

    #printing outputs
    #word count
    print(f'--- Printing Outputs ---\n Total amount of words in book: {word_count}')

    #letter count
    print('Now counting letters in the book.')
    print(f'Data: {total_letters}')
    print('Sorting data to make it more presentable...')
    print('--- Printing Report ---')

    #now for the sorted report
    for item in sorted_letter_list:
        #isaplha is used to return only alphabet letters
        if not item["letter"].isalpha():
            continue
        print(f'The {item["letter"]} character was found {item["num"]} times!')

    print('--- Report Complete ---') 

#pulling text from file
def get_text(text):
    try:
        with open(text, 'r') as f:
            return f.read()
    except FileNotFoundError as e:
        print(e, "oopsies")

#getting total words
def num_words(b):
    words = b.split()
    return len(words)

#counting the characters
def count_char(b):
    letters = {}
    for letter in b:
        l_letter = letter.lower()
        if l_letter in letters:
            letters[l_letter] += 1
        else:
            letters[l_letter] = 1
    return letters

#function used with the sort method
def sort_on(d):
    return d["num"]

#cconverting the dictionary into a list
def sorted_dic_letters(d):
    n_list = []
    for item in d:
        n_list.append({"letter": item, "num": d[item]})
    n_list.sort(reverse=True, key=sort_on)
    return n_list

main()