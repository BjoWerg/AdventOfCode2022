stack = [[],[],[],[],[],[],[],[],[]]

with open('input5.txt') as crates:
	setup = True
	for line in crates:
		if setup:
			if line[1] == '1':
				setup = False
			else:
				for pos in range(len(line)):
					if (pos-1)%4 == 0 and line[pos] != ' ':
						stack[(pos-1)//4] = [line[pos]] + stack[(pos-1)//4]
		elif 'move' in line:
			moves = line.split(' ')
			for i in range(int(moves[1])):
				stack[int(moves[5])-1].append(stack[int(moves[3])-1].pop())
answer = ''
for i in range(9):
	if len(stack[i]) > 0:
		answer += stack[i].pop()
print(answer)
