prioritySum = 0

# bit flag for each letter [Z..Az..a] stored in an integer
def getItemFlag(in_char):
	if ord(in_char) >= ord('a'):
		return 0b1 << (ord(in_char)-ord('a'))
	else:
		return 0b1 << (ord(in_char)-ord('A')+26)
	
def getAllFlags(allItems):
	itemFlags = 0
	for item in allItems:
		itemFlags |= getItemFlag(item)
	return itemFlags
		
with open('input3.txt') as backPack:
	groupCounter = 0
	badgeFlag = 0
	
	for items in backPack:
		if groupCounter == 0:
			badgeFlag = getAllFlags(items.replace('\n',''))
		else:
			badgeFlag &= getAllFlags(items.replace('\n',''))
		
		if groupCounter == 2:
			priorityValue = 0
			while badgeFlag != 0:
				priorityValue += 1
				badgeFlag >>= 1				
			prioritySum += priorityValue
				
		groupCounter = (groupCounter+1)%3
		
print(prioritySum)
