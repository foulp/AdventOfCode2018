from collections import deque

ns_marbles = [25, 1618, 7999, 1104, 6111, 5807, 70848]
ns_elfs = [9, 10, 13, 17, 21, 30, 425]

# Part One
def find_max_score(n_marbles, n_elfs, multi=1):
	scores = {i: 0 for i in xrange(n_elfs)}
	marbles = deque([0])
	current_player = 1

	for i in xrange(1, multi*n_marbles + 1):
		if i%23 == 0:
			marbles.rotate(-7)
			scores[current_player] += i + marbles.pop()
		else:
			marbles.rotate(2)
			marbles.append(i)

		current_player += 1
		current_player %= n_elfs

	return max(scores.values())

for n_marbles, n_elfs in zip(ns_marbles, ns_elfs):
	print 'For %d marbles and %d elfs, winning score is %d' % \
	(n_marbles, n_elfs, find_max_score(n_marbles, n_elfs))


# Part Two
print find_max_score(ns_marbles[-1], ns_elfs[-1], multi=100)