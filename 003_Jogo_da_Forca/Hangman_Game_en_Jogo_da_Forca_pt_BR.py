import pygame as pg
import random

# Cores do jogo
branco = (255, 255, 255)
preto = (0, 0, 0)

# Setup da tela do Jogo
window = pg.display.set_mode((1000, 600))

# Inicializando fonte
pg.font.init()
# Escolhendo uma fonte e tamanho
fonte = pg.font.SysFont("Courier New", 50)
fonte_rb = pg.font.SysFont("Courier New", 30)

palavras = ['PARALELEPIPEDO',
            'ORNITORINCO',
            'APARTAMENTO',
            'XICARA DE CHA']

tentativas_de_letras = [' ', '-']
palavra_escolhida = ''
palavra_camuflada = ''
end_game = True
chance = 0
letra = ' '
click_last_status = False

def Desenho_da_Forca(window, chance):
    # Desenho da Forca
    pg.draw.rect(window, branco, (0, 0, 1000, 600))
    pg.draw.line(window, preto, (100, 500), (100, 100), 10)
    pg.draw.line(window, preto, (50, 500), (150, 500), 10)
    pg.draw.line(window, preto, (100, 100), (300, 100), 10)
    pg.draw.line(window, preto, (300, 100), (300, 150), 10)
    if chance >= 1:
        # Cabeça
        pg.draw.circle(window, preto, (300, 200), 50, 10)
    if chance >= 2:
        # Tronco
        pg.draw.line(window, preto, (300, 250), (300, 350), 10)
    if chance >= 3:
        # Braço Direito
        pg.draw.line(window, preto, (300, 260), (225, 350), 10)
    if chance >= 4:
        # Braço Esquerdo
        pg.draw.line(window, preto, (300, 260), (375, 350), 10)
    if chance >= 5:
        # Perna Direita
        pg.draw.line(window, preto, (300, 350), (375, 450), 10)
    if chance >= 6:
        # Perna Direita
        pg.draw.line(window, preto, (300, 350), (225, 450), 10)

def Desenho_Restart_Button(window):
    pg.draw.rect(window, preto, (700, 100, 200, 65))
    texto = fonte_rb.render('Restart', 1, branco)
    window.blit(texto, (740, 120))

def Sorteando_Palavra(palavras, palavra_escolhida, end_game):
    if end_game == True:
        palavra_n = random.randint(0, len(palavras) - 1)
        palavra_escolhida = palavras[palavra_n]
        end_game = False
        chance = 0
    return palavra_escolhida, end_game

def Camuflando_Palavra(palavra_escolhida, palavra_camuflada, tentativas_de_letras):
    palavra_camuflada = palavra_escolhida
    for n in range(len(palavra_camuflada)):
        if palavra_camuflada[n:n + 1] not in tentativas_de_letras:
            palavra_camuflada = palavra_camuflada.replace(palavra_camuflada[n], '#')
    return palavra_camuflada

def Tentando_uma_Letra(tentativas_de_letras, palavra_escolhida, letra, chance):
    if letra not in tentativas_de_letras:
        tentativas_de_letras.append(letra)
        if letra not in palavra_escolhida:
            chance += 1
    elif letra in tentativas_de_letras:
        pass
    return tentativas_de_letras, chance

def Palavra_do_Jogo(window, palavra_camuflada):
    palavra = fonte.render(palavra_camuflada, 1, preto)
    window.blit(palavra, (200, 500))

def Restart_do_Jogo(palavra_camuflada, end_game, chance, letra, tentativas_de_letras, click_last_status, click, x, y):
    count = 0
    limite = len(palavra_camuflada)
    for n in range(len(palavra_camuflada)):
        if palavra_camuflada[n] != '#':
            count += 1
    if count == limite and click_last_status == False and click[0] == True:
        print('Ok')
        if x >= 700 and x <= 900 and y >= 100 and y <= 165:
            tentativas_de_letras = [' ', '-']
            end_game = True
            chance = 0
            letra = ' '
    return end_game, chance, tentativas_de_letras, letra

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            letra = str(pg.key.name(event.key)).upper()

    # Declarando variavel da posição do mouse
    mouse = pg.mouse.get_pos()
    mouse_position_x = mouse[0]
    mouse_position_y = mouse[1]

    # Declarando variavel do click do mouse
    click = pg.mouse.get_pressed()

    # Jogo
    Desenho_da_Forca(window, chance)
    Desenho_Restart_Button(window)
    palavra_escolhida, end_game = Sorteando_Palavra(palavras, palavra_escolhida, end_game)
    palavra_camuflada = Camuflando_Palavra(palavra_escolhida, palavra_camuflada, tentativas_de_letras)
    tentativas_de_letras, chance = Tentando_uma_Letra(tentativas_de_letras, palavra_escolhida, letra, chance)
    Palavra_do_Jogo(window, palavra_camuflada)
    end_game, chance, tentativas_de_letras, letra = Restart_do_Jogo(palavra_camuflada, end_game, chance, letra, tentativas_de_letras, click_last_status, click, mouse_position_x, mouse_position_y)

    # Click Last Status
    if click[0] == True:
        click_last_status = True
    else:
        click_last_status = False

    pg.display.update()