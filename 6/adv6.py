def isStartOfPacket(InputList):
	found_SoP = True
	for i in range(len(InputList)-1):
		test_ch = InputList.pop()
		if test_ch in InputList:
			found_SoP = False
			break
	return found_SoP
	
with open('input6.txt') as messages:
	for message in messages:
		search_window = []
		letter_count = 0
		for letter in message:
			search_window.append(letter)
			letter_count += 1
			if letter_count >4:
				search_window.pop(0)
			if letter_count >= 4:
				if isStartOfPacket(search_window.copy()):
					print(letter_count)
					break