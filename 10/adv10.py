x_reg = 1
clock = 1
period = 40
offset = 20
sum_of_signal_strengths = 0

with open('input10.txt') as instructions:

	for cmd in instructions:
		instr = cmd.strip('\n').split(' ')
		if (clock+offset)%period == 0:
			sum_of_signal_strengths += clock * x_reg
		clock += 1
		if instr[0] == 'addx':
			if (clock+offset)%period == 0:
				sum_of_signal_strengths += clock * x_reg
			clock += 1
			x_reg += int(instr[1])

print(sum_of_signal_strengths)