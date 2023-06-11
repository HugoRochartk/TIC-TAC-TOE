def create_empty_map():
	map_ = [
			[' ', ' ', ' '], 
			[' ', ' ', ' '], 
			[' ', ' ', ' ']
			]

	return map_
	

def start_game(players):
	print(f"começar entre {players[0]} e {players[1]}. são {len(players)} jogadores.")