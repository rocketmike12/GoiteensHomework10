def generate_xy(a: int, b: int):
    import random
    x = [0, random.randint(a, b), random.randint(a, b), random.randint(a, b), random.randint(a, b)]
    y = [0, random.randint(a, b), random.randint(a, b), random.randint(a, b), random.randint(a, b)]
    return [x, y]
