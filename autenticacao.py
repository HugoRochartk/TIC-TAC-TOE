import server as sv
from game import start_game



def separate():
	print('-------------------------------------')


def menu_login():
	sv.start()

	while True:
		separate()
		print('\n\n')
		print("1 - Registar uma conta")
		print("2 - Login")
		print("3 - Fechar conta")
		print("4 - Começar um jogo")
		print("5 - Sair")
		print('\n\n')

		opt = int(input('Opção: '))
		if opt == 1:
			separate()
			sv.register()
		elif opt == 2:
			separate()
			sv.login()
		elif opt == 3:
			separate()
			sv.close()
		elif opt == 4:
			separate()
			sv.start_game()
		else:
			sv.stop()
			sv.take_info_into_dic()
			break


