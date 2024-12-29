import pygame as pg
import time

class Sokoban:
    def __init__(self, window_size):
        self.window_size = window_size
        self.image_size = window_size / 9
        self.level = 1
        self.show_level = True

        self.window = pg.display.set_mode((window_size, window_size))

        pg.font.init()
        self.font = pg.font.SysFont("Courier New", 50, bold=True)

        self.agent = pg.image.load('./agent.png')
        self.agent = pg.transform.scale(self.agent, (self.image_size, self.image_size))
        self.agent_on_target = pg.image.load('./agent on target.png')
        self.agent_on_target = pg.transform.scale(self.agent_on_target, (self.image_size, self.image_size))
        self.box_on_target = pg.image.load('./box on target.png')
        self.box_on_target = pg.transform.scale(self.box_on_target, (self.image_size, self.image_size))
        self.box = pg.image.load('./box.png')
        self.box = pg.transform.scale(self.box, (self.image_size, self.image_size))
        self.floor = pg.image.load('./floor.png')
        self.floor = pg.transform.scale(self.floor, (self.image_size, self.image_size))
        self.target = pg.image.load('./target.png')
        self.target = pg.transform.scale(self.target, (self.image_size, self.image_size))
        self.tree = pg.image.load('./tree.png')
        self.tree = pg.transform.scale(self.tree, (self.image_size, self.image_size))
        self.wall = pg.image.load('./wall.png')
        self.wall = pg.transform.scale(self.wall, (self.image_size, self.image_size))

        self.main_level = [['', '', '', '', '', '', '', '', ''],
                           ['', '', '', '', '', '', '', '', ''],
                           ['', '', '', '', '', '', '', '', ''],
                           ['', '', '', '', '', '', '', '', ''],
                           ['', '', '', '', '', '', '', '', ''],
                           ['', '', '', '', '', '', '', '', ''],
                           ['', '', '', '', '', '', '', '', ''],
                           ['', '', '', '', '', '', '', '', ''],
                           ['', '', '', '', '', '', '', '', '']]

        self.level_1 = [['t', 't', 'w', 'w', 'w', 't', 't', 't', 't'],
                        ['t', 't', 'w', 'o', 'w', 't', 't', 't', 't'],
                        ['t', 't', 'w', 'f', 'w', 'w', 'w', 'w', 't'],
                        ['w', 'w', 'w', 'b', 'f', 'b', 'o', 'w', 't'],
                        ['w', 'o', 'f', 'b', 'a', 'w', 'w', 'w', 't'],
                        ['w', 'w', 'w', 'w', 'b', 'w', 't', 't', 't'],
                        ['t', 't', 't', 'w', 'o', 'w', 't', 't', 't'],
                        ['t', 't', 't', 'w', 'w', 'w', 't', 't', 't'],
                        ['t', 't', 't', 't', 't', 't', 't', 't', 't']]

        self.level_2 = [['w', 'w', 'w', 'w', 'w', 't', 't', 't', 't'],
                        ['w', 'f', 'f', 'f', 'w', 't', 't', 't', 't'],
                        ['w', 'f', 'b', 'a', 'w', 't', 'w', 'w', 'w'],
                        ['w', 'f', 'b', 'b', 'w', 't', 'w', 'o', 'w'],
                        ['w', 'w', 'w', 'f', 'w', 'w', 'w', 'o', 'w'],
                        ['t', 'w', 'w', 'f', 'f', 'f', 'f', 'o', 'w'],
                        ['t', 'w', 'f', 'f', 'f', 'w', 'f', 'f', 'w'],
                        ['t', 'w', 'f', 'f', 'f', 'w', 'w', 'w', 'w'],
                        ['t', 'w', 'w', 'w', 'w', 'w', 't', 't', 't']]

        self.level_3 = [['t', 'w', 'w', 'w',   'w', 't', 't', 't', 't'],
                        ['w', 'w', 'f', 'f',   'w', 't', 't', 't', 't'],
                        ['w', 'f', 'a', 'b',   'w', 't', 't', 't', 't'],
                        ['w', 'w', 'b', 'f',   'w', 'w', 't', 't', 't'],
                        ['w', 'w', 'f', 'b',   'f', 'w', 't', 't', 't'],
                        ['w', 'o', 'b', 'f',   'f', 'w', 't', 't', 't'],
                        ['w', 'o', 'o', 'bot', 'o', 'w', 't', 't', 't'],
                        ['w', 'w', 'w', 'w',   'w', 'w', 't', 't', 't'],
                        ['t', 't', 't', 't',   't', 't', 't', 't', 't']]

        self.level_4 = [['t', 'w', 'w', 'w', 'w', 't', 't', 't', 't'],
                        ['t', 'w', 'a', 'f', 'w', 'w', 'w', 't', 't'],
                        ['t', 'w', 'f', 'b', 'f', 'f', 'w', 't', 't'],
                        ['w', 'w', 'w', 'f', 'w', 'f', 'w', 'w', 't'],
                        ['w', 'o', 'w', 'f', 'w', 'f', 'f', 'w', 't'],
                        ['w', 'o', 'b', 'f', 'f', 'w', 'f', 'w', 't'],
                        ['w', 'o', 'f', 'f', 'f', 'b', 'f', 'w', 't'],
                        ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 't'],
                        ['t', 't', 't', 't', 't', 't', 't', 't', 't']]

        self.level_5 = [['t', 't', 'w', 'w', 'w', 'w', 'w', 'w', 't'],
                        ['t', 't', 'w', 'f', 'f', 'f', 'f', 'w', 't'],
                        ['w', 'w', 'w', 'b', 'b', 'b', 'f', 'w', 't'],
                        ['w', 'a', 'f', 'b', 'o', 'o', 'f', 'w', 't'],
                        ['w', 'f', 'b', 'o', 'o', 'o', 'w', 'w', 't'],
                        ['w', 'w', 'w', 'w', 'f', 'f', 'w', 't', 't'],
                        ['t', 't', 't', 'w', 'w', 'w', 'w', 't', 't'],
                        ['t', 't', 't', 't', 't', 't', 't', 't', 't'],
                        ['t', 't', 't', 't', 't', 't', 't', 't', 't']]

        self.level_6 = [['t', 't', 'w', 'w', 'w',   'w', 'w', 't', 't'],
                        ['w', 'w', 'w', 'f', 'f',   'a', 'w', 't', 't'],
                        ['w', 'f', 'f', 'b', 'o',   'f', 'w', 'w', 't'],
                        ['w', 'f', 'f', 'o', 'b',   'o', 'f', 'w', 't'],
                        ['w', 'w', 'w', 'f', 'bot', 'b', 'f', 'w', 't'],
                        ['t', 't', 'w', 'f', 'f',   'f', 'w', 'w', 't'],
                        ['t', 't', 'w', 'w', 'w',   'w', 'w', 't', 't'],
                        ['t', 't', 't', 't', 't',   't', 't', 't', 't'],
                        ['t', 't', 't', 't', 't',   't', 't', 't', 't']]

        self.level_7 = [['t', 't', 'w', 'w', 'w', 'w', 't', 't', 't'],
                        ['t', 't', 'w', 'o', 'o', 'w', 't', 't', 't'],
                        ['t', 'w', 'w', 'f', 'o', 'w', 'w', 't', 't'],
                        ['t', 'w', 'f', 'f', 'b', 'o', 'w', 't', 't'],
                        ['w', 'w', 'f', 'b', 'f', 'f', 'w', 'w', 't'],
                        ['w', 'f', 'f', 'w', 'b', 'b', 'f', 'w', 't'],
                        ['w', 'f', 'f', 'a', 'f', 'f', 'f', 'w', 't'],
                        ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 't'],
                        ['t', 't', 't', 't', 't', 't', 't', 't', 't']]

        self.level_8 = [['w', 'w', 'w', 'w', 'w',   'w', 'w', 'w', 't'],
                        ['w', 'f', 'f', 'w', 'f',   'f', 'f', 'w', 't'],
                        ['w', 'a', 'b', 'o', 'o',   'b', 'f', 'w', 't'],
                        ['w', 'f', 'b', 'o', 'bot', 'f', 'w', 'w', 't'],
                        ['w', 'f', 'b', 'o', 'o',   'b', 'f', 'w', 't'],
                        ['w', 'f', 'f', 'w', 'f',   'f', 'f', 'w', 't'],
                        ['w', 'w', 'w', 'w', 'w',   'w', 'w', 'w', 't'],
                        ['t', 't', 't', 't', 't',   't', 't', 't', 't'],
                        ['t', 't', 't', 't', 't',   't', 't', 't', 't']]

        self.level_9 = [['w', 'w', 'w', 'w', 'w', 'w', 't', 't', 't'],
                        ['w', 'f', 'f', 'f', 'f', 'w', 't', 't', 't'],
                        ['w', 'f', 'b', 'b', 'b', 'w', 'w', 't', 't'],
                        ['w', 'f', 'f', 'w', 'o', 'o', 'w', 'w', 'w'],
                        ['w', 'w', 'f', 'f', 'o', 'o', 'b', 'f', 'w'],
                        ['t', 'w', 'f', 'a', 'f', 'f', 'f', 'f', 'w'],
                        ['t', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
                        ['t', 't', 't', 't', 't', 't', 't', 't', 't'],
                        ['t', 't', 't', 't', 't', 't', 't', 't', 't']]

        self.level_10 = [['w', 'w', 'w', 'w', 'w', 'w', 'w', 't', 't'],
                         ['w', 'o', 'o', 'b', 'o', 'o', 'w', 't', 't'],
                         ['w', 'o', 'o', 'w', 'o', 'o', 'w', 't', 't'],
                         ['w', 'f', 'b', 'b', 'b', 'f', 'w', 't', 't'],
                         ['w', 'f', 'f', 'b', 'f', 'f', 'w', 't', 't'],
                         ['w', 'f', 'b', 'b', 'b', 'f', 'w', 't', 't'],
                         ['w', 'f', 'f', 'w', 'a', 'f', 'w', 't', 't'],
                         ['w', 'w', 'w', 'w', 'w', 'w', 'w', 't', 't'],
                         ['t', 't', 't', 't', 't', 't', 't', 't', 't']]

        self.level_11 = [['t', 'w', 'w',   'w', 'w', 'w', 't', 't', 't'],
                         ['t', 'w', 'f',   'a', 'f', 'w', 'w', 'w', 't'],
                         ['w', 'w', 'f',   'w', 'b', 'f', 'f', 'w', 't'],
                         ['w', 'f', 'bot', 'o', 'f', 'o', 'f', 'w', 't'],
                         ['w', 'f', 'f',   'b', 'b', 'f', 'w', 'w', 't'],
                         ['w', 'w', 'w',   'f', 'w', 'o', 'w', 't', 't'],
                         ['t', 't', 'w',   'f', 'f', 'f', 'w', 't', 't'],
                         ['t', 't', 'w',   'w', 'w', 'w', 'w', 't', 't'],
                         ['t', 't', 't',   't', 't', 't', 't', 't', 't']]

        self.level_12 = [['w', 'w', 'w',   'w', 'w', 'w', 't', 't', 't'],
                         ['w', 'f', 'f',   'f', 'f', 'w', 't', 't', 't'],
                         ['w', 'f', 'b',   'f', 'a', 'w', 't', 't', 't'],
                         ['w', 'w', 'bot', 'f', 'f', 'w', 't', 't', 't'],
                         ['w', 'f', 'bot', 'f', 'w', 'w', 't', 't', 't'],
                         ['w', 'f', 'bot', 'f', 'w', 't', 't', 't', 't'],
                         ['w', 'f', 'bot', 'f', 'w', 't', 't', 't', 't'],
                         ['w', 'f', 'o',   'f', 'w', 't', 't', 't', 't'],
                         ['w', 'w', 'w',   'w', 'w', 't', 't', 't', 't']]

        self.level_13 = [['t', 't', 'w', 'w',   'w', 'w', 't', 't', 't'],
                         ['t', 't', 'w', 'f',   'f', 'w', 't', 't', 't'],
                         ['w', 'w', 'w', 'b',   'f', 'w', 'w', 't', 't'],
                         ['w', 'f', 'f', 'bot', 'f', 'a', 'w', 't', 't'],
                         ['w', 'f', 'f', 'bot', 'f', 'f', 'w', 't', 't'],
                         ['w', 'f', 'f', 'bot', 'f', 'w', 'w', 't', 't'],
                         ['w', 'w', 'w', 'bot', 'f', 'w', 't', 't', 't'],
                         ['t', 't', 'w', 'o',   'w', 'w', 't', 't', 't'],
                         ['t', 't', 'w', 'w',   'w', 't', 't', 't', 't']]

        self.level_14 = [['w', 'w', 'w', 'w', 'w', 't', 't', 't', 't'],
                         ['w', 'f', 'f', 'f', 'w', 'w', 'w', 'w', 'w'],
                         ['w', 'f', 'w', 'f', 'w', 'f', 'f', 'f', 'w'],
                         ['w', 'f', 'b', 'f', 'f', 'f', 'b', 'f', 'w'],
                         ['w', 'o', 'o', 'w', 'b', 'w', 'b', 'w', 'w'],
                         ['w', 'o', 'a', 'b', 'f', 'f', 'f', 'w', 't'],
                         ['w', 'o', 'o', 'f', 'f', 'w', 'w', 'w', 't'],
                         ['w', 'w', 'w', 'w', 'w', 'w', 't', 't', 't'],
                         ['t', 't', 't', 't', 't', 't', 't', 't', 't']]

        self.level_15 = [['t', 'w', 'w', 'w', 'w', 'w', 'w', 't', 't'],
                         ['t', 'w', 'f', 'f', 'f', 'f', 'w', 'w', 't'],
                         ['w', 'w', 'o', 'w', 'w', 'b', 'f', 'w', 't'],
                         ['w', 'f', 'o', 'o', 'b', 'f', 'f', 'w', 't'],
                         ['w', 'f', 'f', 'w', 'b', 'f', 'f', 'w', 't'],
                         ['w', 'f', 'f', 'a', 'f', 'w', 'w', 'w', 't'],
                         ['w', 'w', 'w', 'w', 'w', 'w', 't', 't', 't'],
                         ['t', 't', 't', 't', 't', 't', 't', 't', 't'],
                         ['t', 't', 't', 't', 't', 't', 't', 't', 't']]

        self.level_16 = [['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
                         ['w', 'o', 'f', 'f', 'o', 'f', 'f', 'o', 'w'],
                         ['w', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'w'],
                         ['w', 'f', 'f', 'b', 'b', 'b', 'f', 'f', 'w'],
                         ['w', 'o', 'f', 'b', 'a', 'b', 'f', 'o', 'w'],
                         ['w', 'f', 'f', 'b', 'b', 'b', 'f', 'f', 'w'],
                         ['w', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'w'],
                         ['w', 'o', 'f', 'f', 'o', 'f', 'f', 'o', 'w'],
                         ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w']]

    def clear_window(self):
        pg.draw.rect(self.window, (255, 255, 255), (0, 0, self.window.get_width(), self.window.get_height()))

    def copy_level(self, level):
        for y in range(9):
            for x in range(9):
                self.main_level[y][x] = level[y][x]

    def select_level(self):
        if self.level == 1:
            self.copy_level(self.level_1)
        elif self.level == 2:
            self.copy_level(self.level_2)
        elif self.level == 3:
            self.copy_level(self.level_3)
        elif self.level == 4:
            self.copy_level(self.level_4)
        elif self.level == 5:
            self.copy_level(self.level_5)
        elif self.level == 6:
            self.copy_level(self.level_6)
        elif self.level == 7:
            self.copy_level(self.level_7)
        elif self.level == 8:
            self.copy_level(self.level_8)
        elif self.level == 9:
            self.copy_level(self.level_9)
        elif self.level == 10:
            self.copy_level(self.level_10)
        elif self.level == 11:
            self.copy_level(self.level_11)
        elif self.level == 12:
            self.copy_level(self.level_12)
        elif self.level == 13:
            self.copy_level(self.level_13)
        elif self.level == 14:
            self.copy_level(self.level_14)
        elif self.level == 15:
            self.copy_level(self.level_15)
        elif self.level == 16:
            self.copy_level(self.level_16)

    def draw_map(self):
        for y in  range(9):
            for x in  range(9):
                string = self.main_level[y][x]
                if string == 'a':
                    self.window.blit(self.agent, (x * self.image_size, y * self.image_size))
                elif string == 'aot':
                    self.window.blit(self.agent_on_target, (x * self.image_size, y * self.image_size))
                elif string == 't':
                    self.window.blit(self.tree, (x * self.image_size, y * self.image_size))
                elif string == 'w':
                    self.window.blit(self.wall, (x * self.image_size, y * self.image_size))
                elif string == 'o':
                    self.window.blit(self.target, (x * self.image_size, y * self.image_size))
                elif string == 'f':
                    self.window.blit(self.floor, (x * self.image_size, y * self.image_size))
                elif string == 'b':
                    self.window.blit(self.box, (x * self.image_size, y * self.image_size))
                elif string == 'bot':
                    self.window.blit(self.box_on_target, (x * self.image_size, y * self.image_size))

    def get_agent_position(self):
        agent_position = [0, 0]
        for y in range(9):
            for x in range(9):
                if self.main_level[y][x] == 'a' or self.main_level[y][x] == 'aot':
                    agent_position[0] = x
                    agent_position[1] = y
        return agent_position

    def move(self, key):
        agent_position = self.get_agent_position()

        agent_new_position = [agent_position[0], agent_position[1]]
        space_ahead = [agent_position[0], agent_position[1]]

        if key == 'w' or key == 'up':
            agent_new_position[1] -= 1
            space_ahead[1] -= 2
        elif key == 'a' or key == 'left':
            agent_new_position[0] -= 1
            space_ahead[0] -= 2
        elif key == 's' or key == 'down':
            agent_new_position[1] += 1
            space_ahead[1] += 2
        elif key == 'd' or key == 'right':
            agent_new_position[0] += 1
            space_ahead[0] += 2

        if space_ahead[0] <= -1 or space_ahead[0] >= 10 or space_ahead[1] <= -1 or space_ahead[1] >= 10:
            pass
        else:
            if self.main_level[agent_new_position[1]][agent_new_position[0]] == 'b' and self.main_level[space_ahead[1]][space_ahead[0]] == 'f':
                self.change_map(agent_position, agent_new_position, space_ahead)
            elif self.main_level[agent_new_position[1]][agent_new_position[0]] == 'bot' and self.main_level[space_ahead[1]][space_ahead[0]] == 'f':
                self.change_map(agent_position, agent_new_position, space_ahead)
            elif self.main_level[agent_new_position[1]][agent_new_position[0]] == 'b' and self.main_level[space_ahead[1]][space_ahead[0]] == 'o':
                self.change_map(agent_position, agent_new_position, space_ahead)
            elif self.main_level[agent_new_position[1]][agent_new_position[0]] == 'bot' and self.main_level[space_ahead[1]][space_ahead[0]] == 'o':
                self.change_map(agent_position, agent_new_position, space_ahead)
            elif self.main_level[agent_new_position[1]][agent_new_position[0]] == 'f':
                self.change_map(agent_position, agent_new_position, space_ahead)
            elif self.main_level[agent_new_position[1]][agent_new_position[0]] == 'o':
                self.change_map(agent_position, agent_new_position, space_ahead)

    def change_map(self, agent_position, agent_new_position, space_ahead):
        if self.main_level[agent_position[1]][agent_position[0]] == 'a':
            self.main_level[agent_position[1]][agent_position[0]] = 'f'
        elif self.main_level[agent_position[1]][agent_position[0]] == 'aot':
            self.main_level[agent_position[1]][agent_position[0]] = 'o'

        if self.main_level[agent_new_position[1]][agent_new_position[0]] == 'b' and self.main_level[space_ahead[1]][space_ahead[0]] == 'f':
            self.main_level[space_ahead[1]][space_ahead[0]] = 'b'
            self.main_level[agent_new_position[1]][agent_new_position[0]] = 'a'
        elif self.main_level[agent_new_position[1]][agent_new_position[0]] == 'bot' and self.main_level[space_ahead[1]][space_ahead[0]] == 'f':
            self.main_level[space_ahead[1]][space_ahead[0]] = 'b'
            self.main_level[agent_new_position[1]][agent_new_position[0]] = 'aot'
        elif self.main_level[agent_new_position[1]][agent_new_position[0]] == 'b' and self.main_level[space_ahead[1]][space_ahead[0]] == 'o':
            self.main_level[space_ahead[1]][space_ahead[0]] = 'bot'
            self.main_level[agent_new_position[1]][agent_new_position[0]] = 'a'
        elif self.main_level[agent_new_position[1]][agent_new_position[0]] == 'bot' and self.main_level[space_ahead[1]][space_ahead[0]] == 'o':
            self.main_level[space_ahead[1]][space_ahead[0]] = 'bot'
            self.main_level[agent_new_position[1]][agent_new_position[0]] = 'aot'
        elif self.main_level[agent_new_position[1]][agent_new_position[0]] == 'f':
            self.main_level[agent_new_position[1]][agent_new_position[0]] = 'a'
        elif self.main_level[agent_new_position[1]][agent_new_position[0]] == 'o':
            self.main_level[agent_new_position[1]][agent_new_position[0]] = 'aot'

    def new_level(self):
        if self.show_level:
            text = self.font.render(f'Level {self.level}', 1, (0, 0, 0))
            x = (self.window.get_width() / 2) - (text.get_width() / 2)
            y = (self.window.get_height() / 2) - (text.get_height() / 2)
            self.window.blit(text, (x, y))
            pg.display.update()
            time.sleep(2)
            self.show_level = False
            self.select_level()

    def is_level_completed(self):
        count = 0
        for y in  range(9):
            for x in  range(9):
                if self.main_level[y][x] == 'b':
                    count += 1
        if count == 0:
            self.show_level = True
            self.level += 1
            if self.level == 17:
                self.level = 1
            pg.display.update()
            time.sleep(1)

sokoban = Sokoban(504)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            sokoban.move(pg.key.name(event.key))
            if pg.key.name(event.key) == 'r':
                sokoban.select_level()
            if pg.key.name(event.key) == 'escape':
                pg.quit()
                quit()

    # Game
    sokoban.clear_window()

    sokoban.new_level()

    sokoban.draw_map()

    sokoban.is_level_completed()

    pg.display.update()
