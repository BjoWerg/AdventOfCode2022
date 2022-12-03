topElfCal = 0
calSumma = 0

with open('input.txt') as input:
	for line in input:
		if line != '\n':
			calSumma += int(line)
		else:
			if calSumma > topElfCal:
				topElfCal = calSumma
			calSumma = 0
print(topElfCal) 
