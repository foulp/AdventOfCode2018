with open('advent08.txt', 'r') as f:
	licence = f.read()

# licence = """2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"""

licence = map(int, licence.split())
 
# Part One
def node(tree, total):
	a, b = tree[:2]
	temp = int(total)
	nodes = tree[2:]
	for i in xrange(a):
		nodes, temp = node(nodes, temp)
	
	temp += sum(nodes[:b])

	return nodes[b:], temp

print node(licence, 0)[1]

# Part Two
def node_value(tree):
	"""
	Return the value of the coming node
	"""
	a, b = tree[:2]
	child_values = []
	nodes = tree[2:]
	for i in xrange(a):
		nodes, value = node_value(nodes)
		child_values.append(value)

	if a == 0:
		value = sum(nodes[:b])
	else:
		value = 0
		for i in xrange(b):
			try:
				if nodes[i]>0: 
					value += child_values[nodes[i]-1]
			except:
				pass

	return nodes[b:], value

print node_value(licence)[1]