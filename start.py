import keyboard
import os

from util import params, menu, up, down

if __name__ == '__main__':
	params.options = ['Hangman', 'Rock, Paper, Scissors!', 'Tic Tac Toe', 'Minesweeper']
	params.l = len(params.options)
	game = ['hangman', 'rock_paper_scissors', 'tic_tac_toe', 'minesweeper']

	def enter():
		if params.s == 1:
			os.system(f'cd arcade/{game[0]} && python __init__.py')
		elif params.s == 2:
			os.system(f'cd arcade/{game[1]} && python __init__.py')
		elif params.s == 3:
			os.system(f'cd arcade/{game[2]} && python __init__.py')
		else:
			os.system(f'cd arcade/{game[3]} && python __init__.py')
		
	menu()
	keyboard.add_hotkey('up', up)
	keyboard.add_hotkey('down', down)
	keyboard.add_hotkey('enter', enter)
	keyboard.wait('enter')