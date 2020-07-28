import pathlib

if __name__ == '__main__':
    with open(f'../inputs/{pathlib.Path(__file__).stem}.txt', 'r') as f:
        changes = f.read().split('\n')

    # Part One
    freq = sum(eval(c) for c in changes)
    print(f"The result of first star is {freq}")

    # Part Two
    freqs = set()
    freq = 0
    i = 0
    while freq not in freqs:
        freqs.add(freq)
        freq += eval(changes[i])
        i = (i+1) % len(changes)
    print(f"The result of second star is {freq}")
