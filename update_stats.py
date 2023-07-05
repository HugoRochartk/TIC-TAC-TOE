import menu_actions as act
import csv


def create_line(line_splitted):
	res = ""
	for piece in line_splitted:
		res += f"{piece},"
	res = res[:-1]
	return res


def update_draw_counter(User1, User2):
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
	
	
def update_victory_counter(winner, loser):
	lines = act.readlines()
	new_lines = []
	
	count = 0
	for line in lines:
		aux = line.split(",")  #user,pw,l,v,e,d,mh
		if count:
			if aux[0] == winner:
				aux[3] = str(int(aux[3]) + 1) 
				new_lines.append(create_line(aux))
			elif aux[0] == loser:
				aux[5] = str(int(aux[5]) + 1)
				new_lines.append(create_line(aux))
			else:
				new_lines.append(line)
		else:
			new_lines.append(line)
		count+=1
	act.overwrite(new_lines)



def push_empty(char, string):
	res = string[:-2]
	res += f"{char}]\n"
	return res



def push(char, string):
	res = string[:-2]
	res += f";{char}]\n"
	return res



def push_full(char, string):
	res = "["
	for c in string[3:-2]:
		res += c
	res += f";{char}]\n"
	return res



def update_mh_draw(fst, snd):
	lines = act.readlines()
	new_lines = []
	
	count = 0
	for line in lines:
		aux = line.split(",")  #user,pw,l,v,e,d,mh
		if count:
			if aux[0] == fst or aux[0] == snd:
				if len(aux[6]) == 22:
					aux[6] = push_full('E', aux[6]) 
				elif len(aux[6]) == 3:
					aux[6] = push_empty('E', aux[6])
				else:
					aux[6] = push('E', aux[6])
				new_lines.append(create_line(aux))
			else:
				new_lines.append(line)
		else:
			new_lines.append(line)
		count+=1
	act.overwrite(new_lines)
	

def update_mh_victory(winner, loser):
	lines = act.readlines()
	new_lines = []
	
	count = 0
	for line in lines:
		aux = line.split(",")  #user,pw,l,v,e,d,mh
		print(aux)
		if count:
			if aux[0] == winner:
				if len(aux[6]) == 22:
					aux[6] = push_full('V', aux[6]) 
				elif len(aux[6]) == 3:
					aux[6] = push_empty('V', aux[6])
				else:
					aux[6] = push('V', aux[6])
				new_lines.append(create_line(aux))
			elif aux[0] == loser:
				if len(aux[6]) == 22:
					aux[6] = push_full('D', aux[6]) 
				elif len(aux[6]) == 3:
					aux[6] = push_empty('D', aux[6])
				else:
					aux[6] = push('D', aux[6])
				new_lines.append(create_line(aux))
			else:
				new_lines.append(line)
		else:
			new_lines.append(line)
		count+=1
	act.overwrite(new_lines)
	


def update_level(winner, loser):
	pass
	

def update_level_draw(fst, snd):
	pass
