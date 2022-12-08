tree = []

with open('input8.txt') as tree_map:
	for line in tree_map:
		tree.append([int(c) for c in list(line.strip('\n'))])

rows = len(tree)
columns = len(tree[0])

num_visible = 0
for i in range(1,rows-1):
	for j in range(1,columns-1):
		v_left = True
		for l in range(j-1,-1,-1):
			if tree[i][l] >= tree[i][j]:
				v_left = False

		v_right = True
		for r in range(j+1,columns):
			if tree[i][r] >= tree[i][j]:
				v_right = False

		v_upp = True
		for u in range(i-1,-1,-1):
			if tree[u][j] >= tree[i][j]:
				v_upp = False

		v_down = True
		for d in range(i+1,rows):
			if tree[d][j] >= tree[i][j]:
				v_down = False

		if v_left or v_right or v_upp or v_down:
			num_visible += 1


print(num_visible+2*columns+ 2*(rows-2))