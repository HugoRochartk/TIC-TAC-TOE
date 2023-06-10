'''class Player:
	def __init__(self, username_, passwd_):
		self.username = username_
		self.password = passwd_
	
	def __repr__(self):
		toString = f"Player: Username -> {self.username} | Pass -> {self.password}"
		return toString 
'''

def readlines():
	with open("data/cache.csv", "r") as f:
		lines = f.readlines()
		if lines == []:
			lines = ['username,password\n']
		f.close()
	return lines, f

def overwrite(f, lines, buf):
	with open("data/cache.csv", "w") as f:
		for line in lines:
			f.write(line)
		f.write(buf)
		f.close()


def register():
	usern = input('Username: ')
	passwd = input('Password: ')

	buf = f"{usern},{passwd}\n"

	lines, f = readlines()
	overwrite(f, lines, buf)
	
			


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

		



