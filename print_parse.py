from utils import *
import re

def prettyprint(value, quotes=True):
    "Convert a value into a human-readable string."
    if is_atom(value):
        if value.type == AtomType.num:
            return str(value.value)
        else:
            return "'"*quotes + chr(abs(int(value.value))) + "'"*quotes
    all_chars = all(atom.type == AtomType.char for atom in flatten(value))
    if all_chars and height(value) == 1:
        return '"' + ''.join(prettyprint(item, quotes=False) for item in value) + '"'
    else:
        return "[" + " ".join(prettyprint(item) for item in value) + "]"

def matrix_print(value):
    "Convert a value into a beautiful grid-style string."
    if is_atom(value):
        return prettyprint(value)
    level = height(value)
    flat = flatten(value)
    rows = flatten(value, 1)
    max_len = max(len(row) for row in rows)
    all_chars = all(atom.type == AtomType.char for atom in flat)
    pads = [1 + max(print_len(row[i], not all_chars) if i < len(row) else 0
                    for row in rows)
            for i in range(max_len)]
    if not all_chars:
        pads[0] -= 1
    return matrix_print_aux(value, level, pads, not all_chars)

def print_len(atom, quotes):
    if atom.type == AtomType.num:
        return len(str(atom.value))
    else:
        return 3*quotes

def matrix_print_aux(value, level, pads, quotes):
    if level == 1:
        string = ""
        for index, item in enumerate(value):
            if item.type == AtomType.num:
                string += str(item.value).rjust(pads[index])
            else:
                char = chr(abs(int(item.value)))
                string += ("'"*quotes + char + "'"*quotes).rjust(pads[index])
        return string
    else:
        item_strings = [matrix_print_aux(item, level-1, pads, quotes)
                        for item in value]
        return ("\n"*(level-1)).join(item_strings)
        
def parse_value(string):
    digits = "0123456789"
    string = string.lstrip()
    if string[0] in '-.e' + digits:
        neg = string[0] == '-'
        j = j0 = 1 if neg else 0
        while j < len(string) and string[j] in digits:
            j += 1
        if j < len(string) and string[j] == '.':
            dec = True
            j += 1
            while j < len(string) and string[j] in digits:
                j += 1
        else:
            dec = False
        j1 = j
        if j < len(string) and string[j] == 'e':
            exp = True
            j += 1
            neg_exp = j < len(string) and string[j] == '-'
            j = j2 = j+1 if neg_exp else j
            while j < len(string) and string[j] in digits:
                j += 1
            if j < len(string) and string[j] == '.':
                dec_exp = True
                j += 1
                while j < len(string) and string[j] in digits:
                    j += 1
            else:
                dec_exp = False
        else:
            exp = False
        multiplier = (-1 if neg else 1) * (float if dec else int)(string[j0:j1])
        if exp:
            exponent = (-1 if neg_exp else 1) * (float if dec_exp else int)(string[j2:j])
        else:
            exponent = 0
        return to_num_atom(multiplier * 10**exponent), string[j:]
    elif string[0] == "'":
        if string[1] == '\\' and string[3] == "'":
            char = string[2]
            if char == 'n':
                char == '\n'
            j = 4
        elif string[2] == "'":
            char = string[1]
            j = 3
        return to_char_atom(char), string[j:]
    elif string[0] == '"':
        parsed_string = ""
        j = 1
        while string[j] != '"':
            if string[j] == '\\':
                char = string[j+1]
                if char == 'n':
                    char = '\n'
                parsed_string += char
                j += 2
            else:
                parsed_string += string[j]
                j += 1
        return [to_char_atom(char) for char in parsed_string], string[j+1:]
    elif string[0] == '[':
        array = []
        string = string[1:].lstrip()
        while string[0] != ']':
            value, string = parse_value(string)
            array.append(value)
            string = string.lstrip()
        return array, string[1:]
