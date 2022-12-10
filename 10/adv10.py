sum_of_signal_strengths = 0

def action(reg):
	global sum_of_signal_strengths
	if not hasattr(action,"clock"):
		action.clock = 1
		
	if (action.clock+20)%40 == 0:
		sum_of_signal_strengths += action.clock * reg
	action.clock += 1


with open('input10.txt') as instructions:
	x_reg = 1
	for cmd in instructions:
		action(x_reg)
		if 'addx' in cmd:
			action(x_reg)
			x_reg += int(cmd.strip('\n').split(' ')[1])

print(sum_of_signal_strengths)