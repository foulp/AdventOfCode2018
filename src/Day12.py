import pathlib


def run(pots, patterns_dict, n):
    for _ in range(n):
        pots = '..' + pots + '..'
        plants = ''
        for idx, p in enumerate(pots):
            patt = '.' * max(0, 2-idx) + pots[max(0, idx-2): min(len(pots), idx+3)] + '.' * max(0, idx + 3 - len(pots))
            plants += patterns_dict[patt]
        pots = plants
    return sum(idx - 2 * n for idx, p in enumerate(pots) if p == '#')


if __name__ == '__main__':
    with open(f'../inputs/{pathlib.Path(__file__).stem}.txt', 'r') as f:
        current, patterns = f.read().split('\n\n')

    current = current[current.index(': ')+2:]
    patterns = {seq: new for seq, new in [line.split(' => ') for line in patterns.split('\n')]}

    print(f"The result of first star is {run(current, patterns, 20)}")
