import pygame as pg
import random


class FlapBirds:
    def __init__(self, window_size):
        self.white  = (255, 255, 255)
        self.black  = (  0,   0,   0)
        self.orange = (255, 165,   0)

        self.window = pg.display.set_mode(window_size)

        pg.font.init()
        self.font = pg.font.SysFont("Courier New", 50, bold=True)

        self.clock = pg.time.Clock()

        # Mouse variables
        self.last_click_status = (False, False, False)

        self.gravity = 5
        self.in_play = False

        self.bird_pos       = [100, 100]
        self.vertical_speed = 0
        self.score          = 0
        self.last_random_height_for_pipe = 0
        self.bird_passing_through_obstacle = False

        self.pipe_1_pos       = [ 400, self.new_height_for_pipe()]
        self.pipe_2_pos       = [ 800, self.new_height_for_pipe()]
        self.pipe_3_pos       = [1200, self.new_height_for_pipe()]
        self.pipe_4_pos       = [1600, self.new_height_for_pipe()]
        self.pipe_5_pos       = [2000, self.new_height_for_pipe()]
        self.background_1_pos = [   0,   0]
        self.background_2_pos = [2120,   0]
        self.ground_1_pos     = [   0, 634]
        self.ground_2_pos     = [1010, 634]
        self.ground_3_pos     = [2020, 634]

        background = pg.image.load('./Background.png')
        bird       = pg.image.load('./Bird.png')
        ground     = pg.image.load('./Ground.png')
        pipe       = pg.image.load('./Pipe.png')
        pipe_usd   = pg.image.load('./Pipe Up Side Down.png')
        self.background = pg.transform.scale(background, (2120, 634))
        self.bird       = pg.transform.scale(bird,       (  51,  36))
        self.ground     = pg.transform.scale(ground,     (1010,  86))
        self.pipe       = pg.transform.scale(pipe,       ( 123, 600))
        self.pipe_usd   = pg.transform.scale(pipe_usd,   ( 123, 600))

    def mouse_has_clicked(self, input):
            if self.last_click_status == input:
                return (False, False, False)
            else:
                left_button = False
                center_button = False
                right_button = False
                if self.last_click_status[0] == False and input[0] == True:
                    left_button = True
                if self.last_click_status[1] == False and input[1] == True:
                    center_button = True
                if self.last_click_status[2] == False and input[2] == True:
                    right_button = True

                return (left_button, center_button, right_button)

    def clear_window(self):
        pg.draw.rect(self.window, self.white, (0, 0, self.window.get_width(), self.window.get_height()))

    def board(self):
        # Background
        self.window.blit(self.background, (self.background_1_pos[0], self.background_1_pos[1]))
        self.window.blit(self.background, (self.background_2_pos[0], self.background_2_pos[1]))

        # Pipes
        self.window.blit(self.pipe,     (self.pipe_1_pos[0], self.pipe_1_pos[1]))
        self.window.blit(self.pipe_usd, (self.pipe_1_pos[0], self.pipe_1_pos[1] - 800))
        self.window.blit(self.pipe,     (self.pipe_2_pos[0], self.pipe_2_pos[1]))
        self.window.blit(self.pipe_usd, (self.pipe_2_pos[0], self.pipe_2_pos[1] - 800))
        self.window.blit(self.pipe,     (self.pipe_3_pos[0], self.pipe_3_pos[1]))
        self.window.blit(self.pipe_usd, (self.pipe_3_pos[0], self.pipe_3_pos[1] - 800))
        self.window.blit(self.pipe,     (self.pipe_4_pos[0], self.pipe_4_pos[1]))
        self.window.blit(self.pipe_usd, (self.pipe_4_pos[0], self.pipe_4_pos[1] - 800))
        self.window.blit(self.pipe,     (self.pipe_5_pos[0], self.pipe_5_pos[1]))
        self.window.blit(self.pipe_usd, (self.pipe_5_pos[0], self.pipe_5_pos[1] - 800))

        # Ground
        self.window.blit(self.ground, (self.ground_1_pos[0], self.ground_1_pos[1]))
        self.window.blit(self.ground, (self.ground_2_pos[0], self.ground_2_pos[1]))
        self.window.blit(self.ground, (self.ground_3_pos[0], self.ground_3_pos[1]))

        # Bird
        self.window.blit(self.bird, (self.bird_pos[0], self.bird_pos[1]))

    def move(self, key):
        if key == 'space':
            self.vertical_speed = -10
        elif key == 'r':
            self.restart()

    def new_height_for_pipe(self):
        new_height = random.randint(6, 10) * 50
        while self.last_random_height_for_pipe == new_height:
            new_height = random.randint(6, 10) * 50

        self.last_random_height_for_pipe = new_height

        return new_height

    def movement(self):
        if self.in_play:
            # Pipes
            self.pipe_1_pos[0] -= 1.2
            self.pipe_2_pos[0] -= 1.2
            self.pipe_3_pos[0] -= 1.2
            self.pipe_4_pos[0] -= 1.2
            self.pipe_5_pos[0] -= 1.2
            if self.pipe_1_pos[0] <= -123:
                self.pipe_1_pos[0] = self.pipe_2_pos[0]
                self.pipe_1_pos[1] = self.pipe_2_pos[1]
                self.pipe_2_pos[0] = self.pipe_3_pos[0]
                self.pipe_2_pos[1] = self.pipe_3_pos[1]
                self.pipe_3_pos[0] = self.pipe_4_pos[0]
                self.pipe_3_pos[1] = self.pipe_4_pos[1]
                self.pipe_4_pos[0] = self.pipe_5_pos[0]
                self.pipe_4_pos[1] = self.pipe_5_pos[1]
                self.pipe_5_pos[0] = 1877
                self.pipe_5_pos[1] = self.new_height_for_pipe()

            # Background
            self.background_1_pos[0] -= 1.2
            self.background_2_pos[0] -= 1.2
            if self.background_1_pos[0] <= -2120:
                self.background_1_pos[0] = 0
                self.background_2_pos[0] = 2120

            # Ground
            self.ground_1_pos[0]     -= 1.2
            self.ground_2_pos[0]     -= 1.2
            self.ground_3_pos[0]     -= 1.2
            if self.ground_1_pos[0] <= -1010:
                self.ground_1_pos[0] = 0
                self.ground_2_pos[0] = 1010
                self.ground_3_pos[0] = 2020

            # Bird
            if self.vertical_speed <= 5:
                self.vertical_speed += self.gravity / 15
            self.bird_pos[1] += self.vertical_speed

    def scoreboard(self):
        if self.pipe_1_pos[0] < self.bird_pos[0] + 51 and self.pipe_1_pos[0] + 123 > self.bird_pos[0]:
            self.bird_passing_through_obstacle = True
        else:
            if self.bird_passing_through_obstacle:
                self.score += 1
            self.bird_passing_through_obstacle = False

        border = 5
        x = 1100
        y = 50
        height = 100
        width = 150

        text = self.font.render(str(self.score), 1, self.white)
        text_x = (x + (width / 2)) - (text.get_width() / 2)
        text_y = (y + (height / 2)) - (text.get_height() / 2)

        pg.draw.rect(self.window, self.orange, (x, y, width, height))
        pg.draw.rect(self.window, self.black, (x, y, width, height), border)
        pg.draw.rect(self.window, self.white, (x + border, y + border, width - (border * 2), height - (border * 2)), border)
        self.window.blit(text, (text_x, text_y))

    def collision(self):
        if self.pipe_1_pos[0] < self.bird_pos[0] + 51 and self.pipe_1_pos[0] + 123 > self.bird_pos[0]:
            if self.bird_pos[1] + 36 > self.pipe_1_pos[1] or self.bird_pos[1] < self.pipe_1_pos[1] - 200:
                self.in_play = False

        if self.bird_pos[1] + 36 > 634:
            self.in_play = False

    def restart_button(self, mouse):
        if self.in_play == False:
            text = self.font.render('Restart', 1, self.white)
            text_x = (self.window.get_width() / 2) - (text.get_width() / 2)
            text_y = (self.window.get_height() / 2) - (text.get_height() / 2)

            border = 5
            height = text.get_height() + 50
            width = text.get_width() + 50
            x = (self.window.get_width() / 2) - (width / 2)
            y = (self.window.get_height() / 2) - (height / 2)

            if mouse[0][0] >= x and mouse[0][0] <= x + width and mouse[0][1] >= y and mouse[0][1] <= y + height:
                hover_color = tuple(min(rgb + 50, 255) for rgb in self.orange)
                pg.draw.rect(self.window, hover_color, (x, y, width, height))
                if mouse[2][0]:
                    self.restart()
            else:
                pg.draw.rect(self.window, self.orange, (x, y, width, height))
            pg.draw.rect(self.window, self.black, (x, y, width, height), border)
            pg.draw.rect(self.window, self.white, (x + border, y + border, width - (border * 2), height - (border * 2)), border)

            self.window.blit(text, (text_x, text_y))

    def restart(self):
        self.bird_pos       = [100, 100]
        self.vertical_speed = 0
        self.score          = 0
        self.last_random_height_for_pipe = 0
        self.bird_passing_through_obstacle = False

        self.pipe_1_pos       = [ 400, self.new_height_for_pipe()]
        self.pipe_2_pos       = [ 800, self.new_height_for_pipe()]
        self.pipe_3_pos       = [1200, self.new_height_for_pipe()]
        self.pipe_4_pos       = [1600, self.new_height_for_pipe()]
        self.pipe_5_pos       = [2000, self.new_height_for_pipe()]
        self.background_1_pos = [   0,   0]
        self.background_2_pos = [2120,   0]
        self.ground_1_pos     = [   0, 634]
        self.ground_2_pos     = [1010, 634]
        self.ground_3_pos     = [2020, 634]
        self.in_play = True


jogo = FlapBirds((1280, 720))


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            jogo.move(pg.key.name(event.key))
            if pg.key.name(event.key) == 'escape':
                pg.quit()
                quit()

    # Mouse info
    mouse_position  = pg.mouse.get_pos()
    mouse_input = pg.mouse.get_pressed()
    mouse_click = jogo.mouse_has_clicked(mouse_input)
    mouse = (mouse_position, mouse_input, mouse_click)

    # Game
    jogo.clock.tick(60)
    jogo.clear_window()
    jogo.board()
    jogo.movement()
    jogo.scoreboard()
    jogo.collision()
    jogo.restart_button(mouse)

    jogo.last_click_status = mouse_input

    pg.display.update()
