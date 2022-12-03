top1ElfCal = 0
top2ElfCal = 0
top3ElfCal = 0

calSumma = 0

with open('input.txt') as input:
	for line in input:
		if line != '\n':
			calSumma += int(line)			
		else:
			if calSumma > top3ElfCal:
				if calSumma > top2ElfCal:
					top3ElfCal = top2ElfCal
					if calSumma > top1ElfCal:
						top2ElfCal = top1ElfCal				
						top1ElfCal = calSumma
					else:
						top2ElfCal = calSumma
				else:
					top3ElfCal = calSumma
			calSumma = 0 
print(top1ElfCal+top2ElfCal+top3ElfCal) 
