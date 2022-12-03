score = 0

def fight(opponent,outcome):
	if outcome == 'X': # loose
		result = 0
		if opponent == 'A': # rock
			result += 3
		elif opponent == 'B': # paper
			result += 1
		elif opponent == 'C': # scissor
			result += 2
		else:
			print('Error opponent = ' + opponent)
	elif outcome == 'Y': # draw
		result = 3
		if opponent == 'A': # rock
			result += 1 
		elif opponent == 'B': # paper
			result += 2
		elif opponent == 'C': # scissor
			result += 3
		else:
			print('Error opponent = ' + opponent)
	elif outcome == 'Z': # win
		result = 6
		if opponent == 'A': #rock
			result += 2
		elif opponent == 'B': # paper
			result += 3
		elif opponent == 'C': # scissor
			result += 1
		else:
			print('Error opponent = ' + opponent)
	else:
		print('Error me = ' + me)
	return result
	
with open('input2.txt') as input:
	for line in input:
		item = line.split()
		score += fight(item[0],item[1])

print(score)


