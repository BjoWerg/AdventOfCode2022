class Node:
	def __init__(self,x,y,val,p):
		self.x = x
		self.y = y
		self.val = val
		self.p = p

def find_path(s_x, s_y, e_x, e_y):
	visited = [[False for i in range(col_nr)] for j in range(row_nr)]
	node_list = [Node(s_x,s_y,0,[])]
	result = 0
	while len(node_list) != 0:
		curr = node_list.pop(0)
		if (curr.x == e_x) and (curr.y == e_y):
			result = curr.val
			break
			
		else:
			if curr.x > 0 \
			and not visited[curr.y][curr.x-1] \
			and (height_map[curr.y][curr.x-1] - height_map[curr.y][curr.x] < 2):
				node_list.append(Node(curr.x-1, curr.y, curr.val+1, [curr.x, curr.y]))
				visited[curr.y][curr.x-1]= True

			if curr.x < (col_nr - 1) \
			and not visited[curr.y][curr.x+1] \
			and (height_map[curr.y][curr.x+1] - height_map[curr.y][curr.x] < 2):
				node_list.append(Node(curr.x+1, curr.y, curr.val+1, [curr.x, curr.y]))
				visited[curr.y][curr.x+1]= True

			if curr.y > 0 \
			and not visited[curr.y-1][curr.x] \
			and (height_map[curr.y-1][curr.x] - height_map[curr.y][curr.x] < 2):
				node_list.append(Node(curr.x, curr.y-1, curr.val+1, [curr.x, curr.y]))
				visited[curr.y-1][curr.x]= True

			if curr.y < (row_nr - 1) \
			and not visited[curr.y+1][curr.x] \
			and (height_map[curr.y+1][curr.x] - height_map[curr.y][curr.x] < 2):
				node_list.append(Node(curr.x, curr.y+1, curr.val+1, [curr.x, curr.y]))
				visited[curr.y+1][curr.x]= True
	return result

# Build hight map, find start and end points
height_map = []
start_list = []
with open('input12.txt') as file:
	
	row_nr = 0
	for row in file:
		col_nr = 0
		col_heights = []
		for height in row.strip('\n'):
			if height == 'S':
				s_x = col_nr
				s_y = row_nr
				height = 'a'
			elif height == 'E':
				e_x = col_nr
				e_y = row_nr
				height = 'z'
			if height == 'a':
				start_list.append([col_nr,row_nr])
			col_heights.append(ord(height))
			col_nr += 1
		height_map.append(col_heights)
		row_nr += 1

# part 1
#start_list = [[s_x,s_y]]

shortest = 10000
for start in start_list:
	steps = find_path(start[0],start[1],e_x,e_y)
	if steps != 0 and steps < shortest:
		shortest = steps
print(f'Route has {shortest} steps')