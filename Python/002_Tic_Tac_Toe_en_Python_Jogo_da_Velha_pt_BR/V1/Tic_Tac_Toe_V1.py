import pygame

# Cores do Jogo
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

# Setup da tela do Jogo
window = pygame.display.set_mode((600, 600))
window.fill(branco)

# Grade do tabuleiro 
pygame.draw.line(window, preto, (205, 50), (205, 521), 10)
pygame.draw.line(window, preto, (365, 50), (365, 521), 10)
pygame.draw.line(window, preto, (50, 205), (521, 205), 10)
pygame.draw.line(window, preto, (50, 365), (521, 365), 10)

# Declarando estado X ou O - Onde (1 = X) e (0 = O)
x_ou_o = 1
position = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# Declarando traço final
fim = 0

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

	# Declarando mouse
	mouse = pygame.mouse.get_pos()

	# Declarando click do mouse
	click = pygame.mouse.get_pressed()

	# Blocos de Seleção - Linha 1 - Coluna 1
	if 50 <= mouse[0] <= 200 and 50 <= mouse[1] <= 200:
		if click[0] == 1 and position[0] == 0 and x_ou_o == 1:
			pygame.draw.line(window, vermelho, (100, 100), (150, 150), 10)
			pygame.draw.line(window, vermelho, (150, 100), (100, 150), 10)
			position[0] = 1
			x_ou_o = 0
		elif click[0] == 1 and position[0] == 0 and x_ou_o == 0:
			pygame.draw.circle(window, azul, (125, 125), 25)
			pygame.draw.circle(window, branco, (125, 125), 15)
			position[0] = 2
			x_ou_o = 1

	# Blocos de Seleção - Linha 1 - Coluna 2
	if 211 <= mouse[0] <= 360 and 50 <= mouse[1] <= 200:
		if click[0] == 1 and position[1] == 0 and x_ou_o == 1:
			pygame.draw.line(window, vermelho, (261, 100), (311, 150), 10)
			pygame.draw.line(window, vermelho, (311, 100), (261, 150), 10)
			position[1] = 1
			x_ou_o = 0
		elif click[0] == 1 and position[1] == 0 and x_ou_o == 0:
			pygame.draw.circle(window, azul, (286, 125), 25)
			pygame.draw.circle(window, branco, (286, 125), 15)
			position[1] = 2
			x_ou_o = 1

	# Blocos de Seleção - Linha 1 - Coluna 3
	if 371 <= mouse[0] <= 520 and 50 <= mouse[1] <= 200:
		if click[0] == 1 and position[2] == 0 and x_ou_o == 1:
			pygame.draw.line(window, vermelho, (421, 100), (471, 150), 10)
			pygame.draw.line(window, vermelho, (471, 100), (421, 150), 10)
			position[2] = 1
			x_ou_o = 0
		elif click[0] == 1 and position[2] == 0 and x_ou_o == 0:
			pygame.draw.circle(window, azul, (446, 125), 25)
			pygame.draw.circle(window, branco, (446, 125), 15)
			position[2] = 2
			x_ou_o = 1


	# Blocos de Seleção - Linha 2 - Coluna 1
	if 50 <= mouse[0] <= 200 and 211 <= mouse[1] <= 361:
		if click[0] == 1 and position[3] == 0 and x_ou_o == 1:
			pygame.draw.line(window, vermelho, (100, 311), (150, 261), 10)
			pygame.draw.line(window, vermelho, (150, 311), (100, 261), 10)
			position[3] = 1
			x_ou_o = 0
		elif click[0] == 1 and position[3] == 0 and x_ou_o == 0:
			pygame.draw.circle(window, azul, (125, 286), 25)
			pygame.draw.circle(window, branco, (125, 286), 15)
			position[3] = 2
			x_ou_o = 1

	# Blocos de Seleção - Linha 2 - Coluna 2
	if 211 <= mouse[0] <= 360 and 211 <= mouse[1] <= 361:
		if click[0] == 1 and position[4] == 0 and x_ou_o == 1:
			pygame.draw.line(window, vermelho, (261, 311), (311, 261), 10)
			pygame.draw.line(window, vermelho, (311, 311), (261, 261), 10)
			position[4] = 1
			x_ou_o = 0
		elif click[0] == 1 and position[4] == 0 and x_ou_o == 0:
			pygame.draw.circle(window, azul, (286, 286), 25)
			pygame.draw.circle(window, branco, (286, 286), 15)
			position[4] = 2
			x_ou_o = 1

	# Blocos de Seleção - Linha 2 - Coluna 3
	if 371 <= mouse[0] <= 520 and 211 <= mouse[1] <= 361:
		if click[0] == 1 and position[5] == 0 and x_ou_o == 1:
			pygame.draw.line(window, vermelho, (421, 311), (471, 261), 10)
			pygame.draw.line(window, vermelho, (471, 311), (421, 261), 10)
			position[5] = 1
			x_ou_o = 0
		elif click[0] == 1 and position[5] == 0 and x_ou_o == 0:
			pygame.draw.circle(window, azul, (446, 286), 25)
			pygame.draw.circle(window, branco, (446, 286), 15)
			position[5] = 2
			x_ou_o = 1



	# Blocos de Seleção - Linha 3 - Coluna 1
	if 50 <= mouse[0] <= 200 and 371 <= mouse[1] <= 521:
		if click[0] == 1 and position[6] == 0 and x_ou_o == 1:
			pygame.draw.line(window, vermelho, (100, 472), (150, 422), 10)
			pygame.draw.line(window, vermelho, (150, 472), (100, 422), 10)
			position[6] = 1
			x_ou_o = 0
		elif click[0] == 1 and position[6] == 0 and x_ou_o == 0:
			pygame.draw.circle(window, azul, (125, 447), 25)
			pygame.draw.circle(window, branco, (125, 447), 15)
			position[6] = 2
			x_ou_o = 1

	# Blocos de Seleção - Linha 3 - Coluna 2
	if 211 <= mouse[0] <= 360 and 371 <= mouse[1] <= 521:
		if click[0] == 1 and position[7] == 0 and x_ou_o == 1:
			pygame.draw.line(window, vermelho, (261, 472), (311, 422), 10)
			pygame.draw.line(window, vermelho, (311, 472), (261, 422), 10)
			position[7] = 1
			x_ou_o = 0
		elif click[0] == 1 and position[7] == 0 and x_ou_o == 0:
			pygame.draw.circle(window, azul, (286, 447), 25)
			pygame.draw.circle(window, branco, (286, 447), 15)
			position[7] = 2
			x_ou_o = 1

	# Blocos de Seleção - Linha 3 - Coluna 3
	if 371 <= mouse[0] <= 520 and 371 <= mouse[1] <= 521:
		if click[0] == 1 and position[8] == 0 and x_ou_o == 1:
			pygame.draw.line(window, vermelho, (421, 472), (471, 422), 10)
			pygame.draw.line(window, vermelho, (471, 472), (421, 422), 10)
			position[8] = 1
			x_ou_o = 0
		elif click[0] == 1 and position[8] == 0 and x_ou_o == 0:
			pygame.draw.circle(window, azul, (446, 447), 25)
			pygame.draw.circle(window, branco, (446, 447), 15)
			position[8] = 2
			x_ou_o = 1

	# Traço final
	# Linha 1 
	if position[0] == 1 and position[1] == 1 and position[2] == 1 and fim == 0 or position[0] == 2 and position[1] == 2 and position[2] == 2 and fim == 0:
		pygame.draw.line(window, verde, (100, 125), (470, 125), 10)
		position[0] = 3
		position[1] = 3
		position[2] = 3
		position[3] = 3
		position[4] = 3
		position[5] = 3
		position[6] = 3
		position[7] = 3
		position[8] = 3
		fim = 1
	# Linha 2 
	elif position[3] == 1 and position[4] == 1 and position[5] == 1 and fim == 0 or position[3] == 2 and position[4] == 2 and position[5] == 2 and fim == 0:
		pygame.draw.line(window, verde, (100, 286), (470, 286), 10)
		position[0] = 3
		position[1] = 3
		position[2] = 3
		position[3] = 3
		position[4] = 3
		position[5] = 3
		position[6] = 3
		position[7] = 3
		position[8] = 3
		fim = 1
	# Linha 3
	elif position[6] == 1 and position[7] == 1 and position[8] == 1 and fim == 0 or position[6] == 2 and position[7] == 2 and position[8] == 2 and fim == 0:
		pygame.draw.line(window, verde, (100, 447), (470, 447), 10)
		position[0] = 3
		position[1] = 3
		position[2] = 3
		position[3] = 3
		position[4] = 3
		position[5] = 3
		position[6] = 3
		position[7] = 3
		position[8] = 3
		fim = 1
	# Coluna 1
	elif position[0] == 1 and position[3] == 1 and position[6] == 1 and fim == 0 or position[0] == 2 and position[3] == 2 and position[6] == 2 and fim == 0:
		pygame.draw.line(window, verde, (125, 100), (125, 472), 10)
		position[0] = 3
		position[1] = 3
		position[2] = 3
		position[3] = 3
		position[4] = 3
		position[5] = 3
		position[6] = 3
		position[7] = 3
		position[8] = 3
		fim = 1
	# Coluna 2
	elif position[1] == 1 and position[4] == 1 and position[7] == 1 and fim == 0 or position[1] == 2 and position[4] == 2 and position[7] == 2 and fim == 0:
		pygame.draw.line(window, verde, (286, 100), (286, 472), 10)
		position[0] = 3
		position[1] = 3
		position[2] = 3
		position[3] = 3
		position[4] = 3
		position[5] = 3
		position[6] = 3
		position[7] = 3
		position[8] = 3
		fim = 1
	# Coluna 3
	elif position[2] == 1 and position[5] == 1 and position[8] == 1 and fim == 0 or position[2] == 2 and position[5] == 2 and position[8] == 2 and fim == 0:
		pygame.draw.line(window, verde, (446, 100), (446, 472), 10)
		position[0] = 3
		position[1] = 3
		position[2] = 3
		position[3] = 3
		position[4] = 3
		position[5] = 3
		position[6] = 3
		position[7] = 3
		position[8] = 3
		fim = 1
	# Diagonal 1
	elif position[0] == 1 and position[4] == 1 and position[8] == 1 and fim == 0 or position[0] == 2 and position[4] == 2 and position[8] == 2 and fim == 0:
		pygame.draw.line(window, verde, (100, 100), (471, 472), 10)
		position[0] = 3
		position[1] = 3
		position[2] = 3
		position[3] = 3
		position[4] = 3
		position[5] = 3
		position[6] = 3
		position[7] = 3
		position[8] = 3
		fim = 1
	# Diagonal 2
	elif position[2] == 1 and position[4] == 1 and position[6] == 1 and fim == 0 or position[2] == 2 and position[4] == 2 and position[6] == 2 and fim == 0:
		pygame.draw.line(window, verde, (100, 472), (471, 100), 10)
		position[0] = 3
		position[1] = 3
		position[2] = 3
		position[3] = 3
		position[4] = 3
		position[5] = 3
		position[6] = 3
		position[7] = 3
		position[8] = 3
		fim = 1
		
	if 0 <= mouse[0] <= 600 and click[2] == 1 and fim == 1:
		# Blocos de Seleção - Linha 1 - Coluna 1
		pygame.draw.rect(window, branco, (50, 50, 150, 150))
		# Blocos de Seleção - Linha 1 - Coluna 2
		pygame.draw.rect(window, branco, (211, 50, 150, 150))
		# Blocos de Seleção - Linha 1 - Coluna 3
		pygame.draw.rect(window, branco, (371, 50, 150, 150))
		# Blocos de Seleção - Linha 2 - Coluna 1
		pygame.draw.rect(window, branco, (50, 211, 150, 150))
		# Blocos de Seleção - Linha 2 - Coluna 2
		pygame.draw.rect(window, branco, (211, 211, 150, 150))
		# Blocos de Seleção - Linha 2 - Coluna 3
		pygame.draw.rect(window, branco, (371, 211, 150, 150))
		# Blocos de Seleção - Linha 3 - Coluna 1
		pygame.draw.rect(window, branco, (50, 371, 150, 150))
		# Blocos de Seleção - Linha 3 - Coluna 2
		pygame.draw.rect(window, branco, (211, 371, 150, 150))
		# Blocos de Seleção - Linha 3 - Coluna 3
		pygame.draw.rect(window, branco, (371, 371, 150, 150))
		# Grade do tabuleiro 
		pygame.draw.line(window, preto, (205, 50), (205, 521), 10)
		pygame.draw.line(window, preto, (365, 50), (365, 521), 10)
		pygame.draw.line(window, preto, (50, 205), (521, 205), 10)
		pygame.draw.line(window, preto, (50, 365), (521, 365), 10)
		position[0] = 0
		position[1] = 0
		position[2] = 0
		position[3] = 0
		position[4] = 0
		position[5] = 0
		position[6] = 0
		position[7] = 0
		position[8] = 0
		x_ou_o = 1
		fim = 0
	elif sum(position) == 13 and click[2] == 1:
		# Blocos de Seleção - Linha 1 - Coluna 1
		pygame.draw.rect(window, branco, (50, 50, 150, 150))
		# Blocos de Seleção - Linha 1 - Coluna 2
		pygame.draw.rect(window, branco, (211, 50, 150, 150))
		# Blocos de Seleção - Linha 1 - Coluna 3
		pygame.draw.rect(window, branco, (371, 50, 150, 150))
		# Blocos de Seleção - Linha 2 - Coluna 1
		pygame.draw.rect(window, branco, (50, 211, 150, 150))
		# Blocos de Seleção - Linha 2 - Coluna 2
		pygame.draw.rect(window, branco, (211, 211, 150, 150))
		# Blocos de Seleção - Linha 2 - Coluna 3
		pygame.draw.rect(window, branco, (371, 211, 150, 150))
		# Blocos de Seleção - Linha 3 - Coluna 1
		pygame.draw.rect(window, branco, (50, 371, 150, 150))
		# Blocos de Seleção - Linha 3 - Coluna 2
		pygame.draw.rect(window, branco, (211, 371, 150, 150))
		# Blocos de Seleção - Linha 3 - Coluna 3
		pygame.draw.rect(window, branco, (371, 371, 150, 150))
		# Grade do tabuleiro 
		pygame.draw.line(window, preto, (205, 50), (205, 521), 10)
		pygame.draw.line(window, preto, (365, 50), (365, 521), 10)
		pygame.draw.line(window, preto, (50, 205), (521, 205), 10)
		pygame.draw.line(window, preto, (50, 365), (521, 365), 10)
		position[0] = 0
		position[1] = 0
		position[2] = 0
		position[3] = 0
		position[4] = 0
		position[5] = 0
		position[6] = 0
		position[7] = 0
		position[8] = 0
		x_ou_o = 1
		fim = 0

	pygame.display.update()