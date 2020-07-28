import pathlib


def find_next(k, chain):
    return next((i + k for i, v in enumerate(chain[k:-1]) if
                 v.lower() == chain[i + k + 1].lower() and v.isupper() != chain[i + k + 1].isupper()), -1)


def fully_react(chain):
    i = find_next(0, chain)
    while i >= 0:
        chain = chain[:i] + chain[i + 2:]
        i = find_next(max(0, i - 1), chain)
    return chain


if __name__ == '__main__':
    with open(f'../inputs/{pathlib.Path(__file__).stem}.txt', 'r') as f:
        polymer = f.read()

    # Part One
    print(f"The result of first star is {len(fully_react(polymer))}")

    # Part Two
    best = len(polymer)
    for letter in set(polymer.lower()):
        short_poly = polymer.replace(letter, '')
        short_poly = short_poly.replace(letter.upper(), '')
        best = min(best, len(fully_react(short_poly)))
    print(f"The result of second star is {best}")
