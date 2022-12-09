class Knot:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.positions_visited = [str(self.x)+'_'+str(self.y)]
		
	def __str__(self):
		return f"{self.x},{self.y}"	

	def Step(self, direction):
		if direction == 'U':
			self.y += 1
		if direction == 'D':
			self.y -= 1
		if direction == 'R':
			self.x += 1
		if direction == 'L':
			self.x -= 1
		if direction == 'UR':
			self.y += 1
			self.x += 1
		if direction == 'UL':
			self.y += 1
			self.x -= 1
		if direction == 'DR':
			self.y -= 1
			self.x += 1
		if direction == 'DL':
			self.y -= 1
			self.x -= 1
		new_pos = str(self.x)+'_'+str(self.y)
		if new_pos not in self.positions_visited:
			self.positions_visited.append(new_pos)

	def Positions_visited(self):
		return len(self.positions_visited)

def get_tail_move(h, t):
	move =''
	if (h.y - t.y) == 2:
		if (h.x - t.x) <= -1:
			move = 'UL'
		elif (h.x - t.x) >= 1:
			move = 'UR'
		else:
			move = 'U'
	elif (h.y - t.y) == -2:
		if (h.x - t.x) <= -1:
			move = 'DL'
		elif (h.x - t.x) >= 1:
			move = 'DR'
		else:
			move = 'D'
	elif (h.x - t.x) == 2:
		if (h.y - t.y) <= -1:
			move = 'DR'
		elif (h.y - t.y) >= 1:
			move = 'UR'
		else:
			move = 'R'
	elif (h.x - t.x) == -2:
		if (h.y - t.y) <= -1:
			move = 'DL'
		elif (h.y - t.y) >= 1:
			move = 'UL'
		else:
			move = 'L'
	return move


number_of_knots_in_rope = 10
rope = []
for i in range(0,number_of_knots_in_rope):
	rope.append(Knot(0,0))

with open('input9.txt') as list_of_steps:
	for move in list_of_steps:
		direction, steps = move.split(' ')
		for i in range(0,int(steps)):
			rope[0].Step(direction)
			for i in range(1,number_of_knots_in_rope):
				rope[i].Step(get_tail_move(rope[i-1], rope[i]))

print(rope[number_of_knots_in_rope-1].Positions_visited())