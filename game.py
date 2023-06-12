from random import choice
from time import sleep

def create_empty_map():
	map_ = [
			[' ', ' ', ' '], 
			[' ', ' ', ' '], 
			[' ', ' ', ' ']
			]

	return map_
	

def start_game(player1, player2):
	print(f'\nIniciando o jogo entre {player1} e {player2}...')
	sleep(2)
	print(f'\nGerando aleatoriamente o primeiro a jogar...')
	first_player = choice([player1, player2])
	sleep(2)
	print(f'\nO primeiro jogador a jogar é {first_player}.')
	map_ = create_empty_map()
