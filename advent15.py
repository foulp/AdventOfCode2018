import numpy as np
from itertools import product

with open('advent15.txt', 'r') as f:
	puzzle_input = f.read()

attack_power = 3
hit_points = 200
hp = {}
pos = {}

carte = np.array(map(list, puzzle_input.split('\n')))

kG = 0
kE = ord('a')
for i in xrange(carte.shape[0]):
	for j in xrange(carte.shape[1]):
		if carte[i,j] == 'G':
			carte[i,j] = str(kG)
			hp[str(kG)] = hit_points
			pos[str(kG)] = (i, j)
			kG += 1
		if carte[i,j] == 'E':
			carte[i,j] = chr(kE)
			hp[str(kE)] = hit_points
			pos[str(kE)] = (i, j)
			kE += 1



for i, j in product(xrange(carte.shape[0]), xrange(carte.shape[1])):
	if carte[i, j] in 'EG':
		ennemy = 'EG'.replace(carte[i,j], '')

		targets = np.where(carte==ennemy)
		targets = zip(*targets)
		if len(targets) == 0:
			break

		adja_open_ennemy = []
		for x_e, y_e in targets:
			for xx,yy in [(x_e+1,y_e),(x_e-1,y_e),(x,y_e+1),(x,y_e-1)]:
				if carte[xx,yy]=='.':
					adja_open_ennemy.append((xx,yy))

			if i,j in adja_open_ennemy:
				hp[pos.index((x_e,y_e))] -= attack_power
				break
