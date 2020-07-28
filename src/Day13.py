import numpy as np
import pathlib


def init_track():
    with open(f'../inputs/{pathlib.Path(__file__).stem}.txt', 'r') as f:
        rails = f.read().split('\n')

    rails[-1] = rails[-1].ljust(len(rails[0]))
    rails = np.array(list(map(list, rails)))

    sledges = []
    for i in range(rails.shape[1]):
        for j in range(rails.shape[0]):
            if rails[i, j] in '><^v':
                sledges.append((0, (i, j), 0, rails[i, j]))
                rails[i, j] = '-'
    sledges.sort()

    return sledges, rails


def find_next(sledges, rails):
    directions = '>v<^'
    n, (i, j), t, direction = sledges[0]

    # Case sledge continues straight
    if rails[i, j] in '|-' or (rails[i, j] == '+' and t == 1):
        if rails[i, j] == '+':
            t = (t + 1) % 3
        j += {'>': 1, '<': -1}.get(direction, 0)
        i += {'v': 1, '^': -1}.get(direction, 0)

    # Case n2
    elif rails[i, j] == '\\':
        j += {'v': 1, '^': -1}.get(direction, 0)
        i += {'>': 1, '<': -1}.get(direction, 0)
        direction = {'^': '<', '<': '^', 'v': '>', '>': 'v'}[direction]

    # Case n3
    elif rails[i, j] == '/':
        j += {'^': 1, 'v': -1}.get(direction, 0)
        i += {'<': 1, '>': -1}.get(direction, 0)
        direction = {'^': '>', '>': '^', 'v': '<', '<': 'v'}[direction]

    # Case intersection and turn
    elif rails[i, j] == '+':
        if t == 0:
            j += {'v': 1, '^': -1}.get(direction, 0)
            i += {'<': 1, '>': -1}.get(direction, 0)
            direction = directions[(directions.index(direction) - 1) % len(directions)]

        elif t == 2:
            j += {'^': 1, 'v': -1}.get(direction, 0)
            i += {'>': 1, '<': -1}.get(direction, 0)
            direction = directions[(directions.index(direction) + 1) % len(directions)]

        t = (t + 1) % 3

    return n+1, (i, j), t, direction


if __name__ == '__main__':
    # Part One
    carts, track = init_track()

    loc = [sledge[1] for sledge in carts]
    while len(set(loc)) == len(carts):
        carts[0] = find_next(carts, track)
        carts.sort()
        loc = [sledge[1] for sledge in carts]

    print(f"The result of first star is {next((x,y) for (y,x) in loc if loc.count((y,x)) > 1)}")

    # Part Two
    carts, track = init_track()

    while len(carts) > 1:
        carts[0] = find_next(carts, track)

        if any(carts[0][1] == cart[1] for cart in carts[1:]):
            carts = [cart for cart in carts if cart[1] != carts[0][1]]

        carts.sort()

    _, (x, y), _, _ = find_next(carts, track)
    print(f"The result of second star is {y, x}")
