from array import array

max_right = 7
#tower = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0]]
tower = array('B',[0b11111111])

#rocks = [
#	[[2,0],[3,0],[4,0],[5,0]],\
#	[[3,0],[2,1],[3,1],[4,1],[3,2]],\
#	[[2,0],[3,0],[4,0],[4,1],[4,2]],\
#	[[2,0],[2,1],[2,2],[2,3]],\
#	[[2,0],[3,0],[2,1],[3,1]]]
	
rocks = [
	array('B',[0b00111100]),\
	array('B',[0b00010000,0b00111000,0b00010000]),\
	array('B',[0b00111000,0b00001000,0b00001000]),\
	array('B',[0b00100000,0b00100000,0b00100000,0b00100000]),\
	array('B',[0b00110000,0b00110000])]
x_maxs = [5, 4,	4, 2, 3]
direction = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
#with open('input17.txt') as f:
#	direction = f.readline().strip()

dir_nbr = 0
top_row = [0]*max_right
offset = 0
rock_nbr = 0

while rock_nbr < 2022:

#	print(f' --- {rock_nbr} ---')

	#create new rock
	rock = rocks[rock_nbr%len(rocks)]
#	rock = []
#	for r in rocks[rock_nbr%len(rocks)]:
#		rock.append(r)
	hight = range(len(rock))
	x_min = 2
	x_max = x_maxs[rock_nbr%len(rocks)]

	top = max(top_row)
	row = top+4
	falling = True
	shift = 0
#	print(x_min,x_max)
#	print('row',row, direction[dir_nbr])
#	for h in range(len(rock)-1,-1,-1):
#		print(f'{rock[h]:08b}')

	while falling:
		if direction[dir_nbr] == '<':
			if x_min > 0:
				blocked = False
				for h in hight:
					if row+h > top:
						break
					else:
						if shift-1 < 0:
							if not ((rock[h]<<abs(shift-1)) & tower[row+h-offset] == 0):
								blocked = True
								break
						elif shift-1 > 0:
							if not ((rock[h]>>shift-1) & tower[row+h-offset] == 0):
								blocked = True
								break
				if not blocked:
					x_min -= 1
					x_max -= 1
					shift -= 1
		else:
			if x_max < max_right-1:
				blocked = False
				for h in hight:
					if row+h > top:
						break
					else:
						if shift+1 < 0:
							if not ((rock[h]<<abs(shift+1)) & tower[row+h-offset] == 0):
								blocked = True
								break
						elif shift+1 > 0:
							if not ((rock[h]>>shift+1) & tower[row+h-offset] == 0):
								blocked = True
								break
				if not blocked:
					x_min += 1
					x_max += 1
					shift += 1
		
		# check if stopped or not 
		blocked = False
		for h in hight:
			if row+h > top+1:
				break
			else:
				if shift >= 0:
					if not ((rock[h]>>shift) & tower[row+h-1-offset] == 0):
						blocked = True
						break
				else:
					if not ((rock[h]<<abs(shift)) & tower[row+h-1-offset] == 0):
						blocked = True
						break
		if not blocked:
			row -= 1
		else:
			falling = False
		
#		print('row',row, direction[dir_nbr])
#		for h in range(len(rock)-1,-1,-1):
#			print(f'{rock[h]:08b}')
		dir_nbr = (dir_nbr+1)%len(direction)

	# add rock to tower
	for h in hight:
		if row+h <= top:
			if shift >= 0:
				tower[row+h-offset] |= (rock[h]>>shift)
			else:
				tower[row+h-offset] |= (rock[h]<<abs(shift))
		else:
			if shift >= 0:
				tower.append(rock[h]>>shift)
			else:
				tower.append(rock[h]<<abs(shift))
				
		for i in range(max_right):
			if not ((tower[row+h-offset] & (0b10000000>>i)) == 0):
				if row+h > top_row[i]:
					top_row[i] = row+h

	drop = len(tower)-(max(top_row)-min(top_row))
	if drop > 10:
		for i in range(drop-10):
			tower.pop(0)
			offset += 1
			
	rock_nbr += 1
	if rock_nbr%10000 == 0:
		print(rock_nbr)

#	print('')
#	for i in range(len(tower)-1,-1,-1):
#		print(f'{tower[i]:08b}')
#	input(' --- press return ---')

print(max(top_row))
#print(top)