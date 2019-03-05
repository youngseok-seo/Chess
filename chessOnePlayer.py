from chessAI import *
from chessSolver import *
from time import time



print('Welcome to Chess!')

board = genBoard()


while True:
	colour = input('Pick a colour: (white = 1/ black = 2)\n')

	if colour == 1:
		player = 10
		computer = 20
		break
	elif colour == 2:
		player = 20
		computer = 10
		break
	else:
		print('Invalid entry. Please ensure that you enter exactly as shown below.')

while True:

	#PLAYER

	printBoard(board, player)

	#take in user input, check if valid

	print('*PLAYER*')

	while True:

		curr = input('Please enter the current position of the piece you would like to move.\n')
		
		if (0 <= curr < 64) and (p(board[curr]) == player):
			
			pmoves = GetPieceLegalMoves(board, curr)
			
			if len(pmoves) > 0:
				print('Here are your possible moves: ' + str(pmoves))
				break 
			else: 
				print('There are no possible moves.')

		else:
			print('Position not available.')


	while True:

		new = input('Where would you like to play?\n')

		valid = False
		for move in pmoves:
			if move == new:
				valid = True

		if valid == True:
			break
		else:
			print('Illegal move.')

	#make move on board 

	placePiece(board, curr, new)

	#check for end of game

	win = True
	for square in board:
		if square == computer + 5:
			win = False

	if win == True:
		printBoard(board, player)
		print('Player wins!')
		break
	

	#COMPUTER


	print('*COMPUTER*')
	print('Calculating...')

	startTime = time()

	#calculate optimal move

	cmove = minimax(board, -999999, 999999, 4, computer)

	curr = cmove[0][0] 
	new = cmove[0][1]

	#make move on board

	placePiece(board, curr, new)

	runtime = str(time() - startTime)
	print('time elapsed: ', runtime)

	#check for end of game

	win = True
	for square in board:
		if square == computer + 5:
			win = False

	if win == True:
		printBoard(board, computer)
		print('Computer wins!')
		break
	
