with open('advent13.txt', 'r') as f:
	track = f.read()
track = track.replace('\\', '\\').split('\n')

track[-1] += ' ' * (len(track[0]) - len(track[-1]))

sledges = []
for x in xrange(len(track[0])):
	for y in xrange(len(track)):
		if track[y][x] in ['>', '<', '^', 'v']:
			sledges.append((0, (y, x), 0, track[y][x]))
sledges.sort()
for _, (y, x), _, _ in sledges: track[y] = track[y][:x] + '-' + track[y][x+1:]

directions = '<v>^'

loc = [sledge[:2] for sledge in sledges]
while len(set(loc)) == len(sledges):
	n, (y, x), t, path = sledges[0]
	if track[y][x] in '|-' or (track[y][x]=='+' and t==1): 
		if track[y][x]=='+': t = (t + 1) % 3
		if path == '>': x += 1
		elif path == '<': x-= 1
		elif  path =='v': y += 1
		elif path == '^': y -= 1

	elif track[y][x] == '\\':
		if path == '>': y += 1; path = 'v'
		elif path == '^': x -= 1; path = '<'
		elif path == '<': y -= 1; path = '^'
		elif path == 'v': x += 1; path = '>'
	elif track[y][x] == '/':
		if path == '>': y -= 1; path = '^'
		elif path == '^': x += 1; path = '>'
		elif path == '<': y += 1; path = 'v'
		elif path == 'v': x -= 1; path = '<'
	elif track[y][x] =='+':
		if t==0: 
			if path=='>': y -= 1
			elif path=='^': x -= 1
			elif path=='<': y += 1
			elif path=='v': x += 1
			path = directions[(directions.index(path) + 1) % 4]

		elif t==2: 
			if path=='>': y += 1
			elif path=='^': x += 1
			elif path=='<': y -= 1
			elif path=='v': x -= 1
			path = directions[(directions.index(path) - 1) % 4]
		t = (t + 1) % 3

	sledges[0] = (n+1, (y, x), t, path)
	sledges.sort()
	loc = [sledge[1] for sledge in sledges]

print next((x,y) for (y,x) in loc if loc.count((y,x)) > 1) 

# Part Two

with open('advent13.txt', 'r') as f:
	track = f.read()
track = track.replace('\\', '\\').split('\n')

track[-1] += ' ' * (len(track[0]) - len(track[-1]))

sledges = []
for x in xrange(len(track[0])):
	for y in xrange(len(track)):
		if track[y][x] in ['>', '<', '^', 'v']:
			sledges.append((0, (y, x), 0, track[y][x]))
sledges.sort()
for _, (y, x), _, _ in sledges: track[y] = track[y][:x] + '-' + track[y][x+1:]

directions = '<v>^'

N = 0
while len(sledges) > 1 or sledges[0][0] < N:
	if all(n==N for n, _, _, _ in sledges): N+= 1;print 'N up to %d'%N

	n, (y, x), t, path = sledges[0]
	if track[y][x] in '|-' or (track[y][x]=='+' and t==1): 
		if track[y][x]=='+': t = (t + 1) % 3
		if path == '>': x += 1
		elif path == '<': x-= 1
		elif  path =='v': y += 1
		elif path == '^': y -= 1

	elif track[y][x] == '\\':
		if path == '>': y += 1; path = 'v'
		elif path == '^': x -= 1; path = '<'
		elif path == '<': y -= 1; path = '^'
		elif path == 'v': x += 1; path = '>'
	elif track[y][x] == '/':
		if path == '>': y -= 1; path = '^'
		elif path == '^': x += 1; path = '>'
		elif path == '<': y += 1; path = 'v'
		elif path == 'v': x -= 1; path = '<'
	elif track[y][x] =='+':
		if t==0: 
			if path=='>': y -= 1
			elif path=='^': x -= 1
			elif path=='<': y += 1
			elif path=='v': x += 1
			path = directions[(directions.index(path) + 1) % 4]

		elif t==2: 
			if path=='>': y += 1
			elif path=='^': x += 1
			elif path=='<': y -= 1
			elif path=='v': x -= 1
			path = directions[(directions.index(path) - 1) % 4]
		t = (t + 1) % 3

	sledges[0] = (n+1, (y, x), t, path)

	good = []
	for i, s in enumerate(sledges):
		if s[1] not in [sledge[1] for sledge in sledges[:i]+sledges[i+1:]]:
			good.append(i)

	sledges = [s for i,s in enumerate(sorted(sledges)) if i in good]

print sledges[0][1][::-1]