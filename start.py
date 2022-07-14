import keyboard
import os

from util import params, menu, up, down

if __name__ == '__main__':
	params.options = ['Hangman', 'Rock, Paper, Scissors!', 'Tic Tac Toe', 'Minesweeper']
	params.l = len(params.options)
	game = ['hangman', 'rock_paper_scissors', 'tic_tac_toe', 'minesweeper']

	def enter():
		for i in range(1, len(game)):
			if params.s == i:
				os.system(f'cd arcade/{game[i - 1]} && python __init__.py')
		
	menu()
	keyboard.add_hotkey('up', up)
	keyboard.add_hotkey('down', down)
	keyboard.add_hotkey('enter', enter)
	keyboard.wait('enter')