def generate_xy(a: int, b: int):
    import random
    if a < b:
        a, b = b, a
    x = random.randint(a, b)
    y = random.randint(a, b)
    return [x, y]
