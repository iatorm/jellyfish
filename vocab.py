from utils import *
import math
from enum import Enum

func_defs = {}
oper_defs = {}

class Roles(Enum):
    function = 0
    operator = 1

def get_defs(role):
    if role == Roles.function:
        return func_defs
    else:
        return oper_defs

def defun(char, arity, role):
    def define_cmd(func):
        defs = get_defs(role)
        if char in defs:
            impl = list(defs[char])
        else:
            impl = [None, None]
        impl[arity-1] = func
        defs[char] = tuple(impl)
        return func
    return define_cmd

defun_unary = lambda char: defun(char, 1, Roles.function)
defun_binary = lambda char: defun(char, 2, Roles.function)
defop_unary = lambda char: defun(char, 1, Roles.operator)
defop_binary = lambda char: defun(char, 2, Roles.operator)

def mathy_unary(f):
    return lambda x: Atom(x.type, f(x.value))
    
def mathy_binary(f):
    return lambda x, y: Atom(x.type, f(x.value, y.value))

threaded_unary = lambda rank: lambda f: thread_unary(f, rank)
threaded_binary = lambda rank1, rank2: lambda f: thread_binary(f, rank1, rank2)

@defun_unary('{')
def func_left_id(a):
    return a

@defun_binary('{')
def func_left(a, b):
    return a

@defun_unary('}')
def func_right_id(a):
    return a

@defun_binary('}')
def func_right(a, b):
    return b

@defun_unary('+')
@threaded_unary(0)
@mathy_unary
def func_abs(a): return abs(a)

@defun_binary('+')
@threaded_binary(0, 0)
@mathy_binary
def func_add(a, b): return a + b

@defun_unary('-')
@threaded_unary(0)
@mathy_unary
def func_negate(a): return -a

@defun_binary('-')
@threaded_binary(0, 0)
@mathy_binary
def func_subtract(a, b): return b - a

@defun_unary('*')
@threaded_unary(0)
@mathy_unary
def func_signum(a): return (a>0) - (a<0)

@defun_binary('*')
@threaded_binary(0, 0)
@mathy_binary
def func_multiply(a, b): return a * b

@defun_unary('%')
@threaded_unary(0)
@mathy_unary
def func_reciprocal(a):
    if a == 0:
        return 0 # TODO: give error?
    return 1/a

@defun_binary('%')
@threaded_binary(0, 0)
@mathy_binary
def func_divide(a, b):
    if a != 0 != b:
        return b / a
    return 0 # TODO: give errors?

@defun_unary('|')
@threaded_unary(0)
@mathy_unary
def func_floor(a): return math.floor(a)

@defun_binary('|')
@threaded_binary(0, 0)
@mathy_binary
def func_modulus(a, b):
    if a != 0 != b:
        return b % a
    return 0 # TODO: give errors?

@defun_unary(',')
def func_flatten(a):
    return flatten(a)

@defun_binary(',')
def func_append(a, b):
    if is_atom(a):
        if is_atom(b):
            return [a, b]
        else:
            return [a] + b
    elif is_atom(b):
        return a + [b]
    else:
        return a + b

@defun_unary(';')
def func_singleton(a):
    return [a]

@defun_binary(';')
def func_pair(a, b):
    return [a, b]

@defun_unary('$')
def func_shape(a):
    return [to_num_atom(dim) for dim in shape(a)]

@defun_binary('$')
@threaded_binary(1, -1)
def func_reshape(a, b):
    return reshape(b, a)

@defun_unary('@')
def func_indices(a):
    if is_atom(a):
        return to_num_atom(0)
    res = []
    for ind, item in enumerate(a):
        if is_atom(item):
            res.append([to_num_atom(ind)])
        else:
            for subind in func_indices(item):
                res.append([to_num_atom(ind)] + subind)
    return res

@defun_binary('@')
@threaded_binary(1, -1)
def func_index(a, b):
    if is_atom(b):
        return b
    if is_atom(a):
        return b[int(a) % len(b)]
    for ind in a:
        b = b[int(ind) % len(b)]
        if is_atom(b):
            return b
    return b

def variadize(func, binary=None):
    if binary is None:
        unary, binary = func
    else:
        unary = func
    def variadic(a, b=None):
        if a is None:
            if b is None:
                return None
            else:
                return unary(b)
        elif b is None:
            return unary(a)
        else:
            return binary(a, b)
    return variadic

@defop_unary('~')
def oper_const_or_flip(f):
    if is_value(f):
        return variadize(lambda a: f,
                         lambda a, b: f)
    return variadize(lambda a: func(a),
                     lambda a, b: func(b, a))

@defop_binary('~')
def oper_curry_or_precompose(f, g):
    if is_value(f):
        if is_value(g):
            return variadize(lambda a: [f, g],
                             lambda a, b: [f, g])
        return variadize(lambda a: g(f, a),
                         lambda a, b: g(f, b))
    elif is_value(g):
        return variadize(lambda a: f(a, g),
                         lambda a, b: f(a, g))
    return variadize(lambda a: f(g(a)),
                     lambda a, b: f(g(a), g(b)))

@defop_unary('&')
def oper_swap_arity(f):
    return variadize(lambda a: f(a, a),
                     lambda a, b: f(b))

@defop_binary('&')
def oper_postcompose(f, g):
    return variadize(lambda a: f(g(a)),
                     lambda a, b: f(g(a, b)))

@defop_unary('(')
def oper_left_unary_hook(f):
    return variadize(lambda a: [f(a), a],
                     lambda a, b: [f(a), b])

@defop_binary('(')
def oper_left_hook(f, g):
    return variadize(lambda a: g(f(a), a),
                     lambda a, b: g(f(a), b))

@defop_unary(')')
def oper_right_unary_hook(f):
    return variadize(lambda a: [a, f(a)],
                     lambda a, b: [a, f(b)])

@defop_binary(')')
def oper_right_hook(f, g):
    return variadize(lambda a: f(a, g(a)),
                     lambda a, b: f(a, g(b)))

@defop_unary('[')
def oper_left_unary_fork(f):
    return variadize(lambda a: [f(a), a],
                     lambda a, b: [f(a, b), b])

@defop_binary('[')
def oper_left_fork(f, g):
    return variadize(lambda a: g(f(a), a),
                     lambda a, b: g(f(a, b), b))

@defop_unary(']')
def oper_right_unary_fork(f):
    return variadize(lambda a: [a, f(a)],
                     lambda a, b: [a, f(a, b)])

@defop_binary(']')
def oper_right_fork(f, g):
    return variadize(lambda a: f(a, g(a)),
                     lambda a, b: f(a, g(a, b)))

@defop_unary('`')
def oper_unary_thread(f):
    if is_value(f):
        return variazide(thread_unary(lambda a: f, 0),
                         thread_binary(lambda a, b: f, 0, 0))
    return variadize(thread_unary(f, 0),
                     thread_binary(f, 0, 0))

@defop_binary('`')
def oper_binary_thread(f, g):
    if is_value(f):
        if is_value(g):
            sole, right, left = reshape(g, [3])
            return variadize(thread_unary(lambda a: f, int(sole)),
                             thread_binary(lambda a, b: f, int(left), int(right)))
        sole, right, left = reshape(f, [3])
        return variadize(thread_unary(g, int(sole)),
                         thread_binary(g, int(left), int(right)))
    elif is_value(g):
        sole, right, left = reshape(g, [3])
        return variadize(thread_unary(f, int(sole)),
                         thread_binary(f, int(left), int(right)))
    def dynamic_thread_unary(a):
        level = reshape(f(a), [])
        return thread_unary(g, int(level))(a)
    def dynamic_thread_binary(a, b):
        _, right, left = reshape(f(a, b), [3])
        return thread_binary(g, int(left), int(right))(a, b)
    return variadize(dynamic_thread_unary, dynamic_thread_binary)

@defop_unary('/')
def unary_foldl(f):
    def folded(a):
        if is_atom(a):
            return a
        if not a:
            return to_num_atom(0)
        x = a[0]
        for y in a[1:]:
            x = f(x, y)
        return x
    def folded_init(a, b):
        if is_atom(b):
            return f(a, b)
        for y in b:
            a = f(a, y)
        return a
    return variadize(folded, folded_init)

@defop_binary('/')
def binary_fold(f, g):
    raise Error("Binary '/' not implemented.")

func_defs = {c:variadize(f) for (c,f) in func_defs.items()}
oper_defs = {c:variadize(f) for (c,f) in oper_defs.items()}
