import autenticacao as aut 
from pprint import pprint


def create_empty_map():
	map_ = [
			[' ', ' ', ' '], 
			[' ', ' ', ' '], 
			[' ', ' ', ' ']
			]

	return map_



def main():

	map_ = create_empty_map()
	aut.menu_login()


main()