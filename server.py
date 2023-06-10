import csv
import autenticacao as aut

'''class Player:
	def __init__(self, username_, passwd_):
		self.username = username_
		self.password = passwd_
	
	def __repr__(self):
		toString = f"Player: Username -> {self.username} | Pass -> {self.password}"
		return toString 
'''

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
	pass

def close():
	pass



data = []
stop = False

def stop():
	stop = True

def start():

	while not stop:
		pass

		



