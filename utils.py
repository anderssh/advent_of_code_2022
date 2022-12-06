import sys
import requests
import os.path


def inputfile_to_array(input_file, convert_to_int=False):
    with open(input_file) as f:
        lines = f.read().splitlines()
    lines_as_array = [(line) for line in lines]
    if convert_to_int:
        lines_as_array = [int(item) for item in lines_as_array]
    return lines_as_array


def get_input_file(day):

    cookie = {'session': '53616c7465645f5f07886ce5e3d010a41c0d5dd4dfbaca172cf72ddcdfd3b499ca8d98273ce56382c38330c8c3ca6b857adc15a83c6fbe1b4eaabef2f24640d6'}
    url = "https://adventofcode.com/2022/day/" + str(day) + "/input"
    filepath = 'inputs/input_day_' + str(day) + ".txt"
    if not os.path.isfile(filepath):
        r = requests.get(url, cookies = cookie)
        open(filepath, 'wb').write(r.content)

def remove_empty_lines_and_concat(list_with_empty_lines, space_separated = True):
    '''
    Takes in the list as read from the file, puts the lines that belong together in
    same list element.
    '''
    space_character = ''
    if space_separated:
        space_character = ' '
    element = ''
    line_list = []
    for i, item in enumerate(list_with_empty_lines):
        if item == "":
            line_list.append(element)
            element = ''
        else:
            if element == '':
                element = element + item
            else:
                element = element + space_character + item
            if i == len(list_with_empty_lines)-1:
                line_list.append(element)
    return line_list

def pretty_print_table(table):
    for i in table:
        print (i)
    print("\n")