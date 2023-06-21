import menu_actions as act


def create_line(line_splitted):
	res = ""
	for piece in line_splitted:
		res += f"{piece},"
	res = res[:-1]
	return res


def update_draw(User1, User2):
	lines = act.readlines()
	new_lines = []
	
	count = 0
	for line in lines:
		aux = line.split(",")  #user,pw,l,v,e,d
		if (count and (aux[0] == User1 or aux[0] == User2)):
			aux[4] = str(int(aux[4]) + 1) 
			new_lines.append(create_line(aux))
		else:
			new_lines.append(line)
		count+=1
	act.overwrite(new_lines)
	
	
def update_victory(winner, loser):
	lines = act.readlines()
	new_lines = []
	
	count = 0
	for line in lines:
		aux = line.split(",")  #user,pw,l,v,e,d
		if count:
			if aux[0] == winner:
				aux[3] = str(int(aux[3]) + 1) 
				new_lines.append(create_line(aux))
			elif aux[0] == loser:
				aux[5] = (str(int(aux[5]) + 1) + '\n')
				new_lines.append(create_line(aux))
			else:
				new_lines.append(line)
		else:
			new_lines.append(line)
		count+=1
	act.overwrite(new_lines)