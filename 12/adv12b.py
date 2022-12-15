class Node:
	def __init__(self, height):
		self.height = height
		self.steps = 0
		self.visited = False

	def IsMyParent(self, node):
		if not self.visited and (self.height - node.height) < 2:
			self.steps = node.steps+1
			self.visited = True
			return True
		else:
			return False

def find_path(start, end):
	node_list = [start]
	steps = 0
	while len(node_list) != 0:
		x, y = node_list.pop(0)
		if [x,y] == end:
			steps = node_map[y][x].steps
			break
		else:
			if x > 0 and node_map[y][x-1].IsMyParent(node_map[y][x]):
				node_list.append([x-1,y])
			if x < x_count-1 and node_map[y][x+1].IsMyParent(node_map[y][x]):
				node_list.append([x+1,y])
			if y > 0 and node_map[y-1][x].IsMyParent(node_map[y][x]):
				node_list.append([x,y-1])
			if y < y_count-1 and node_map[y+1][x].IsMyParent(node_map[y][x]):
				node_list.append([x,y+1])
	return steps

# Build height map, find start and end points
node_map = []
with open('input12.txt') as file:
	y_count = 0
	for row in file:
		x_count = 0
		x_nodes = []
		for height in row.strip('\n'):
			pos = [x_count, y_count]
			if height == 'S':
				start_pos = pos
				height = 'a'
			elif height == 'E':
				end_pos = pos
				height = 'z'
			x_nodes.append(Node(ord(height)))
			x_count += 1
		node_map.append(x_nodes)
		y_count += 1

# part 1
print(f'Route from start has {find_path(start_pos, end_pos)} steps to end')


# part 2
start_list = []
for y in range(len(node_map)):
	for x in range(len(node_map[0])):
		if node_map[y][x].height == ord('a'):
			start_list.append([x,y])

shortest = 10000
for pos in start_list:
	# Clear node visit flag and steps before next try
	for y in range(len(node_map)):
		for x in range(len(node_map[0])):
			node_map[y][x].visited  = False
			node_map[y][x].steps  = 0
			
	steps = find_path(pos, end_pos)
	if steps != 0 and steps < shortest:
		shortest = steps
print(f'Shortest route has {shortest} steps')