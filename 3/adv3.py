prioritySum = 0

# bit flag for each letter [Z..Az..a] stored in an integer
def getItemFlag(in_char):
	if ord(in_char) >= ord('a'):
		return 0b1 << (ord(in_char)-ord('a'))
	else:
		return 0b1 << (ord(in_char)-ord('A')+26)

def findPriorityValue(allItems):
	itemsInCompartment1 = allItems[:len(allItems)//2]
	itemFlags1 = 0
	for item in itemsInCompartment1:
		itemFlags1 |= getItemFlag(item)
	
	itemsInCompartment2 = allItems[len(allItems)//2:]
	itemFlags2 = 0
	for item in itemsInCompartment2:
		itemFlags2 |= getItemFlag(item)
	
	errorFlag = itemFlags1 & itemFlags2
	
	priorityVal = 0
	while errorFlag != 0:
		priorityVal += 1
		errorFlag >>= 1
	
	return priorityVal


with open('input3.txt') as backPack:
	for items in backPack:
		prioritySum += findPriorityValue(items.replace('\n',''))

print(prioritySum)
