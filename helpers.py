import itertools
import string


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return itertools.zip_longest(fillvalue=fillvalue, *args)


def all_caps(word):
    return all(letter in string.ascii_uppercase for letter in word)


def contains_no_number(element):
    return not any(char in string.digits for char in element)


def is_name(element):
    words = element.split(" ")
    return len(words) > 1 and all_caps(words[0]) and contains_no_number(element)


def parse_name(element) -> (str, str):
    last_name = ""
    first_name = ""
    name = element.split(" ")
    for part in name:
        if all_caps(part):
            last_name += part
            last_name += " "
        else:
            first_name += part
            first_name += " "
    last_name = last_name.strip().title()
    first_name = first_name.strip()
    return first_name, last_name


def is_fee(element):
    return len(element) == 2 and all(char in string.digits for char in element)


def is_postal_code(element):
    return len(element) == 4 and all(char in string.digits for char in element)

def is_phone_number(element):
    return len(element) > 6 and all(char in string.digits for char in element.replace(" ", ""))