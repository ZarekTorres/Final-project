import math

def area_of_circle(r):
    if type(r) != int and type(r) != float:
        raise TypeError
    if r <= 0:
        raise ValueError
    c = math.pi*r*r
    return c

def area_of_rectangle(w,l):
    if type(w) and type(l) != int and type(w) and type(l) != float:
        raise TypeError
    if w and l <= 0:
        raise ValueError
    return w * l

def area_of_square(x):
    if type(x) != int and type(x) != float:
        raise TypeError
    if x <= 0:
        raise ValueError
    s = math.pow(x, 2)
    return s

def area_of_triangle(h,b):
    if type(h) and type(b) != int and type(h) and type(b) != float:
        raise TypeError
    if h and b <= 0:
        raise ValueError
    return (h*b)/2

