import csv
import game


'''class Player:
	def __init__(self, username_, passwd_):
		self.username = username_
		self.password = passwd_
	
	def __repr__(self):
		toString = f"Player: Username -> {self.username} | Pass -> {self.password}"
		return toString 
'''

logged_in = set()


def overwrite(lines, buf=""):
	with open("data/cache.csv", "w") as f:
		for line in lines:
			f.write(line)
		f.write(buf)
		f.close()



def remove_from_csv(user):
	count = 0
	with open("data/cache.csv", "r") as f:
		lines = f.readlines()
		for line in lines:
			if count == 0:
				pass
			else:
				line_splitted = line.split(",")
				user_to_compare = line_splitted[0]
				if user_to_compare == user:
					lines[count] = ""
			count+=1
	overwrite(lines)
	



def take_info_into_dic():
	res = {}
	with open("data/cache.csv") as f:
		info = csv.reader(f, delimiter=",")
		count = 0
		for row in info:
			if count:
				res[row[0]] = (row[1], int(row[2]), int(row[3]), int(row[4]), int(row[5]))
			count+=1
		f.close()
	return res


def readlines():
	with open("data/cache.csv", "r") as f:
		lines = f.readlines()
		if lines == []:
			lines = ['username,password,level,V,E,D,MatchHistory\n']
		f.close()
	return lines



def register():
	cache_info = take_info_into_dic()
	lines = readlines()
	usern = input('Username: ')
	if usern in cache_info:
		print("\nNão é possível criar conta. O username já existe.")
		overwrite(lines)
	else:
		passwd = input('Password: ')
		buffer = f"{usern},{passwd},1,0,0,0,[]\n"
		overwrite(lines, buffer)
		print("\nConta criada com sucesso.")
	
			


def login():
	cache_info = take_info_into_dic()
	usern = input('Username: ')
	if usern not in cache_info:
		print("\nNão é possível iniciar sessão. O username não existe.")
	else:
		passwd = input('Password: ')
		if passwd != cache_info[usern][0]:
			print("\nNão é possível iniciar sessão. A senha está incorreta.")
		else:
			if usern in logged_in:
				print("\nO utilizador já se encontra online.")
			else:
				logged_in.add(usern)
				print("\nLog-in efetuado com sucesso.")

	

def start_game():
	cache_info = take_info_into_dic()
	usern1 = input('Username 1: ')
	if usern1 not in cache_info:
		print("\nO jogador 1 não existe.")
	else:
		if usern1 not in logged_in:
				print("\nO jogador 1 não se encontra online.")
		else:
			usern2 = input('Username 2: ')
			if usern2 not in cache_info:
				print("\nO jogador 2 não existe.")
			else:
					if usern2 not in logged_in:
						print("\nO jogador 2 não se encontra online.")
					else:
						game.setup_game(usern1, usern2)

					

def close():
	cache_info = take_info_into_dic()
	usern = input('Username: ')
	if usern not in cache_info:
		print("\nO username não existe.")
	else:
		if usern not in logged_in:
				print("\nO username não se encontra online.")
		else:
			remove_from_csv(usern)





