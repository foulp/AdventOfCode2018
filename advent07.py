with open('advent07.txt', 'r') as f:
	steps_input = f.read()

steps = steps_input.split('\n')

before = [step[5] for step in steps]
after = [step[-12] for step in steps]
steps = zip(before, after)

letters = set(step[0] for step in steps).union(set(step[1] for step in steps))

# Part One
done = []
for i in xrange(len(letters)):
	new = sorted(set([bef for bef in letters if bef not in after+done]))[0]
	steps = [t for t in steps if t[0] != new]
	before = [t[0] for t in steps]
	after = [t[1] for t in steps]
	done.append(new)

print ''.join(done)


# Part Two
workers = 5
steps_duration = 60

steps = steps_input.split('\n')
before = [step[5] for step in steps]
after = [step[-12] for step in steps]
steps = zip(before, after)
letters = set(step[0] for step in steps).union(set(step[1] for step in steps))

clock = 0
done = []
doing = {}
for i in sorted(set([bef for bef in letters if bef not in after+done])):
	doing.update({i: len(doing)})
	if len(doing) == workers:
		break

time_started = {a: 0 for a in doing.keys()}
while len(done) < len(letters):
	clock += 1
	ended = [action for action in doing.keys() if clock-time_started[action]==steps_duration+sorted(letters).index(action)+1]
	done += sorted(ended)
	free = [w for w in xrange(workers) if w not in doing.values()]
	for action in ended:
		del time_started[action]
		free.append(doing[action])
		del doing[action]

	steps = [t for t in steps if t[0] not in ended]
	before = [t[0] for t in steps]
	after = [t[1] for t in steps]
	to_be_started = sorted([l for l in letters if l not in done+after+doing.keys()])
	for a in to_be_started:
		if len(free):
			doing[a] = free[0]
			time_started[a] = clock
			free = free[1:]


print clock