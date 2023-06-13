from random import choice
from time import sleep


def separate():
	print('-------------------------------------')


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
	


	

def start_game(player1, player2):
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
	print(f'O símbolo \'{sndplayer_symbol}\' está associado a {snd_player}.')
       
	map_ = create_empty_map()
	sleep(2)
	print('\n')
	separate()
	print_map(map_)




