import pygame as pg
import random
import math


class TypingShooter:
    def __init__(self):
        self.white = (255, 255, 255)
        self.black = (  0,   0,   0)
        self.green = (  0, 255,   0)
        self.red   = (255,   0,   0)

        self.window = pg.display.set_mode((1500, 900))

        pg.font.init()
        self.font = pg.font.SysFont("Courier New", 25, bold=True)

        self.clock = pg.time.Clock()

        background = pg.image.load('./background.jpg')
        spaceship  = pg.image.load('./spaceship.png')
        enemy_lv_1 = pg.image.load('./enemy_lv_1.png')
        enemy_lv_3 = pg.image.load('./enemy_lv_3.png')
        enemy_lv_5 = pg.image.load('./enemy_lv_5.png')
        self.background = pg.transform.scale(background, (1500, 900))
        self.spaceship  = pg.transform.scale(spaceship,  (  92, 110))
        self.enemy_lv_1 = pg.transform.scale(enemy_lv_1, (  65,  65))
        self.enemy_lv_3 = pg.transform.scale(enemy_lv_3, (  80,  72))
        self.enemy_lv_5 = pg.transform.scale(enemy_lv_5, (  90,  90))

        self.words_5 = [
            'canto', 'prato', 'vento', 'certo', 'livro', 'plano', 'festa', 'carta', 'firme', 'campo',
            'verde', 'areia', 'primo', 'banco', 'cobre', 'ferro', 'folha', 'setor', 'claro', 'feira',
            'limpo', 'tarde', 'noite', 'andar', 'porto', 'nuvem', 'risco', 'jovem', 'posto', 'teste',
            'custo', 'metas', 'dente', 'farol', 'ganho', 'gosto', 'curso', 'dados', 'etapa', 'forma',
            'fonte', 'lente', 'marca', 'pacto', 'pista', 'ponto', 'serie', 'sinal', 'chave', 'trama',
            'vazio', 'astro', 'barra', 'cinto', 'cobra', 'folga', 'grade', 'justo', 'lapis', 'mapas',
            'nobre', 'quase', 'regra', 'saldo', 'touro', 'unico', 'vindo', 'zebra', 'caixa', 'bolsa',
            'calmo', 'grupo', 'humor', 'ideia', 'julho', 'lenha', 'navio', 'pleno', 'barco', 'senha']

        self.words_7 = [
            'corrida', 'amizade', 'barulho', 'cultura', 'enxoval', 'jardins', 'leitura', 'naturez',
            'quebrar', 'retorno', 'sistema', 'teclado', 'visitar', 'zelador', 'caminho', 'desafio',
            'formado', 'garrafa', 'habitar', 'jornada', 'operado', 'palheta', 'querido', 'relatar',
            'salgado', 'tamanho', 'viagens', 'zangado', 'alicate', 'brincar', 'calçado', 'derrota',
            'elevado', 'fornada', 'honesto', 'julgado', 'lateral', 'meditar', 'unidade', 'consumo',
            'desenho', 'engajar', 'foguete', 'gramado', 'manobra', 'olharam', 'quartel', 'rabisco',
            'sorriso', 'tempero', 'urgente', 'carpete', 'enfeite', 'formosa', 'garante', 'interno']

        self.words_10 = [
            'computador', 'informaçao', 'relacionar', 'aproveitar', 'habilidade', 'pensamento', 'ferramenta',
            'capacidade', 'orientaçao', 'transporte', 'construçao', 'planejador', 'disciplina', 'argumentar',
            'fundamento', 'matematica', 'observador', 'questionar', 'realizando', 'universais', 'adaptativo',
            'habilitado', 'interativo', 'libertador', 'navegadora', 'objetivada', 'participar', 'qualificar',
            'utilizaçao', 'acelerador', 'biblioteca', 'carregador', 'dependente', 'facilidade', 'identidade',
            'justamente', 'manutençao', 'quantidade', 'reciclagem', 'utilizador', 'aprimorado', 'burocracia']

        self.words_15 = [
            'desenvolvimento', 'transformadores', 'desaparecimento', 'telecomunicaçao', 'reorganizadores',
            'identificadores', 'contraintuitivo', 'filosoficamente', 'teletransmissao', 'descarbonizaçao',
            'desconfiguraçao', 'interacionistas', 'socioeconomicas', 'espiritualidade', 'microcomputador',
            'desaconselhavel', 'fundamentalismo', 'obrigatoriedade', 'particularidade', 'paralelepipedos']

        self.typed_letters = 0
        self.typed_words = 0
        self.score = 0
        self.speed = 0.5
        self.game_over = False

        # [enemy level, display untyped_word, display typed_word, memory of the untyped word, memory of the typed word]
        word_1 = random.choice(self.words_15)
        word_2 = random.choice(self.words_7)
        enemy_1_x = random.randint(600, 1150)
        enemy_2_x = random.randint(50, 450)
        enemy_1_y = random.randint(50, 100)
        enemy_2_y = random.randint(50, 100)
        self.enemies = [[5, word_1, '', [enemy_1_x, enemy_1_y], word_1, ''],
                        [1, word_2, '', [enemy_2_x, enemy_2_y], word_2, '']]
        self.shots = []
        self.cannon = 'left' # left and right

    def clear_window(self):
        self.window.blit(self.background, (0, 0))

    def draw_spaceship_word(self, word, typed, position):
        typed_word = self.font.render(typed, 1, self.green)
        untyped_word = self.font.render(word, 1, self.white)
        self.window.blit(typed_word, (position[0] + 100, position[1] + 35))
        self.window.blit(untyped_word, (position[0] + 100 + typed_word.get_width(), position[1] + 35))

    def draw_spaceships(self):
        # Player's spaceship
        self.window.blit(self.spaceship, (705, 750))

        # Enemy's spaceship
        for enemy in self.enemies:
            if enemy[0] == 1:
                self.draw_spaceship_word(enemy[1], enemy[2], enemy[3])
                self.window.blit(self.enemy_lv_1, (enemy[3][0], enemy[3][1]))
            elif enemy[0] == 3:
                self.draw_spaceship_word(enemy[1], enemy[2], enemy[3])
                self.window.blit(self.enemy_lv_3, (enemy[3][0], enemy[3][1]))
            elif enemy[0] == 5:
                self.draw_spaceship_word(enemy[1], enemy[2], enemy[3])
                self.window.blit(self.enemy_lv_5, (enemy[3][0], enemy[3][1]))

    def shots_animation(self):
        for i in range(len(self.shots)):
            delta_x = (self.shots[i][2][0] - self.shots[i][1][0])
            delta_y = (self.shots[i][2][1] - self.shots[i][1][1])
            angle = math.atan2(delta_y, delta_x)
            self.shots[i][1][0] += math.cos(angle) * 15
            self.shots[i][1][1] += math.sin(angle) * 15
            shot_trail_x = self.shots[i][1][0] - math.cos(angle) * 20
            shot_trail_y = self.shots[i][1][1] - math.sin(angle) * 20
            pg.draw.circle(self.window, self.red, (self.shots[i][1][0], self.shots[i][1][1]), 5)
            pg.draw.line(self.window, self.red, (self.shots[i][1][0], self.shots[i][1][1]), (shot_trail_x, shot_trail_y), 3)

            if self.shots[i][1][1] <= self.shots[i][2][1] and abs(self.shots[i][1][0] - self.shots[i][2][0]) <= 50:
                for ii in range(len(self.enemies)):
                    if self.shots[i][0] == self.enemies[ii][1][0:1]:
                        if self.shots[i][3][4] == self.enemies[ii][4] and self.shots[i][3][5] == self.enemies[ii][5]:
                            self.enemies[ii][2] += self.shots[i][0]
                            self.enemies[ii][1] = self.enemies[ii][1][1:len(self.enemies[ii][1])]
                            self.shots.pop(i)
                            self.typed_letters += 1
                            return

    def enimies_animation(self):
        if self.game_over == False:
            for enemy in self.enemies:
                enemy[3][1] += self.speed

    def keyboard(self, key):
        if self.game_over == False:
            for enemy in self.enemies:
                if enemy[4][len(enemy[5]):len(enemy[5]) + 1] == key:
                    enemy[5] += key
                    if self.cannon == 'left':
                        self.shots.append([key, [725, 785], [enemy[3][0]+45, enemy[3][1]+80], enemy])
                        self.cannon = 'right'
                    else:
                        self.shots.append([key, [777, 785], [enemy[3][0]+45, enemy[3][1]+80], enemy])
                        self.cannon = 'left'

    def add_new_enemy(self):
        word_level = random.randint(1, 4)
        enemy_x = random.randint(50, 1150)
        if word_level == 1:
            word = random.choice(self.words_5)
            self.enemies.append([1, word, '', [enemy_x, -100], word, ''])
        elif word_level == 2:
            word = random.choice(self.words_7)
            self.enemies.append([1, word, '', [enemy_x, -100], word, ''])
        elif word_level == 3:
            word = random.choice(self.words_10)
            self.enemies.append([3, word, '', [enemy_x, -100], word, ''])
        elif word_level == 4:
            word = random.choice(self.words_15)
            self.enemies.append([5, word, '', [enemy_x, -100], word, ''])

    def check_for_enemies(self):
        if len(self.enemies) == 0:
            self.add_new_enemy()
        elif self.enemies[-1][3][1] >= 50 and len(self.enemies) <= 5:
            self.add_new_enemy()

    def destroy_enemy(self):
        for i in range(len(self.enemies)):
            if len(self.enemies[i][1]) == 0:
                self.enemies.pop(i)
                self.typed_words += 1
                return

    def game_speed(self):
        self.speed = min(0.5 + ((self.score // 100) / 10), 2)

    def game_score(self):
        self.score = self.typed_letters + (self.typed_words * 5)
        score = self.font.render(f'Score: {self.score}', 1, self.white)
        self.window.blit(score, (0, 875))

    def is_game_over(self):
        for enemy in self.enemies:
            if enemy[0] == 1:
                if enemy[3][1] >= 900 - 65:
                    self.game_over = True
            elif enemy[0] == 3:
                if enemy[3][1] >= 900 - 72:
                    self.game_over = True
            elif enemy[0] == 5:
                if enemy[3][1] >= 900 - 90:
                    self.game_over = True

    def game_over_screen(self):
        if self.game_over:
            pg.draw.rect(self.window, self.black, (500, 300, 500, 300))
            pg.draw.rect(self.window, self.white, (500, 300, 500, 300), 5)
            game_over = self.font.render('Game Over',                            1, self.white)
            score = self.font.render(f'Score: {self.score}',                     1, self.white)
            letters = self.font.render(f'Typed letters: {self.typed_letters}',   1, self.white)
            enemies = self.font.render(f'Destroyed enemies: {self.typed_words}', 1, self.white)
            speed = self.font.render(f'Game speed: {self.speed}',                1, self.white)
            restart_instructions = self.font.render('Press enter to play again', 1, self.white)
            width = self.window.get_width()
            height = self.window.get_height()
            self.window.blit(game_over,            ((width/2)-(game_over.get_width()/2),            (height/2) - (4*25)))
            self.window.blit(score,                ((width/2)-(score.get_width()/2),                (height/2) - (2*25)))
            self.window.blit(letters,              ((width/2)-(letters.get_width()/2),              (height/2) - (1*25)))
            self.window.blit(enemies,              ((width/2)-(enemies.get_width()/2),              (height/2)         ))
            self.window.blit(speed,                ((width/2)-(speed.get_width()/2),                (height/2) + (1*25)))
            self.window.blit(restart_instructions, ((width/2)-(restart_instructions.get_width()/2), (height/2) + (3*25)))

    def restart(self, key):
        if self.game_over:
            if key == 'return':
                self.typed_letters = 0
                self.typed_words = 0
                self.score = 0
                self.speed = 0.5
                self.game_over = False
                word_1 = random.choice(self.words_15)
                word_2 = random.choice(self.words_7)
                enemy_1_x = random.randint(600, 1150)
                enemy_2_x = random.randint(50, 450)
                enemy_1_y = random.randint(50, 100)
                enemy_2_y = random.randint(50, 100)
                self.enemies = [[5, word_1, '', [enemy_1_x, enemy_1_y], word_1, ''],
                                [1, word_2, '', [enemy_2_x, enemy_2_y], word_2, '']]
                self.shots = []
                self.cannon = 'left'


typing_shooter = TypingShooter()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            typing_shooter.keyboard(event.unicode)
            typing_shooter.restart(pg.key.name(event.key))
            if pg.key.name(event.key) == 'escape':
                pg.quit()
                quit()

    # Game
    typing_shooter.clock.tick(60)
    typing_shooter.clear_window()
    typing_shooter.check_for_enemies()
    typing_shooter.draw_spaceships()
    typing_shooter.shots_animation()
    typing_shooter.enimies_animation()
    typing_shooter.game_score()
    typing_shooter.game_speed()
    typing_shooter.destroy_enemy()
    typing_shooter.is_game_over()
    typing_shooter.game_over_screen()

    pg.display.update()
