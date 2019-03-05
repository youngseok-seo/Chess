from chessSolver import *
from time import time


def evalBoard(board, player):

	evalsum = 0

	#evaluate board according to piece and its position on board

	queenEval = [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0,
				 -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0,
				 -1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0, 
				 -0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5,
				 0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5,
				 -1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0,
				 -1.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, -1.0,
				 -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0 ]

	bishopEval = [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0,
				  -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0,
				  -1.0, 0.0, 0.5, 1.0, 1.0, 0.5, 0.0, -1.0,
				  -1.0, 0.5, 0,5, 1.0, 1.0, 0.5, 0.5, -1.0,
				  -1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.0,
				  -1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0,
				  -1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0,
				  -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0 ]

	kingEval = [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
				-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
				-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
				-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
				-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0,
				-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0,
				2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0,
				2.0, 3.0,  1.0,  0.0,  0.0,  1.0,  3.0, 2.0 ]

	rookEval = [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
				0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5,
				-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
				-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
				-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
				-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
				-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
				0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.5 ]

	knightEval = [ -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0,
				-4.0, -2.0, 0.0, 0.0, 0.0, 0.0, -2.0, -4.0,
				-3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0,
				-3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.5, -3.0,
				-3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0,
				-3.0, 0.5, 1.0, 1.5, 1,5, 1.0, 0.5, -3.0,
				-4.0, -2.0, 0.0, 0.5, 0.5, 0.0, -2.0, -4.0,
				-5.0, -4.0, -3.0, -3.0, -3.0, -4.0, -5.0 ]

	pawnEval = [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
				5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0,
				1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0,
				0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5,
				0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0, 
				0.5, -0.5, -1.0, 0.0, 0.0, -1.0, -0.5, 0.5,
				0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5,
				0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ]


	x = 1

	#sum up all evaluations to obtain a score

	if player == 10:
		for i in range(1, 65, 1):

			if board[-i] == 10:
				evalsum += 10 + x*pawnEval[-i]
			elif board[-i] == 11:
				evalsum += 30 + x*knightEval[-i]
			elif board[-i] == 12:
				evalsum += 30 + x*bishopEval[-i]
			elif board[-i] == 13:
				evalsum += 50 + x*rookEval[-i]
			elif board[-i] == 14:
				evalsum += 90 + x*queenEval[-i]
			elif board[-i] == 15:
				evalsum += 900 + x*kingEval[-i]

	elif player == 20:
		for i in range(0, 64, 1):
			if board[i] == 20:
				evalsum -= 10 + x*pawnEval[i]
			elif board[i] == 21:
				evalsum -= 30 + x*knightEval[i]
			elif board[i] == 22:
				evalsum -= 30 + x*bishopEval[i]
			elif board[i] == 23:
				evalsum -= 50 + x*rookEval[i]
			elif board[i] == 24:
				evalsum -= 90 + x*queenEval[i]
			elif board[i] == 25:
				evalsum -= 900 + x*kingEval[i]

	return evalsum


def placePiece(board, piece, move):

	#helper function 1: places piece in designated position

	board[move] = board[piece]
	board[piece] = 0


def isMaximizingPlayer(player):

	#helper function 2: determines whether player is a Max/Min player

	if player==10:
		return True
	if player==20:
		return False


def minimax(board, a, b, depth, player):
	
	#base case: DEPTH 1

	if depth == 1:
		pieces = GetPlayerPositions(board, player)

		evals = []
		for piece in pieces:
			possmoves = GetPieceLegalMoves(board, piece)

			for possmove in possmoves:
				test = [] + board
				placePiece(test, piece, possmove)

				e = evalBoard(test, player)
				evals += [[[piece, possmove], e]]

				test = list(board)

		m = -999999
		for element in evals:
			if element[1] > m:
				m = element[1]
				bestpiece = element[0][0]
				bestmove = element[0][1]
				besteval = element[1]

		return [[bestpiece, bestmove], besteval]


	#all other depths

	pieces = GetPlayerPositions(board, player)

	possMoves = []
	maximum = -999999
	minimum = 999999


	for piece in pieces:
		possMoves += [GetPieceLegalMoves(board, piece)]

	pieceMovePair = zip(pieces, possMoves)

	#Maximizing Player (WHITE)

	if isMaximizingPlayer(player):
		for pair in pieceMovePair:

			for move in pair[1]:
				test = [] + board
				placePiece(test, pair[0], move)

				e = minimax(test, a, b, depth-1, opp(player))

				if e[1] > maximum:
					possmove = move
					posspiece = pair[0]
					maximum = e[1]

				#alpha-beta pruning for Maximizing Player

				a = max(a,e[1])
				if b <= a:
					break

				#reset board after testing

				test = list(board)
				

		return [[posspiece, possmove], maximum]
	
	#Minimizing Player (BLACK)

	else:
		for pair in pieceMovePair:

			for move in pair[1]:

				test = [] + board
				placePiece(test, pair[0], move)

				e = minimax(test, a, b, depth-1, opp(player))

				if e[1] < minimum:
					possmove = move
					posspiece = pair[0]
					minimum = e[1]

				#alpha-beta pruning for Minimizing Player

				b = min(b,e[1])
				if b <= a:
					break

				#reset board after testing

				test = list(board)

		return [[posspiece, possmove], minimum]

