import re

class Item:
	
	def __init__(self,val):
		self.init_val = val
		self.tests = {}
		
	def AddTest(self,t):
		self.tests[t] = self.init_val % t

	def Test(self,t):
		return self.tests[t] == 0
		
	def Add(self,val):
		for key in self.tests.keys():
			self.tests[key] = (self.tests[key]+val)%key

	def Mutiply(self,val):
		for key in self.tests.keys():
			self.tests[key] = (self.tests[key]*val)%key

	def Sqr(self):
		for key in self.tests.keys():
			self.tests[key] = (self.tests[key]*self.tests[key])%key
		
class Monkey:
	def __init__(self, items, op, op_val, test, t_true, t_false):
		self.items = items
		self.op = op
		self.op_val = op_val
		self.test = test
		self.t_true = t_true
		self.t_false = t_false
		self.count = 0
	
	def ItemSetup(self,t_list):
		for test in t_list:
			for item in self.items:
				item.AddTest(test)
	
	def Catch(self,item):
		self.items.append(item)
	
	def Inspect(self):
		if len(self.items) > 0:
			self.count += 1
			item = self.items.pop(0)
			if self.op_val == 'old':
				item.Sqr()
			else:
				val = int(self.op_val)
				if self.op == '*':
					 item.Mutiply(val)
				else:
					 item.Add(val)
			
			if item.Test(self.test):
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
alltests = []

input_file = open("input11.txt",'r')
line = input_file.readline()
while 'Monkey' in line:
	monkey_nr = int(re.findall( '(\d+)', line )[0])
#	items = [int(i) for i in re.findall( '(\d+)', input_file.readline())]
	item_list = []
	for i in re.findall( '(\d+)', input_file.readline()):
		item_list.append(Item(int(i)))
	line = input_file.readline()
	operation = line.split()
	operator = operation[4]
	operation_value = operation[5]
	test = int(re.findall( '(\d+)', input_file.readline() )[0])
	alltests.append(test)
	test_true = int(re.findall( '(\d+)', input_file.readline() )[0])
	test_false = int(re.findall( '(\d+)', input_file.readline() )[0])
	line = input_file.readline()
	monkeys.append(Monkey(item_list,operator,operation_value,test,test_true,test_false))
	if line == '\n':
		line = input_file.readline()

for monkey in monkeys:
	monkey.ItemSetup(alltests)

for round in range(1,10001):
	for monkey in monkeys:
		throw = monkey.Inspect()
		while len(throw) > 0:
			monkeys[throw[0]].Catch(throw[1])
			throw = monkey.Inspect()
	
	if (round%1000 == 0) or (round == 1) or (round == 20):
		print(f'== After round {round} ==')
		inspections = []
		for m in range(len(monkeys)):
			inspections.append(monkeys[m].GetCount())
			print(f'Monkey {m}: inspected items {monkeys[m].GetCount()} times')

inspections.sort(reverse=True)
print('monkey business:',inspections[0]*inspections[1])