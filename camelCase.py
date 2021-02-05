"""This program takes any sentence and converts it to camel case, with first word being lowercase
and first letter of subsequent words capitalized"""
import re


def remove_space(sentence):
    remove_more_than_one_space = re.sub(r'\s+', ' ', sentence)  # replace any groups of whitespace with a single space
    remove_remaining_spaces = remove_more_than_one_space.strip()  # remove any remaining leading or trailing whitespace
    return remove_remaining_spaces


def capitalize_first_letters(word_list):
    first_letters_capital = []  # empty list

    for word in word_list:  # loops through each word in word_list
        first_letters_capital.append(word.title())  # creates new list with first letter of each word capitalized
    list_to_single_string = ''.join(first_letters_capital)  # converts list of strings into single string and removes
    # white space - https://stackoverflow.com/questions/36094979/convert-a-list-of-strings-into-one-string
    return list_to_single_string


def camelcase(sentence):
    no_spaces = remove_space(sentence)

    word_list = no_spaces.split(' ')  # turns sentence into list of words
    list_to_single_string = capitalize_first_letters(word_list)

    camel_case_sentence = list_to_single_string[0].lower() + list_to_single_string[1:]  # capitalizes first letter of
    # string - https://www.geeksforgeeks.org/python-lowercase-first-character-of-string/)

    return camel_case_sentence


def main():
    sentence = input('Enter a sentence to convert to camelCase: ')
    output = camelcase(sentence)  # stores camelCase sentence in variable
    print(output)


if __name__ == '__main__':
    # true if running from command prompt
    main()

# false if this file is imported from another file
