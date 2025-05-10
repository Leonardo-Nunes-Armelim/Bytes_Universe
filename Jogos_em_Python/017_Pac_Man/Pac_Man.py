import pygame as pg
import random


class PacMan:
    def __init__(self, scale):
        self.white = (255, 255, 255)
        self.black = (  0,   0,   0)
        self.blue  = ( 25,  25, 255)

        self.window = pg.display.set_mode((scale * 27.5, scale * 35))

        pg.font.init()
        self.font = pg.font.SysFont("Courier New", scale * 2, bold=True)

        self.clock = pg.time.Clock()

        self.scale = scale
        self.sprite_frame = 0
        self.sprite_speed = 2

        self.score = 0
        self.lives = 5
        self.end_game = False
        self.harmless_mode = False
        self.harmless_mode_timer = 0
        self.harmless_mode_ghost_blue   = False
        self.harmless_mode_ghost_orange = False
        self.harmless_mode_ghost_pink   = False
        self.harmless_mode_ghost_red    = False

        self.pac_man_pos            = [self.scale * 13.1, self.scale * 22.6]
        self.pac_man_direction      = [self.scale/16, 0]
        self.pac_man_next_direction = [self.scale/16, 0]

        self.ghost_blue_pos   = [self.scale * 12, self.scale * 13]
        self.ghost_orange_pos = [self.scale * 12, self.scale * 14.5]
        self.ghost_pink_pos   = [self.scale * 14, self.scale * 13]
        self.ghost_red_pos    = [self.scale * 14, self.scale * 14.5]
        self.ghost_blue_direction   = [0, 0]
        self.ghost_orange_direction = [0, 0]
        self.ghost_pink_direction   = [0, 0]
        self.ghost_red_direction    = [0, 0]
        self.ghost_blue_next_direction   = [0, 0]
        self.ghost_orange_next_direction = [0, 0]
        self.ghost_pink_next_direction   = [0, 0]
        self.ghost_red_next_direction    = [0, 0]
        self.distance_ghost_blue_to_pac_man   = self.distance_ghost_to_pac_man(self.ghost_blue_pos)
        self.distance_ghost_orange_to_pac_man = self.distance_ghost_to_pac_man(self.ghost_orange_pos)
        self.distance_ghost_pink_to_pac_man   = self.distance_ghost_to_pac_man(self.ghost_pink_pos)
        self.distance_ghost_red_to_pac_man    = self.distance_ghost_to_pac_man(self.ghost_red_pos)

        # Pac-Man
        pac_man_1 = pg.image.load('./img/Pac_Man_1.png')
        pac_man_2 = pg.image.load('./img/Pac_Man_2.png')
        pac_man_3 = pg.image.load('./img/Pac_Man_3.png')
        pac_man_4 = pg.image.load('./img/Pac_Man_4.png')
        pac_man_5 = pg.image.load('./img/Pac_Man_5.png')
        pac_man_6 = pg.image.load('./img/Pac_Man_6.png')
        pac_man_7 = pg.image.load('./img/Pac_Man_7.png')
        pac_man_8 = pg.image.load('./img/Pac_Man_8.png')
        pac_man_9 = pg.image.load('./img/Pac_Man_9.png')
        pac_man_10 = pg.image.load('./img/Pac_Man_10.png')
        pac_man_11 = pg.image.load('./img/Pac_Man_11.png')
        pac_man_12 = pg.image.load('./img/Pac_Man_12.png')
        pac_man_13 = pg.image.load('./img/Pac_Man_13.png')
        pac_man_14 = pg.image.load('./img/Pac_Man_14.png')
        pac_man_15 = pg.image.load('./img/Pac_Man_15.png')
        pac_man_16 = pg.image.load('./img/Pac_Man_16.png')
        pac_man_17 = pg.image.load('./img/Pac_Man_17.png')
        self.pac_man_1 = pg.transform.scale(pac_man_1, (self.scale * 1.3, self.scale * 1.3))
        self.pac_man_2 = pg.transform.scale(pac_man_2, (self.scale * 1.3, self.scale * 1.3))
        self.pac_man_3 = pg.transform.scale(pac_man_3, (self.scale * 1.3, self.scale * 1.3))
        self.pac_man_4 = pg.transform.scale(pac_man_4, (self.scale * 1.3, self.scale * 1.3))
        self.pac_man_5 = pg.transform.scale(pac_man_5, (self.scale * 1.3, self.scale * 1.3))
        self.pac_man_6 = pg.transform.scale(pac_man_6, (self.scale * 1.3, self.scale * 1.3))
        self.pac_man_7 = pg.transform.scale(pac_man_7, (self.scale * 1.3, self.scale * 1.3))
        self.pac_man_8 = pg.transform.scale(pac_man_8, (self.scale * 1.3, self.scale * 1.3))
        self.pac_man_9 = pg.transform.scale(pac_man_9, (self.scale * 1.3, self.scale * 1.3))
        self.pac_man_10 = pg.transform.scale(pac_man_10, (self.scale * 1.3, self.scale * 1.3))
        self.pac_man_11 = pg.transform.scale(pac_man_11, (self.scale * 1.3, self.scale * 1.3))
        self.pac_man_12 = pg.transform.scale(pac_man_12, (self.scale * 1.3, self.scale * 1.3))
        self.pac_man_13 = pg.transform.scale(pac_man_13, (self.scale * 1.3, self.scale * 1.3))
        self.pac_man_14 = pg.transform.scale(pac_man_14, (self.scale * 1.3, self.scale * 1.3))
        self.pac_man_15 = pg.transform.scale(pac_man_15, (self.scale * 1.3, self.scale * 1.3))
        self.pac_man_16 = pg.transform.scale(pac_man_16, (self.scale * 1.3, self.scale * 1.3))
        self.pac_man_17 = pg.transform.scale(pac_man_17, (self.scale * 1.3, self.scale * 1.3))

        # Blue Ghost
        ghost_blue_down_right_0 = pg.image.load('./img/Blue_Ghost_Down_Right_0.png')
        ghost_blue_down_right_1 = pg.image.load('./img/Blue_Ghost_Down_Right_1.png')
        self.ghost_blue_down_right_0 = pg.transform.scale(ghost_blue_down_right_0, (self.scale * 1.3, self.scale * 1.3))
        self.ghost_blue_down_right_1 = pg.transform.scale(ghost_blue_down_right_1, (self.scale * 1.3, self.scale * 1.3))

        # Orange Ghost
        ghost_orange_down_right_0 = pg.image.load('./img/Orange_Ghost_Down_Right_0.png')
        ghost_orange_down_right_1 = pg.image.load('./img/Orange_Ghost_Down_Right_1.png')
        self.ghost_orange_down_right_0 = pg.transform.scale(ghost_orange_down_right_0, (self.scale * 1.3, self.scale * 1.3))
        self.ghost_orange_down_right_1 = pg.transform.scale(ghost_orange_down_right_1, (self.scale * 1.3, self.scale * 1.3))

        # Pink Ghost
        ghost_pink_down_right_0 = pg.image.load('./img/Pink_Ghost_Down_Right_0.png')
        ghost_pink_down_right_1 = pg.image.load('./img/Pink_Ghost_Down_Right_1.png')
        self.ghost_pink_down_right_0 = pg.transform.scale(ghost_pink_down_right_0, (self.scale * 1.3, self.scale * 1.3))
        self.ghost_pink_down_right_1 = pg.transform.scale(ghost_pink_down_right_1, (self.scale * 1.3, self.scale * 1.3))

        # Red Ghost
        ghost_red_down_right_0 = pg.image.load('./img/Red_Ghost_Down_Right_0.png')
        ghost_red_down_right_1 = pg.image.load('./img/Red_Ghost_Down_Right_1.png')
        self.ghost_red_down_right_0 = pg.transform.scale(ghost_red_down_right_0, (self.scale * 1.3, self.scale * 1.3))
        self.ghost_red_down_right_1 = pg.transform.scale(ghost_red_down_right_1, (self.scale * 1.3, self.scale * 1.3))

        # Harmless Ghost
        ghost_harmless_0       = pg.image.load('./img/Harmless_Ghost_0.png')
        ghost_harmless_1       = pg.image.load('./img/Harmless_Ghost_1.png')
        self.ghost_harmless_0 = pg.transform.scale(ghost_harmless_0, (self.scale * 1.3, self.scale * 1.3))
        self.ghost_harmless_1 = pg.transform.scale(ghost_harmless_1, (self.scale * 1.3, self.scale * 1.3))

        self.map = [['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
                    ['#','.','.','.','.','.','.','.','.','.','.','.','.','#','#','.','.','.','.','.','.','.','.','.','.','.','.','#'],
                    ['#','.','#','#','#','#','.','#','#','#','#','#','.','#','#','.','#','#','#','#','#','.','#','#','#','#','.','#'],
                    ['#','o','#','#','#','#','.','#','#','#','#','#','.','#','#','.','#','#','#','#','#','.','#','#','#','#','o','#'],
                    ['#','.','#','#','#','#','.','#','#','#','#','#','.','#','#','.','#','#','#','#','#','.','#','#','#','#','.','#'],
                    ['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'],
                    ['#','.','#','#','#','#','.','#','#','.','#','#','#','#','#','#','#','#','.','#','#','.','#','#','#','#','.','#'],
                    ['#','.','#','#','#','#','.','#','#','.','#','#','#','#','#','#','#','#','.','#','#','.','#','#','#','#','.','#'],
                    ['#','.','.','.','.','.','.','#','#','.','.','.','.','#','#','.','.','.','.','#','#','.','.','.','.','.','.','#'],
                    ['#','#','#','#','#','#','.','#','#','#','#','#',' ','#','#',' ','#','#','#','#','#','.','#','#','#','#','#','#'],
                    [' ',' ',' ',' ',' ','#','.','#','#','#','#','#',' ','#','#',' ','#','#','#','#','#','.','#',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ','#','.','#','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#','#','.','#',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ','#','.','#','#',' ','#','#','#','-','-','#','#','#',' ','#','#','.','#',' ',' ',' ',' ',' '],
                    ['#','#','#','#','#','#','.','#','#',' ','#',' ',' ',' ',' ',' ',' ','#',' ','#','#','.','#','#','#','#','#','#'],
                    [' ',' ',' ',' ',' ',' ','.',' ',' ',' ','#',' ',' ',' ',' ',' ',' ','#',' ',' ',' ','.',' ',' ',' ',' ',' ',' '],
                    ['#','#','#','#','#','#','.','#','#',' ','#',' ',' ',' ',' ',' ',' ','#',' ','#','#','.','#','#','#','#','#','#'],
                    [' ',' ',' ',' ',' ','#','.','#','#',' ','#','#','#','#','#','#','#','#',' ','#','#','.','#',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ','#','.','#','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#','#','.','#',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ','#','.','#','#',' ','#','#','#','#','#','#','#','#',' ','#','#','.','#',' ',' ',' ',' ',' '],
                    ['#','#','#','#','#','#','.','#','#',' ','#','#','#','#','#','#','#','#',' ','#','#','.','#','#','#','#','#','#'],
                    ['#','.','.','.','.','.','.','.','.','.','.','.','.','#','#','.','.','.','.','.','.','.','.','.','.','.','.','#'],
                    ['#','.','#','#','#','#','.','#','#','#','#','#','.','#','#','.','#','#','#','#','#','.','#','#','#','#','.','#'],
                    ['#','.','#','#','#','#','.','#','#','#','#','#','.','#','#','.','#','#','#','#','#','.','#','#','#','#','.','#'],
                    ['#','o','.','.','#','#','.','.','.','.','.','.','.',' ',' ','.','.','.','.','.','.','.','#','#','.','.','o','#'],
                    ['#','#','#','.','#','#','.','#','#','.','#','#','#','#','#','#','#','#','.','#','#','.','#','#','.','#','#','#'],
                    ['#','#','#','.','#','#','.','#','#','.','#','#','#','#','#','#','#','#','.','#','#','.','#','#','.','#','#','#'],
                    ['#','.','.','.','.','.','.','#','#','.','.','.','.','#','#','.','.','.','.','#','#','.','.','.','.','.','.','#'],
                    ['#','.','#','#','#','#','#','#','#','#','#','#','.','#','#','.','#','#','#','#','#','#','#','#','#','#','.','#'],
                    ['#','.','#','#','#','#','#','#','#','#','#','#','.','#','#','.','#','#','#','#','#','#','#','#','#','#','.','#'],
                    ['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'],
                    ['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']]

    def clear_window(self):
        pg.draw.rect(self.window, self.black, (0, 0, self.window.get_width(), self.window.get_height()))

    def move(self, key):
        if key == 'r':
            self.restart()
        if key == 'w' or key == 'up':
            if self.pac_man_direction[0] == 0 and self.pac_man_direction[1] > 0:
                self.pac_man_direction[0] = 0
                self.pac_man_direction[1] = -self.scale/16
                self.pac_man_next_direction[0] = 0
                self.pac_man_next_direction[1] = -self.scale/16
            elif self.pac_man_direction[0] != 0 and self.pac_man_direction[1] == 0:
                self.pac_man_next_direction[0] = 0
                self.pac_man_next_direction[1] = -self.scale/16
        elif key == 'a' or key == 'left':
            if self.pac_man_direction[0] > 0 and self.pac_man_direction[1] == 0:
                self.pac_man_direction[0] = -self.scale/16
                self.pac_man_direction[1] = 0
                self.pac_man_next_direction[0] = -self.scale/16
                self.pac_man_next_direction[1] = 0
            elif self.pac_man_direction[0] == 0 and self.pac_man_direction[1] != 0:
                self.pac_man_next_direction[0] = -self.scale/16
                self.pac_man_next_direction[1] = 0
        elif key == 's' or key == 'down':
            if self.pac_man_direction[0] == 0 and self.pac_man_direction[1] < 0:
                self.pac_man_direction[0] = 0
                self.pac_man_direction[1] = self.scale/16
                self.pac_man_next_direction[0] = 0
                self.pac_man_next_direction[1] = self.scale/16
            elif self.pac_man_direction[0] != 0 and self.pac_man_direction[1] == 0:
                self.pac_man_next_direction[0] = 0
                self.pac_man_next_direction[1] = self.scale/16
        elif key == 'd' or key == 'right':
            if self.pac_man_direction[0] < 0 and self.pac_man_direction[1] == 0:
                self.pac_man_direction[0] = self.scale/16
                self.pac_man_direction[1] = 0
                self.pac_man_next_direction[0] = self.scale/16
                self.pac_man_next_direction[1] = 0
            elif self.pac_man_direction[0] == 0 and self.pac_man_direction[1] != 0:
                self.pac_man_next_direction[0] = self.scale/16
                self.pac_man_next_direction[1] = 0

    def board(self):
        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                if self.map[y][x] == '#':
                    pg.draw.rect(self.window, self.blue, (x * self.scale, y * self.scale, self.scale, self.scale))
                if self.map[y][x] == '-':
                    pg.draw.rect(self.window, self.white, (x * self.scale, y * self.scale, self.scale, self.scale))
                if self.map[y][x] == ' ' or self.map[y][x] == '.' or self.map[y][x] == 'o':
                    pg.draw.rect(self.window, self.black, ((x * self.scale) - (self.scale / 2), (y * self.scale) - (self.scale / 2), self.scale * 1.5, self.scale * 1.5))
        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                if self.map[y][x] == '.':
                    pg.draw.circle(self.window, self.white, ((x * self.scale) + (self.scale / 4), (y * self.scale) + (self.scale / 4)), self.scale / 5)
                if self.map[y][x] == 'o':
                    pg.draw.circle(self.window, self.white, ((x * self.scale) + (self.scale / 4), (y * self.scale) + (self.scale / 4)), self.scale / 2)

    def animation_step(self):
        if self.sprite_frame == 60:
            self.sprite_frame = 0
        else:
            self.sprite_frame += self.sprite_speed

    def player_rotation(self, image):
        x_dir = self.pac_man_direction[0]
        y_dir = self.pac_man_direction[1]
        if x_dir > 0 and y_dir == 0:
            return image
        elif x_dir == 0 and y_dir > 0:
            return pg.transform.rotate(image, -90)
        elif x_dir < 0 and y_dir == 0:
            return pg.transform.flip(image, True, False)
        elif x_dir == 0 and y_dir < 0:
            return pg.transform.rotate(image, 90)

    def collider(self, position, direction):
        if self.end_game == False:
            position[0] += direction[0]
            position[1] += direction[1]
            for y in range(len(self.map)):
                for x in range(len(self.map[0])):
                    if self.map[y][x] == '#' or self.map[y][x] == '-':
                        x_wall = (x * self.scale) - (self.scale * 0.65)
                        y_wall = (y * self.scale) - (self.scale * 0.65)
                        wall_size = self.scale * 1.85
                        x_agent = position[0] + (self.scale * 0.65)
                        y_agent = position[1] + (self.scale * 0.65)

                        if x_agent >= x_wall and x_agent <= x_wall + wall_size and y_agent >= y_wall and y_agent <= y_wall + wall_size:
                            position[0] -= direction[0]
                            position[1] -= direction[1]

        return position

    def turning_corner(self, position, direction, next_direction):
        turned_corner = True
        position[0] += next_direction[0] * 16
        position[1] += next_direction[1] * 16
        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                if self.map[y][x] == '#' or self.map[y][x] == '-':
                    x_wall = (x * self.scale) - (self.scale * 0.65)
                    y_wall = (y * self.scale) - (self.scale * 0.65)
                    wall_size = self.scale * 1.85
                    x_agent = position[0] + (self.scale * 0.65)
                    y_agent = position[1] + (self.scale * 0.65)
                    if x_agent >= x_wall and x_agent <= x_wall + wall_size and y_agent >= y_wall and y_agent <= y_wall + wall_size:
                        turned_corner = False
        position[0] -= next_direction[0] * 16
        position[1] -= next_direction[1] * 16
        if turned_corner:
            direction[0] = next_direction[0]
            direction[1] = next_direction[1]

        return direction, next_direction

    def collect_dots(self):
        x_pac_man = self.pac_man_pos[0] + (self.scale * 0.65)
        y_pac_man = self.pac_man_pos[1] + (self.scale * 0.65)
        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                if self.map[y][x] == '.':
                    x_dot = (x * self.scale) + (self.scale / 4)
                    y_dot = (y * self.scale) + (self.scale / 4)
                    radius = self.scale / 5
                    if x_pac_man >= x_dot - radius and x_pac_man <= x_dot + radius and y_pac_man >= y_dot - radius and y_pac_man <= y_dot + radius:
                        self.map[y][x] = ' '
                        self.score += 1
                if self.map[y][x] == 'o':
                    x_dot = (x * self.scale) + (self.scale / 4)
                    y_dot = (y * self.scale) + (self.scale / 4)
                    radius = self.scale / 2
                    if x_pac_man >= x_dot - radius and x_pac_man <= x_dot + radius and y_pac_man >= y_dot - radius and y_pac_man <= y_dot + radius:
                        self.map[y][x] = ' '
                        self.score += 5
                        self.harmless_mode = True
                        self.harmless_mode_ghost_blue   = True
                        self.harmless_mode_ghost_orange = True
                        self.harmless_mode_ghost_pink   = True
                        self.harmless_mode_ghost_red    = True

    def pacman_tunnel(self, position):
        x_pos = position[0]
        y_pos = position[1]
        if position[0] >= self.scale * 27.5:
            x_pos = 0 - (self.scale * 1.3)
        elif position[0] <= -(self.scale * 1.3):
            x_pos = self.scale * 27.5
        return [x_pos, y_pos]

    def player(self):
        self.pac_man_direction, self.pac_man_next_direction = self.turning_corner(self.pac_man_pos, self.pac_man_direction, self.pac_man_next_direction)
        self.pac_man_pos = self.collider(self.pac_man_pos, self.pac_man_direction)
        self.pac_man_pos = self.pacman_tunnel(self.pac_man_pos)
        x = self.pac_man_pos[0]
        y = self.pac_man_pos[1]

        if self.end_game:
            if self.sprite_frame <= 5:
                self.window.blit(self.player_rotation(self.pac_man_6), (x, y))
            elif self.sprite_frame <= 10:
                self.window.blit(self.player_rotation(self.pac_man_7), (x, y))
            elif self.sprite_frame <= 15:
                self.window.blit(self.player_rotation(self.pac_man_8), (x, y))
            elif self.sprite_frame <= 20:
                self.window.blit(self.player_rotation(self.pac_man_9), (x, y))
            elif self.sprite_frame <= 25:
                self.window.blit(self.player_rotation(self.pac_man_10), (x, y))
            elif self.sprite_frame <= 30:
                self.window.blit(self.player_rotation(self.pac_man_11), (x, y))
            elif self.sprite_frame <= 35:
                self.window.blit(self.player_rotation(self.pac_man_12), (x, y))
            elif self.sprite_frame <= 40:
                self.window.blit(self.player_rotation(self.pac_man_13), (x, y))
            elif self.sprite_frame <= 45:
                self.window.blit(self.player_rotation(self.pac_man_14), (x, y))
            elif self.sprite_frame <= 50:
                self.window.blit(self.player_rotation(self.pac_man_15), (x, y))
            elif self.sprite_frame <= 55:
                self.window.blit(self.player_rotation(self.pac_man_16), (x, y))
            elif self.sprite_frame <= 60:
                self.window.blit(self.player_rotation(self.pac_man_17), (x, y))
        else:
            if self.sprite_frame <= 6:
                self.window.blit(self.player_rotation(self.pac_man_1), (x, y))
            elif self.sprite_frame <= 12:
                self.window.blit(self.player_rotation(self.pac_man_1), (x, y))
            elif self.sprite_frame <= 18:
                self.window.blit(self.player_rotation(self.pac_man_2), (x, y))
            elif self.sprite_frame <= 24:
                self.window.blit(self.player_rotation(self.pac_man_3), (x, y))
            elif self.sprite_frame <= 30:
                self.window.blit(self.player_rotation(self.pac_man_4), (x, y))
            elif self.sprite_frame <= 36:
                self.window.blit(self.player_rotation(self.pac_man_5), (x, y))
            elif self.sprite_frame <= 42:
                self.window.blit(self.player_rotation(self.pac_man_4), (x, y))
            elif self.sprite_frame <= 48:
                self.window.blit(self.player_rotation(self.pac_man_3), (x, y))
            elif self.sprite_frame <= 54:
                self.window.blit(self.player_rotation(self.pac_man_2), (x, y))
            elif self.sprite_frame <= 60:
                self.window.blit(self.player_rotation(self.pac_man_1), (x, y))

    def ghost_render(self, color, position):
        x = position[0]
        y = position[1]
        if color == 'blue':
            if self.sprite_frame <= 15:
                self.window.blit(self.ghost_blue_down_right_0, (x, y))
            elif self.sprite_frame <= 30:
                self.window.blit(self.ghost_blue_down_right_1, (x, y))
            elif self.sprite_frame <= 45:
                self.window.blit(self.ghost_blue_down_right_0, (x, y))
            elif self.sprite_frame <= 60:
                self.window.blit(self.ghost_blue_down_right_1, (x, y))
        elif color == 'orange':
            if self.sprite_frame <= 15:
                self.window.blit(self.ghost_orange_down_right_0, (x, y))
            elif self.sprite_frame <= 30:
                self.window.blit(self.ghost_orange_down_right_1, (x, y))
            elif self.sprite_frame <= 45:
                self.window.blit(self.ghost_orange_down_right_0, (x, y))
            elif self.sprite_frame <= 60:
                self.window.blit(self.ghost_orange_down_right_1, (x, y))
        elif color == 'pink':
            if self.sprite_frame <= 15:
                self.window.blit(self.ghost_pink_down_right_0, (x, y))
            elif self.sprite_frame <= 30:
                self.window.blit(self.ghost_pink_down_right_1, (x, y))
            elif self.sprite_frame <= 45:
                self.window.blit(self.ghost_pink_down_right_0, (x, y))
            elif self.sprite_frame <= 60:
                self.window.blit(self.ghost_pink_down_right_1, (x, y))
        elif color == 'red':
            if self.sprite_frame <= 15:
                self.window.blit(self.ghost_red_down_right_0, (x, y))
            elif self.sprite_frame <= 30:
                self.window.blit(self.ghost_red_down_right_1, (x, y))
            elif self.sprite_frame <= 45:
                self.window.blit(self.ghost_red_down_right_0, (x, y))
            elif self.sprite_frame <= 60:
                self.window.blit(self.ghost_red_down_right_1, (x, y))
        elif color == 'harmless':
            if self.sprite_frame <= 15:
                self.window.blit(self.ghost_harmless_0, (x, y))
            elif self.sprite_frame <= 30:
                self.window.blit(self.ghost_harmless_1, (x, y))
            elif self.sprite_frame <= 45:
                self.window.blit(self.ghost_harmless_0, (x, y))
            elif self.sprite_frame <= 60:
                self.window.blit(self.ghost_harmless_1, (x, y))

    def random_direction_for_ghost(self):
        move_up_or_sideways = random.randint(0, 1)
        x_direction = random.randint(0, 1)
        y_direction = random.randint(0, 1)
        direction = []
        if move_up_or_sideways == 0:
            if x_direction == 0:
                direction = [-self.scale/16, 0]
            else:
                direction = [self.scale/16, 0]
        else:
            if y_direction == 0:
                direction = [0, -self.scale/16]
            else:
                direction = [0, self.scale/16]

        return direction

    def random_next_direction_for_ghost(self, direction):
        new_direction = [0, 0]
        if direction[0] != 0:
            if random.randint(0, 1) == 0:
                new_direction[1] = -self.scale/16
            else:
                new_direction[1] = self.scale/16
        elif direction[1] != 0:
            if random.randint(0, 1) == 0:
                new_direction[0] = -self.scale/16
            else:
                new_direction[0] = self.scale/16

        return new_direction

    def distance_ghost_to_pac_man(self, ghost_pos):
        ghost_x = ghost_pos[0] + (self.scale * 0.65)
        ghost_y = ghost_pos[1] + (self.scale * 0.65)
        pac_man_x = self.pac_man_pos[0] + (self.scale * 0.65)
        pac_man_y = self.pac_man_pos[1] + (self.scale * 0.65)
        delta_x = (ghost_x - pac_man_x) ** 2
        delta_y = (ghost_y - pac_man_y) ** 2
        distance = (delta_x + delta_y) ** (1 / 2)

        return distance

    def direction_ghost_to_pac_man(self, position, direction):
        new_direction = [0, 0]
        ghost_x = position[0]
        ghost_y = position[1]
        pac_man_x = self.pac_man_pos[0]
        pac_man_y = self.pac_man_pos[1]
        delta_x = ghost_x - pac_man_x
        delta_y = ghost_y - pac_man_y
        if direction[1] != 0:
            if delta_x <= 0:
                new_direction[0] = self.scale/16
            else:
                new_direction[0] = -self.scale/16
        if direction[0] != 0:
            if delta_y <= 0:
                new_direction[1] = self.scale/16
            else:
                new_direction[1] = -self.scale/16

        return new_direction

    def direction_harmless_ghost_to_pac_man(self, position, direction):
        new_direction = [0, 0]
        ghost_x = position[0]
        ghost_y = position[1]
        pac_man_x = self.pac_man_pos[0]
        pac_man_y = self.pac_man_pos[1]
        delta_x = ghost_x - pac_man_x
        delta_y = ghost_y - pac_man_y
        if direction[1] != 0:
            if delta_x <= 0:
                new_direction[0] = -self.scale/16
            else:
                new_direction[0] = self.scale/16
        if direction[0] != 0:
            if delta_y <= 0:
                new_direction[1] = -self.scale/16
            else:
                new_direction[1] = self.scale/16

        return new_direction

    def new_random_direction_for_ghost(self, position, direction):
        new_direction = [0, 0]
        pos = [0, 0]
        pos[0] = position[0]
        pos[1] = position[1]

        if direction[0] != 0:
            if random.randint(0, 1) == 0:
                new_direction[1] = -self.scale/8
            else:
                new_direction[1] = self.scale/8
        elif direction[1] != 0:
            if random.randint(0, 1) == 0:
                new_direction[0] = -self.scale/8
            else:
                new_direction[0] = self.scale/8

        new_position = self.collider(pos, new_direction)

        if position == new_position:
            new_direction[0] *= -1
            new_direction[1] *= -1
            new_position = self.collider(pos, new_direction)

        new_direction[0] /= 2
        new_direction[1] /= 2

        return new_position, new_direction

    def ghost_intelligence(self, ghost_pos, ghost_direction, ghost_next_direction, distance_ghost_to_pac_man, harmless_ghost_mode):
        ghost_blue_pos = [0, 0]
        ghost_blue_pos[0] = ghost_pos[0]
        ghost_blue_pos[1] = ghost_pos[1]
        distance_ghost_to_pac_man = self.distance_ghost_to_pac_man(ghost_pos)
        if distance_ghost_to_pac_man <= self.scale * 10:
            if harmless_ghost_mode:
                ghost_next_direction = self.direction_harmless_ghost_to_pac_man(ghost_pos, ghost_direction)
            else:
                ghost_next_direction = self.direction_ghost_to_pac_man(ghost_pos, ghost_direction)
            ghost_direction, ghost_next_direction = self.turning_corner(ghost_pos, ghost_direction, ghost_next_direction)
        if ghost_direction == ghost_next_direction:
            if harmless_ghost_mode:
                ghost_next_direction = self.direction_harmless_ghost_to_pac_man(ghost_pos, ghost_direction)
            else:
                ghost_next_direction = self.direction_ghost_to_pac_man(ghost_pos, ghost_direction)
            ghost_pos = self.collider(ghost_pos, ghost_direction)
        ghost_pos = self.pacman_tunnel(ghost_pos)
        ghost_pos = self.collider(ghost_pos, ghost_direction)
        if ghost_blue_pos == ghost_pos:
            ghost_pos, ghost_direction = self.new_random_direction_for_ghost(ghost_pos, ghost_direction)
        return ghost_pos, ghost_direction, ghost_next_direction, distance_ghost_to_pac_man

    def ghost(self):
        if self.ghost_blue_pos != [self.scale * 12, self.scale * 13]:
            input_1 = self.ghost_blue_pos
            input_2 = self.ghost_blue_direction
            input_3 = self.ghost_blue_next_direction
            input_4 = self.distance_ghost_blue_to_pac_man
            input_5 = self.harmless_mode_ghost_blue
            output_1, output_2, output_3, output_4 = self.ghost_intelligence(input_1, input_2, input_3, input_4, input_5)
            self.ghost_blue_pos = output_1
            self.ghost_blue_direction = output_2
            self.ghost_blue_next_direction = output_3
            self.distance_ghost_blue_to_pac_man = output_4
        if self.ghost_orange_pos != [self.scale * 12, self.scale * 14.5]:
            input_1 = self.ghost_orange_pos
            input_2 = self.ghost_orange_direction
            input_3 = self.ghost_orange_next_direction
            input_4 = self.distance_ghost_orange_to_pac_man
            input_5 = self.harmless_mode_ghost_orange
            output_1, output_2, output_3, output_4 = self.ghost_intelligence(input_1, input_2, input_3, input_4, input_5)
            self.ghost_orange_pos = output_1
            self.ghost_orange_direction = output_2
            self.ghost_orange_next_direction = output_3
            self.distance_ghost_orange_to_pac_man = output_4
        if self.ghost_pink_pos != [self.scale * 14, self.scale * 13]:
            input_1 = self.ghost_pink_pos
            input_2 = self.ghost_pink_direction
            input_3 = self.ghost_pink_next_direction
            input_4 = self.distance_ghost_pink_to_pac_man
            input_5 = self.harmless_mode_ghost_pink
            output_1, output_2, output_3, output_4 = self.ghost_intelligence(input_1, input_2, input_3, input_4, input_5)
            self.ghost_pink_pos = output_1
            self.ghost_pink_direction = output_2
            self.ghost_pink_next_direction = output_3
            self.distance_ghost_pink_to_pac_man = output_4
        if self.ghost_red_pos != [self.scale * 14, self.scale * 14.5]:
            input_1 = self.ghost_red_pos
            input_2 = self.ghost_red_direction
            input_3 = self.ghost_red_next_direction
            input_4 = self.distance_ghost_red_to_pac_man
            input_5 = self.harmless_mode_ghost_red
            output_1, output_2, output_3, output_4 = self.ghost_intelligence(input_1, input_2, input_3, input_4, input_5)
            self.ghost_red_pos = output_1
            self.ghost_red_direction = output_2
            self.ghost_red_next_direction = output_3
            self.distance_ghost_red_to_pac_man = output_4

    def moving_ghost_into_the_game(self, color):
        if color == 'blue':
            self.ghost_blue_pos = [self.scale * 13.1, self.scale * 10.6]
            self.ghost_blue_direction = self.random_direction_for_ghost()
            self.ghost_blue_next_direction = self.random_next_direction_for_ghost(self.ghost_blue_direction)
        elif color == 'orange':
            self.ghost_orange_pos = [self.scale * 13.1, self.scale * 10.6]
            self.ghost_orange_direction = self.random_direction_for_ghost()
            self.ghost_orange_next_direction = self.random_next_direction_for_ghost(self.ghost_orange_direction)
        elif color == 'pink':
            self.ghost_pink_pos = [self.scale * 13.1, self.scale * 10.6]
            self.ghost_pink_direction = self.random_direction_for_ghost()
            self.ghost_pink_next_direction = self.random_next_direction_for_ghost(self.ghost_pink_direction)
        elif color == 'red':
            self.ghost_red_pos = [self.scale * 13.1, self.scale * 10.6]
            self.ghost_red_direction = self.random_direction_for_ghost()
            self.ghost_red_next_direction = self.random_next_direction_for_ghost(self.ghost_red_direction)

    def ghost_manager(self):
        if self.harmless_mode:
            if self.sprite_frame == 60:
                self.harmless_mode_timer += 1
            if self.harmless_mode_timer == 16:
                self.harmless_mode = False
                self.harmless_mode_ghost_blue   = False
                self.harmless_mode_ghost_orange = False
                self.harmless_mode_ghost_pink   = False
                self.harmless_mode_ghost_red    = False
                self.harmless_mode_timer = 0
        if self.harmless_mode_ghost_blue:
            self.ghost_render('harmless', self.ghost_blue_pos)
        else:
            self.ghost_render('blue',   self.ghost_blue_pos)
        if self.harmless_mode_ghost_orange:
            self.ghost_render('harmless', self.ghost_orange_pos)
        else:
            self.ghost_render('orange', self.ghost_orange_pos)
        if self.harmless_mode_ghost_pink:
            self.ghost_render('harmless', self.ghost_pink_pos)
        else:
            self.ghost_render('pink',   self.ghost_pink_pos)
        if self.harmless_mode_ghost_red:
            self.ghost_render('harmless', self.ghost_red_pos)
        else:
            self.ghost_render('red',    self.ghost_red_pos)

        if self.sprite_frame == 60:
            if self.ghost_blue_pos == [self.scale * 12, self.scale * 13]:
                self.moving_ghost_into_the_game('blue')
            elif self.ghost_orange_pos == [self.scale * 12, self.scale * 14.5]:
                self.moving_ghost_into_the_game('orange')
            elif self.ghost_pink_pos == [self.scale * 14, self.scale * 13]:
                self.moving_ghost_into_the_game('pink')
            elif self.ghost_red_pos == [self.scale * 14, self.scale * 14.5]:
                self.moving_ghost_into_the_game('red')

    def ghost_and_pacman_collider(self):
        if self.distance_ghost_blue_to_pac_man <= (self.scale * 1.1):
            if self.harmless_mode_ghost_blue:
                self.ghost_blue_pos = [self.scale * 12, self.scale * 13]
                self.harmless_mode_ghost_blue = False
                self.distance_ghost_blue_to_pac_man = self.distance_ghost_to_pac_man(self.ghost_blue_pos)
                self.score += 10
            else:
                if self.end_game == False:
                    self.sprite_frame = 0
                    self.sprite_speed = 1
                    self.lives -= 1
                self.end_game = True
        elif self.distance_ghost_orange_to_pac_man <= (self.scale * 1.1):
            if self.harmless_mode_ghost_orange:
                self.ghost_orange_pos = [self.scale * 12, self.scale * 14.5]
                self.harmless_mode_ghost_orange = False
                self.distance_ghost_orange_to_pac_man = self.distance_ghost_to_pac_man(self.ghost_orange_pos)
                self.score += 10
            else:
                if self.end_game == False:
                    self.sprite_frame = 0
                    self.sprite_speed = 1
                    self.lives -= 1
                self.end_game = True
        elif self.distance_ghost_pink_to_pac_man <= (self.scale * 1.1):
            if self.harmless_mode_ghost_pink:
                self.ghost_pink_pos = [self.scale * 14, self.scale * 13]
                self.harmless_mode_ghost_pink = False
                self.distance_ghost_pink_to_pac_man = self.distance_ghost_to_pac_man(self.ghost_pink_pos)
                self.score += 10
            else:
                if self.end_game == False:
                    self.sprite_frame = 0
                    self.sprite_speed = 1
                    self.lives -= 1
                self.end_game = True
        elif self.distance_ghost_red_to_pac_man <= (self.scale * 1.1):
            if self.harmless_mode_ghost_red:
                self.ghost_red_pos = [self.scale * 14, self.scale * 14.5]
                self.harmless_mode_ghost_red = False
                self.distance_ghost_red_to_pac_man = self.distance_ghost_to_pac_man(self.ghost_red_pos)
                self.score += 10
            else:
                if self.end_game == False:
                    self.sprite_frame = 0
                    self.sprite_speed = 1
                    self.lives -= 1
                self.end_game = True

    def restart(self):
        self.sprite_frame = 0
        self.sprite_speed = 2
        self.score = 0
        self.lives = 5
        self.end_game = False
        self.harmless_mode = False
        self.harmless_mode_timer = 0
        self.harmless_mode_ghost_blue   = False
        self.harmless_mode_ghost_orange = False
        self.harmless_mode_ghost_pink   = False
        self.harmless_mode_ghost_red    = False
        self.pac_man_pos            = [self.scale * 13.1, self.scale * 22.6]
        self.pac_man_direction      = [self.scale/16, 0]
        self.pac_man_next_direction = [self.scale/16, 0]
        self.ghost_blue_pos   = [self.scale * 12, self.scale * 13]
        self.ghost_orange_pos = [self.scale * 12, self.scale * 14.5]
        self.ghost_pink_pos   = [self.scale * 14, self.scale * 13]
        self.ghost_red_pos    = [self.scale * 14, self.scale * 14.5]
        self.ghost_blue_direction   = [0, 0]
        self.ghost_orange_direction = [0, 0]
        self.ghost_pink_direction   = [0, 0]
        self.ghost_red_direction    = [0, 0]
        self.ghost_blue_next_direction   = [0, 0]
        self.ghost_orange_next_direction = [0, 0]
        self.ghost_pink_next_direction   = [0, 0]
        self.ghost_red_next_direction    = [0, 0]
        self.distance_ghost_blue_to_pac_man   = self.distance_ghost_to_pac_man(self.ghost_blue_pos)
        self.distance_ghost_orange_to_pac_man = self.distance_ghost_to_pac_man(self.ghost_orange_pos)
        self.distance_ghost_pink_to_pac_man   = self.distance_ghost_to_pac_man(self.ghost_pink_pos)
        self.distance_ghost_red_to_pac_man    = self.distance_ghost_to_pac_man(self.ghost_red_pos)
        self.map = [['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
                    ['#','.','.','.','.','.','.','.','.','.','.','.','.','#','#','.','.','.','.','.','.','.','.','.','.','.','.','#'],
                    ['#','.','#','#','#','#','.','#','#','#','#','#','.','#','#','.','#','#','#','#','#','.','#','#','#','#','.','#'],
                    ['#','o','#','#','#','#','.','#','#','#','#','#','.','#','#','.','#','#','#','#','#','.','#','#','#','#','o','#'],
                    ['#','.','#','#','#','#','.','#','#','#','#','#','.','#','#','.','#','#','#','#','#','.','#','#','#','#','.','#'],
                    ['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'],
                    ['#','.','#','#','#','#','.','#','#','.','#','#','#','#','#','#','#','#','.','#','#','.','#','#','#','#','.','#'],
                    ['#','.','#','#','#','#','.','#','#','.','#','#','#','#','#','#','#','#','.','#','#','.','#','#','#','#','.','#'],
                    ['#','.','.','.','.','.','.','#','#','.','.','.','.','#','#','.','.','.','.','#','#','.','.','.','.','.','.','#'],
                    ['#','#','#','#','#','#','.','#','#','#','#','#',' ','#','#',' ','#','#','#','#','#','.','#','#','#','#','#','#'],
                    [' ',' ',' ',' ',' ','#','.','#','#','#','#','#',' ','#','#',' ','#','#','#','#','#','.','#',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ','#','.','#','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#','#','.','#',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ','#','.','#','#',' ','#','#','#','-','-','#','#','#',' ','#','#','.','#',' ',' ',' ',' ',' '],
                    ['#','#','#','#','#','#','.','#','#',' ','#',' ',' ',' ',' ',' ',' ','#',' ','#','#','.','#','#','#','#','#','#'],
                    [' ',' ',' ',' ',' ',' ','.',' ',' ',' ','#',' ',' ',' ',' ',' ',' ','#',' ',' ',' ','.',' ',' ',' ',' ',' ',' '],
                    ['#','#','#','#','#','#','.','#','#',' ','#',' ',' ',' ',' ',' ',' ','#',' ','#','#','.','#','#','#','#','#','#'],
                    [' ',' ',' ',' ',' ','#','.','#','#',' ','#','#','#','#','#','#','#','#',' ','#','#','.','#',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ','#','.','#','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#','#','.','#',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ','#','.','#','#',' ','#','#','#','#','#','#','#','#',' ','#','#','.','#',' ',' ',' ',' ',' '],
                    ['#','#','#','#','#','#','.','#','#',' ','#','#','#','#','#','#','#','#',' ','#','#','.','#','#','#','#','#','#'],
                    ['#','.','.','.','.','.','.','.','.','.','.','.','.','#','#','.','.','.','.','.','.','.','.','.','.','.','.','#'],
                    ['#','.','#','#','#','#','.','#','#','#','#','#','.','#','#','.','#','#','#','#','#','.','#','#','#','#','.','#'],
                    ['#','.','#','#','#','#','.','#','#','#','#','#','.','#','#','.','#','#','#','#','#','.','#','#','#','#','.','#'],
                    ['#','o','.','.','#','#','.','.','.','.','.','.','.',' ',' ','.','.','.','.','.','.','.','#','#','.','.','o','#'],
                    ['#','#','#','.','#','#','.','#','#','.','#','#','#','#','#','#','#','#','.','#','#','.','#','#','.','#','#','#'],
                    ['#','#','#','.','#','#','.','#','#','.','#','#','#','#','#','#','#','#','.','#','#','.','#','#','.','#','#','#'],
                    ['#','.','.','.','.','.','.','#','#','.','.','.','.','#','#','.','.','.','.','#','#','.','.','.','.','.','.','#'],
                    ['#','.','#','#','#','#','#','#','#','#','#','#','.','#','#','.','#','#','#','#','#','#','#','#','#','#','.','#'],
                    ['#','.','#','#','#','#','#','#','#','#','#','#','.','#','#','.','#','#','#','#','#','#','#','#','#','#','.','#'],
                    ['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'],
                    ['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']]

    def restart_ghost_collision(self):
        if self.sprite_frame == 60 and self.end_game == True and self.lives > -1:
            self.end_game = False
            self.harmless_mode = False
            self.harmless_mode_timer = 0
            self.harmless_mode_ghost_blue   = False
            self.harmless_mode_ghost_orange = False
            self.harmless_mode_ghost_pink   = False
            self.harmless_mode_ghost_red    = False
            self.pac_man_pos            = [self.scale * 13.1, self.scale * 22.6]
            self.pac_man_direction      = [self.scale/16, 0]
            self.pac_man_next_direction = [self.scale/16, 0]
            self.ghost_blue_pos   = [self.scale * 12, self.scale * 13]
            self.ghost_orange_pos = [self.scale * 12, self.scale * 14.5]
            self.ghost_pink_pos   = [self.scale * 14, self.scale * 13]
            self.ghost_red_pos    = [self.scale * 14, self.scale * 14.5]
            self.distance_ghost_blue_to_pac_man   = self.distance_ghost_to_pac_man(self.ghost_blue_pos)
            self.distance_ghost_orange_to_pac_man = self.distance_ghost_to_pac_man(self.ghost_orange_pos)
            self.distance_ghost_pink_to_pac_man   = self.distance_ghost_to_pac_man(self.ghost_pink_pos)
            self.distance_ghost_red_to_pac_man    = self.distance_ghost_to_pac_man(self.ghost_red_pos)
            self.sprite_speed = 2
            self.end_game = False

    def colect_all_dots(self):
        count = 0
        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                if self.map[y][x] == '.' or self.map[y][x] == 'o':
                    count += 1
        if count == 0:
            self.end_game = False
            self.harmless_mode = False
            self.harmless_mode_timer = 0
            self.harmless_mode_ghost_blue   = False
            self.harmless_mode_ghost_orange = False
            self.harmless_mode_ghost_pink   = False
            self.harmless_mode_ghost_red    = False
            self.pac_man_pos            = [self.scale * 13.1, self.scale * 22.6]
            self.pac_man_direction      = [self.scale/16, 0]
            self.pac_man_next_direction = [self.scale/16, 0]
            self.ghost_blue_pos   = [self.scale * 12, self.scale * 13]
            self.ghost_orange_pos = [self.scale * 12, self.scale * 14.5]
            self.ghost_pink_pos   = [self.scale * 14, self.scale * 13]
            self.ghost_red_pos    = [self.scale * 14, self.scale * 14.5]
            self.distance_ghost_blue_to_pac_man   = self.distance_ghost_to_pac_man(self.ghost_blue_pos)
            self.distance_ghost_orange_to_pac_man = self.distance_ghost_to_pac_man(self.ghost_orange_pos)
            self.distance_ghost_pink_to_pac_man   = self.distance_ghost_to_pac_man(self.ghost_pink_pos)
            self.distance_ghost_red_to_pac_man    = self.distance_ghost_to_pac_man(self.ghost_red_pos)
            self.sprite_speed = 2
            self.end_game = False
            self.map = [['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
                        ['#','.','.','.','.','.','.','.','.','.','.','.','.','#','#','.','.','.','.','.','.','.','.','.','.','.','.','#'],
                        ['#','.','#','#','#','#','.','#','#','#','#','#','.','#','#','.','#','#','#','#','#','.','#','#','#','#','.','#'],
                        ['#','o','#','#','#','#','.','#','#','#','#','#','.','#','#','.','#','#','#','#','#','.','#','#','#','#','o','#'],
                        ['#','.','#','#','#','#','.','#','#','#','#','#','.','#','#','.','#','#','#','#','#','.','#','#','#','#','.','#'],
                        ['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'],
                        ['#','.','#','#','#','#','.','#','#','.','#','#','#','#','#','#','#','#','.','#','#','.','#','#','#','#','.','#'],
                        ['#','.','#','#','#','#','.','#','#','.','#','#','#','#','#','#','#','#','.','#','#','.','#','#','#','#','.','#'],
                        ['#','.','.','.','.','.','.','#','#','.','.','.','.','#','#','.','.','.','.','#','#','.','.','.','.','.','.','#'],
                        ['#','#','#','#','#','#','.','#','#','#','#','#',' ','#','#',' ','#','#','#','#','#','.','#','#','#','#','#','#'],
                        [' ',' ',' ',' ',' ','#','.','#','#','#','#','#',' ','#','#',' ','#','#','#','#','#','.','#',' ',' ',' ',' ',' '],
                        [' ',' ',' ',' ',' ','#','.','#','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#','#','.','#',' ',' ',' ',' ',' '],
                        [' ',' ',' ',' ',' ','#','.','#','#',' ','#','#','#','-','-','#','#','#',' ','#','#','.','#',' ',' ',' ',' ',' '],
                        ['#','#','#','#','#','#','.','#','#',' ','#',' ',' ',' ',' ',' ',' ','#',' ','#','#','.','#','#','#','#','#','#'],
                        [' ',' ',' ',' ',' ',' ','.',' ',' ',' ','#',' ',' ',' ',' ',' ',' ','#',' ',' ',' ','.',' ',' ',' ',' ',' ',' '],
                        ['#','#','#','#','#','#','.','#','#',' ','#',' ',' ',' ',' ',' ',' ','#',' ','#','#','.','#','#','#','#','#','#'],
                        [' ',' ',' ',' ',' ','#','.','#','#',' ','#','#','#','#','#','#','#','#',' ','#','#','.','#',' ',' ',' ',' ',' '],
                        [' ',' ',' ',' ',' ','#','.','#','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#','#','.','#',' ',' ',' ',' ',' '],
                        [' ',' ',' ',' ',' ','#','.','#','#',' ','#','#','#','#','#','#','#','#',' ','#','#','.','#',' ',' ',' ',' ',' '],
                        ['#','#','#','#','#','#','.','#','#',' ','#','#','#','#','#','#','#','#',' ','#','#','.','#','#','#','#','#','#'],
                        ['#','.','.','.','.','.','.','.','.','.','.','.','.','#','#','.','.','.','.','.','.','.','.','.','.','.','.','#'],
                        ['#','.','#','#','#','#','.','#','#','#','#','#','.','#','#','.','#','#','#','#','#','.','#','#','#','#','.','#'],
                        ['#','.','#','#','#','#','.','#','#','#','#','#','.','#','#','.','#','#','#','#','#','.','#','#','#','#','.','#'],
                        ['#','o','.','.','#','#','.','.','.','.','.','.','.',' ',' ','.','.','.','.','.','.','.','#','#','.','.','o','#'],
                        ['#','#','#','.','#','#','.','#','#','.','#','#','#','#','#','#','#','#','.','#','#','.','#','#','.','#','#','#'],
                        ['#','#','#','.','#','#','.','#','#','.','#','#','#','#','#','#','#','#','.','#','#','.','#','#','.','#','#','#'],
                        ['#','.','.','.','.','.','.','#','#','.','.','.','.','#','#','.','.','.','.','#','#','.','.','.','.','.','.','#'],
                        ['#','.','#','#','#','#','#','#','#','#','#','#','.','#','#','.','#','#','#','#','#','#','#','#','#','#','.','#'],
                        ['#','.','#','#','#','#','#','#','#','#','#','#','.','#','#','.','#','#','#','#','#','#','#','#','#','#','.','#'],
                        ['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'],
                        ['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']]

    def scoreboard(self):
        score_text = self.font.render(f'Score: {str(self.score)}', 1, self.white)
        lives_text = self.font.render(f'Lives: {str(max(self.lives, 0))}X', 1, self.white)
        x_score_pos = (self.window.get_width() / 2) - (score_text.get_width() / 2)
        y_score_pos = self.scale * 30.75
        x_lives_pos = (self.window.get_width() / 2) - (lives_text.get_width() / 2)
        y_lives_pos = self.scale * 33
        self.window.blit(score_text, (x_score_pos, y_score_pos))
        self.window.blit(lives_text, (x_lives_pos, y_lives_pos))
        if self.lives == -1:
            end_text = self.font.render('game', 1, self.white)
            game_text = self.font.render('over', 1, self.white)
            x_end_pos = (self.window.get_width() / 2) - (end_text.get_width() / 2)
            y_end_pos = self.scale * 12.25
            x_game_pos = (self.window.get_width() / 2) - (game_text.get_width() / 2)
            y_game_pos = self.scale * 13.75
            self.window.blit(end_text, (x_end_pos, y_end_pos))
            self.window.blit(game_text, (x_game_pos, y_game_pos))


jogo = PacMan(26)


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

    # Game
    jogo.clock.tick(60)
    jogo.clear_window()
    jogo.board()
    jogo.animation_step()
    jogo.player()
    jogo.ghost()
    jogo.collect_dots()
    jogo.ghost_manager()
    jogo.ghost_and_pacman_collider()
    jogo.scoreboard()
    jogo.restart_ghost_collision()
    jogo.colect_all_dots()

    pg.display.update()
