def generate_xy(a: int, b: int):
    from random import randint
    from numpy import linspace
    if a > b:
        a, b = b, a
    x = linspace(0, randint(a, b), randint(7, 15))
    y = x ** randint(1, 5)
    if x[0] > x[1]:
        x[0], x[1] = x[1], x[0]
    if y[0] > y[1]:
        y[0], y[1] = y[1], y[0]
    return [x, y]
