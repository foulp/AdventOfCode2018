import numpy as np

with open('advent18.txt', 'r') as f:
	puzzle = f.read()

puzzle = np.array([list(l) for l in puzzle.split('\n')])


def adj(i, j, size_x, size_y):
	adjacents = []
	if i > 0:
		adjacents.append((i-1, j))
		if j > 0: adjacents.append((i-1, j-1))
		if j < size_y - 1: adjacents.append((i-1, j+1))
	if j < size_y - 1:
		adjacents.append((i, j+1))
	if j > 0 :
		adjacents.append((i, j-1))
	if i < size_x - 1:
		adjacents.append((i+1, j))
		if j > 0: adjacents.append((i+1, j-1))
		if j < size_y - 1: adjacents.append((i+1, j+1))
	return adjacents

def evol(puzzle_input, i, j, size_x, size_y):
	adja = adj(i, j, size_x, size_y)
	if puzzle_input[i][j]=='.':
		if sum(puzzle_input[ii,jj]=='|' for ii, jj in adja) >= 3:
			return '|'
		return '.'
	if puzzle_input[i][j]=='|':
		if sum(puzzle_input[ii,jj]=='#' for ii, jj in adja) >= 3:
			return '#'
		return '|'
	if puzzle_input[i][j]=='#':
		if any(puzzle_input[ii,jj]=='#' for ii, jj in adja) and any(puzzle_input[ii,jj]=='|' for ii, jj in adja):
			return '#'
		return '.'


def ressources_left(puzzle_input, minutes):
	current = np.copy(puzzle_input)
	size_x, size_y = puzzle_input.shape
	met = [''.join(puzzle_input.reshape((-1, )))]
	for m in xrange(minutes):
		for i in xrange(len(current)):
			for j in xrange(len(current[i])):
				current[i,j] = evol(puzzle_input, i, j, size_x, size_y)

		new = ''.join(current.reshape((-1, )))
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

for minutes in [10, 1000000000]:
	print "Ressources left after %d minutes are %d" % (minutes, ressources_left(puzzle, minutes))