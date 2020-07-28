import numpy as np


def cell_power(i, j, serial_number):
	rack_id = i + 10
	fuel_power = rack_id * j
	fuel_power += serial_number
	fuel_power *= rack_id
	fuel_power //= 100
	fuel_power = int(str(fuel_power)[-1])
	fuel_power -= 5
	return fuel_power


if __name__ == '__main__':
	# Part One
	grid_serial_number = 9005
	grid_size = (300, 300)

	grid = np.zeros(grid_size)
	for x in range(grid_size[1]):
		for y in range(grid_size[0]):
			grid[y, x] = cell_power(x, y, grid_serial_number)

	best = (0, (0, 0))
	for x in range(grid_size[1] - 3):
		for y in range(grid_size[0] - 3):
			best = max(best, (np.sum(grid[y:y+3, x:x+3]), (x, y)))

	print(f"The result of first star is {best[1]}")

	# Part Two
	best = (0, (0, 0), 0)
	for x in range(grid_size[1]):
		for y in range(grid_size[0]):
			max_size = min(grid_size[0] - y, grid_size[1] - x)
			for size in range(1, max_size + 1):
				best = max(best, (np.sum(grid[y:y+size, x:x+size]), (x, y), size))

	print(f"The result of second star is {best[1:]}")
