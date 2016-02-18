from utils import *
from vocab import *
from enum import Enum
import math


class Dir(Enum):
    east = 0
    south = 1

class ItemType(Enum):
    data = 0
    function = 1
    operator = 2
    control = 3
    dummy = 4

class Item:
    "An item in the matrix"
    
    def __init__(self, type, content, filled=False):
        self.type = type
        self.content = content
        self.filled = filled
        self.value = None
        self.func = None
        self.l_arg = None
        self.r_arg = None

class Connection:
    "A connection to an item, possibly blocking some fields."
    
    def __init__(self, pos, has_value, has_func, has_args):
        self.pos = pos
        self.has_value = has_value
        self.has_func = has_func
        self.has_args = has_args

def find_item(items, max_x, max_y, x, y, direction):
    "Returns a Connection object."
    has_value = has_func = has_args = True
    while x <= max_x and y <= max_y:
        if (x,y) in items:
            item = items[(x,y)]
            if item.type == ItemType.data:
                return Connection((x,y), has_value, False, False)
            elif item.type == ItemType.function or item.type == ItemType.operator:
                return Connection((x,y), has_value, has_func, has_args)
            elif item.type == ItemType.control:
                char = item.content
                if char == 'B': # Block all
                    return Connection(None, False, False, False)
                elif char == 'V': # Block value
                    has_value = False
                elif char == 'F': # Block function
                    has_func = False
                elif char == 'A': # Block arguments
                    has_args = False
                elif char == 'X': # Switch direction
                    if direction == Dir.east:
                        direction = Dir.south
                    else:
                        direction = Dir.east
                elif char == 'S': # Turn south
                    direction = Dir.south
                elif char == 'E': # Turn east
                    direction = Dir.east
        if direction == Dir.east:
            x += 1
        else:
            y += 1
    return Connection(None, False, False, False)

def parse(matrix):
    "Parse a code matrix into a graph of items."
    items = {}
    digits = "0123456789"
    control_chars = "BVFAESX"
    for y in range(len(matrix)):
        # Parse a row
        x = 0
        while x < len(matrix[y]):
            char = matrix[y][x]
            if char == "'":
                # Parse a character
                if x == len(matrix[y]) - 1:
                    parsed_char = '\n'
                else:
                    parsed_char = matrix[y][x+1]
                item = Item(ItemType.data, to_char_atom(parsed_char))
                items[(x,y)] = item
                x += 2
            elif char == '"':
                # Parse a string
                i = x + 1
                chars = []
                while i < len(matrix[y]) and matrix[y][i] != '"':
                    parsed_char = matrix[y][i]
                    if parsed_char == '\\':
                        if i == len(matrix[y]) - 1:
                            parsed_char = '\n'
                        else:
                            parsed_char = matrix[y][i+1]
                            if parsed_char == 'n':
                                parsed_char = '\n'
                        i += 2
                    else:
                        i += 1
                    chars.append(parsed_char)
                item = Item(ItemType.data, [to_char_atom(c) for c in chars])
                items[(x,y)] = item
                x = i + 1
            elif char in digits:
                # Parse a number
                num = ""
                i = x
                while i < len(matrix[y]) and matrix[y][i] in digits:
                    num += matrix[y][i]
                    i += 1
                item = Item(ItemType.data, to_num_atom(int(num)))
                items[(x,y)] = item
                x = i
            elif char == 'i':
                # Parse input
                input_value = parse_value(input())[0]
                item = Item(ItemType.data, input_value)
                items[(x,y)] = item
                x += 1
            elif char == 'I':
                # Parse raw string input
                input_string = input()
                input_value = [to_char_value(char) for char in input_string]
                item = Item(ItemType.data, input_value)
                items[(x,y)] = item
                x += 1
            elif char in func_defs:
                # Parse a function
                item = Item(ItemType.function, func_defs[char])
                items[(x,y)] = item
                x += 1
            elif char in oper_defs:
                # Parse a operator
                item = Item(ItemType.operator, oper_defs[char])
                items[(x,y)] = item
                x += 1
            elif char in control_chars:
                # Parse a control character
                item = Item(ItemType.control, char)
                items[(x,y)] = item
                x += 1
            else:
                x += 1
    triples = {}
    max_x = max(len(row) for row in matrix)
    max_y = len(matrix)
    for ((x, y), item) in items.items():
            l_conn = find_item(items, max_x, max_y, x, y+1, Dir.south)
            r_conn = find_item(items, max_x, max_y, x+1, y, Dir.east)
            triples[(x,y)] = (item, l_conn, r_conn)
    triples[None] = (Item(ItemType.dummy, "Dummy"), None, None)
    return triples

def fill(items, pos=(0,0), level=0):
    "Fill in the fields of the given items."
    item, l_conn, r_conn = items[pos]
    if item.filled or item.type == ItemType.dummy:
        return item
    if item.type == ItemType.data:
        item.value = item.content
    else:
        l_nbor = fill(items, l_conn.pos, level+1)
        r_nbor = fill(items, r_conn.pos, level+1)
        if item.type == ItemType.function:
            item.func = item.content
            item.l_arg = l_nbor.value if l_conn.has_value else None
            item.r_arg = r_nbor.value if r_conn.has_value else None
            item.value = item.func(item.l_arg, item.r_arg)
        elif item.type == ItemType.operator:
            oper = item.content
            if l_conn.has_func and l_nbor.func is not None:
                l_input = l_nbor.func
            else:
                l_input = l_nbor.value if l_conn.has_value else None
            if r_conn.has_func and r_nbor.func is not None:
                r_input = r_nbor.func
            else:
                r_input = r_nbor.value if r_conn.has_value else None
            item.func = oper(l_input, r_input)
            r_l_arg = r_nbor.l_arg if r_conn.has_args else None
            r_r_arg = r_nbor.r_arg if r_conn.has_args else None
            if r_l_arg is None and r_r_arg is None:
                item.l_arg = l_nbor.l_arg if l_conn.has_args else None
                item.r_arg = l_nbor.r_arg if l_conn.has_args else None
            else:
                item.l_arg, item.r_arg = r_l_arg, r_r_arg
            item.value = item.func(item.l_arg, item.r_arg)
    return item

def interpret(matrix):
    "Interpret a program, returning the top left value."
    items = parse(matrix)
    corner = fill(items)
    return corner.value

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
    if string[0] in '-.' + digits:
        j = 1
        while j < len(string) and string[j] in '.e' + digits:
            j += 1
        return to_num_atom(eval(string[:j])), string[j:]
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
