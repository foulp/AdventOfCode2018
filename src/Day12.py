from itertools import chain
from more_itertools import windowed
import pathlib


def run(pots, patterns_dict, n):
    start = 0
    last_pots = ''
    last_start = 0

    for k in range(n):
        pots = '..' + pots + '..'
        start -= 2
        plants = ''.join(patterns_dict[''.join(patt)] for patt in windowed(chain('..', pots, '..'), 5))
        pots = plants.lstrip('.')
        start += len(plants) - len(pots)
        pots = pots.rstrip('.')
        if pots == last_pots:
            return sum(idx + start for idx, p in enumerate(pots) if p == '#') + (n - k - 1) * pots.count('#') * (start - last_start)
        else:
            last_pots = str(pots)
            last_start = int(start)
    return sum(idx + start for idx, p in enumerate(pots) if p == '#')


if __name__ == '__main__':
    with open(f'../inputs/{pathlib.Path(__file__).stem}.txt', 'r') as f:
        current, patterns = f.read().split('\n\n')

    current = current[current.index(': ')+2:]
    patterns = {seq: new for seq, new in [line.split(' => ') for line in patterns.split('\n')]}

    print(f"The result of first star is {run(str(current), patterns, 20)}")

    print(f"The result of first star is {run(str(current), patterns, 50000000000)}")
