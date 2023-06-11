import server as sv
from game import start_game



def separate():
	print('-------------------------------------')


def menu_login():
	users_logged_in = list()
	sv.start()

	while True:
		separate()
		print('\n\n')
		if len(users_logged_in) == 2:
			start_game(users_logged_in)
			break
		print("1 - Registar uma conta")
		print("2 - Login")
		print("3 - Fechar conta")
		print("4 - Sair")
		print('\n\n')

		opt = int(input('Opção: '))
		if opt == 1:
			separate()
			sv.register()
		elif opt == 2:
			separate()
			(flag, usern) = sv.login()
			if flag:
				users_logged_in.append(usern)
		elif opt == 3:
			separate()
			sv.close()
		else:
			sv.stop()
			sv.take_info_into_dic()
			break


