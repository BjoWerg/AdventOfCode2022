def action(reg):
	if not hasattr(action,"clock"):
		action.clock = 1

	if abs(reg-(action.clock-1)%40) <= 1:
		print("#",end='')
	else:
		print('.',end='')
	if action.clock%40 == 0:
		print('')
	action.clock += 1
	
with open('input10.txt') as instructions:
	x_reg = 1
	for cmd in instructions:
		action(x_reg)
		if 'addx' in cmd:
			action(x_reg)
			x_reg += int(cmd.strip('\n').split(' ')[1])
