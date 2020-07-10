with open('advent05.txt', 'r') as f:
	polymer = f.read()

# Part One
def find_next(k, polymer):
	return next((i+k for i, v in enumerate(polymer[k:-1]) if v.lower() == polymer[i+k+1].lower() and v.isupper()!=polymer[i+k+1].isupper()), -1)

def fully_react(polymer):
	i = find_next(0, polymer)
	while  i >= 0:
		polymer = polymer[:i] + polymer[i+2:]
		i = find_next(max(0, i-1), polymer)
	return polymer

print len(fully_react(polymer))

# Part Two
with open('advent05.txt', 'r') as f:
	polymer = f.read()

best = len(polymer)
for letter in set(polymer.lower()):
	short_poly = polymer.replace(letter, '')
	short_poly = short_poly.replace(letter.upper(), '')
	best = min(best, len(fully_react(short_poly)))
print best