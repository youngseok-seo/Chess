from chessSolver import *

board = genBoard()

while True:

	#WHITE

	printBoard(board, 10)

	#take in user input, check if valid

	print('*WHITE*')

	while True:

		current = input('Please enter the current position of the piece you would like to move.\n')
		
		if (0 <= current < 64) and (p(board[current]) == 10):
			
			wmoves = GetPieceLegalMoves(board, current)
			
			if len(wmoves) > 0:
				print('Here are your possible moves: ' + str(wmoves))
				break 
			else: 
				print('There are no possible moves.')

		else:
			print('Position not available.')


	while True:

		new = input('Where would you like to play?\n')

		valid = True
		if new not in wmoves:
			valid = False

		if valid == True:
			break
		else:
			print('Illegal move.')

	#make changs to the board

	board[new] = board[current]
	board[current] = 0

	#check for end of game

	win = True
	for square in board:
		if square == 25:
			win = False

	if win == True:
		printBoard(board, 10)
		print('White wins!')
		break


	#BLACK

	printBoard(board, 20)

	#take in user input, check if valid

	print('*BLACK*')

	while True:

		current = input('Please enter the current position of the piece you would like to move.\n')
		
		if (0 <= current < 64) and (p(board[current]) == 20):
			
			bmoves = GetPieceLegalMoves(board, current)
			
			if len(bmoves) > 0:
				print('Here are your possible moves: ' + str(bmoves))
				break 
			else: 
				print('There are no possible moves.')

		else:
			print('Position not available.')


	while True:

		new = input('Where would you like to play?\n')

		valid = True
		if new not in bmoves:
			valid = False

		if valid == True:
			break
		else:
			print('Illegal move.')

	#make changs to the board

	board[new] = board[current]
	board[current] = 0

	#check for end of game

	win = True
	for square in board:
		if square == 15:
			win = False

	if win == True:
		printBoard(board, 20)
		print('Black wins!')
		break