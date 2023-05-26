import pygame as pg
import math
import numpy as np
import pandas as pd

# Nome no GitHub: (English: Chess) (Português: Xadrez)

# Instructions:
# 001 - To select a house press the left mouse button
# 002 - To deselect a house press the right mouse button
# 003 - To move a piece, first select the piece and secondly choose a movement place

# To Do List:
# >>> Small Castling
# >>> Big Castling
# >>> Check
# >>> Checkmate
# >>> Pawn Passant
# Okay >>> Pawn Promotion (To Queen)

# Game colors
white = (255, 255, 255)
black = (0, 0, 0)
beige = (240, 217, 181)
brown = (181, 136, 99)
greenish_beige = (174, 177, 135)
greenish_brown  = (100, 111, 64)

# Game images - White pieces
king_white_image = pg.image.load('./images/king white.png')
king_white_image = pg.transform.scale(king_white_image, (100, 100))
queen_white_image = pg.image.load('./images/queen white.png')
queen_white_image = pg.transform.scale(queen_white_image, (100, 100))
bishop_white_image = pg.image.load('./images/bishop white.png')
bishop_white_image = pg.transform.scale(bishop_white_image, (100, 100))
knight_white_image = pg.image.load('./images/knight white.png')
knight_white_image = pg.transform.scale(knight_white_image, (100, 100))
rook_white_image = pg.image.load('./images/rook white.png')
rook_white_image = pg.transform.scale(rook_white_image, (100, 100))
pawn_white_image = pg.image.load('./images/pawn white.png')
pawn_white_image = pg.transform.scale(pawn_white_image, (100, 100))
# Game images - Black pieces
king_black_image = pg.image.load('./images/king black.png')
king_black_image = pg.transform.scale(king_black_image, (100, 100))
queen_black_image = pg.image.load('./images/queen black.png')
queen_black_image = pg.transform.scale(queen_black_image, (100, 100))
bishop_black_image = pg.image.load('./images/bishop black.png')
bishop_black_image = pg.transform.scale(bishop_black_image, (100, 100))
knight_black_image = pg.image.load('./images/knight black.png')
knight_black_image = pg.transform.scale(knight_black_image, (100, 100))
rook_black_image = pg.image.load('./images/rook black.png')
rook_black_image = pg.transform.scale(rook_black_image, (100, 100))
pawn_black_image = pg.image.load('./images/pawn black.png')
pawn_black_image = pg.transform.scale(pawn_black_image, (100, 100))
# Simble Dot image
dot_greenish_beige_image = pg.image.load('./images/dot greenish beige.png')
dot_greenish_beige_image = pg.transform.scale(dot_greenish_beige_image, (100, 100))
dot_greenish_brown_image = pg.image.load('./images/dot greenish brown.png')
dot_greenish_brown_image = pg.transform.scale(dot_greenish_brown_image, (100, 100))
# Simble Mark image
mark_greenish_beige_image = pg.image.load('./images/mark greenish beige.png')
mark_greenish_beige_image = pg.transform.scale(mark_greenish_beige_image, (100, 100))
mark_greenish_brown_image = pg.image.load('./images/mark greenish brown.png')
mark_greenish_brown_image = pg.transform.scale(mark_greenish_brown_image, (100, 100))

# Setup da tela do Jogo
window = pg.display.set_mode((800, 800))
window.fill(white)

# board
def board(window):
	for n in range(8):
		for nn in range(8):
			if (n % 2) == 0 and (nn % 2) == 0 or (n % 2) != 0 and (nn % 2) != 0:
				pg.draw.rect(window, beige, (n * 100, nn * 100, 100, 100))
			elif (n % 2) != 0 and (nn % 2) == 0 or (n % 2) == 0 and (nn % 2) != 0:
				pg.draw.rect(window, brown, ((n * 100, nn * 100, 100, 100)))

# Resizing white pieces images
def king_white(window, x, y):
	window.blit(king_white_image, (x * 100, y * 100))
def queen_white(window, x, y):
	window.blit(queen_white_image, (x * 100, y * 100))
def bishop_white(window, x, y):
	window.blit(bishop_white_image, (x * 100, y * 100))
def knight_white(window, x, y):
	window.blit(knight_white_image, (x * 100, y * 100))
def rook_white(window, x, y):
	window.blit(rook_white_image, (x * 100, y * 100))
def pawn_white(window, x, y):
	window.blit(pawn_white_image, (x * 100, y * 100))
# Resizing black pieces images
def king_black(window, x, y):
	window.blit(king_black_image, (x * 100, y * 100))
def queen_black(window, x, y):
	window.blit(queen_black_image, (x * 100, y * 100))
def bishop_black(window, x, y):
	window.blit(bishop_black_image, (x * 100, y * 100))
def knight_black(window, x, y):
	window.blit(knight_black_image, (x * 100, y * 100))
def rook_black(window, x, y):
	window.blit(rook_black_image, (x * 100, y * 100))
def pawn_black(window, x, y):
	window.blit(pawn_black_image, (x * 100, y * 100))
# Simble Dot
def dot_greenish_beige(window, x, y):
	window.blit(dot_greenish_beige_image, (x * 100, y * 100))
def dot_dot_greenish_brown(window, x, y):
	window.blit(dot_greenish_brown_image, (x * 100, y * 100))
# Simble Mark
def mark_greenish_beige(window, x, y):
	window.blit(mark_greenish_beige_image, (x * 100, y * 100))
def mark_greenish_brown(window, x, y):
	window.blit(mark_greenish_brown_image, (x * 100, y * 100))

# Selected cell and painting when selected
def paint_selected_cell(window, x, y, click_on_off, color_1, color_2):
	if (x % 2) == 0 and (y % 2) == 0 and click_on_off == 1 or (x % 2) != 0 and (y % 2) != 0 and click_on_off == 1:
		pg.draw.rect(window, color_1, (x * 100, y * 100, 100, 100))
	elif (x % 2) == 0 and (y % 2) != 0 and click_on_off == 1 or (x % 2) != 0 and (y % 2) == 0 and click_on_off == 1:
		pg.draw.rect(window, color_2, (x * 100, y * 100, 100, 100))

# Placing simbles of muvement and placemment
def place_simbles(window):
	# Dotted places (Can move)
	for n in range(8):
		for nn in range(8):
			if (n % 2) == 0 and (nn % 2) == 0 or (n % 2) != 0 and (nn % 2) != 0:
				if board_array[n][nn] == 'dot_':
					dot_greenish_beige(window, nn, n)
			elif (n % 2) != 0 and (nn % 2) == 0 or (n % 2) == 0 and (nn % 2) != 0:
				if board_array[n][nn] == 'dot_':
					dot_dot_greenish_brown(window, nn, n)
	# Maked places (Can place)
	for n in range(8):
		for nn in range(8):
			if (n % 2) == 0 and (nn % 2) == 0 or (n % 2) != 0 and (nn % 2) != 0:
				if (board_array[n][nn])[2:3] == 'm':
					mark_greenish_beige(window, nn, n)
			elif (n % 2) != 0 and (nn % 2) == 0 or (n % 2) == 0 and (nn % 2) != 0:
				if (board_array[n][nn])[2:3] == 'm':
					mark_greenish_brown(window, nn, n)

# Placing pieces on the board
def place_pieces(window):
	for n in range(8):
		for nn in range(8):
			# Black pieces
			if board_array[n][nn] == 'rk_b' or board_array[n][nn] == 'rkmb':
				rook_black(window, nn, n)
			elif board_array[n][nn] == 'kt_b' or board_array[n][nn] == 'ktmb':
				knight_black(window, nn, n)
			elif board_array[n][nn] == 'bp_b' or board_array[n][nn] == 'bpmb':
				bishop_black(window, nn, n)
			elif board_array[n][nn] == 'qn_b' or board_array[n][nn] == 'qnmb':
				queen_black(window, nn, n)
			elif board_array[n][nn] == 'kg_b' or board_array[n][nn] == 'kgmb':
				king_black(window, nn, n)
			elif board_array[n][nn] == 'pn_b' or board_array[n][nn] == 'pnmb':
				pawn_black(window, nn, n)
			# White pieces
			elif board_array[n][nn] == 'rk_w' or board_array[n][nn] == 'rkmw':
				rook_white(window, nn, n)
			elif board_array[n][nn] == 'kt_w' or board_array[n][nn] == 'ktmw':
				knight_white(window, nn, n)
			elif board_array[n][nn] == 'bp_w' or board_array[n][nn] == 'bpmw':
				bishop_white(window, nn, n)
			elif board_array[n][nn] == 'qn_w' or board_array[n][nn] == 'qnmw':
				queen_white(window, nn, n)
			elif board_array[n][nn] == 'kg_w' or board_array[n][nn] == 'kgmw':
				king_white(window, nn, n)
			elif board_array[n][nn] == 'pn_w' or board_array[n][nn] == 'pnmw':
				pawn_white(window, nn, n)
			# Empty place
			elif board_array[n][nn] == 'none':
				pass

# Cleaning the last selected dots and marks
def clean_all_symbols(board_array):
	for n in range(8):
		for nn in range(8):
			# Black pieces
			if board_array[n][nn] == 'dot_' or board_array[n][nn] == 'dot_' and click_on_off == 0:
				board_array[n][nn] = 'none'
			elif (board_array[n][nn])[2:3] == 'm' \
			or (board_array[n][nn])[2:3] == 'm' and click_on_off == 0:
				board_array[n][nn] = (board_array[n][nn])[0:2] + '_' + (board_array[n][nn])[3:4]
	return board_array

# Paths and Targets of king piece
def king_dot_mark(board_array, x, y, turn_white_black):
	if (board_array[y][x])[3:4] == turn_white_black:
		# Dot paths
		if board_array[y - 1][x] == 'none':
			board_array[y - 1][x] = 'dot_'
		try:
			if board_array[y - 1][x + 1] == 'none':
				board_array[y - 1][x + 1] = 'dot_'
		except:
			pass
		try:
			if board_array[y][x + 1] == 'none':
				board_array[y][x + 1] = 'dot_'
		except:
			pass
		try:
			if board_array[y + 1][x + 1] == 'none':
				board_array[y + 1][x + 1] = 'dot_'
		except:
			pass
		try:
			if board_array[y + 1][x] == 'none':
				board_array[y + 1][x] = 'dot_'
		except:
			pass
		try:
			if board_array[y + 1][x - 1] == 'none':
				board_array[y + 1][x - 1] = 'dot_'
		except:
			pass
		if board_array[y][x - 1] == 'none':
			board_array[y][x - 1] = 'dot_'
		if board_array[y - 1][x - 1] == 'none':
			board_array[y - 1][x - 1] = 'dot_'
		# Mark targets
		if (board_array[y - 1][x])[2:3] == '_':
			board_array[y - 1][x] = (board_array[y - 1][x])[0:2] + 'm' + (board_array[y - 1][x])[3:4]
		try:
			if (board_array[y - 1][x + 1])[2:3] == '_':
				board_array[y - 1][x + 1] = (board_array[y - 1][x + 1])[0:2] + 'm' + (board_array[y - 1][x + 1])[3:4]
		except:
			pass
		try:
			if (board_array[y][x + 1])[2:3] == '_':
				board_array[y][x + 1] = (board_array[y][x + 1])[0:2] + 'm' + (board_array[y][x + 1])[3:4]
		except:
			pass
		try:
			if (board_array[y + 1][x + 1])[2:3] == '_':
				board_array[y + 1][x + 1] = (board_array[y + 1][x + 1])[0:2] + 'm' + (board_array[y + 1][x + 1])[3:4]
		except:
			pass
		try:
			if (board_array[y + 1][x])[2:3] == '_':
				board_array[y + 1][x] = (board_array[y + 1][x])[0:2] + 'm' + (board_array[y + 1][x])[3:4]
		except:
			pass
		try:
			if (board_array[y + 1][x - 1])[2:3] == '_':
				board_array[y + 1][x - 1] = (board_array[y + 1][x - 1])[0:2] + 'm' + (board_array[y + 1][x - 1])[3:4]
		except:
			pass
		if (board_array[y][x - 1])[2:3] == '_':
			board_array[y][x - 1] = (board_array[y][x - 1])[0:2] + 'm' + (board_array[y][x - 1])[3:4]
		if (board_array[y - 1][x - 1])[2:3] == '_':
			board_array[y - 1][x - 1] = (board_array[y - 1][x - 1])[0:2] + 'm' + (board_array[y - 1][x - 1])[3:4]
	return board_array

# Paths and Targets of quenn piece
def queen_dot_mark(board_array, x, y, turn_white_black):
	bishop_dot_mark(board_array, x, y, turn_white_black)
	rook_dot_mark(board_array, x, y, turn_white_black)

# Paths and Targets of bishop piece
def bishop_dot_mark(board_array, x, y, turn_white_black):
	if (board_array[y][x])[3:4] == turn_white_black:
		# Dot Paths
		for n in range(8):
			try:
				if board_array[y - n - 1][x + n + 1] == 'none' and y != -1 and x != -1 and (y - n - 1) > -1:
					board_array[y - n - 1][x + n + 1] = 'dot_'
				else:
					break
			except:
				pass
		for n in range(8):
			try:
				if board_array[y - n - 1][x - n - 1] == 'none' and y != -1 and x != -1 and (x - n - 1) > -1 and (y - n - 1) > -1:
					board_array[y - n - 1][x - n - 1] = 'dot_'
				else:
					break
			except:
				pass
		for n in range(8):
			try:
				if board_array[y + n + 1][x - n - 1] == 'none' and y != -1 and x != -1 and (x - n - 1) > -1:
					board_array[y + n + 1][x - n - 1] = 'dot_'
				else:
					break
			except:
				pass
		for n in range(8):
			try:
				if board_array[y + n + 1][x + n + 1] == 'none' and y != -1 and x != -1:
					board_array[y + n + 1][x + n + 1] = 'dot_'
				else:
					break
			except:
				pass
		# Mark Targets
		for n in range(8):
			try:
				if (board_array[y - n - 1][x + n + 1])[2:3] == '_' and y != -1 and x != -1 and (y - n - 1) > -1:
					board_array[y - n - 1][x + n + 1] = (board_array[y - n - 1][x + n + 1])[0:2] + 'm' + (board_array[y - n - 1][x + n + 1])[3:4]
					break
				else:
					pass
			except:
				break
		for n in range(8):
			try:
				if (board_array[y - n - 1][x - n - 1])[2:3] == '_' and y != -1 and x != -1 and (x - n - 1) > -1 and (y - n - 1) > -1:
					board_array[y - n - 1][x - n - 1] = (board_array[y - n - 1][x - n - 1])[0:2] + 'm' + (board_array[y - n - 1][x - n - 1])[3:4]
					break
				else:
					pass
			except:
				break
		for n in range(8):
			try:
				if (board_array[y + n + 1][x + n + 1])[2:3] == '_' and y != -1 and x != -1 and (x - n - 1) > -1 and (y - n - 1) > -1:
					board_array[y + n + 1][x + n + 1] = (board_array[y + n + 1][x + n + 1])[0:2] + 'm' + (board_array[y + n + 1][x + n + 1])[3:4]
					break
				else:
					pass
			except:
				break
		for n in range(8):
			try:
				if (board_array[y + n + 1][x - n - 1])[2:3] == '_' and y != -1 and x != -1 and (x - n - 1) > -1:
					board_array[y + n + 1][x - n - 1] = (board_array[y + n + 1][x - n - 1])[0:2] + 'm' + (board_array[y + n + 1][x - n - 1])[3:4]
					break
				else:
					pass
			except:
				break

# Paths and Targets of knight piece
def knight_dot_mark(board_array, x, y, turn_white_black):
	if (board_array[y][x])[3:4] == turn_white_black and y != -1 and x != -1:
		# Dot Paths
		try:
			if board_array[y - 2][x + 1] == 'none':
				board_array[y - 2][x + 1] = 'dot_'
			else:
				pass
		except:
			pass
		try:
			if board_array[y - 2][x - 1] == 'none':
				board_array[y - 2][x - 1] = 'dot_'
			else:
				pass
		except:
			pass
		try:
			if board_array[y - 1][x + 2] == 'none':
				board_array[y - 1][x + 2] = 'dot_'
			else:
				pass
		except:
			pass
		try:
			if board_array[y + 1][x + 2] == 'none':
				board_array[y + 1][x + 2] = 'dot_'
			else:
				pass
		except:
			pass
		try:
			if board_array[y - 1][x - 2] == 'none':
				board_array[y - 1][x - 2] = 'dot_'
			else:
				pass
		except:
			pass
		try:
			if board_array[y + 1][x - 2] == 'none':
				board_array[y + 1][x - 2] = 'dot_'
			else:
				pass
		except:
			pass
		try:
			if board_array[y + 2][x + 1] == 'none':
				board_array[y + 2][x + 1] = 'dot_'
			else:
				pass
		except:
			pass
		try:
			if board_array[y + 2][x - 1] == 'none':
				board_array[y + 2][x - 1] = 'dot_'
			else:
				pass
		except:
			pass
		# Mark Targets
		try:
			if (board_array[y - 2][x + 1])[2:3] == '_' and (y - 2) > -1:
				board_array[y - 2][x + 1] = (board_array[y - 2][x + 1])[0:2] + 'm' + (board_array[y - 2][x + 1])[3:4]
			else:
				pass
		except:
			pass
		try:
			if (board_array[y - 2][x - 1])[2:3] == '_' and (y - 2) > -1 and (x - 1) > -1:
				board_array[y - 2][x - 1] = (board_array[y - 2][x - 1])[0:2] + 'm' + (board_array[y - 2][x - 1])[3:4]
			else:
				pass
		except:
			pass
		try:
			if (board_array[y - 1][x + 2])[2:3] == '_' and (y - 1) > -1:
				board_array[y - 1][x + 2] = (board_array[y - 1][x + 2])[0:2] + 'm' + (board_array[y - 1][x + 2])[3:4]
			else:
				pass
		except:
			pass
		try:
			if (board_array[y + 1][x + 2])[2:3] == '_':
				board_array[y + 1][x + 2] = (board_array[y + 1][x + 2])[0:2] + 'm' + (board_array[y + 1][x + 2])[3:4]
			else:
				pass
		except:
			pass
		try:
			if (board_array[y - 1][x - 2])[2:3] == '_' and (y - 1) > -1 and (x - 2) > -1:
				board_array[y - 1][x - 2] = (board_array[y - 1][x - 2])[0:2] + 'm' + (board_array[y - 1][x - 2])[3:4]
			else:
				pass
		except:
			pass
		try:
			if (board_array[y + 1][x - 2])[2:3] == '_' and (x - 2) > -1:
				board_array[y + 1][x - 2] = (board_array[y + 1][x - 2])[0:2] + 'm' + (board_array[y + 1][x - 2])[3:4]
			else:
				pass
		except:
			pass
		try:
			if (board_array[y + 2][x + 1])[2:3] == '_':
				board_array[y + 2][x + 1] = (board_array[y + 2][x + 1])[0:2] + 'm' + (board_array[y + 2][x + 1])[3:4]
			else:
				pass
		except:
			pass
		try:
			if (board_array[y + 2][x - 1])[2:3] == '_' and (x - 1) > -1:
				board_array[y + 2][x - 1] = (board_array[y + 2][x - 1])[0:2] + 'm' + (board_array[y + 2][x - 1])[3:4]
			else:
				pass
		except:
			pass

# Paths and Targets of rook piece
def rook_dot_mark(board_array, x, y, turn_white_black):
	if (board_array[y][x])[3:4] == turn_white_black:
		# Dot Paths
		for n in range(8):
			try:
				if board_array[y - n - 1][x] == 'none' and y != -1 and x != -1:
					board_array[y - n - 1][x] = 'dot_'
				else:
					break
			except:
				pass
		for n in range(8):
			try:
				if board_array[y + n + 1][x] == 'none' and y != -1 and x != -1:
					board_array[y + n + 1][x] = 'dot_'
				else:
					break
			except:
				pass
		for n in range(8):
			try:
				if board_array[y][x + n + 1] == 'none' and y != -1 and x != -1:
					board_array[y][x + n + 1] = 'dot_'
				else:
					break
			except:
				pass
			# Bug fix
			try:
				if (board_array[y][x + n + 1])[2:3] == 'm' and y != -1 and x != -1:
					break
			except:
				pass
		for n in range(8):
			try:
				if board_array[y][x - n - 1] == 'none' and y != -1 and x != -1  and (x - n - 1) > -1:
					board_array[y][x - n - 1] = 'dot_'
				else:
					break
			except:
				pass
		# Mark Targets
		for n in range(8):
			try:
				if (board_array[y - n - 1][x])[2:3] == '_' and y != -1 and x != -1 and (y - n - 1) > -1:
					board_array[y - n - 1][x] = (board_array[y - n - 1][x])[0:2] + 'm' + (board_array[y - n - 1][x])[3:4]
					break
				else:
					pass
			except:
				pass
		for n in range(8):
			try:
				if (board_array[y + n + 1][x])[2:3] == '_' and y != -1 and x != -1:
					board_array[y + n + 1][x] = (board_array[y + n + 1][x])[0:2] + 'm' + (board_array[y + n + 1][x])[3:4]
					break
				else:
					pass
			except:
				pass
		for n in range(8):
			try:
				if (board_array[y][x + n + 1])[2:3] == '_' and y != -1 and x != -1:
					board_array[y][x + n + 1] = (board_array[y][x + n + 1])[0:2] + 'm' + (board_array[y][x + n + 1])[3:4]
					break
				else:
					pass
			except:
				pass
		for n in range(8):
			try:
				if (board_array[y][x - n - 1])[2:3] == '_' and y != -1 and x != -1 and (x - n - 1) > -1:
					board_array[y][x - n - 1] = (board_array[y][x - n - 1])[0:2] + 'm' + (board_array[y][x - n - 1])[3:4]
					break
				else:
					pass
			except:
				pass

# Paths and Targets of pawn piece
def pawn_dot_mark(board_array, x, y, turn_white_black):
	if (board_array[y][x])[3:4] == turn_white_black:
		# Dot Paths
		if y == 6 and board_array[y - 1][x] == 'none' and board_array[y - 2][x] == 'none':
			board_array[y - 1][x] = 'dot_'
			board_array[y - 2][x] = 'dot_'
		if y == 6 and board_array[y - 1][x] == 'none':
			board_array[y - 1][x] = 'dot_'
		# Mark Targets
		if (board_array[y - 1][x - 1])[2:3] == '_' and (x - 1) != -1:
			board_array[y - 1][x - 1] = (board_array[y - 1][x - 1])[0:2] + 'm' + (board_array[y - 1][x - 1])[3:4]
		try:
			if (board_array[y - 1][x + 1])[2:3] == '_':
				board_array[y - 1][x + 1] = (board_array[y - 1][x + 1])[0:2] + 'm' + (board_array[y - 1][x + 1])[3:4]
		except:
			pass
		if board_array[y - 1][x] == 'none' and (y - 1) != -1:
			board_array[y - 1][x] = 'dot_'
	return board_array

# Board array
board_array = [['rk_b', 'kt_b', 'bp_b', 'qn_b', 'kg_b', 'bp_b', 'kt_b', 'rk_b'],
               ['pn_b', 'pn_b', 'pn_b', 'pn_b', 'pn_b', 'pn_b', 'pn_b', 'pn_b'],
               ['none', 'none', 'none', 'none', 'none', 'none', 'none', 'none'],
               ['none', 'none', 'none', 'none', 'none', 'none', 'none', 'none'],
               ['none', 'none', 'none', 'none', 'none', 'none', 'none', 'none'],
               ['none', 'none', 'none', 'none', 'none', 'none', 'none', 'none'],
               ['pn_w', 'pn_w', 'pn_w', 'pn_w', 'pn_w', 'pn_w', 'pn_w', 'pn_w'],
               ['rk_w', 'kt_w', 'bp_w', 'qn_w', 'kg_w', 'bp_w', 'kt_w', 'rk_w']]
# Click variable
click_last_status = 0
# Click on and off variable
click_on_off = 0
# Click positon variable
click_position_x = -1
click_position_y = -1
# Last Click Position
last_click_position_x = -1
last_click_position_y = -1
# Turn White or Black
turn_white_black = 'w'

while True:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			quit()

	# Mouse variable
	mouse = pg.mouse.get_pos()

	# Click variable
	click = pg.mouse.get_pressed()

	# Last Click Position
	last_click_position_x = click_position_x
	last_click_position_y = click_position_y

	# Board
	board(window)

	# Click logic
	if click[0] == 0 and click_last_status == 1:
		click_on_off = 1
		click_position_x = (math.ceil(mouse[0] / 100) - 1)
		click_position_y = (math.ceil(mouse[1] / 100) - 1)
	elif click[2] == 1 and click_last_status == 0:
		click_on_off = 0
		click_position_x = -1
		click_position_y = -1

	# Moving pieces
	if board_array[click_position_y][click_position_x] == 'dot_' \
	or (board_array[click_position_y][click_position_x])[2:3] == 'm' and (board_array[click_position_y][click_position_x])[3:4] != turn_white_black:
		board_array[click_position_y][click_position_x] = board_array[last_click_position_y][last_click_position_x]
		board_array[last_click_position_y][last_click_position_x] = 'none'
		# Pawn Promotion to Queen
		if (board_array[click_position_y][click_position_x])[0:2] == 'pn' and click_position_y == 0:
			board_array[click_position_y][click_position_x] = 'qn_' + turn_white_black
		# Turn White or Black (White = 1 and Black = 0)
		if turn_white_black == 'w':
			turn_white_black = 'b'
		else:
			turn_white_black = 'w'
		# Turn Board
		board_array = zip(*board_array)
		board_array = list(board_array)
		board_array.reverse()
		board_array = zip(*board_array)
		board_array = list(board_array)
		board_array.reverse()
		board_array = np.asarray(board_array)
		# Click position reset
		click_position_x = -1
		click_position_y = -1

	# Cleaning the last selected dots and marks
	clean_all_symbols(board_array)

	# Selected cell and painting when selected
	paint_selected_cell(window, click_position_x, click_position_y, click_on_off,greenish_beige, greenish_brown)

	# Paths and targets of the pieces
	if (board_array[click_position_y][click_position_x])[0:2] == 'kg':
		king_dot_mark(board_array, click_position_x, click_position_y, turn_white_black)
	elif (board_array[click_position_y][click_position_x])[0:2] == 'qn':
		queen_dot_mark(board_array, click_position_x, click_position_y, turn_white_black)
	elif (board_array[click_position_y][click_position_x])[0:2] == 'bp':
		bishop_dot_mark(board_array, click_position_x, click_position_y, turn_white_black)
	elif (board_array[click_position_y][click_position_x])[0:2] == 'kt':
		knight_dot_mark(board_array, click_position_x, click_position_y, turn_white_black)
	elif (board_array[click_position_y][click_position_x])[0:2] == 'rk':
		rook_dot_mark(board_array, click_position_x, click_position_y, turn_white_black)
	elif (board_array[click_position_y][click_position_x])[0:2] == 'pn':
		pawn_dot_mark(board_array, click_position_x, click_position_y, turn_white_black)
	# Pawn Promotion to Queen
	#if (board_array[last_click_position_y][last_click_position_x])[0:2] == 'pn':
	#	if last_click_position_y == 0:
	#		board_array[last_click_position_y][last_click_position_y] = (board_array[last_click_position_y][last_click_position_y])[0:3] + 'w'

	# Placing simbles images (Dot, Mark)
	place_simbles(window)

	# Placing pieces images on the board
	place_pieces(window)

	print(pd.DataFrame(board_array))

	# Click Last Status
	if click[0] == 1:
		click_last_status = 1
	else:
		click_last_status = 0

	pg.display.update()