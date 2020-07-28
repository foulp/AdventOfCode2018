from collections import deque


def find_max_score(n_marbles, n_elfs, multi=1):
	scores = {i: 0 for i in range(n_elfs)}
	marbles = deque([0])
	current_player = 1

	for i in range(1, multi*n_marbles + 1):
		if i%23 == 0:
			marbles.rotate(-7)
			scores[current_player] += i + marbles.pop()
		else:
			marbles.rotate(2)
			marbles.append(i)

		current_player += 1
		current_player %= n_elfs

	return max(scores.values())


if __name__ == '__main__':
	ns_marbles = [25, 1618, 7999, 1104, 6111, 5807]
	ns_elfs = [9, 10, 13, 17, 21, 30]
	scores = [32, 8317, 146373, 2764, 54718, 37305]

	# Part One
	for n_marbles, n_elfs, score in zip(ns_marbles, ns_elfs, scores):
		assert find_max_score(n_marbles, n_elfs) == score

	n_marble = 70848
	n_elf = 425
	print(f'The result of first star is {find_max_score(n_marble, n_elf)}')

	# Part Two
	print(f"The result of second star is {find_max_score(ns_marbles[-1], ns_elfs[-1], multi=100)}")
