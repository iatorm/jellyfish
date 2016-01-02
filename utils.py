

def char_to_data(c):
    return (False, ord(c))

def digits_to_data(d):
    return (True, int(d))

def is_value(item):
    return type(item) is not callable

def is_atom(value):
    return type(value) is not list

def shape(value):
    if is_atom(value):
        return []
    else:
        shapes = zip(*[shape(item) for item in value])
        return [len(value)] + [min(x) for x in shapes]

def rank(value):
    return len(shape(value))

def incneg(n):
    return n + (n<0)

def thread_binary(f, rank1, rank2):
    def threaded_f(a, b, lev1=rank1, lev2=rank2):
        rank_a, rank_b = rank(a), rank(b)
        if rank_a <= max(0, lev1) or lev1 == -1:
            if rank_b <= max(0, lev2) or lev2 == -1:
                return f(a, b)
            else:
                return [threaded_f(a, y, rank_a, incneg(lev2))
                        for y in b]
        elif rank_b <= max(0, lev2) or lev2 == -1:
            return [threaded_f(x, b, incneg(lev1), rank_b)
                    for x in a]
        else:
            return [threaded_f(x, y, incneg(lev1), incneg(lev2))
                    for (x, y) in zip(a,b)]
    return threaded_f

def thread_unary(f, rank):
    return lambda a: thread_binary(f, rank)(a, None)