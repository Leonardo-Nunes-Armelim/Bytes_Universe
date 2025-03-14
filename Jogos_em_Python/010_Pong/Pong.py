import pygame as pg
import math
import random

class Pong:
    def __init__(self, window_size):
        self.white = (255, 255, 255)
        self.black = (  0,   0,   0)

        self.window = pg.display.set_mode(window_size)

        pg.font.init()
        self.font = pg.font.SysFont("Courier New", 100, bold=True)

        self.clock = pg.time.Clock()

        self.player_1_pos = (self.window.get_height() - 300) / 2
        self.player_1_score = 0
        self.player_2_pos = (self.window.get_height() - 300) / 2
        self.player_2_score = 0

        self.ball_directions = [[4 * math.cos(math.radians(60)), 4 * math.sin(math.radians(60))],
                                [4 * math.cos(math.radians(45)), 4 * math.sin(math.radians(45))],
                                [4 * math.cos(math.radians(30)), 4 * math.sin(math.radians(30))],
                                [4 * math.cos(math.radians(-30)), 4 * math.sin(math.radians(-30))],
                                [4 * math.cos(math.radians(-45)), 4 * math.sin(math.radians(-45))],
                                [4 * math.cos(math.radians(-60)), 4 * math.sin(math.radians(-60))],
                                [-4 * math.cos(math.radians(60)), 4 * math.sin(math.radians(60))],
                                [-4 * math.cos(math.radians(45)), 4 * math.sin(math.radians(45))],
                                [-4 * math.cos(math.radians(30)), 4 * math.sin(math.radians(30))],
                                [-4 * math.cos(math.radians(-30)), 4 * math.sin(math.radians(-30))],
                                [-4 * math.cos(math.radians(-45)), 4 * math.sin(math.radians(-45))],
                                [-4 * math.cos(math.radians(-60)), 4 * math.sin(math.radians(-60))],
                                [0, 0]]
        self.ball_angle = 12
        self.ball_pos = [50, ((self.window.get_height() - 300) / 2) + 150]
        self.ball_direction = [0, 0]

    def clear_window(self):
        pg.draw.rect(self.window, self.black, (0, 0, self.window.get_width(), self.window.get_height()))

    def board(self):
        # Midle line
        pg.draw.line(self.window, self.white, (self.window.get_width() / 2, 0), (self.window.get_width() / 2, self.window.get_height()), 10)
        # Left player
        player_1_score_text = self.font.render(str(self.player_1_score), 1, self.white)
        blit_x = (self.window.get_width() / 2) - player_1_score_text.get_width() - 25
        self.window.blit(player_1_score_text, (blit_x, 25))
        # Right player
        player_2_score_text = self.font.render(str(self.player_2_score), 1, self.white)
        blit_x = (self.window.get_width() / 2) + 25
        self.window.blit(player_2_score_text, (blit_x, 25))
        # Player 1
        pg.draw.rect(self.window, self.white, (0, self.player_1_pos, 50, 300))
        # Player 2
        pg.draw.rect(self.window, self.white, (self.window.get_width() - 50, self.player_2_pos, 50, 300))
        # Ball
        pg.draw.rect(self.window, self.white, (self.ball_pos[0], self.ball_pos[1], 30, 30))

    def move(self, keys):
        key = None
        for i in range(1, len(keys)):
            if keys[i] == True:
                key = i

        if key == 119 and self.player_1_pos > 0:
            if self.ball_direction[0] == 0:
                self.ball_angle = random.randint(3, 5)
                self.ball_direction = self.ball_directions[self.ball_angle]
            self.player_1_pos -= 2
        elif key == 115 and self.player_1_pos < (self.window.get_height() - 300):
            if self.ball_direction[0] == 0:
                self.ball_angle = random.randint(0, 2)
                self.ball_direction = self.ball_directions[self.ball_angle]
            self.player_1_pos += 2

    def reset_game_variables(self):
        self.ball_angle = 12
        self.ball_direction = [0, 0]
        self.ball_pos = [50, ((self.window.get_height() - 300) / 2) + 150]
        self.player_1_pos = (self.window.get_height() - 300) / 2
        self.player_2_pos = (self.window.get_height() - 300) / 2

    def is_this_a_score(self):
        if self.ball_pos[0] <= 50:
            if self.ball_pos[1] + 30 < self.player_1_pos or self.ball_pos[1] > self.player_1_pos + 300:
                if self.ball_direction[0] != 0:
                    self.player_2_score += 1
                self.reset_game_variables()
        elif self.ball_pos[0] + 30 >= self.window.get_width() - 50:
            if self.ball_pos[1] + 30 < self.player_2_pos or self.ball_pos[1] > self.player_2_pos + 300:
                self.player_1_score += 1
                self.reset_game_variables()

    def ball_colliding_top_and_bottom(self):
        if self.ball_pos[1] <= 0:
            if self.ball_angle == 3:
                self.ball_angle = 2
            elif self.ball_angle == 4:
                self.ball_angle = 1
            elif self.ball_angle == 5:
                self.ball_angle = 0
            elif self.ball_angle == 9:
                self.ball_angle = 8
            elif self.ball_angle == 10:
                self.ball_angle = 7
            elif self.ball_angle == 11:
                self.ball_angle = 6
        elif self.ball_pos[1] + 30 >= self.window.get_height():
            if self.ball_angle == 2:
                self.ball_angle = 3
            elif self.ball_angle == 1:
                self.ball_angle = 4
            elif self.ball_angle == 0:
                self.ball_angle = 5
            elif self.ball_angle == 6:
                self.ball_angle = 11
            elif self.ball_angle == 7:
                self.ball_angle = 10
            elif self.ball_angle == 8:
                self.ball_angle = 9

    def ball_bouncing_off_a_player(self):
        if self.ball_pos[0] + 30 >= self.window.get_width() - 50:
            if self.ball_pos[1] + 30 >= self.player_2_pos or self.ball_pos[1] <= self.player_2_pos + 300:
                if self.ball_angle == 0:
                    self.ball_angle = 6
                elif self.ball_angle == 1:
                    self.ball_angle = 7
                elif self.ball_angle == 2:
                    self.ball_angle = 8
                elif self.ball_angle == 3:
                    self.ball_angle = 9
                elif self.ball_angle == 4:
                    self.ball_angle = 10
                elif self.ball_angle == 5:
                    self.ball_angle = 11
        elif self.ball_pos[0] <=  50:
            if self.ball_pos[1] + 30 >= self.player_1_pos or self.ball_pos[1] <= self.player_1_pos + 300:
                if self.ball_angle == 6:
                    self.ball_angle = 0
                elif self.ball_angle == 7:
                    self.ball_angle = 1
                elif self.ball_angle == 8:
                    self.ball_angle = 2
                elif self.ball_angle == 9:
                    self.ball_angle = 3
                elif self.ball_angle == 10:
                    self.ball_angle = 4
                elif self.ball_angle == 11:
                    self.ball_angle = 5

    def ball_movement(self):
        self.ball_colliding_top_and_bottom()

        self.ball_direction = self.ball_directions[self.ball_angle]
        self.ball_pos[0] += self.ball_direction[0]
        self.ball_pos[1] += self.ball_direction[1]

        self.ball_bouncing_off_a_player()

        self.is_this_a_score()

    def player_2_movement(self):
        if self.player_2_pos > self.ball_pos[1] + 30:
            self.player_2_pos -= 1
        elif self.player_2_pos + 300 < self.ball_pos[1]:
            self.player_2_pos += 1


pong = Pong((1280, 720))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            if pg.key.name(event.key) == 'escape':
                pg.quit()
                quit()

    # Game
    pong.clock.tick(60)
    pong.clear_window()
    pong.move(pg.key.get_pressed())
    pong.ball_movement()
    pong.board()
    pong.player_2_movement()

    pg.display.update()