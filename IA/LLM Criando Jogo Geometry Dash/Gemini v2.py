import pygame
import sys
import random

# Inicialização do Pygame
pygame.init()

# --- CONFIGURAÇÕES DE TELA ---
LARGURA_TELA = 800
ALTURA_TELA = 500
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Geometry Dash Avançado (Pygame)")
relogio = pygame.time.Clock()

# --- CORES ---
AZUL_CUBO = (0, 180, 255)
PRETO_FUNDO = (15, 15, 25)      # Fundo escuro estilizado
ROXO_CHAO = (60, 20, 100)       # Blocos de chão e plataformas
VERMELHO_ESPINHO = (255, 60, 60)
AMARELO_MOVEL = (255, 200, 0)   # Obstáculos dinâmicos
TEXTO_COR = (255, 255, 255)
LINHA_GRADE = (30, 30, 50)

# --- CONFIGURAÇÕES DO JOGO ---
FPS = 60
VELOCIDADE_CENARIO = 7 
ALTURA_CHAO_PADRAO = 400
TAMANHO_BLOCO = 40

# --- CLASSE JOGADOR (CUBO) ---
class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.tamanho = 36 # Um pouco menor que o bloco para facilitar manobras
        self.image = pygame.Surface((self.tamanho, self.tamanho))
        self.image.fill(AZUL_CUBO)
        
        # Borda interna estilizada
        pygame.draw.rect(self.image, (255, 255, 255), (0, 0, self.tamanho, self.tamanho), 3)
        
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = ALTURA_CHAO_PADRAO - self.tamanho
        
        # Física
        self.vel_y = 0
        self.gravidade = 1.4
        self.forca_pulo = -17
        self.no_chao = False

    def update(self, plataformas):
        # Aplicar gravidade constantemente
        self.vel_y += self.gravidade
        
        # Movimento Vertical
        self.rect.y += self.vel_y
        self.no_chao = False
        
        # Testar colisão vertical com as plataformas/chão
        for plat in plataformas:
            if self.rect.colliderect(plat.rect):
                # Se o cubo estiver caindo e colidir com o topo da plataforma
                if self.vel_y > 0 and self.rect.bottom <= plat.rect.top + 15:
                    self.rect.bottom = plat.rect.top
                    self.vel_y = 0
                    self.no_chao = True
                # Se o cubo bater a cabeça por baixo de uma plataforma
                elif self.vel_y < 0 and self.rect.top >= plat.rect.bottom - 15:
                    self.rect.top = plat.rect.bottom
                    self.vel_y = 0

        # Verificação de queda no buraco (fora da tela)
        if self.rect.top > ALTURA_TELA:
            return True # Retorna True indicando que morreu
        return False

    def pular(self):
        if self.no_chao:
            self.vel_y = self.forca_pulo
            self.no_chao = False

# --- CLASSE BLOCO (CHÃO E PLATAFORMAS) ---
class Bloco(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TAMANHO_BLOCO, TAMANHO_BLOCO))
        self.image.fill(ROXO_CHAO)
        # Borda estética para destacar os blocos
        pygame.draw.rect(self.image, (100, 50, 180), (0, 0, TAMANHO_BLOCO, TAMANHO_BLOCO), 2)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x -= VELOCIDADE_CENARIO
        if self.rect.right < 0:
            self.kill()

# --- CLASSE ESPINHO ESTÁTICO ---
class Espinho(pygame.sprite.Sprite):
    def __init__(self, x, y_bottom):
        super().__init__()
        self.image = pygame.Surface((TAMANHO_BLOCO, TAMANHO_BLOCO), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, VERMELHO_ESPINHO, [
            (TAMANHO_BLOCO // 2, 0),         
            (0, TAMANHO_BLOCO),              
            (TAMANHO_BLOCO, TAMANHO_BLOCO)    
        ])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y_bottom

    def update(self):
        self.rect.x -= VELOCIDADE_CENARIO
        if self.rect.right < 0:
            self.kill()

# --- CLASSE OBSTÁCULO DINÂMICO (ESPINHO QUE SE MOVE) ---
class EspinhoMovel(pygame.sprite.Sprite):
    def __init__(self, x, y_base):
        super().__init__()
        self.image = pygame.Surface((TAMANHO_BLOCO, TAMANHO_BLOCO), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, AMARELO_MOVEL, [
            (TAMANHO_BLOCO // 2, 0),         
            (0, TAMANHO_BLOCO),              
            (TAMANHO_BLOCO, TAMANHO_BLOCO)    
        ])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.y_base = y_base
        self.rect.bottom = y_base
        
        # Variáveis de movimento (sobe e desce)
        self.faixa_movimento = 80
        self.velocidade_subida = 3
        self.direcao = -1 # -1 para subir, 1 para descer

    def update(self):
        self.rect.x -= VELOCIDADE_CENARIO
        
        # Movimento vertical dinâmico
        self.rect.y += self.velocidade_subida * self.direcao
        
        # Inverter direção se atingir os limites
        if self.rect.bottom <= self.y_base - self.faixa_movimento:
            self.direcao = 1 # Começa a descer
        elif self.rect.bottom >= self.y_base:
            self.rect.bottom = self.y_base
            self.direcao = -1 # Começa a subir

        if self.rect.right < 0:
            self.kill()

# --- GERADOR DE CENÁRIO (CHUNKS) ---
def gerar_proximo_segmento(x_start, grupo_blocos, grupo_obstaculos):
    """Gera padrões de fase dinamicamente: plataformas, buracos e espinhos"""
    tipo_segmento = random.choice(["normal", "buraco_simples", "plataforma_alta", "obstaculo_movel", "escada"])
    largura_segmento = 0

    if tipo_segmento == "normal":
        # 6 blocos de chão reto com um espinho no meio
        largura_segmento = 6 * TAMANHO_BLOCO
        for i in range(6):
            grupo_blocos.add(Bloco(x_start + (i * TAMANHO_BLOCO), ALTURA_CHAO_PADRAO))
        if random.choice([True, False]):
            grupo_obstaculos.add(Espinho(x_start + (3 * TAMANHO_BLOCO), ALTURA_CHAO_PADRAO))

    elif tipo_segmento == "buraco_simples":
        # Cria chão, pula 3 blocos (buraco) e cria chão de novo
        largura_segmento = 7 * TAMANHO_BLOCO
        for i in range(2):
            grupo_blocos.add(Bloco(x_start + (i * TAMANHO_BLOCO), ALTURA_CHAO_PADRAO))
        # i = 2, 3, 4 são deixados vazios (Buraco!)
        for i in range(5, 7):
            grupo_blocos.add(Bloco(x_start + (i * TAMANHO_BLOCO), ALTURA_CHAO_PADRAO))

    elif tipo_segmento == "plataforma_alta":
        # Chão embaixo com um vão, e plataformas flutuantes suspensas
        largura_segmento = 8 * TAMANHO_BLOCO
        # Chão no início e fim
        grupo_blocos.add(Bloco(x_start, ALTURA_CHAO_PADRAO))
        grupo_blocos.add(Bloco(x_start + (7 * TAMANHO_BLOCO), ALTURA_CHAO_PADRAO))
        
        # Plataformas flutuantes no meio (altura menor)
        for i in range(2, 6):
            grupo_blocos.add(Bloco(x_start + (i * TAMANHO_BLOCO), ALTURA_CHAO_PADRAO - 100))
            # Chance de espinho em cima da plataforma flutuante
            if i == 3 and random.choice([True, False]):
                grupo_obstaculos.add(Espinho(x_start + (i * TAMANHO_BLOCO), ALTURA_CHAO_PADRAO - 100))

    elif tipo_segmento == "obstaculo_movel":
        # Chão seguro, mas com um espinho amarelo que fica subindo e descendo
        largura_segmento = 6 * TAMANHO_BLOCO
        for i in range(6):
            grupo_blocos.add(Bloco(x_start + (i * TAMANHO_BLOCO), ALTURA_CHAO_PADRAO))
        grupo_obstaculos.add(EspinhoMovel(x_start + (3 * TAMANHO_BLOCO), ALTURA_CHAO_PADRAO))

    elif tipo_segmento == "escada":
        # Estrutura em formato de escada para testar pulos em sequência
        largura_segmento = 8 * TAMANHO_BLOCO
        grupo_blocos.add(Bloco(x_start, ALTURA_CHAO_PADRAO))
        grupo_blocos.add(Bloco(x_start + (1 * TAMANHO_BLOCO), ALTURA_CHAO_PADRAO))
        
        grupo_blocos.add(Bloco(x_start + (3 * TAMANHO_BLOCO), ALTURA_CHAO_PADRAO - 50))
        grupo_blocos.add(Bloco(x_start + (4 * TAMANHO_BLOCO), ALTURA_CHAO_PADRAO - 50))
        
        grupo_blocos.add(Bloco(x_start + (6 * TAMANHO_BLOCO), ALTURA_CHAO_PADRAO - 100))
        grupo_blocos.add(Bloco(x_start + (7 * TAMANHO_BLOCO), ALTURA_CHAO_PADRAO - 100))

    return largura_segmento

# --- REINICIALIZAÇÃO DO JOGO ---
def inicializar_jogo():
    jogador = Jogador()
    grupo_jogador = pygame.sprite.GroupSingle(jogador)
    grupo_blocos = pygame.sprite.Group()
    grupo_obstaculos = pygame.sprite.Group()

    # Gerar chão inicial plano embaixo do jogador para ele não cair logo no spawn
    for i in range(0, LARGURA_TELA // TAMANHO_BLOCO + 5):
        grupo_blocos.add(Bloco(i * TAMANHO_BLOCO, ALTURA_CHAO_PADRAO))

    return jogador, grupo_jogador, grupo_blocos, grupo_obstaculos

# --- FUNÇÃO PRINCIPAL ---
def main():
    jogador, grupo_jogador, grupo_blocos, grupo_obstaculos = inicializar_jogo()
    
    # Controla onde o próximo segmento de cenário deve ser renderizado
    proximo_x_geracao = LARGURA_TELA + 80
    
    fonte = pygame.font.SysFont("Impact", 28)
    score = 0

    while True:
        relogio.tick(FPS)
        score += 1

        # --- EVENTOS ---
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Mecânica do Geometry Dash: Segurar ESPAÇO faz o cubo pular continuamente ao tocar no chão
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_SPACE]:
            jogador.pular()

        # --- GERAÇÃO INFINITA DE CENÁRIO ---
        # Se o último bloco gerado estiver entrando na tela, gera o próximo trecho da fase
        if proximo_x_geracao < LARGURA_TELA + 200:
            largura_gerada = gerar_proximo_segmento(proximo_x_geracao, grupo_blocos, grupo_obstaculos)
            proximo_x_geracao += largura_gerada

        # Atualiza a posição de geração com a velocidade do cenário
        proximo_x_geracao -= VELOCIDADE_CENARIO

        # --- ATUALIZAÇÕES DOS SPRITES ---
        grupo_blocos.update()
        grupo_obstaculos.update()
        caiu_no_buraco = jogador.update(grupo_blocos.sprites())

        # --- VERIFICAÇÃO DE DERROTA (COLISÕES E PAREDES) ---
        colisao_obstaculo = pygame.sprite.spritecollide(jogador, grupo_obstaculos, False)
        
        # Testar se o jogador bateu de frente contra a lateral de algum bloco (Parede)
        bateu_na_parede = False
        for bloco in grupo_blocos:
            if jogador.rect.colliderect(bloco.rect):
                # Se o lado direito do cubo ultrapassou a lateral esquerda do bloco, mas ele não está em cima
                if jogador.rect.right > bloco.rect.left + 6 and jogador.rect.left < bloco.rect.left:
                    if jogador.rect.bottom > bloco.rect.top + 10:
                        bateu_na_parede = True

        # Se morreu por qualquer motivo, reseta tudo instantaneamente
        if caiu_no_buraco or colisao_obstaculo or bateu_na_parede:
            jogador, grupo_jogador, grupo_blocos, grupo_obstaculos = inicializar_jogo()
            proximo_x_geracao = LARGURA_TELA + 80
            score = 0

        # --- DESENHO / RENDERIZAÇÃO ---
        tela.fill(PRETO_FUNDO)

        # Desenhar uma grade de fundo (Estética Tron/Geometry Dash)
        for x in range(0, LARGURA_TELA, TAMANHO_BLOCO):
            pygame.draw.line(tela, LINHA_GRADE, (x, 0), (x, ALTURA_TELA))
        for y in range(0, ALTURA_TELA, TAMANHO_BLOCO):
            pygame.draw.line(tela, LINHA_GRADE, (0, y), (LARGURA_TELA, y))

        # Desenhar os objetos reais do jogo
        grupo_blocos.draw(tela)
        grupo_obstaculos.draw(tela)
        grupo_jogador.draw(tela)

        # UI - Pontuação
        texto_score = fonte.render(f"DISTÂNCIA: {score // 10}m", True, TEXTO_COR)
        tela.blit(texto_score, (20, 20))

        pygame.display.flip()

if __name__ == "__main__":
    main()