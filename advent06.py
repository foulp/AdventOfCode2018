import numpy as np

def manhattan_d(p_1, p_2):
	return abs(p_1[0] - p_2[0]) + abs(p_1[1] - p_2[1])

with open('advent06.txt', 'r') as f:
	coords = f.read()

coords = [map(int, coord.split(', ')[::-1]) for coord in coords.split('\n')]

maps = np.zeros((max(x for x,y in coords)+1, max(y for x,y in coords)+1)) - 1

for i, (x,y) in enumerate(coords):
	maps[x,y] = i

for x in xrange(maps.shape[0]):
	for y in xrange(maps.shape[1]):
		best = (sum(maps.shape), -1)
		for i, coord in enumerate(coords):
			d = manhattan_d((x,y), coord)
			if d < best[0]:
				best = (d, i)
			elif d == best[0]:
				best = (d, -1)

		maps[x,y] = best[1]

borders = (maps[0,:], maps[:,0], maps[-1,:], maps[:,-1])

unique, counts = np.unique(maps, return_counts=True)
areas = zip(counts, unique)
print next(v for v,i in sorted(areas)[::-1] if all(i not in bord for bord in borders))

# Part Two
limit = 10000
area_size = 0
for x in xrange(maps.shape[0]):
	for y in xrange(maps.shape[1]):
		inside = True
		distance_sum = 0
		for coord in coords:
			distance_sum += manhattan_d(coord, (x,y))
			if distance_sum > limit:
				inside = False
				break
		if inside:
			area_size += 1

print area_size
		
