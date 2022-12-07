folders = {}


class folder:
	def __init__(self,name,size,subfolders):
		self.name = name
		self.size = size
		self.subfolders = subfolders

	def sizeOf():
		d_size = self.size
		for f in subfolders:
			d_size += f.sizeOf()
		return d_size
	
with open('input7.txt') as log:
	d_size = 0
	d_curr = ''
	d_sub = []
	listing = False
	
	for line in log:
		if line.startswith("$"):
			if listing:
				if not d_curr in folders:
					folders[d_curr] = d_size, d_sub
				else:
					print("Double name:", d_curr)
				listing = False
				d_size = 0
				d_sub = []
				
			cmd = line.split()
			if cmd[1] == "cd" and cmd[2] != "..":
				d_curr = cmd[2]
			elif cmd[1] == "ls":
				listing = True
		else:
			ls_response = line.split()
			if ls_response[0] == 'dir':
				d_sub.append(ls_response[1])
			else:
				d_size += int(ls_response[0])
	if listing:
		folders[d_curr] = d_size, d_sub
		
answer = 0
for f in folders:

	d_size = sizeOfDir(folders[f])
	if d_size <= 100000:
		answer += d_size
		
print(answer)