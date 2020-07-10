import numpy as np

# Part One
grid_serial_number = 9005
grid_size = (300, 300)

def cell_power(x, y, grid_serial_number):
	rack_id = x + 10
	fuel_power = rack_id * y
	fuel_power += grid_serial_number
	fuel_power *= rack_id
	fuel_power //= 100
	fuel_power = int(str(fuel_power)[-1])
	fuel_power -= 5
	return fuel_power

grid = np.zeros(grid_size)
for x in xrange(grid_size[1]):
	for y in xrange(grid_size[0]):
		grid[y, x] = cell_power(x, y, grid_serial_number)

best = (0, (0, 0))
for x in xrange(grid_size[1] - 3):
	for y in xrange(grid_size[0] - 3):
		best = max(best, (np.sum(grid[y:y+3, x:x+3]), (x,y)))

print best

# Part Two 
best = (0, (0, 0), 0)
for x in xrange(grid_size[1]):
	for y in xrange(grid_size[0]):
		max_size = min(grid_size[0] - y, grid_size[1] - x)
		for size in xrange(1, max_size + 1):
			best = max(best, (np.sum(grid[y:y+size, x:x+size]), (x,y), size))

print best