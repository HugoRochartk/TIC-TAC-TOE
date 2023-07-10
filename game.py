from random import choice
from time import sleep
from update_stats import update_victory_counter, update_draw_counter, update_level, update_level_draw, update_mh_draw, update_mh_victory

def separate():
	print('-----------------------------------------------------------')


def create_empty_map():
	map_ = [
			[' ', ' ', ' '], 
			[' ', ' ', ' '], 
			[' ', ' ', ' ']
			]

	return map_


def print_map(map):
	print("\n   1   2   3")
	for i,row in enumerate(map):
		print(f"{i+1}  {row[0]}   {row[1]}   {row[2]}\n")
	


def is_full(Map):
	for row in Map:
		for symbol in row:
			if symbol != ' ':
				pass
			else:
				return False
	return True


def check_victory(Map, symbol):
	if Map[0][0] == Map[0][1] == Map[0][2] == symbol:
		return True
	elif Map[1][0] == Map[1][1] == Map[1][2] == symbol:
		return True
	elif Map[2][0] == Map[2][1] == Map[2][2] == symbol:
		return True
	elif Map[0][0] == Map[1][0] == Map[2][0] == symbol:
		return True
	elif Map[0][1] == Map[1][1] == Map[2][1] == symbol:
		return True
	elif Map[0][2] == Map[1][2] == Map[2][2] == symbol:
		return True
	elif Map[0][0] == Map[1][1] == Map[2][2] == symbol:
		return True
	elif Map[0][2] == Map[1][1] == Map[2][0] == symbol:
		return True
	else:
		return False



def check_draw(Map, Symbol1, Symbol2):
	if is_full(Map) and check_victory(Map, Symbol1) == check_victory(Map, Symbol2) == False:
		return True
	else:
		return False

	


def game(FstPlayerInfo, SndPlayerInfo):
	count = 0
	draw = False
	victory = False
	fst_player, fstplayer_symbol = FstPlayerInfo
	snd_player, sndplayer_symbol = SndPlayerInfo
	last_player = snd_player
	Map = create_empty_map()
	while ((not draw) and (not victory)):
		count += 1
		sleep(1)
		separate()
		print('\n')
		print_map(Map)
		if last_player == snd_player:
			print(f"\nÉ a vez de {fst_player}, escolha a linha e a coluna onde deseja jogar:")
			symbol = fstplayer_symbol
			last_player = fst_player
		else:
			print(f"\nÉ a vez de {snd_player}, escolha a linha e a coluna onde deseja jogar:")
			symbol = sndplayer_symbol
			last_player = snd_player
		row = int(input("Linha: "))
		if row < 1 or row > 3:
			print('\nNúmero de linha inválido, o número deve ser entre 1 e 3 (inclusive). Escolha outro.')
			count -= 1
			if last_player == fst_player:
				last_player = snd_player
			else:
				last_player = fst_player
		else:
			column = int(input("Coluna: "))
			if column < 1 or column > 3:
				print('\nNúmero de coluna inválido, o número deve ser entre 1 e 3 (inclusive). Escolha outro.')
				count -= 1
				if last_player == fst_player:
					last_player = snd_player
				else:
					last_player = fst_player
			else:
				if Map[row-1][column-1] != ' ':
					print('\nA posição já se encontra preenchida, coloque outra.')
					count -= 1
					if last_player == fst_player:
						last_player = snd_player
					else:
						last_player = fst_player
				else:
					Map[row-1][column-1] = symbol
					if count >= 3:
						victory = check_victory(Map, symbol)
					if count == 9:
						draw = check_draw(Map, fstplayer_symbol, sndplayer_symbol)
	if draw:
		sleep(1)
		separate()
		print('\n')
		print_map(Map)
		print("Empate!!")
		update_draw_counter(fst_player, snd_player)
		update_mh_draw(fst_player, snd_player)
		tup = update_level_draw(fst_player, snd_player)
		if tup[0][0] == 1:
			if tup[0][1] == 1:
				print(f"\nParabéns {fst_player}, subiste para o nível {tup[1]}!")
				print(f"\nParabéns {snd_player}, subiste para o nível {tup[2]}!")
			else:
				print(f"\nParabéns {fst_player}, subiste para o nível {tup[1]}!")
		else:
			if tup[0][1] == 1:
				print(f"\nParabéns {snd_player}, subiste para o nível {tup[2]}!")


	else:
		sleep(1)
		separate()
		print('\n')
		print_map(Map)
		if symbol == FstPlayerInfo[1]:
			print(f"Parabéns {fst_player}, venceste!")
			update_victory_counter(fst_player, snd_player)
			update_mh_victory(fst_player, snd_player)
			tup = update_level(fst_player, snd_player)
			if tup[0][0] == 1:
				print(f"\nParabéns {fst_player}, subiste para o nível {tup[1]}!")
		elif symbol == SndPlayerInfo[1]:
			print(f'Parabéns {snd_player}, venceste!')
			update_victory_counter(snd_player, fst_player)
			update_mh_victory(snd_player, fst_player)
			tup = update_level(snd_player, fst_player)
			if tup[0][0] == 1:
				print(f"\nParabéns {snd_player}, subiste para o nível {tup[1]}!")


def setup_game(player1, player2):
	print(f'\nIniciando o jogo entre {player1} e {player2}...')
	sleep(2)
	print(f'\nGerando aleatoriamente o primeiro a jogar...')
	fst_player = choice([player1, player2])
	if fst_player == player1:
		snd_player = player2
	else:
		snd_player = player1
	sleep(2)
	print(f'\nO primeiro jogador a jogar é {fst_player}.\n')
	fstplayer_symbol = choice(['X', 'O'])
	if fstplayer_symbol == 'X':
		sndplayer_symbol = 'O'
	else:
		sndplayer_symbol = 'X'
	sleep(2)
	print(f'O símbolo \'{fstplayer_symbol}\' está associado a {fst_player}.')
	print(f'O símbolo \'{sndplayer_symbol}\' está associado a {snd_player}.\n')
	game((fst_player, fstplayer_symbol), (snd_player, sndplayer_symbol))






