import autenticacao as aut 
from pprint import pprint


def create_empty_map():
	map_ = [
			['x', ' ', ' '], 
			[' ', 'y', ' '], 
			['z', ' ', 'w']
			]

	return map_



def main():

	map_ = create_empty_map()
	pprint(map_)
	aut.menu_login()


main()