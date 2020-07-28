import pathlib

if __name__ == '__main__':
    with open(f'../inputs/{pathlib.Path(__file__).stem}.txt', 'r') as f:
        idx = f.read().split('\n')

    # Part One
    twos = 0
    threes = 0
    for ids in idx:
        if any(ids.count(letter) == 2 for letter in set(ids)):
            twos += 1
        if any(ids.count(letter) == 3 for letter in set(ids)):
            threes += 1
    print(f"The result of first star is {twos * threes}")

    # Part Two
    for i, ids1 in enumerate(idx):
        for ids2 in idx[i+1:]:
            if sum([a != b for a, b in zip(ids1, ids2)]) == 1:
                print(f"The result of second star is {''.join([a for i, a in enumerate(ids1) if a == ids2[i]])}")
                break
