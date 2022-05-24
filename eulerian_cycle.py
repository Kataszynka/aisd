def find_euler_cycle(adj_list, element, stack):
	previous = element
	first = True
	path = []
	while len(stack) != 0 or first:
		first = False
		while  len(adj_list[previous]) > 0:
			chosen = adj_list[previous][0]
			adj_list[previous].pop(0)
			adj_list[chosen].remove(previous)
			stack.append(chosen)
			previous = chosen
		previous = stack[len(stack)-1]
		path.append(stack.pop())
	path.append(path[0])
	print(path)