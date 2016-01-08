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

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __repr__(self):
        if self.type == AtomType.num:
            return "<{}>".format(self.value)
        else:
            return "<'{}>".format(chr(abs(int(self.value))))

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

def flatten(value, max_height=0):
    if height(value) <= max_height:
        return [value]
    return [subitem for item in value for subitem in flatten(item, max_height)]

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

def bin_range(x):
    if not x:
        return [[]]
    elif height(x) == 1:
        lo, hi = map(lambda y: int(y.value), x)
        if lo <= hi:
            return [to_num_atom(y) for y in range(lo, hi)]
        else:
            return [to_num_atom(y) for y in reversed(range(hi, lo))]
    else:
        return [[y] + w
                for y in bin_range(x[0])
                for w in bin_range(x[1:])]
