from asyncio import _enter_task
import math
import time
import keyboard
from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
import sys
sys.path.insert(0, '..\..')
from util import up, down, difficulty, selected, get_selected

class TicTacToe:
	def __init__(self):
		self.board = self.make_board()
		self.current_winner = None # keep track of winner!

	@staticmethod
	def make_board():
		return [' ' for _ in range(9)] # we use a single list to rep a 3x3 board

	def print_board(self):
		for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
			print('| ' + ' | '.join(row) + ' |')

	@staticmethod
	def print_board_nums():
		# 0 | 1 | 2 etc (tells us what number corresponds to what box)
		number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
		for row in number_board:
			print('| ' + ' | '.join(row) + ' |')
	
	def available_moves(self):
		# ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
		return [i for i, spot in enumerate(self.board) if spot == ' ']

	def empty_squares(self):
		return ' ' in self.board # returns boolean

	def num_empty_squares(self):
		return self.board.count(' ')

	def make_move(self, square, letter):
		# if valid move, then make the move (assign square to letter)
		# then return true. if invalid, return false
		if self.board[square] == ' ':
			self.board[square] = letter
			if self.winner(square, letter):
				self.current_winner = letter
			return True
		return False

	def winner(self, square, letter):
		# if 3 in a row anywhere.. we have to check all of these!
		# check rows
		row_ind = math.floor(square / 3)
		row = self.board[row_ind*3 : (row_ind + 1) * 3]
		if all([spot == letter for spot in row]):
			return True

		# check columns
		col_ind = square % 3
		column = [self.board[col_ind+i*3] for i in range(3)]
		if all([spot == letter for spot in column]):
			return True

		# check diagonals
		# but only if the square is an even number (0,2,4,6,8)
		# these are the only moves possible to win a diagonal
		if square % 2 == 0:
			diagonal1 = [self.board[i] for i in [0, 4, 8]] # left to right diagonal
			if all([spot == letter for spot in diagonal1]):
				return True
			diagonal2 = [self.board[i] for i in [2, 4, 6]] # right to left diagonal
			if all([spot == letter for spot in diagonal2]):
				return True
		# if all of these fail
		return False


def play(game, x_player, o_player, print_game=True):
	# returns the winer of the game (letter)! or None for a tie
	if print_game:
		game.print_board_nums()

	letter = 'X' # starting letter
	# iterate while the game still has empty squares
	# (we don't have to worry about winner because we'll just return 
	# that which breaks the loop)
	while game.empty_squares():
		print("\n")
		# get move from the appropriate player
		if letter == 'O':
			square = o_player.get_move(game)
		else:
			square = x_player.get_move(game)

		if game.make_move(square, letter):
			if print_game:
				print(letter + f' makes a move to square {square}')
				game.print_board()
				print('') # just empty line

		if game.current_winner:
			if print_game:
				print(letter + ' wins!')
			return letter  # ends the loop and exits the game

		# after we made our move, we need to alternate letters
		letter = 'O' if letter == 'X' else 'X'
		time.sleep(0.8)
	if print_game:
		print('It\'s a tie!')

if __name__ == '__main__':
	x_player = HumanPlayer('X')
	#o_player = RandomComputerPlayer('O')

	def enter():
		global o_player
		if selected.s == 1:
			o_player = RandomComputerPlayer('O')
		elif selected.s == 2:
			o_player = GeniusComputerPlayer('O')
		else:
			o_player = HumanPlayer('O')
		
	difficulty()
	keyboard.add_hotkey('up', up)
	keyboard.add_hotkey('down', down)
	keyboard.add_hotkey('enter', enter)
	keyboard.wait('enter')

	t = TicTacToe()
	print(selected.s)
	play(t, x_player, o_player, print_game=True)