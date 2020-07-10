import numpy as np
import matplotlib.pyplot as plt

with open('advent10.txt', 'r') as f:
	points = f.read()


points = points.split('\n')

points = [p[10:-1].split('> velocity=<') for p in points]
points = [map(int,xy.split(',')) + map(int, v.split(',')) for xy, v in points]
mx, my = min(p[0] for p in points), min(p[1] for p in points)
points = [(x-mx, y-my, vx, vy) for x, y, vx, vy in points]

compte = 0
maxi = max(p[1] for p in points)
mini = my
while True:
	temp = [(x+vx, y+vy, vx, vy) for x,y,vx,vy in points]
	mxa, mni = max(p[1] for p in temp), min(p[1] for p in temp)
	if mxa - mni > maxi - mini:
		break
	maxi = float(mxa)
	mini = float(mni)
	points = list(temp)
	compte +=1

plt.scatter([p[0] for p in points], [p[1] for p in points])
plt.show()

# Part Two
print compte