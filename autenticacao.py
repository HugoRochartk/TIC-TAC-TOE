import server as sv



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
		print("4 - Sair")
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
		else:
			sv.stop()
			sv.take_info_into_dic()
			break


