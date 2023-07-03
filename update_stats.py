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


def update_mh_draw(fst, snd):
	pass

def update_mh_victory(winner, loser):
	pass



def get_level(Username):
	with open("data/cache.csv", "r") as f:
		info = csv.reader(f, delimiter=",")
		count = 0
		for row in info:
			if count and row[0] == Username:
				return int(row[2])
		f.close()
	


def update_level(winner, loser):
	pass
	

def update_level_draw(fst, snd):
	pass
