# -*- coding: cp437 -*-
def genBoard():

	board = [13, 11, 12, 14, 15, 12, 11, 13, 
				10, 10, 10, 10, 10, 10, 10, 10,
				0, 0, 0, 0, 0, 0, 0, 0,
				0, 0, 0, 0, 0, 0, 0, 0,
				0, 0, 0, 0, 0, 0, 0, 0,
				0, 0, 0, 0, 0, 0, 0, 0,				
				20, 20, 20, 20, 20, 20, 20, 20,
				23, 21, 22, 25, 24, 22, 21, 23]

	return board


def printBoard(board, player):

	chessboard = list(board)


	for i in range(0, 8, 1):
		if i % 2 == 0:
			for j in range(0, 8, 1):
				if board[(i * 8) + j] == 0:
					if j % 2 == 0:
						chessboard[(i * 8) + j] = '#'
					else:
						chessboard[(i * 8) + j] = '_'

		else:
			for k in range(0, 8, 1):
				if board[(i * 8) + k] == 0:
					if k % 2 == 0:
						chessboard[(i * 8) + k] = '_'
					else:
						chessboard[(i * 8) + k] = '#'



		
	for i in range (0, 64, 1):

		#white pieces

		if board[i] == 10:
			chessboard[i] = '♟'
		elif board[i] == 11:
			chessboard[i] = '♞'		
		elif board[i] == 12:
			chessboard[i] = '♝'
		elif board[i] == 13:
			chessboard[i] = '♜'
		elif board[i] == 14:
			chessboard[i] = '♛'
		elif board[i] == 15:
			chessboard[i] = '♚'

		#black pieces

		elif board[i] == 20:
			chessboard[i] = '♙'
		elif board[i] == 21:
			chessboard[i] = '♘'		
		elif board[i] == 22:
			chessboard[i] = '♗'
		elif board[i] == 23:
			chessboard[i] = '♖'
		elif board[i] == 24:
			chessboard[i] = '♕'
		elif board[i] == 25:
			chessboard[i] = '♔'


	if player == 10:
		for j in range (56, -1, -8):
			row = ''
			for k in range (0, 8, 1):
				row = row + ' ' + str(chessboard[j + k]) + ' '
			print(row)

	elif player == 20:
		for j in range(0, 57, 8):
			row = ''
			for k in range (7, -1, -1):
				row = row + ' ' + str(chessboard[j + k]) + ' '
			print(row)

	return True



def p(val):
	#helper function to determine player colour
	#white = 10; black = 20
	if 10 <= val <= 15:
		return 10
	elif 20 <= val <= 25:
		return 20
	else:
		return 0


def GetPlayerPositions(board, player):
	poslist = []
	position = 0
	
	#white
	if player == 10:
		for i in range(len(board)):
			if p(board[i]) == 10:
				poslist+=[i]
		return poslist

		# for square in board:
		# 	if p(square) == 10:
		# 		poslist += [position]
		# 	position += 1
		# return poslist

	#black
	elif player == 20:
		for i in range(len(board)):
			if p(board[i]) == 20:
				poslist+=[i]
		return poslist
		# for square in board:
		# 	if p(square) == 20:
		# 		poslist += [position]
		# 	position += 1
		# return poslist 


def opp(player):
	if player == 10:
		return 20
	elif player == 20:
		return 10


def PawnMoves(board, position, player):
	
	moveslist = []

	#white
	if player == 10:

		#move one square ahead
		if (board[position + 8]) == 0:
			moveslist += [position + 8]
			
		#move one square diagonally to take black
		if position % 8 != 0:
			if p(board[position + 9]) == opp(player):
				moveslist += [position + 9]
		if (position + 1) % 8 != 0:
			if p(board[position + 7]) == opp(player):
	 	 		moveslist += [position + 7]

	 #black
	elif player == 20:

	 	#move one square ahead
		if (board[position - 8]) == 0:
			moveslist += [position - 8]
			
		#move one square diagonally to take black
		if position % 8 != 0:
			if p(board[position - 9]) == opp(player):
				moveslist += [position - 9]
		if (position + 1) % 8 != 0:
			if p(board[position - 7]) == opp(player):
	 	 		moveslist += [position - 7]

	return moveslist


def KnightMoves(board, position, player):
	
	moveslist = []
	n1 = [10, 17]
	n2 = [6, 15]
	n3 = [6, 10, 15, 17]

	#left edge
	if position % 8 == 0:
		for num in n1:
			if position + num < 64:
				if p(board[position + num]) != player:
					moveslist += [position + num]
		for num in n2:
			if position - num >= 0:
				if p(board[position - num]) != player:
					moveslist += [position - num]

	#column 1
	elif position % 8 == 1:
		# print(n3[1:2])
		for num in [10,15, 17]:
			if position + num < 64:
				if p(board[position + num]) != player:
					moveslist += [position + num]
		# newlist = [] + [n3[0]] + n3[2:4]
		# print(newlist)
		for num in [6,15,17]:
			if position - num >= 0:
				if p(board[position - num]) != player:
					moveslist += [position - num]	
					# print(position-num)	

	#right edge
	elif (position + 1) % 8 == 0:
		for num in n2:
			if position + num < 64:
				if p(board[position + num]) != player:
					moveslist += [position + num]
			if position - num >= 0:
				if p(board[position - num]) != player:
					moveslist += [position - num]

	#column 7
	
	elif position % 8 == 6:
		for num in [6, 15, 17]:
			if position + num < 64:
				if p(board[position + num]) != player:
					moveslist += [position + num]
		for num in [10, 15, 17]:
			if position - num >= 0:
				if p(board[position - num]) != player:
					moveslist += [position - num]		

	#all other squares
	else:
		for num in n3:
			if position + num < 64:
				if p(board[position + num]) != player:
					moveslist += [position + num]
			if position - num >= 0:
				if p(board[position - num]) != player:
					moveslist += [position - num]

	return moveslist


def BishopMoves(board, position, player):
	
	moveslist = []

	#direction: LEFT UP
	square = position
	while ((square + 7) < 64) and (square % 8 != 0):
		leftup = square + 7
		if p(board[leftup]) == 0:
			moveslist += [leftup]
		elif p(board[leftup]) == opp(player):
			moveslist += [leftup]
			break
		else:
			break
		square += 7

	#direction: LEFT DOWN
	square = position
	while ((square - 9) >= 0) and (square % 8 != 0):
		leftdown = square - 9
		if p(board[leftdown]) == 0:
			moveslist += [leftdown]
		elif p(board[leftdown]) == opp(player):
			moveslist += [leftdown]
			break
		else:
			break
		square -= 9	

	#direction: RIGHT UP
	square = position
	while ((square + 9) < 64) and ((square + 1) % 8 != 0):
		rightup = square + 9
		if p(board[rightup]) == 0:
			moveslist += [rightup]
		elif p(board[rightup]) == opp(player):
			moveslist += [rightup]
			break
		else:
			break
		square += 9

	#direction: RIGHT DOWN
	square = position
	while ((square - 7) >= 0) and ((square + 1) % 8 != 0):
		rightdown = square - 7
		if p(board[rightdown]) == 0:
			moveslist += [rightdown]
		elif p(board[rightdown]) == opp(player):
			moveslist += [rightdown]
			break
		else:
			break
		square -= 7	

	return moveslist


def RookMoves(board, position, player):
	
	moveslist = []

	#direction: LEFT
	square = position
	while square % 8 != 0:
		left = square - 1
		if p(board[left]) == 0:
			moveslist += [left]
		elif p(board[left]) == opp(player):
			moveslist += [left]
			break
		else:
			break
		square -= 1

	#direction: RIGHT
	square = position
	while (square + 1) % 8 != 0:
		right = square + 1
		if p(board[right]) == 0:
			moveslist += [right]
		elif p(board[right]) == opp(player):
			moveslist += [right]
			break
		else:
			break
		square += 1

	#direction: UP
	square = position
	while (square + 8) < 64:
		up = square + 8
		if p(board[up]) == 0:
			moveslist += [up]
		elif p(board[up]) == opp(player):
			moveslist += [up]
			break
		else:
			break
		square += 8

	#direction: DOWN
	square = position
	while (square - 8) >= 0:
		down = square - 8
		if p(board[down]) == 0:
			moveslist += [down]
		elif p(board[down]) == opp(player):
			moveslist += [down]
			break
		else:
			break
		square -= 8

	return moveslist	


def QueenMoves(board, position, player):
	
	return BishopMoves(board, position, player) + RookMoves(board, position, player)


def KingMoves(board, position, player):

	moveslist = []
	
	#upper row
	for i in range(position + 7, position + 10, 1):
		if  (0 <= i < 64) and (p(board[i]) != player):
			moveslist += [i]

	#current row
	for j in range(position - 1, position + 2, 2):
		if (0 <= j < 64) and (p(board[j]) != player):
			moveslist += [j]

	#lower row
	for k in range(position - 9, position - 6, 1):
		if (0 <= k < 64) and (p(board[k]) != player):
			moveslist += [k]

	return moveslist


def GetPieceLegalMoves(board, position):

	piece = board[position] 
	
	#white moves
	if p(piece) == 10:
		
		#pawn 
		if piece == 10:
			return PawnMoves(board, position, 10)
		
		#knight
		if piece == 11:
			return KnightMoves(board, position, 10)
			
		#bishop
		if piece == 12:
			return BishopMoves(board, position, 10)

		#rook
		if piece == 13:
			return RookMoves(board, position, 10)

		#queen
		if piece == 14:
			return QueenMoves(board, position, 10)

		#king
		if piece == 15:
			return KingMoves(board, position, 10)


	#black moves
	if p(piece) == 20:

		#pawn 
		if piece == 20:
			return PawnMoves(board, position, 20)
		
		#knight
		if piece == 21:
			return KnightMoves(board, position, 20)
			
		#bishop
		if piece == 22:
			return BishopMoves(board, position, 20)

		#rook
		if piece == 23:
			return RookMoves(board, position, 20)

		#queen
		if piece == 24:
			return QueenMoves(board, position, 20)

		#king
		if piece == 25:
			return KingMoves(board, position, 20)


def IsPositionUnderThreat(board, position, player):

	opponent = GetPlayerPositions(board, opp(player))
	for pos in opponent:
		oppmoves = GetPieceLegalMoves(board, pos)
		for moves in oppmoves:
			if moves == position:
				return True

	return False


def roundDown(val):
	valstr = str(val)
	num = valstr[0]
	return int(num)

def convertIndexForward(index):

	#convert board structure to match different indexing

	col = 7 - (index % 8)

	row = roundDown(index / 8)

	newindex = 8 * row + col

	return newindex

def convertIndexBackward(index):

	col = index % 8

	row = (index - col) / 8

	newindex = (8 * row) + 7 - col

	return newindex








