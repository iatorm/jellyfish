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
    def mathy_f(x):
        flag, a = x
        return flag, f(a)
    return mathy_f
    
def mathy_binary(f):
    def mathy_f(x, y):
        flag, a = x
        _, b = y
        return flag, f(a, b)
    return mathy_f

threaded_unary = lambda rank: lambda f: thread_unary(f, rank)
threaded_binary = lambda rank1, rank2: lambda f: thread_binary(f, rank1, rank2)

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

@defop_unary('@')
def oper_swap_arity(f):
    return variadize(lambda a: f(a, a),
                     lambda a, b: f(b))

@defop_binary('@')
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
            (_, unary), (_, right), (_, left) = reshape(g, [3])
            return variadize(thread_unary(lambda a: f, round(unary)),
                             thread_binary(lambda a, b: f,
                                           round(left),
                                           round(right)))
        (_, unary), (_, right), (_, left) = reshape(f, [3])
        return variadize(thread_unary(g, round(unary)),
                         thread_binary(g,
                                       round(left),
                                       round(right)))
    elif is_value(g):
        (_, unary), (_, right), (_, left) = reshape(g, [3])
        return variadize(thread_unary(f, round(unary)),
                         thread_binary(f,
                                       round(left),
                                       round(right)))
    def dynamic_thread_unary(a):
        (_, level) = reshape(f(a), [])
        return thread_unary(g, level)(a)
    def dynamic_thread_binary(a, b):
        _, (_, right), (_, left) = reshape(f(a, b), [3])
        return thread_binary(g, left, right)(a, b)
    return variadize(dynamic_thread_unary, dynamic_thread_binary)

func_defs = {c:variadize(f) for (c,f) in func_defs.items()}
oper_defs = {c:variadize(f) for (c,f) in oper_defs.items()}
