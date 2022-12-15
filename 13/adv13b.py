def order_ok(list_1,list_2):
	if list_1 == [] and list_2 == []:
		result = 'Equal'
	else:
		result = 'True'
	
	for i in range(len(list_1)):
		if i == len(list_2):
			result = 'False'
			break
		
		left = list_1[i]
		right = list_2[i]

		if type(left) == int and type(right) == int:
			if left == right:
				result = 'Equal'
			elif left < right:
				result = 'True'
				break
			else:
				result = 'False'
				break
		else:
			if type(left) == int:
				left = [left]
			elif type(right) == int:
				right = [right]
			
			result = order_ok(left,right)
			if result != 'Equal':
				break
				
	if result == 'Equal' and len(list_1) < len(list_2):
		result = True
		
	return result

packets = []
with open('input13.txt') as file:
	for line in file:
		if line != '\n':
			packets.append(eval(line.strip('\n')))

packets.append([[2]])
packets.append([[6]])

done = False
while not done:
	done = True
	for i in range(len(packets)-1):
		if order_ok(packets[i],packets[i+1]) == 'False':
			temp_packet = packets[i]
			packets[i] = packets[i+1]
			packets[i+1] = temp_packet
			done = False

for i in range(len(packets)):
	print(packets[i])
	if packets[i] == [[2]]:
		pos_2 = i+1
	if packets[i] == [[6]]:
		pos_6 = i+1

print(f'Decoder key is {pos_2*pos_6}')
