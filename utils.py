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

def is_truthy(value):
    if is_atom(value):
        return value.value != 0
    else:
        return value != []

def uniques(array):
    out = []
    for item in array:
        if item not in out:
            out.append(item)
    return out

def prefixes(a):
    if is_atom(a):
        a = un_range(a)
    return [a[:i] for i in range(1, len(a)+1)]

def infixes(a, n):
    if is_atom(a):
        a = un_range(a)
    if n > 0:
        return [a[i:i+n] for i in range(len(a)-n+1)]
    elif n < 0:
        n = -n
        return [a[i*n:(i+1)*n] for i in range((len(a)+n-1)//n)]
    else:
        return [a[i:i+k] for k in reversed(range(1,len(a)+1)) for i in range(len(a)-k+1)]

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

def join_times(value, times=1):
    if is_atom(value) or times == 0:
        return value
    if times > 0:
        joined = []
        for item in value:
            if is_atom(item):
                joined += [item]
            else:
                joined += item
        return join_times(joined, times-1)
    raise Exception("Can't join a negative number of times.")

def intersperse(value, array):
    if is_atom(array):
        return array
    res = array[:1]
    for item in array[1:]:
        res += [value, item]
    return res

def cartesian_product(array):
    if array:
        head, *rest = array
        if is_atom(head):
            head = [head]
        for item in head:
            for word in cartesian_product(rest):
                yield [item] + word
    else:
        yield []

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

def un_range(x):
    if is_atom(x):
        end = int(x.value)
        if end >= 0:
            return [Atom(x.type, n) for n in range(end)]
        else:
            return [Atom(x.type, -n) for n in reversed(range(-end))]
    elif x:
        return [[n] + w
                for n in un_range(x[0])
                for w in un_range(x[1:])]
    else:
        return [[]]

def bin_range(x):
    if not x:
        return [[]]
    elif height(x) == 1:
        (lo_type, lo), (hi_type, hi) = map(lambda y: (y.type, int(y.value)), x)
        if lo <= hi:
            return [Atom(lo_type, y) for y in range(lo, hi)]
        else:
            return [Atom(lo_type, y) for y in reversed(range(hi, lo))]
    else:
        return [[y] + w
                for y in bin_range(x[0])
                for w in bin_range(x[1:])]

def iterate(f, a, n):
    for i in range(n):
        a = f(a)
    return a

def iterate_until(f, a, g):
    while True:
        b = f(a)
        if is_truthy(g(a, b)):
            return b
        a = b

def acc_iterate_until(f, a, g):
    out = [a]
    while True:
        b = f(a)
        out.append(b)
        if is_truthy(g(a, b)):
            return out
        a = b
