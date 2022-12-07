folders = {}

def sizeOfDir(d_in):
	d_size = d_in[0]
	for d in d_in[1]:
		d_size += sizeOfDir(folders[d])
	return d_size
	
with open('input7.txt') as log:
	d_size = 0
	path = []
	d_sub = []
	listing = False
	
	for line in log:
		if line.startswith("$"):
			if listing:
				folders['/'.join(map(str,path))] = d_size, d_sub
				listing = False
				d_size = 0
				d_sub = []
				
			cmd = line.split()
			if cmd[1] == "cd":
				if cmd[2] == "..":
					path.pop()
				else:
					path.append(cmd[2])
			elif cmd[1] == "ls":
				listing = True
		else:
			ls_response = line.split()
			if ls_response[0] == 'dir':
				d_sub.append('/'.join(map(str,path))+'/'+ls_response[1])
			else:
				d_size += int(ls_response[0])
	if listing:
		folders['/'.join(map(str,path))] = d_size, d_sub

#print(folders)

answer = 0
for f in folders:

	d_size = sizeOfDir(folders[f])
	if d_size <= 100000:
		answer += d_size
		
print(answer)