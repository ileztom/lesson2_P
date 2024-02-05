def square(n): return n*n
def sum_of_squares(a, b): return square(a) + square(b)
def larger(a, b): return a if a > b else b

def fn(a, b, c):
    if a == larger(a, b):
        return sum_of_squares(a, larger(b, c))
    return sum_of_squares(b, larger(a, c))