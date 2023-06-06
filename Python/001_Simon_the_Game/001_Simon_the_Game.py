import pygame
from random import randrange
import time

# Cores do Jogo
preto = (0, 0, 0)
cinza = (100, 100, 100)
branco = (255, 255, 255)
vermelho = (255, 100, 100)
vermelho_escuro = (200, 0, 0)
amarelo = (255, 255, 150)
amarelo_escuro = (255, 255, 0)
verde = (100, 255, 100)
verde_escuro = (0, 200, 0)
azul = (150, 150, 255)
azul_escuro = (0, 0, 255)

# Setup da tela do Jogo
window = pygame.display.set_mode((600, 600))
window.fill(branco)

# Inicializando fonte
pygame.font.init()
# Escolhendo uma fonte e tamanho
fonte = pygame.font.SysFont("Comic Sans MS", 30)

# Variáveis do Jogo
click_on_off = 0
sequencia_do_jogo = []
repeticao_das_cores = 0
resposta = []

def inicio(window):
	pygame.draw.rect(window, verde_escuro, (100, 100, 200, 200))
	pygame.draw.rect(window, vermelho_escuro, (300, 100, 200, 200))
	pygame.draw.rect(window, amarelo_escuro, (100, 300, 200, 200))
	pygame.draw.rect(window, azul_escuro, (300, 300, 200, 200))
	pygame.draw.rect(window, preto, (100, 300, 400, 10))
	pygame.draw.rect(window, preto, (300, 100, 10, 400))
	pygame.draw.circle(window, branco, (300, 300), 300, 100)
	pygame.draw.circle(window, preto, (300, 300), 90)
	pygame.draw.circle(window, preto, (300, 300), 210, 10)
	texto = fonte.render("Simon", 1, branco)
	window.blit(texto, (260, 275))
	pygame.display.update()

def b_verde(window):
	pygame.draw.rect(window, verde, (100, 100, 200, 200))
	pygame.draw.rect(window, vermelho_escuro, (300, 100, 200, 200))
	pygame.draw.rect(window, amarelo_escuro, (100, 300, 200, 200))
	pygame.draw.rect(window, azul_escuro, (300, 300, 200, 200))
	pygame.draw.rect(window, preto, (100, 300, 400, 10))
	pygame.draw.rect(window, preto, (300, 100, 10, 400))
	pygame.draw.circle(window, branco, (300, 300), 300, 100)
	pygame.draw.circle(window, preto, (300, 300), 90)
	pygame.draw.circle(window, preto, (300, 300), 210, 10)
	texto = fonte.render("Simon", 1, branco)
	window.blit(texto, (260, 275))
	pygame.display.update()

def b_vermelho(window):
	pygame.draw.rect(window, verde_escuro, (100, 100, 200, 200))
	pygame.draw.rect(window, vermelho, (300, 100, 200, 200))
	pygame.draw.rect(window, amarelo_escuro, (100, 300, 200, 200))
	pygame.draw.rect(window, azul_escuro, (300, 300, 200, 200))
	pygame.draw.rect(window, preto, (100, 300, 400, 10))
	pygame.draw.rect(window, preto, (300, 100, 10, 400))
	pygame.draw.circle(window, branco, (300, 300), 300, 100)
	pygame.draw.circle(window, preto, (300, 300), 90)
	pygame.draw.circle(window, preto, (300, 300), 210, 10)
	texto = fonte.render("Simon", 1, branco)
	window.blit(texto, (260, 275))
	pygame.display.update()

def b_amarelo(window):
	pygame.draw.rect(window, verde_escuro, (100, 100, 200, 200))
	pygame.draw.rect(window, vermelho_escuro, (300, 100, 200, 200))
	pygame.draw.rect(window, amarelo, (100, 300, 200, 200))
	pygame.draw.rect(window, azul_escuro, (300, 300, 200, 200))
	pygame.draw.rect(window, preto, (100, 300, 400, 10))
	pygame.draw.rect(window, preto, (300, 100, 10, 400))
	pygame.draw.circle(window, branco, (300, 300), 300, 100)
	pygame.draw.circle(window, preto, (300, 300), 90)
	pygame.draw.circle(window, preto, (300, 300), 210, 10)
	texto = fonte.render("Simon", 1, branco)
	window.blit(texto, (260, 275))
	pygame.display.update()

def b_azul(window):
	pygame.draw.rect(window, verde_escuro, (100, 100, 200, 200))
	pygame.draw.rect(window, vermelho_escuro, (300, 100, 200, 200))
	pygame.draw.rect(window, amarelo_escuro, (100, 300, 200, 200))
	pygame.draw.rect(window, azul, (300, 300, 200, 200))
	pygame.draw.rect(window, preto, (100, 300, 400, 10))
	pygame.draw.rect(window, preto, (300, 100, 10, 400))
	pygame.draw.circle(window, branco, (300, 300), 300, 100)
	pygame.draw.circle(window, preto, (300, 300), 90)
	pygame.draw.circle(window, preto, (300, 300), 210, 10)
	texto = fonte.render("Simon", 1, branco)
	window.blit(texto, (260, 275))
	pygame.display.update()

def b_centro(window):
	pygame.draw.rect(window, verde_escuro, (100, 100, 200, 200))
	pygame.draw.rect(window, vermelho_escuro, (300, 100, 200, 200))
	pygame.draw.rect(window, amarelo_escuro, (100, 300, 200, 200))
	pygame.draw.rect(window, azul_escuro, (300, 300, 200, 200))
	pygame.draw.rect(window, preto, (100, 300, 400, 10))
	pygame.draw.rect(window, preto, (300, 100, 10, 400))
	pygame.draw.circle(window, branco, (300, 300), 300, 100)
	pygame.draw.circle(window, preto, (300, 300), 90)
	pygame.draw.circle(window, preto, (300, 300), 210, 10)
	pygame.draw.circle(window, cinza, (300, 300), 80)
	texto = fonte.render("Simon", 1, branco)
	window.blit(texto, (260, 275))
	pygame.display.update()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

	# Declarando mouse:
	mouse = pygame.mouse.get_pos()

	# Declarando click do mouse
	click = pygame.mouse.get_pressed()

	# Lógica de repetição das cores
	if repeticao_das_cores == 1:
		inicio(window)
		time.sleep(1)
		for i in range(len(sequencia_do_jogo)):
			pygame.draw.rect(window, branco, (0, 0, 500, 50))
			texto = fonte.render(str(i + 1) + ' / ' + str(len(sequencia_do_jogo)), 1, preto)
			window.blit(texto, (10, 10))
			pygame.display.update()
			if sequencia_do_jogo[i] == 0:
				b_verde(window)
			if sequencia_do_jogo[i] == 1:
				b_vermelho(window)
			if sequencia_do_jogo[i] == 2:
				b_amarelo(window)
			if sequencia_do_jogo[i] == 3:
				b_azul(window)
			time.sleep(1)
			inicio(window)
			time.sleep(0.5)
		repeticao_das_cores = 0

	# Lógica de Certo e Errado
	if resposta == sequencia_do_jogo and sequencia_do_jogo != []:
		repeticao_das_cores = 1
		sequencia_do_jogo.append(randrange(4))
		resposta = []
	if len(resposta) > 0 and \
	   len(sequencia_do_jogo) > 0 and \
	   resposta[len(resposta) - 1] != sequencia_do_jogo[len(resposta) - 1] and \
	   sequencia_do_jogo != []:
		pygame.draw.rect(window, branco, (0, 0, 500, 50))
		texto = fonte.render('Fim de Jogo - Você fez ' + str(len(sequencia_do_jogo) - 1) + ' pontos', 1, vermelho_escuro)
		window.blit(texto, (10, 10))
		pygame.display.update()
		time.sleep(3)
		sequencia_do_jogo = []
		resposta = []
		
	# Verde
	if (mouse[0] - 300) ** 2 + (mouse[1] - 300) ** 2 <= 40000 and \
		(mouse[0] - 300) ** 2 + (mouse[1] - 300) ** 2 >= 8100 and \
		100 <= mouse[0] <= 300 and \
		100 <= mouse[1] <= 300:
		b_verde(window)
		if click[0] == 0 and click_on_off == 1:
			resposta.append(0)
	# Vermelho
	elif (mouse[0] - 300) ** 2 + (mouse[1] - 300) ** 2 <= 40000 and \
		(mouse[0] - 300) ** 2 + (mouse[1] - 300) ** 2 >= 8100 and \
		300 <= mouse[0] <= 500 and \
		100 <= mouse[1] <= 300:
		b_vermelho(window)
		if click[0] == 0 and click_on_off == 1:
			resposta.append(1)
	# Amarelo
	elif (mouse[0] - 300) ** 2 + (mouse[1] - 300) ** 2 <= 40000 and \
		(mouse[0] - 300) ** 2 + (mouse[1] - 300) ** 2 >= 8100 and \
		100 <= mouse[0] <= 300 and \
		300 <= mouse[1] <= 500:
		b_amarelo(window)
		if click[0] == 0 and click_on_off == 1:
			resposta.append(2)
	# Azul
	elif (mouse[0] - 300) ** 2 + (mouse[1] - 300) ** 2 <= 40000 and \
		(mouse[0] - 300) ** 2 + (mouse[1] - 300) ** 2 >= 8100 and \
		300 <= mouse[0] <= 500 and \
		300 <= mouse[1] <= 500:
		b_azul(window)
		if click[0] == 0 and click_on_off == 1:
			resposta.append(3)
	# Centro - Restart
	elif (mouse[0] - 300) ** 2 + (mouse[1] - 300) ** 2 <= 6400:
		b_centro(window)
		if click[0] == 0 and click_on_off == 1:
			repeticao_das_cores = 1
			sequencia_do_jogo.append(randrange(4))
			resposta = []
	else: inicio(window)

	pygame.draw.rect(window, branco, (0, 0, 500, 50))
	texto = fonte.render(str(len(sequencia_do_jogo)), 1, preto)
	window.blit(texto, (10, 10))

	click_on_off = click[0]

	pygame.display.update()