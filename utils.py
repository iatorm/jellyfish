from itertools import cycle
from enum import Enum

class AtomType(Enum):
    num = 0
    char = 1

class Atom:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __int__(self):
        return int(self.value)

def to_num_atom(d):
    return Atom(AtomType.num, d)

def to_char_atom(c):
    return Atom(AtomType.char, abs(int(ord(c))))

def is_value(item):
    return not callable(item)

def is_atom(value):
    return isinstance(value, Atom)

def shape(value):
    if is_atom(value):
        return []
    else:
        shapes = zip(*[shape(item) for item in value])
        return [len(value)] + [min(x) for x in shapes]

def flatten(value):
    if is_atom(value):
        return [value]
    return [subitem for item in value for subitem in flatten(item)]

def grid(iterator, shape):
    if shape:
        return [grid(iterator, shape[1:]) for i in range(int(shape[0]))]
    return next(iterator)

def reshape(value, shape):
    iterator = cycle(flatten(value))
    return grid(iterator, shape)

def rank(value):
    return len(shape(value))

def height(value):
    if is_atom(value):
        return 0
    if value:
        return 1 + max(height(item) for item in value)
    return 1

def incneg(n):
    return n + (n<0)

def thread_binary(f, height1, height2):
    def threaded_f(a, b, lev1=height1, lev2=height2):
        height_a, height_b = height(a), height(b)
        if height_a <= max(0, lev1) or lev1 == -1:
            if height_b <= max(0, lev2) or lev2 == -1:
                return f(a, b)
            else:
                return [threaded_f(a, y, -1, incneg(lev2))
                        for y in b]
        elif height_b <= max(0, lev2) or lev2 == -1:
            return [threaded_f(x, b, incneg(lev1), -1)
                    for x in a]
        else:
            return [threaded_f(x, y, incneg(lev1), incneg(lev2))
                    for (x, y) in zip(a,b)]
    return threaded_f

def thread_unary(f, height):
    return lambda a: thread_binary(lambda x, y: f(x), height, -1)(a, None)
