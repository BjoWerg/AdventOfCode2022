def order_ok(list_1,list_2):
	print(list_1, 'vs',list_2)
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

		print(left,right)
		
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

	return result

input_file = open("input13b.txt",'r')
line = 'start'
ok_pairs = []
pair_nr = 1
ok_sum = 0 
while line != '':
	print(f' === {pair_nr} === ')
	list_1 = eval(input_file.readline().strip('\n'))
	list_2 = eval(input_file.readline().strip('\n'))
	r = order_ok(list_1,list_2)
	print(r)
	if r != 'False':
		ok_pairs.append(pair_nr)
		ok_sum += pair_nr
	line = input_file.readline()
	pair_nr += 1

print(ok_sum, ok_pairs)
