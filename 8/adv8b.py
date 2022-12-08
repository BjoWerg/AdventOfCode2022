tree = []

with open('input8.txt') as tree_map:
	for line in tree_map:
		tree.append([int(c) for c in list(line.strip('\n'))])

rows = len(tree)
columns = len(tree[0])

max_score = 0
for i in range(1,rows-1):
	for j in range(1,columns-1):
		v_left = 0
		for l in range(j-1,-1,-1):
			v_left += 1
			if tree[i][l] >= tree[i][j]:
				break;

		v_right = 0
		for r in range(j+1,columns):
			v_right += 1
			if tree[i][r] >= tree[i][j]:
				break

		v_upp = 0
		for u in range(i-1,-1,-1):
			v_upp += 1
			if tree[u][j] >= tree[i][j]:
				break

		v_down = 0
		for d in range(i+1,rows):
			v_down += 1
			if tree[d][j] >= tree[i][j]:
				break
				
		v_score = v_left*v_right*v_upp*v_down
		if v_score > max_score:
			max_score = v_score

print(max_score)