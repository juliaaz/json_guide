"""
Module organises a navigation(guide) in a json file.
"""

import json
import pprint
import sys
from os import path

def check_format():
    """
    Checks whether user's file is a json file.
    >>> check_format(1)

    """
    while True:
        user_path = input('Input the path to the file you would like to discover: ')
        if isinstance(user_path, str):
            if path.exists(user_path):
                path_splitted = user_path.split('.')
                if path_splitted[1] == 'json':
                    return user_path
                else:
                    print("---------------------------------------------------------------------")
                    print("Can't navigate you. Wrong file's extension. Needs to be a json file ")
                    print("---------------------------------------------------------------------")
            else:
                print("---------------------------------------------------")
                print('I can not find this file! Try giving a correct path')
                print("---------------------------------------------------")
        else:
            print("------------------------------")
            print('Your input has to be a string!')
            print("------------------------------")

def read_file(user_path):
    """
    Reads a json file and converts it into a dictionary.
    """
    with open(user_path, 'r') as file:
        data = json.load(file)
    return data

def guide(data):
    """
    Navigates(guides) a user throught the json file (dictionary format).
    """
    if isinstance(data, dict):
        while True:
            print()
            print('Currently you can choose a key from given below')
            print()
            print('Possible keys:')
            print("---------------------------------------")
            for key in data:
                print(key)
            print("---------------------------------------")
            print('You also have several options:')
            print()
            print("Type exit if you would like to end the program's work")
            print()
            print("Type print if you want to print current element")
            print()
            print("Type parent if you want to return to a parent element")
            print()

            new_level = input('Your option: ')
            if new_level == 'exit':
                sys.exit()
            if new_level == 'print':
                pprint.pprint(data)
            if new_level == 'parent':
                return 'parent'
            if new_level in data.keys():
                return guide(data[new_level])
            else:
                print("---------------------------------------")
                print("Program can't find this category.")
                print("---------------------------------------")
                new_level = input('Please type the correct one: ')

    elif isinstance(data, list):
        while True:
            print()
            print('Currently you can choose one element from the list. Input\
 a number from 0 to', len(data)-1, 'to choose an element.')
            print('You also have several options:')
            print()
            print("Type exit if you would like to end the program's work")
            print()
            print("Type print if you want to print current element")
            print()
            print("Type parent if you want to return to a parent element")
            print()
            for digit, option in enumerate(data):
                print(digit, '-', option)
            new_level = input('Your option: ')
            if new_level == 'exit':
                sys.exit()
            if new_level == 'print':
                pprint.pprint(data)
            if new_level == 'parent':
                return 'parent'
            if new_level in [str(digit) for digit in range(len(data))] :
                return guide(data[int(digit)])
            else:
                print("---------------------------------------")
                print("Program can't find this category.")
                print("---------------------------------------")
                new_level = input('Please type the correct one: ')
                
    else:
        print(f'Here is your data: {data}\n')
        print('You reached the bottom of your file\n')


if __name__ == "__main__":
    print('Now we are ready to navigate you through json!')
    file_path = check_format()
    json_file = read_file(file_path)
    if json_file:
        json_guide = json_file
        while True:
            if guide(json_file) == 'parent':
                print('You have reached the document root already. Choose something else.')
            guide_file = guide(json_file)
            if isinstance(guide_file, bool):
                break