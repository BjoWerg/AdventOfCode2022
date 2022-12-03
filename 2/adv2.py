score = 0

def round_point(opponent,me):
	if me == 'X':
		result = 1
		if opponent == 'A':
			result += 3
		elif opponent == 'B':
			result += 0
		elif opponent == 'C':
			result += 6
		else:
			print('Error opponent = ' + opponent)
	elif me == 'Y':
		result = 2
		if opponent == 'A':
			result += 6
		elif opponent == 'B':
			result += 3
		elif opponent == 'C':
			result += 0
		else:
			print('Error opponent = ' + opponent)
	elif me == 'Z':
		result = 3
		if opponent == 'A':
			result += 0
		elif opponent == 'B':
			result += 6
		elif opponent == 'C':
			result += 3
		else:
			print('Error opponent = ' + opponent)
	else:
		print('Error me = ' + me)
	return result
	
with open('input2.txt') as input:
	for line in input:
		item = line.split()
		score += round_point(item[0],item[1])

print(score)

