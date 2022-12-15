cave = None
x_min = 0
y_min = 0
y_max = 0

def check_map_dimentions(x,y):
	global cave, x_min, y_min
	if cave == None:
		x_min = x
		y_min = y
		cave = [[0]]
	else:
		if x < x_min:
			for j in range(x_min - x):
				for i in range(len(cave)):
					cave[i].insert(0,0)
			x_min = x
		elif (x - x_min) >= len(cave[0]):
			for j in range(x - x_min - len(cave[0]) + 1):
				for i in range(len(cave)):
					cave[i].append(0)
		if y < y_min:
			for j in range(y_min - y):
				cave.insert(0,[0]*len(cave[0]))
			y_min = y
		elif (y - y_min) >= len(cave):
			for j in range(y - y_min - len(cave) + 1):
				cave.append([0]*len(cave[0]))
		
def add_to_map(x,y):
	global cave
	check_map_dimentions(x,y)
	cave[y-y_min][x-x_min] = 1
		
def check_map(x,y):
	global cave
	check_map_dimentions(x,y)
	return cave[y-y_min][x-x_min] == 1

with open('input14.txt') as file:
	for line in file:
		dot = line.strip('\n').split(' -> ')
		for i in range(len(dot)-1):
			x1,y1 = map(int,dot[i].split(','))
			x2,y2 = map(int,dot[i+1].split(','))

			if y1 > y_max:
				y_max = y1
			if y2 > y_max:
				y_max = y2

			if x1 == x2:
				for j in range(abs(y2-y1)+1):
					if y1 < y2:
						add_to_map(x1,y1+j)
					else:
						add_to_map(x1,y2+j)
			else:
				for j in range(abs(x2-x1)+1):
					if x1 < x2:
						add_to_map(x1+j,y1)
					else:
						add_to_map(x2+j,y1)

done = False
sand_x = 500
sand_y = 0
nr_of_grains = 0
while not done:
	if not check_map(sand_x,sand_y+1):
		sand_y += 1
	elif not check_map(sand_x-1,sand_y+1):
		sand_x -= 1
		sand_y += 1
	elif not check_map(sand_x+1,sand_y+1):
		sand_x += 1
		sand_y += 1
	else:
		add_to_map(sand_x,sand_y)
		sand_x = 500
		sand_y = 0		
		nr_of_grains += 1

	if sand_y == y_max:
		done = True
			
print(f'Number of sand grains {nr_of_grains}')