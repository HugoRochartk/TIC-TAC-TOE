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
		print("3 - Logout")
		print("4 - Fechar conta")
		print("5 - Começar um jogo")
		print("6 - Ver nível de um jogador")
		print("7 - Ver estatísticas de um jogador")
		print("8 - Ver histórico de partidas de um jogador")
		print("9 - Sair")
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
			act.logout()
		elif opt == "4":
			separate()
			act.close()
		elif opt == "5":
			separate()
			act.start_game()
		elif opt == "6":
			separate()
			user = act.get_username_input()
			if user != -1:
				level = act.get_level(user)
				print(f'\nO jogador {user} está no nível {level}.')
		elif opt == "7":
			separate()
			user = act.get_username_input()
			if user != -1:
				stats = act.get_stats(user)
				print(f'\nVitórias: {stats[0]} | Empates: {stats[1]} | Derrotas: {stats[2]}')
		elif opt == "8":
			separate()
			user = act.get_username_input()
			if user != -1:
				mh = act.get_mh(user)
				print(f'Histórico de jogos ([Mais antigo, ..., Mais recente]): {mh}')
		else:
			break


