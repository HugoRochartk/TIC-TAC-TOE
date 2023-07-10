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
	

def convert_mh_to_list(mh):
	if mh == "[]":
		return []
	elif len(mh) == 3:
		return [mh[1]]
	else:
		#[V;E;D;D]   [V;D]
		aux = mh.split(";")
		res = []
		for s in aux:
			if len(s) == 2:
				if s[0] == '[':
					res.append(s[1])
				else:
					res.append(s[0])
			else:
				res.append(s)
		return res
			


def update_level_csv(winner, loser, r):
	count = 0
	to_return = 0;

	if r == (0,-1):

		new_lines = []
		with open("data/cache.csv", "r") as f:
			lines = f.readlines()
			for line in lines:
				if count:
					aux = line.split(",")
					if aux[0] == loser:
						if aux[2] != "1":
							aux[2] = str(int(aux[2]) - 1)
							new_lines.append(create_line(aux))
							count += 1
						else:
							new_lines.append(line)
							count += 1
					else:
						new_lines.append(line)
						count += 1
				else:
					new_lines.append(line)
					count += 1
			act.overwrite(new_lines)	
			f.close()

	elif r == (1, 0):

		new_lines = []
		with open("data/cache.csv", "r") as f:
			lines = f.readlines()
			for line in lines:
				if count:
					aux = line.split(",")
					if aux[0] == winner:
						aux[2] = to_return = str(int(aux[2]) +  1)
						new_lines.append(create_line(aux))
						count += 1
					else:
						new_lines.append(line)
						count += 1
				else:
					new_lines.append(line)
					count += 1
			act.overwrite(new_lines)	
			f.close()

	else:

		new_lines = []
		with open("data/cache.csv", "r") as f:
			lines = f.readlines()
			for line in lines:
				if count:
					aux = line.split(",")
					if aux[0] == winner:
						aux[2] = to_return = str(int(aux[2]) +  1)
						new_lines.append(create_line(aux))
						count += 1
					elif aux[0] == loser:
						if aux[2] != "1":
							aux[2] = str(int(aux[2]) -  1)
							new_lines.append(create_line(aux))
							count += 1
						else:
							new_lines.append(line)
							count += 1
					else:
						new_lines.append(line)
						count += 1
				else:
					new_lines.append(line)
					count += 1
			act.overwrite(new_lines)	
			f.close()
	return to_return



	



def update_level(winner, loser):
	
	mhw = convert_mh_to_list(act.get_mh(winner))
	mhl = convert_mh_to_list(act.get_mh(loser))
	r = (0,0)
	#0 - dont change, 1- level up, -1- level down
	if len(mhw) < 3:
		if len(mhl) < 3:
			r = (0, 0)
		else:
			if mhl[-1] == 'D' and mhl[-1] == mhl[-2] == mhl[-3]:
				r = (0, -1)
			else:
				r = (0, 0)
	else:
		if len(mhl) < 3:
			if mhw[-1] == 'V' and mhw[-1] == mhw[-2] == mhw[-3]:
					r = (1, 0)
			else:
				r = (0, 0)
		else:
			if mhw[-1] == 'V' and mhw[-1] == mhw[-2] == mhw[-3]:
				if mhl[-1] == 'D' and mhl[-1] == mhl[-2] == mhl[-3]:
					r = (1, -1)
				else:
					r = (1, 0)
			else:
				if mhl[-1] == 'D' and mhl[-1] == mhl[-2] == mhl[-3]:
					r = (0, -1)
				else:
					r = (0, 0)

	if r == (0,0):
		return r
	else:
		aux = update_level_csv(winner, loser, r)
		return (r, aux)
	






def update_level_draw_csv(fst, snd, r):
	count = 0
	to_return_fst = to_return_snd = 0;

	if r == (0,-1):

		new_lines = []
		with open("data/cache.csv", "r") as f:
			lines = f.readlines()
			for line in lines:
				if count:
					aux = line.split(",")
					if aux[0] == snd:
						if aux[2] != "1":
							aux[2] = str(int(aux[2]) - 1)
							new_lines.append(create_line(aux))
							count += 1
						else:
							new_lines.append(line)
							count += 1
					else:
						new_lines.append(line)
						count += 1
				else:
					new_lines.append(line)
					count += 1
			act.overwrite(new_lines)	
			f.close()

	elif r == (1, 0):

		new_lines = []
		with open("data/cache.csv", "r") as f:
			lines = f.readlines()
			for line in lines:
				if count:
					aux = line.split(",")
					if aux[0] == fst:
						aux[2] = to_return_fst = str(int(aux[2]) +  1)
						new_lines.append(create_line(aux))
						count += 1
					else:
						new_lines.append(line)
						count += 1
				else:
					new_lines.append(line)
					count += 1
			act.overwrite(new_lines)	
			f.close()

	elif r == (1, -1):

		new_lines = []
		with open("data/cache.csv", "r") as f:
			lines = f.readlines()
			for line in lines:
				if count:
					aux = line.split(",")
					if aux[0] == fst:
						aux[2] = to_return_fst = str(int(aux[2]) +  1)
						new_lines.append(create_line(aux))
						count += 1
					elif aux[0] == snd:
						if aux[2] != "1":
							aux[2] = str(int(aux[2]) -  1)
							new_lines.append(create_line(aux))
							count += 1
						else:
							new_lines.append(line)
							count += 1
					else:
						new_lines.append(line)
						count += 1
				else:
					new_lines.append(line)
					count += 1
			act.overwrite(new_lines)	
			f.close()

	elif r == (1, 1):

		new_lines = []
		with open("data/cache.csv", "r") as f:
			lines = f.readlines()
			for line in lines:
				if count:
					aux = line.split(",")
					if aux[0] == fst:
						aux[2] = to_return_fst = str(int(aux[2]) +  1)
						new_lines.append(create_line(aux))
						count += 1
					elif aux[0] == snd:
						if aux[2] != "1":
							aux[2] = to_return_snd = str(int(aux[2]) +  1)
							new_lines.append(create_line(aux))
							count += 1
						else:
							new_lines.append(line)
							count += 1
					else:
						new_lines.append(line)
						count += 1
				else:
					new_lines.append(line)
					count += 1
			act.overwrite(new_lines)	
			f.close()

	elif r == (0, 1):

		new_lines = []
		with open("data/cache.csv", "r") as f:
			lines = f.readlines()
			for line in lines:
				if count:
					aux = line.split(",")
					if aux[0] == snd:
						if aux[2] != "1":
							aux[2] = to_return_snd = str(int(aux[2]) + 1)
							new_lines.append(create_line(aux))
							count += 1
						else:
							new_lines.append(line)
							count += 1
					else:
						new_lines.append(line)
						count += 1
				else:
					new_lines.append(line)
					count += 1
			act.overwrite(new_lines)	
			f.close()
	

	elif r == (-1, 0):

		new_lines = []
		with open("data/cache.csv", "r") as f:
			lines = f.readlines()
			for line in lines:
				if count:
					aux = line.split(",")
					if aux[0] == fst:
						if aux[2] != "1":
							aux[2] =  str(int(aux[2]) -  1)
							new_lines.append(create_line(aux))
							count += 1
						else:
							new_lines.append(line)
							count += 1
					else:
						new_lines.append(line)
						count += 1
				else:
					new_lines.append(line)
					count += 1
			act.overwrite(new_lines)	
			f.close()

	elif r == (-1, -1):

		new_lines = []
		with open("data/cache.csv", "r") as f:
			lines = f.readlines()
			for line in lines:
				if count:
					aux = line.split(",")
					if aux[0] == fst:
						if aux[2] != "1":
							aux[2] = str(int(aux[2]) -  1)
							new_lines.append(create_line(aux))
							count += 1
						else:
							new_lines.append(line)
							count += 1
					elif aux[0] == snd:
						if aux[2] != "1":
							aux[2] = str(int(aux[2]) -  1)
							new_lines.append(create_line(aux))
							count += 1
						else:
							new_lines.append(line)
							count += 1
					else:
						new_lines.append(line)
						count += 1
				else:
					new_lines.append(line)
					count += 1
			act.overwrite(new_lines)	
			f.close()

	elif r == (-1, 1):

		new_lines = []
		with open("data/cache.csv", "r") as f:
			lines = f.readlines()
			for line in lines:
				if count:
					aux = line.split(",")
					if aux[0] == fst:
						if aux[2] != "1":
							aux[2] = str(int(aux[2]) -  1)
							new_lines.append(create_line(aux))
							count += 1
						else:
							new_lines.append(line)
							count += 1
					elif aux[0] == snd:
						if aux[2] != "1":
							aux[2] = to_return_snd = str(int(aux[2]) +  1)
							new_lines.append(create_line(aux))
							count += 1
						else:
							new_lines.append(line)
							count += 1
					else:
						new_lines.append(line)
						count += 1
				else:
					new_lines.append(line)
					count += 1
			act.overwrite(new_lines)	
			f.close()

	return to_return_fst, to_return_snd

	






def update_level_draw(fst, snd):
	mh1 = convert_mh_to_list(act.get_mh(fst))
	mh2 = convert_mh_to_list(act.get_mh(snd))
	r = (0,0)

	if 'D' not in mh1 and len(mh1) == 10:
		if 'D' not in mh2 and len(mh1) == 10:
			r = (1,1)
		else:
			if mh2.count('D') >= 5:
				r = (1, -1)
			else:
				r = (1, 0)
	else:
		if mh1.count('D') >= 5:
			if 'D' not in mh2 and len(mh1) == 10:
				r = (-1, 1)
			else:
				if mh2.count('D') >= 5:
					r = (-1, -1)
				else:
					r = (-1, 0)
		else:
			if 'D' not in mh2 and len(mh1) == 10:
				r = (0, 1)
			else:
				if mh2.count('D') >= 5:
					r = (0, -1)
				else:
					r = (0, 0)


	if r == (0,0):
		return r
	else:
		aux1, aux2 = update_level_draw_csv(fst, snd, r)
		return (r, aux1, aux2)






