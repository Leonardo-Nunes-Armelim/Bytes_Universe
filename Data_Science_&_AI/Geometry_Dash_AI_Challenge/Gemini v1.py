import pygame
import sys
import random

# Inicialização do Pygame
pygame.init()

# --- CONFIGURAÇÕES DE TELA ---
LARGURA_TELA = 800
ALTURA_TELA = 500
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Geometry Dash Clone (Pygame)")
relogio = pygame.time.Clock()

# --- CORES ---
AZUL_CUBO = (0, 180, 255)
PRETO_FUNDO = (20, 20, 20)
BRANCO_CHÃO = (240, 240, 240)
VERMELHO_ESPINHO = (255, 50, 50)
VERDE_PLATAFORMA = (50, 200, 50)
TEXTO_COR = (255, 255, 255)

# --- CONFIGURAÇÕES DO JOGO ---
FPS = 60
VELOCIDADE_CENARIO = 6  # Velocidade com que os obstáculos vêm
ALTURA_CHAO = 400

# --- CLASSE JOGADOR (CUBO) ---
class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.tamanho = 40
        self.image = pygame.Surface((self.tamanho, self.tamanho))
        self.image.fill(AZUL_CUBO)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = ALTURA_CHAO - self.tamanho
        
        # Física de pulo
        self.vel_y = 0
        self.gravidade = 1.2
        self.forca_pulo = -18
        self.no_chao = True

    def pular(self):
        if self.no_chao:
            self.vel_y = self.forca_pulo
            self.no_chao = False

    def update(self):
        # Aplicar gravidade
        self.vel_y += self.gravidade
        self.rect.y += self.vel_y

        # Colisão com o chão básico
        if self.rect.bottom >= ALTURA_CHAO:
            self.rect.bottom = ALTURA_CHAO
            self.vel_y = 0
            self.no_chao = True

# --- CLASSE ESPINHO (OBSTÁCULO MORTE) ---
class Espinho(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.tamanho = 40
        self.image = pygame.Surface((self.tamanho, self.tamanho), pygame.SRCALPHA)
        # Desenha um triângulo (espinho) na superfície transparente
        pygame.draw.polygon(self.image, VERMELHO_ESPINHO, [
            (self.tamanho // 2, 0),         # Topo
            (0, self.tamanho),              # Inferior Esquerdo
            (self.tamanho, self.tamanho)    # Inferior Direito
        ])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = ALTURA_CHAO

    def update(self):
        self.rect.x -= VELOCIDADE_CENARIO
        if self.rect.right < 0:
            self.kill()  # Remove do jogo se sair da tela

# --- CLASSE PLATAFORMA ---
class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y, largura, altura):
        super().__init__()
        self.image = pygame.Surface((largura, altura))
        self.image.fill(VERDE_PLATAFORMA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x -= VELOCIDADE_CENARIO
        if self.rect.right < 0:
            self.kill()

# --- FUNÇÃO PRINCIPAL ---
def reiniciar_jogo():
    jogador = Jogador()
    grupo_jogador = pygame.sprite.GroupSingle(jogador)
    grupo_obstaculos = pygame.sprite.Group()
    return jogador, grupo_jogador, grupo_obstaculos

def main():
    jogador, grupo_jogador, grupo_obstaculos = reiniciar_jogo()
    
    # Temporizador para gerar obstáculos
    timer_obstaculo = pygame.USEREVENT + 1
    pygame.time.set_timer(timer_obstaculo, 1500)  # Gera algo a cada 1.5 segundos

    fonte = pygame.font.SysFont("Arial", 30)
    score = 0
    jogando = True

    while jogando:
        relogio.tick(FPS)
        score += 1  # Pontuação baseada no tempo de sobrevivência

        # --- EVENTOS ---
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    jogador.pular()

            if evento.type == timer_obstaculo:
                # Escolhe aleatoriamente entre gerar um espinho ou uma plataforma
                if random.choice([True, False]):
                    grupo_obstaculos.add(Espinho(LARGURA_TELA + 50))
                else:
                    # Gera uma plataforma e um espinho em cima dela
                    alt_plat = ALTURA_CHAO - 70
                    grupo_obstaculos.add(Plataforma(LARGURA_TELA + 50, alt_plat, 100, 20))
                    # 50% de chance de ter um espinho em cima da plataforma
                    if random.choice([True, False]):
                        espinho_plat = Espinho(LARGURA_TELA + 80)
                        espinho_plat.rect.bottom = alt_plat
                        grupo_obstaculos.add(espinho_plat)

        # --- ATUALIZAÇÕES ---
        grupo_jogador.update()
        grupo_obstaculos.update()

        # Lógica de colisão com Plataformas (ficar em cima delas)
        # Filtra apenas as plataformas do grupo de obstáculos
        plataformas = [o for o in grupo_obstaculos if isinstance(o, Plataforma)]
        for plat in plataformas:
            if jogador.rect.colliderect(plat.rect):
                # Se estiver caindo e colidir com o topo da plataforma
                if jogador.vel_y > 0 and jogador.rect.bottom <= plat.rect.top + 15:
                    jogador.rect.bottom = plat.rect.top
                    jogador.vel_y = 0
                    jogador.no_chao = True

        # Lógica de colisão mortal (Espinhos ou bater na lateral da plataforma)
        espinhos = [o for o in grupo_obstaculos if isinstance(o, Espinho)]
        colisao_espinho = pygame.sprite.spritecollide(jogador, espinhos, False)
        
        colisao_lateral_plat = False
        for plat in plataformas:
            if jogador.rect.colliderect(plat.rect) and jogador.rect.bottom > plat.rect.top + 15:
                colisao_lateral_plat = True # Bateu na parede da plataforma

        if colisao_espinho or colisao_lateral_plat:
            # Se colidir, o jogo reseta instantaneamente (Mecânica do Geometry Dash)
            jogador, grupo_jogador, grupo_obstaculos = reiniciar_jogo()
            score = 0

        # --- RENDERIZAÇÃO (DESENHO) ---
        tela.fill(PRETO_FUNDO)

        # Desenhar o chão
        pygame.draw.rect(tela, BRANCO_CHÃO, (0, ALTURA_CHAO, LARGURA_TELA, ALTURA_TELA - ALTURA_CHAO))

        # Desenhar sprites
        grupo_obstaculos.draw(tela)
        grupo_jogador.draw(tela)

        # Mostrar Pontuação
        texto_score = fonte.render(f"Pontos: {score // 10}", True, TEXTO_COR)
        tela.blit(texto_score, (20, 20))

        pygame.display.flip()

if __name__ == "__main__":
    main()