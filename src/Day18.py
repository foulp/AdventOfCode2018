import numpy as np
import pathlib


def adj(i, j, size_x, size_y):
    adjacents = []
    if i > 0:
        adjacents.append((i - 1, j))
        if j > 0:
            adjacents.append((i - 1, j - 1))
        if j < size_y - 1:
            adjacents.append((i - 1, j + 1))
    if j < size_y - 1:
        adjacents.append((i, j + 1))
    if j > 0:
        adjacents.append((i, j - 1))
    if i < size_x - 1:
        adjacents.append((i + 1, j))
        if j > 0:
            adjacents.append((i + 1, j - 1))
        if j < size_y - 1:
            adjacents.append((i + 1, j + 1))
    return adjacents


def evol(puzzle_input, i, j, size_x, size_y):
    adja = adj(i, j, size_x, size_y)
    if puzzle_input[i][j] == '.':
        if sum(puzzle_input[ii, jj] == '|' for ii, jj in adja) >= 3:
            return '|'
        return '.'
    if puzzle_input[i][j] == '|':
        if sum(puzzle_input[ii, jj] == '#' for ii, jj in adja) >= 3:
            return '#'
        return '|'
    if puzzle_input[i][j] == '#':
        if any(puzzle_input[ii, jj] == '#' for ii, jj in adja) and any(puzzle_input[ii, jj] == '|' for ii, jj in adja):
            return '#'
        return '.'


def ressources_left(puzzle_input, minutes):
    current = np.copy(puzzle_input)
    size_x, size_y = puzzle_input.shape
    met = [''.join(puzzle_input.reshape((-1,)))]
    for m in range(minutes):
        for i in range(len(current)):
            for j in range(len(current[i])):
                current[i, j] = evol(puzzle_input, i, j, size_x, size_y)

        new = ''.join(current.reshape((-1,)))
        if new in met:
            break
        met.append(new)
        puzzle_input = np.copy(current)

    left = minutes - m - 1
    if left:
        idx = met.index(new)
        left %= (len(met) - idx)
        puzzle_input = met[(met.index(new) + left) % len(met)]
    else:
        puzzle_input = ''.join(puzzle_input.reshape((-1,)))

    return puzzle_input.count('#') * puzzle_input.count('|')


if __name__ == '__main__':
    with open(f'../inputs/{pathlib.Path(__file__).stem}.txt', 'r') as f:
        puzzle = f.read().split('\n')

    puzzle = np.array([list(liste) for liste in puzzle])

    print(f"The result of first star is {ressources_left(puzzle, 10)}")
    print(f"The result of first star is {ressources_left(puzzle, 1000000000)}")
