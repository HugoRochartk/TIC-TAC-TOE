import menu_actions as act


def separate():
	print('-------------------------------------')


def clear_input(input):
	res = input.replace(' ', "")
	res = res.replace('\t', "")
	return res

def menu_login():

	while True:
		separate()
		print('\n\n')
		print("1 - Registar uma conta")
		print("2 - Login")
		print("3 - Fechar conta")
		print("4 - Começar um jogo")
		print("5 - Sair")
		print('\n\n')

		opt = input('Opção: ')
		opt = clear_input(opt)
		if opt == "1":
			separate()
			act.register()
		elif opt == "2":
			separate()
			act.login()
		elif opt == "3":
			separate()
			act.close()
		elif opt == "4":
			separate()
			act.start_game()
		else:
			break


