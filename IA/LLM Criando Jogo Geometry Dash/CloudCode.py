import pygame
import sys
import random

# ─── Init ───────────────────────────────────────────────────────────────────
pygame.init()

WIDTH, HEIGHT = 900, 500
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Geometry Dash – Python Edition")
clock = pygame.time.Clock()

# ─── Palette ────────────────────────────────────────────────────────────────
C_BG_TOP    = (10,  10,  30)
C_BG_BOT    = (20,  20,  60)
C_GROUND    = (30,  30,  80)
C_GROUND_LN = (50,  50, 110)
C_PLAYER    = (0,  200, 255)
C_PLAYER_LN = (0,  120, 200)
C_SPIKE     = (255,  80,  80)
C_BLOCK     = (80,  80, 200)
C_BLOCK_LN  = (120, 120, 255)
C_STAR      = (255, 255, 200)
C_WHITE     = (255, 255, 255)
C_GOLD      = (255, 210,  50)
C_GREEN     = (50,  230, 100)
C_RED       = (255,  60,  60)
C_GRAY      = (160, 160, 180)
C_DARK      = (15,  15,  40)

# ─── Fonts ──────────────────────────────────────────────────────────────────
font_big   = pygame.font.SysFont("consolas", 52, bold=True)
font_med   = pygame.font.SysFont("consolas", 28, bold=True)
font_small = pygame.font.SysFont("consolas", 20)

# ─── Constants ──────────────────────────────────────────────────────────────
GROUND_Y     = HEIGHT - 80
PLAYER_SIZE  = 38
GRAVITY      = 0.65
JUMP_FORCE   = -13.5
SCROLL_SPEED = 5
TILE         = 44

# Posição X do player na TELA (fixa — o mundo é que rola)
PLAYER_SCREEN_X = 160

# ─── Stars (parallax BG) ────────────────────────────────────────────────────
stars = [
    (random.randint(0, WIDTH), random.randint(0, GROUND_Y - 20), random.uniform(0.3, 1.0))
    for _ in range(120)
]

# ─── Level definition ───────────────────────────────────────────────────────
LEVEL_PATTERN = [
    # aquecimento — obstáculos bem espaçados
    ('spike',  20),
    ('spike',  27),
    ('block',  34),
    ('spike',  41),
    ('spike',  48),
    # seção média — um pouco mais próximos
    ('block',  56),
    ('spike',  63),
    ('dbl',    70),
    ('spike',  78),
    ('block2', 85),
    ('spike',  93),
    # seção difícil — pares com espaço para respirar
    ('dbl',   101),
    ('block',  109),
    ('spike', 116),
    ('dbl',   123),
    ('spike', 131),
    ('block2',138),
    ('spike', 146),
    # final
    ('dbl',   154),
    ('spike', 162),
    ('spike', 169),
    ('block', 176),
    ('dbl',   183),
    ('spike', 191),
]
LEVEL_LENGTH_TILES = 202

def build_obstacles():
    obs = []
    for kind, gx in LEVEL_PATTERN:
        x = gx * TILE
        if kind == 'spike':
            obs.append({
                'type': 'spike',
                'rect': pygame.Rect(x, GROUND_Y - TILE, TILE, TILE),
                'pts': [(x, GROUND_Y), (x + TILE//2, GROUND_Y - TILE), (x + TILE, GROUND_Y)],
            })
        elif kind == 'dbl':
            for i in range(2):
                sx = x + i * TILE
                obs.append({
                    'type': 'spike',
                    'rect': pygame.Rect(sx, GROUND_Y - TILE, TILE, TILE),
                    'pts': [(sx, GROUND_Y), (sx + TILE//2, GROUND_Y - TILE), (sx + TILE, GROUND_Y)],
                })
        elif kind == 'block':
            obs.append({'type': 'block', 'rect': pygame.Rect(x, GROUND_Y - TILE, TILE, TILE)})
        elif kind == 'block2':
            obs.append({'type': 'block', 'rect': pygame.Rect(x, GROUND_Y - TILE*2, TILE, TILE*2)})
    return obs

# ─── Particle system ────────────────────────────────────────────────────────
class Particle:
    def __init__(self, world_x, world_y, color):
        # guarda posição em coordenadas de MUNDO
        self.wx = world_x
        self.wy = world_y
        self.vx = random.uniform(-3, 3)
        self.vy = random.uniform(-5, -1)
        self.life = random.randint(20, 40)
        self.max_life = self.life
        self.color = color
        self.size = random.randint(3, 7)

    def update(self):
        self.wx += self.vx
        self.wy += self.vy
        self.vy += 0.2
        self.life -= 1

    def draw(self, surf, cam_x):
        alpha = self.life / self.max_life
        r, g, b = self.color
        col = (int(r * alpha), int(g * alpha), int(b * alpha))
        sx = self.wx - cam_x   # converte mundo → tela
        pygame.draw.rect(surf, col, (sx, self.wy, self.size, self.size))

# ─── Game state ─────────────────────────────────────────────────────────────
def new_game():
    # O player está fixo em PLAYER_SCREEN_X na tela.
    # cam_x é a coordenada MUNDO que está no canto esquerdo da tela.
    # Portanto world_x do player = cam_x + PLAYER_SCREEN_X (sempre).
    return {
        'py': float(GROUND_Y - PLAYER_SIZE),
        'vy': 0.0,
        'on_ground': True,
        'cam_x': 0.0,          # borda esquerda da câmera em coords de mundo
        'obstacles': build_obstacles(),
        'particles': [],
        'angle': 0.0,
        'progress': 0.0,
        'state': 'playing',    # playing | dead | win
        'dead_timer': 0,
    }

# ─── Draw helpers ───────────────────────────────────────────────────────────
def draw_gradient_bg(surf):
    for y in range(HEIGHT):
        t = y / HEIGHT
        r = int(C_BG_TOP[0] + (C_BG_BOT[0] - C_BG_TOP[0]) * t)
        g = int(C_BG_TOP[1] + (C_BG_BOT[1] - C_BG_TOP[1]) * t)
        b = int(C_BG_TOP[2] + (C_BG_BOT[2] - C_BG_TOP[2]) * t)
        pygame.draw.line(surf, (r, g, b), (0, y), (WIDTH, y))

def draw_stars(surf, cam_x):
    for sx, sy, spd in stars:
        rx = (sx - cam_x * spd * 0.08) % WIDTH
        size = max(1, int(spd * 2))
        pygame.draw.circle(surf, C_STAR, (int(rx), int(sy)), size)

def draw_ground(surf, cam_x):
    pygame.draw.rect(surf, C_GROUND, (0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y))
    offset = int(cam_x) % TILE
    for i in range(WIDTH // TILE + 2):
        x = i * TILE - offset
        pygame.draw.line(surf, C_GROUND_LN, (x, GROUND_Y), (x, HEIGHT), 1)
    for row in range(1, 3):
        pygame.draw.line(surf, C_GROUND_LN, (0, GROUND_Y + row * 20), (WIDTH, GROUND_Y + row * 20), 1)
    pygame.draw.rect(surf, C_BLOCK_LN, (0, GROUND_Y, WIDTH, 2))

def draw_player(surf, screen_x, screen_y, angle):
    size = PLAYER_SIZE
    cx = screen_x + size // 2
    cy = screen_y + size // 2

    # glow
    glow = pygame.Surface((size + 20, size + 20), pygame.SRCALPHA)
    pygame.draw.rect(glow, (0, 200, 255, 40), (0, 0, size + 20, size + 20), border_radius=8)
    surf.blit(glow, (cx - size // 2 - 10, cy - size // 2 - 10))

    # cubo rotacionado
    tile_surf = pygame.Surface((size, size), pygame.SRCALPHA)
    pygame.draw.rect(tile_surf, C_PLAYER, (0, 0, size, size), border_radius=4)
    pygame.draw.rect(tile_surf, C_PLAYER_LN, (0, 0, size, size), 2, border_radius=4)
    m = size // 2
    pygame.draw.polygon(tile_surf, C_PLAYER_LN,
                        [(m, 6), (size-6, m), (m, size-6), (6, m)], 2)

    rot = pygame.transform.rotate(tile_surf, -angle)
    rw, rh = rot.get_size()
    surf.blit(rot, (cx - rw // 2, cy - rh // 2))

def draw_obstacles(surf, obstacles, cam_x):
    for obs in obstacles:
        sx = obs['rect'].x - int(cam_x)   # posição na tela
        if sx > WIDTH + 10 or sx < -TILE * 2:
            continue
        if obs['type'] == 'spike':
            pts = [(p[0] - int(cam_x), p[1]) for p in obs['pts']]
            pygame.draw.polygon(surf, C_SPIKE, pts)
            pygame.draw.polygon(surf, (255, 160, 160), pts, 2)
        else:
            r = pygame.Rect(sx, obs['rect'].y, obs['rect'].w, obs['rect'].h)
            pygame.draw.rect(surf, C_BLOCK, r, border_radius=3)
            pygame.draw.rect(surf, C_BLOCK_LN, r, 2, border_radius=3)
            pygame.draw.line(surf, C_BLOCK_LN, (r.x+4, r.y+4), (r.right-4, r.bottom-4), 1)
            pygame.draw.line(surf, C_BLOCK_LN, (r.right-4, r.y+4), (r.x+4, r.bottom-4), 1)

def draw_progress(surf, pct):
    bw, bh = WIDTH - 60, 12
    bx, by = 30, 18
    pygame.draw.rect(surf, C_DARK, (bx, by, bw, bh), border_radius=6)
    fill = int(bw * pct / 100)
    if fill > 0:
        col = C_GREEN if pct < 80 else C_GOLD
        pygame.draw.rect(surf, col, (bx, by, fill, bh), border_radius=6)
    pygame.draw.rect(surf, C_GRAY, (bx, by, bw, bh), 2, border_radius=6)
    surf.blit(font_small.render(f"{int(pct)}%", True, C_WHITE), (bx + bw + 8, by - 2))

def draw_hud(surf, attempt, deaths):
    surf.blit(font_small.render(f"Attempt  {attempt}", True, C_GRAY), (10, HEIGHT - 30))
    surf.blit(font_small.render(f"Deaths: {deaths}", True, C_GRAY), (WIDTH - 130, HEIGHT - 30))

def draw_finish_line(surf, cam_x):
    fx = LEVEL_LENGTH_TILES * TILE - int(cam_x)
    if 0 < fx < WIDTH:
        pygame.draw.rect(surf, C_GOLD, (fx, GROUND_Y - 200, 4, 200))
        surf.blit(font_small.render("FINISH", True, C_GOLD), (fx - 22, GROUND_Y - 220))

def shrink_rect(rect, margin):
    return pygame.Rect(rect.x + margin, rect.y + margin,
                       rect.w - margin*2, rect.h - margin*2)

# ─── Overlays ───────────────────────────────────────────────────────────────
def overlay_dead(surf, attempt_n, best_pct):
    ov = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    ov.fill((0, 0, 0, 160))
    surf.blit(ov, (0, 0))
    surf.blit(font_big.render("YOU DIED", True, C_RED),
              (WIDTH//2 - font_big.size("YOU DIED")[0]//2, HEIGHT//2 - 80))
    t2 = font_med.render(f"Best: {int(best_pct)}%  |  Attempt {attempt_n}", True, C_GRAY)
    surf.blit(t2, (WIDTH//2 - t2.get_width()//2, HEIGHT//2))
    t3 = font_small.render("SPACE to retry     ESC to quit", True, C_GRAY)
    surf.blit(t3, (WIDTH//2 - t3.get_width()//2, HEIGHT//2 + 60))

def overlay_win(surf, attempt_n):
    ov = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    ov.fill((0, 0, 0, 160))
    surf.blit(ov, (0, 0))
    t1 = font_big.render("LEVEL COMPLETE!", True, C_GOLD)
    surf.blit(t1, (WIDTH//2 - t1.get_width()//2, HEIGHT//2 - 80))
    t2 = font_med.render(f"Completed in {attempt_n} attempt(s)", True, C_WHITE)
    surf.blit(t2, (WIDTH//2 - t2.get_width()//2, HEIGHT//2))
    t3 = font_small.render("SPACE to play again     ESC to quit", True, C_GRAY)
    surf.blit(t3, (WIDTH//2 - t3.get_width()//2, HEIGHT//2 + 60))

def screen_title(surf):
    draw_gradient_bg(surf)
    draw_stars(surf, 0)
    t1 = font_big.render("GEOMETRY DASH", True, C_PLAYER)
    surf.blit(t1, (WIDTH//2 - t1.get_width()//2, HEIGHT//2 - 100))
    t2 = font_med.render("Python Edition", True, C_GOLD)
    surf.blit(t2, (WIDTH//2 - t2.get_width()//2, HEIGHT//2 - 30))
    t3 = font_small.render("SPACE = Iniciar / Pular     ESC = Sair", True, C_GRAY)
    surf.blit(t3, (WIDTH//2 - t3.get_width()//2, HEIGHT//2 + 60))

# ─── Main loop ──────────────────────────────────────────────────────────────
MODE     = 'title'
state    = new_game()
attempt  = 1
best_pct = 0.0

while True:
    clock.tick(FPS)

    jump = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit(); sys.exit()
            if event.key == pygame.K_SPACE:
                jump = True

    # ── Título ──────────────────────────────────────────────────────────────
    if MODE == 'title':
        screen_title(screen)
        if jump:
            MODE = 'game'
            state = new_game()
            attempt = 1
            best_pct = 0.0
        pygame.display.flip()
        continue

    s = state

    # ── Morto ───────────────────────────────────────────────────────────────
    if s['state'] == 'dead':
        s['dead_timer'] -= 1
        draw_gradient_bg(screen)
        draw_stars(screen, s['cam_x'])
        draw_ground(screen, s['cam_x'])
        draw_obstacles(screen, s['obstacles'], s['cam_x'])
        overlay_dead(screen, attempt, best_pct)
        pygame.display.flip()
        if s['dead_timer'] <= 0 and jump:
            attempt += 1
            state = new_game()
        continue

    # ── Vitória ─────────────────────────────────────────────────────────────
    if s['state'] == 'win':
        draw_gradient_bg(screen)
        draw_stars(screen, s['cam_x'])
        draw_ground(screen, s['cam_x'])
        draw_obstacles(screen, s['obstacles'], s['cam_x'])
        overlay_win(screen, attempt)
        pygame.display.flip()
        if jump:
            attempt = 1
            best_pct = 0.0
            state = new_game()
        continue

    # ── Física ──────────────────────────────────────────────────────────────
    if jump and s['on_ground']:
        s['vy'] = JUMP_FORCE
        s['on_ground'] = False

    s['vy'] += GRAVITY
    s['py'] += s['vy']

    # Colisão com o chão
    if s['py'] >= GROUND_Y - PLAYER_SIZE:
        s['py'] = float(GROUND_Y - PLAYER_SIZE)
        s['vy'] = 0.0
        s['on_ground'] = True

    # Câmera avança (o mundo rola para a esquerda)
    s['cam_x'] += SCROLL_SPEED

    # Posição do player no MUNDO = cam_x + posição fixa na tela
    world_px = s['cam_x'] + PLAYER_SCREEN_X

    # Progresso
    total_world = LEVEL_LENGTH_TILES * TILE
    # O nível termina quando world_px chega em total_world
    pct = min(100.0, world_px / total_world * 100)
    s['progress'] = pct
    if pct > best_pct:
        best_pct = pct

    # Rotação
    if not s['on_ground']:
        s['angle'] += 6
    else:
        target = round(s['angle'] / 90) * 90
        s['angle'] += (target - s['angle']) * 0.25

    # Partículas (trail)
    if random.random() < 0.4:
        s['particles'].append(
            Particle(world_px, s['py'] + PLAYER_SIZE - 4, C_PLAYER))
    s['particles'] = [p for p in s['particles'] if p.life > 0]
    for p in s['particles']:
        p.update()

    # ── Detecção de colisão ─────────────────────────────────────────────────
    # Hitbox do player em coordenadas de MUNDO
    player_world = shrink_rect(
        pygame.Rect(int(world_px), int(s['py']), PLAYER_SIZE, PLAYER_SIZE), 5)

    hit = False
    for obs in s['obstacles']:
        if not player_world.colliderect(obs['rect']):
            continue

        if obs['type'] == 'spike':
            tri_rect = shrink_rect(obs['rect'], 6)
            if player_world.colliderect(tri_rect):
                hit = True
                break
        else:
            # Bloco: pode pousar em cima
            prev_bottom = player_world.bottom - s['vy'] - 2
            if prev_bottom <= obs['rect'].top + 4 and s['vy'] >= 0:
                s['py'] = float(obs['rect'].top - PLAYER_SIZE)
                s['vy'] = 0.0
                s['on_ground'] = True
            else:
                hit = True
                break

    # Vitória
    if world_px >= total_world:
        for _ in range(40):
            s['particles'].append(Particle(world_px, s['py'], C_GOLD))
        s['state'] = 'win'

    # Morte
    if hit:
        for _ in range(30):
            s['particles'].append(
                Particle(world_px, s['py'] + PLAYER_SIZE//2, C_RED))
        s['state'] = 'dead'
        s['dead_timer'] = 45

    # ── Desenho ─────────────────────────────────────────────────────────────
    draw_gradient_bg(screen)
    draw_stars(screen, s['cam_x'])

    # Grade de fundo (parallax leve)
    offset = int(s['cam_x'] * 0.4) % TILE
    for i in range(WIDTH // TILE + 2):
        x = i * TILE - offset
        pygame.draw.line(screen, (30, 30, 70), (x, 0), (x, GROUND_Y), 1)

    draw_ground(screen, s['cam_x'])

    for p in s['particles']:
        p.draw(screen, s['cam_x'])

    draw_finish_line(screen, s['cam_x'])
    draw_obstacles(screen, s['obstacles'], s['cam_x'])

    # Player na posição FIXA da tela
    draw_player(screen, PLAYER_SCREEN_X, int(s['py']), s['angle'])

    draw_progress(screen, s['progress'])
    draw_hud(screen, attempt, attempt - 1)

    pygame.display.flip()
