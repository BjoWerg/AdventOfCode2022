x_reg = 1
clock = 1
period = 40

with open('input10.txt') as instructions:
	for cmd in instructions:
		instr = cmd.strip('\n').split(' ')
		if abs(x_reg-(clock-1)%period)<= 1:
			print("#",end='')
		else:
			print('.',end='')
		if clock%period == 0:
			print('')
		clock += 1
		if instr[0] == 'addx':
			if abs(x_reg-(clock-1)%period) <= 1:
				print("#",end='')
			else:
				print('.',end='')
			if clock%period == 0:
				print('')
			clock += 1
			x_reg += int(instr[1])
