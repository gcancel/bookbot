#Wrapping the read logic into a function

def main():
    try:
        with open('./books/frankenstein.txt', 'r') as f:
            data = f.read()
            print(data)
        return data
    except FileNotFoundError as e:
        print(e, "Sorry there seems to be an issue with this file...")

def count_words():
    with open('./books/frankenstein.txt', 'r') as f:
        data = f.read()
        words = data.split()
        return len(words)

def count_letters():

    try:
        with open('./books/frankenstein.txt', 'r') as f:
            letters = {}
            data = f.read()
            for c in data:
                new_data = c.lower()
                if new_data in letters:
                    letters[new_data] += 1
                else:
                    letters[new_data] = 1
            return letters
    except Exception as e:
        print(e, "oopsies!!")

report_data = count_letters()
def sort_on(report_data):
    return report_data["num"]

def dict_to_list_sorted(r):
    sorted = []
    for c in r:
        sorted.append({"char": c, "num": r[c]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted

def report(r):
    for letter in r:
        c = r[letter]
        print(f'The {letter} character was found {c} times')
    print('--- End report ---')






#Run the main function
#main()
print(count_words())
print(count_letters())
""" report(report_data) """
print(dict_to_list_sorted(report_data))