numRangesOverlapping = 0

def isOverlapping(lineOfPair):
	rangeOfsections = lineOfPair.split(',')
	range1 = rangeOfsections[0].split('-')
	range2 = rangeOfsections[1].split('-')
	if ((int(range2[0]) > int(range1[1])) or (int(range2[1]) < int(range1[0]))):
		return False
	else:
		return True

with open('input4.txt') as pairList:
	for pairs in pairList:
		if isOverlapping(pairs):
			numRangesOverlapping += 1

print(numRangesOverlapping)