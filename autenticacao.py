class Player:
	def __init__(self, username_, passwd_):
		self.username = username_
		self.password = passwd_
	
	def __repr__(self):
		conas = f"Player: Username -> {self.username} | Pass -> {self.password}"

		return conas 

players = []

def separate():
	print('-------------------------------------')

def menu_login():

	print("1 - Registar uma conta")
	print("2 - Login")
	print("3 - Fechar conta")
	print("4 - Sair")
	print('\n\n')

	opt = int(input('Opção: '))
	if opt == 1:
		separate()
		register()
	elif opt == 2:
		separate()
		login()
	elif opt == 3:
		separate()
		close()
	else:
		pass

def register():
	usern = input('Username: ')
	passwd = input('Password: ')


	p1 = Player(usern, passwd)
	players.append(p1)


def login():
	pass

def close():
	pass

def autentica(Player):
	pass