import pygame
import random
import sys
import math

# ==========================
# CONFIGURAÇÕES
# ==========================
WIDTH = 1200
HEIGHT = 600

GROUND_Y = 500

PLAYER_SIZE = 40
GRAVITY = 0.8
JUMP_FORCE = -15

WORLD_SPEED = 6

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Geometry Dash Melhorado")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 40)

# ==========================
# PLAYER
# ==========================
player = pygame.Rect(
    150,
    GROUND_Y - PLAYER_SIZE,
    PLAYER_SIZE,
    PLAYER_SIZE
)

velocity_y = 0
on_ground = True
rotation = 0

# ==========================
# OBJETOS
# ==========================
platforms = []
spikes = []
moving_spikes = []
gaps = []

score = 0
spawn_timer = 0


# ==========================
# CLASSES
# ==========================
class Platform:

    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)

    def update(self):
        self.rect.x -= WORLD_SPEED

    def draw(self):
        pygame.draw.rect(screen, (100, 220, 255), self.rect)


class Spike:

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)

    def update(self):
        self.rect.x -= WORLD_SPEED

    def draw(self):

        pygame.draw.polygon(
            screen,
            (255, 60, 60),
            [
                (self.rect.left, self.rect.bottom),
                (self.rect.centerx, self.rect.top),
                (self.rect.right, self.rect.bottom)
            ]
        )


class MovingSpike:

    def __init__(self, x, y):

        self.rect = pygame.Rect(x, y, 40, 40)

        self.start_y = y
        self.direction = 1
        self.range = 80
        self.speed = 2

    def update(self):

        self.rect.x -= WORLD_SPEED

        self.rect.y += self.direction * self.speed

        if self.rect.y > self.start_y + self.range:
            self.direction = -1

        if self.rect.y < self.start_y:
            self.direction = 1

    def draw(self):

        pygame.draw.polygon(
            screen,
            (255, 200, 50),
            [
                (self.rect.left, self.rect.bottom),
                (self.rect.centerx, self.rect.top),
                (self.rect.right, self.rect.bottom)
            ]
        )


class Gap:

    def __init__(self, x, width):
        self.rect = pygame.Rect(
            x,
            GROUND_Y,
            width,
            HEIGHT - GROUND_Y
        )

    def update(self):
        self.rect.x -= WORLD_SPEED

    def draw(self):
        pygame.draw.rect(screen, (20, 20, 35), self.rect)


# ==========================
# RESET
# ==========================
def reset_game():

    global velocity_y
    global on_ground
    global score
    global rotation

    player.x = 150
    player.y = GROUND_Y - PLAYER_SIZE

    velocity_y = 0
    on_ground = True

    score = 0
    rotation = 0

    platforms.clear()
    spikes.clear()
    moving_spikes.clear()
    gaps.clear()


# ==========================
# GERADOR DE FASE
# ==========================
def generate_section():

    section_type = random.randint(0, 4)

    x = WIDTH + random.randint(0, 150)

    # ESPINHO NO CHÃO
    if section_type == 0:

        spikes.append(
            Spike(x, GROUND_Y - 40)
        )

    # PLATAFORMA + ESPINHO
    elif section_type == 1:

        plat = Platform(
            x,
            GROUND_Y - 120,
            180,
            20
        )

        platforms.append(plat)

        spikes.append(
            Spike(
                x + 70,
                GROUND_Y - 160
            )
        )

    # BURACO
    elif section_type == 2:

        gaps.append(
            Gap(
                x,
                random.randint(80, 150)
            )
        )

    # ESPINHO MÓVEL
    elif section_type == 3:

        moving_spikes.append(
            MovingSpike(
                x,
                GROUND_Y - 100
            )
        )

    # DUPLO ESPINHO
    else:

        spikes.append(
            Spike(x, GROUND_Y - 40)
        )

        spikes.append(
            Spike(x + 50, GROUND_Y - 40)
        )


# ==========================
# LOOP PRINCIPAL
# ==========================
running = True

while running:

    clock.tick(60)

    # ----------------------
    # EVENTOS
    # ----------------------
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                if on_ground:
                    velocity_y = JUMP_FORCE
                    on_ground = False

    # ----------------------
    # GERADOR
    # ----------------------
    spawn_timer += 1

    if spawn_timer > 80:
        generate_section()
        spawn_timer = 0

    # ----------------------
    # MOVIMENTO PLAYER
    # ----------------------
    velocity_y += GRAVITY
    player.y += velocity_y

    on_ground = False

    # CHÃO
    if player.bottom >= GROUND_Y:

        inside_gap = False

        for gap in gaps:

            if gap.rect.left < player.centerx < gap.rect.right:
                inside_gap = True
                break

        if not inside_gap:

            player.bottom = GROUND_Y
            velocity_y = 0
            on_ground = True

    # PLATAFORMAS
    for platform in platforms:

        if velocity_y >= 0:

            if player.colliderect(platform.rect):

                if player.bottom - velocity_y <= platform.rect.top:

                    player.bottom = platform.rect.top
                    velocity_y = 0
                    on_ground = True

    # ROTAÇÃO
    if not on_ground:
        rotation += 8
    else:
        rotation = (rotation // 90) * 90

    # ----------------------
    # UPDATE OBJETOS
    # ----------------------
    for obj in platforms:
        obj.update()

    for obj in spikes:
        obj.update()

    for obj in moving_spikes:
        obj.update()

    for obj in gaps:
        obj.update()

    # ----------------------
    # REMOVER OBJETOS
    # ----------------------
    platforms = [p for p in platforms if p.rect.right > 0]
    spikes = [s for s in spikes if s.rect.right > 0]
    moving_spikes = [m for m in moving_spikes if m.rect.right > 0]
    gaps = [g for g in gaps if g.rect.right > 0]

    # ----------------------
    # COLISÕES
    # ----------------------
    for spike in spikes:

        if player.colliderect(spike.rect):
            reset_game()

    for spike in moving_spikes:

        if player.colliderect(spike.rect):
            reset_game()

    # caiu no buraco
    if player.top > HEIGHT:
        reset_game()

    # ----------------------
    # SCORE
    # ----------------------
    score += 1

    # ----------------------
    # DESENHO
    # ----------------------
    screen.fill((20, 20, 35))

    # chão
    pygame.draw.rect(
        screen,
        (60, 200, 100),
        (
            0,
            GROUND_Y,
            WIDTH,
            HEIGHT - GROUND_Y
        )
    )

    # buracos
    for gap in gaps:
        gap.draw()

    # plataformas
    for platform in platforms:
        platform.draw()

    # espinhos
    for spike in spikes:
        spike.draw()

    # espinhos móveis
    for spike in moving_spikes:
        spike.draw()

    # cubo girando
    cube_surface = pygame.Surface(
        (PLAYER_SIZE, PLAYER_SIZE),
        pygame.SRCALPHA
    )

    pygame.draw.rect(
        cube_surface,
        (0, 220, 255),
        (0, 0, PLAYER_SIZE, PLAYER_SIZE)
    )

    rotated_cube = pygame.transform.rotate(
        cube_surface,
        rotation
    )

    cube_rect = rotated_cube.get_rect(
        center=player.center
    )

    screen.blit(rotated_cube, cube_rect)

    score_text = font.render(
        f"Score: {score // 10}",
        True,
        (255, 255, 255)
    )

    screen.blit(score_text, (20, 20))

    pygame.display.flip()

pygame.quit()
sys.exit()