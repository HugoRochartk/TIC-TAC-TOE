import csv


'''class Player:
	def __init__(self, username_, passwd_):
		self.username = username_
		self.password = passwd_
	
	def __repr__(self):
		toString = f"Player: Username -> {self.username} | Pass -> {self.password}"
		return toString 
'''

logged_in = {}


def take_info_into_dic():
	res = {}
	with open("data/cache.csv") as f:
		info = csv.reader(f, delimiter=",")
		count = 0
		for row in info:
			if count:
				res[row[0]] = row[1]
			count+=1
		f.close()
	return res


def readlines():
	with open("data/cache.csv", "r") as f:
		lines = f.readlines()
		if lines == []:
			lines = ['username,password\n']
		f.close()
	return lines



def overwrite(lines, buf=""):
	with open("data/cache.csv", "w") as f:
		for line in lines:
			f.write(line)
		f.write(buf)
		f.close()


def register():
	cache_info = take_info_into_dic()
	lines = readlines()
	usern = input('Username: ')
	if usern in cache_info:
		print("\nNão é possível criar conta. O username já existe.")
		overwrite(lines)
	else:
		passwd = input('Password: ')
		buffer = f"{usern},{passwd}\n"
		overwrite(lines, buffer)
		print("\nConta criada com sucesso.")
	
			


def login():
	cache_info = take_info_into_dic()
	usern = input('Username: ')
	if usern not in cache_info:
		print("\nNão é possível iniciar sessão. O username não existe.")
		return (0, -1)
	else:
		passwd = input('Password: ')
		if passwd != cache_info[usern]:
			print("\nNão é possível iniciar sessão. A senha está incorreta.")
			return (0, -1)
		else:
			if usern in logged_in:
				print("\nO utilizador já se encontra online.")
				return (0, -1)
			else:
				logged_in[usern] = True
				print("\nLog-in efetuado com sucesso.")
				return (1, usern)
	



def close():
	pass


stop = False


def stop():
	stop = True


def start():

	while not stop:
		pass

		



