import re

class Monkey:
	def __init__(self, items, op, op_val, test, t_true, t_false):
		self.items = items
		self.op = op
		self.op_val = op_val
		self.test = test
		self.t_true = t_true
		self.t_false = t_false
		self.count = 0
	
	def Catch(self,item):
		self.items.append(item)
	
	def Inspect(self):
		if len(self.items) > 0:
			self.count += 1
			item = self.items.pop(0)
			if self.op_val == 'old':
				val = item
			else:
				val = int(self.op_val)
				
			if self.op == '*':
				 item = int((item * val)/3)
			else:
				 item = int((item + val)/3)
			
			if item%self.test == 0:
				return [self.t_true, item]
			else:
				return [self.t_false, item]
		else:
			return []
			
	def GetCount(self):
		return self.count
		
	def GetItems(self):
		return self.items

monkeys = []
input_file = open("input11.txt",'r')
line = input_file.readline()
while 'Monkey' in line:
	monkey_nr = int(re.findall( '(\d+)', line )[0])
	items = [int(i) for i in re.findall( '(\d+)', input_file.readline())]
	line = input_file.readline()
	operation = line.split()
	operator = operation[4]
	operation_value = operation[5]
	test = int(re.findall( '(\d+)', input_file.readline() )[0])
	test_true = int(re.findall( '(\d+)', input_file.readline() )[0])
	test_false = int(re.findall( '(\d+)', input_file.readline() )[0])
	line = input_file.readline()
	monkeys.append(Monkey(items,operator,operation_value,test,test_true,test_false))
	if line == '\n':
		line = input_file.readline()

for round in range(1,21):
	for monkey in monkeys:
		throw = monkey.Inspect()
		while len(throw) > 0:
			monkeys[throw[0]].Catch(throw[1])
			throw = monkey.Inspect()
	
	print(f'After round {round}, the monkeys are holding items with these worry levels:')
	for m in range(len(monkeys)):
		print(f'Monkey {m}: ', monkeys[m].GetItems())
	print('')

inspections = []
for m in range(len(monkeys)):
	inspections.append(monkeys[m].GetCount())
	print(f'Monkey {m}: inspected items {monkeys[m].GetCount()} times')
inspections.sort(reverse=True)
print('monkey business:',inspections[0]*inspections[1])