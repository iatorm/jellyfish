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
def oper_flip(func):
    return variadize(lambda a: func(a),
                     lambda a, b: func(b, a))

@defop_binary('~')
def oper_compose_pre(func1, func2):
    return variadize(lambda a: func1(func2(a)),
                     lambda a, b: func1(func2(a), func2(b)))

@defop_unary('@')
def oper_swap_arity(func):
    return variadize(lambda a: func(a, a),
                     lambda a, b: func(b))

@defop_binary('@')
def oper_compose_post(func1, func2):
    return variadize(lambda a: func1(func2(a)),
                     lambda a, b: func1(func2(a, b)))

@defop_unary('(')
def oper_left_hook_unary(func):
    return variadize(lambda a: [func(a), a],
                     lambda a, b: [func(a), b])

@defop_binary('(')
def oper_left_hook_binary(func1, func2):
    return variadize(lambda a: func2(func1(a), a),
                     lambda a, b: func2(func1(a), b))

@defop_unary(')')
def oper_right_hook_unary(func):
    return variadize(lambda a: [a, func(a)],
                     lambda a, b: [a, func(b)])

@defop_binary(')')
def oper_right_hook_binary(func1, func2):
    return variadize(lambda a: func1(a, func2(a)),
                     lambda a, b: func1(a, func2(b)))

@defop_unary('[')
def oper_left_fork_unary(func):
    return variadize(lambda a: [func(a), a],
                     lambda a, b: [func(a, b), b])

@defop_binary('[')
def oper_left_fork_binary(func1, func2):
    return variadize(lambda a: func2(func1(a), a),
                     lambda a, b: func2(func1(a, b), b))

@defop_unary(']')
def oper_right_fork_unary(func):
    return variadize(lambda a: [a, func(a)],
                     lambda a, b: [a, func(a, b)])

@defop_binary(']')
def oper_right_fork_binary(func1, func2):
    return variadize(lambda a: func1(a, func2(a)),
                     lambda a, b: func1(a, func2(a, b)))

func_defs = {c:variadize(f) for (c,f) in func_defs.items()}
oper_defs = {c:variadize(f) for (c,f) in oper_defs.items()}
