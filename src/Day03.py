import pathlib

if __name__ == '__main__':
    with open(f'../inputs/{pathlib.Path(__file__).stem}.txt', 'r') as f:
        claims = f.read().split('\n')

    # Part One
    fabric = {(i, j): 0 for i in range(1000) for j in range(1000)}

    for claim in claims:
        claim = claim.split(' @ ')[1]
        corner, size = claim.split(': ')
        a, b = map(int, corner.split(','))
        w, h = map(int, size.split('x'))
        for i in range(a, a+w):
            for j in range(b, b+h):
                if fabric[(i, j)]:
                    overlap = True
                fabric[(i, j)] += 1

    print(f"The result of first star is {sum([v > 1 for v in fabric.values()])}")

    # Part Two
    for claim in claims:
        overlap = False
        idx, claim = claim.split(' @ ')
        corner, size = claim.split(': ')
        a, b = map(int, corner.split(','))
        w, h = map(int, size.split('x'))
        for i in range(a, a+w):
            for j in range(b, b+h):
                if fabric[(i, j)] > 1:
                    overlap = True
                    break
            if overlap:
                break

        if not overlap:
            print(f"The result of second star is {idx}")
            break
