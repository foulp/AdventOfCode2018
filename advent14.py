n_recipes = [9, 5, 18, 2018, 890691]
sequence = ['51589', '01245', '92510', '59414', '890691']

N = 4
recipes = '37'
first = 0
second = 1

# Part One
while len(recipes) < n_recipes[N]+10: 
	recipes += str(int(recipes[first]) + int(recipes[second]))

	first = (first + int(recipes[first]) + 1) % len(recipes)
	second = (second + int(recipes[second]) + 1) % len(recipes)

print recipes[n_recipes[N]:n_recipes[N]+10]

# Part Two
recipes = '37'
first = 0
second = 1
while sequence[N] not in recipes[-len(sequence[N])-1:-1]: 
	recipes += str(int(recipes[first]) + int(recipes[second]))

	first = (first + int(recipes[first]) + 1) % len(recipes)
	second = (second + int(recipes[second]) + 1) % len(recipes)

print len(recipes) - len(sequence[N]) - 1 + recipes[-len(sequence[N])-1:].index(sequence[N])