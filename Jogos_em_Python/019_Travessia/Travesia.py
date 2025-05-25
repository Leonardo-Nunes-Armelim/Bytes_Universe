import pygame as pg


class RiverCrossing:
    def __init__(self):
        self.window = pg.display.set_mode((900, 935))

        self.clock = pg.time.Clock()

        self.frog_pos = [420, 860]
        self.frog_heights = [860, 735, 635, 535, 435, 335, 235, 135, 15]
        self.rows_of_platforms = [[0, 150, 250, 600],
                                  [60, 180, 420, 660],
                                  [50, 650],
                                  [50, 250, 450, 800],
                                  [120, 360, 720],
                                  [0, 700],
                                  [100, 250, 450, 700, 800]]

        frog       = pg.image.load('./frog.png')
        background = pg.image.load('./background.jpg')
        plant      = pg.image.load('./plant.jpg')
        tree_trunk = pg.image.load('./tree trunk.jpg')
        turtle     = pg.image.load('./turtle.jpg')
        self.frog       = pg.transform.scale(frog,       (60, 60))
        self.background = pg.transform.scale(background, (900, 935))
        self.plant      = pg.transform.scale(plant,      (100, 100))
        self.tree_trunk = pg.transform.scale(tree_trunk, (300, 100))
        self.turtle     = pg.transform.scale(turtle,     (120, 100))

    def clear_window(self):
        self.window.blit(self.background, (0, 0))

    def rendering_platforms(self):
        for y in range(len(self.rows_of_platforms)):
            for x in range(len(self.rows_of_platforms[y])):
                if y == 0:
                    self.window.blit(self.plant, (self.rows_of_platforms[y][x], 115))
                if y == 1:
                    self.window.blit(self.turtle, (self.rows_of_platforms[y][x], 215))
                if y == 2:
                    self.window.blit(self.tree_trunk, (self.rows_of_platforms[y][x], 315))
                if y == 3:
                    self.window.blit(self.plant, (self.rows_of_platforms[y][x], 415))
                if y == 4:
                    self.window.blit(self.turtle, (self.rows_of_platforms[y][x], 515))
                if y == 5:
                    self.window.blit(self.tree_trunk, (self.rows_of_platforms[y][x], 615))
                if y == 6:
                    self.window.blit(self.plant, (self.rows_of_platforms[y][x], 715))

    def frog_is_on_the_platform(self):
        if self.frog_pos[1] in [860, 15]:
            return True

        is_in_platform = False

        frog_height_index = 0
        for index in range(len(self.frog_heights)):
            if self.frog_heights[index] == self.frog_pos[1]:
                frog_height_index = index

        for y in range(len(self.rows_of_platforms)):
            for x in range(len(self.rows_of_platforms[y])):
                if y in [0, 3, 6] and frog_height_index in [1, 4, 7] and self.compare_platforms_index_to_frog_height_index(y, frog_height_index):
                    if self.frog_pos[0]>= self.rows_of_platforms[y][x] and self.frog_pos[0] <= self.rows_of_platforms[y][x] + 40:
                        is_in_platform = True
                elif y in [1, 4] and frog_height_index in [3, 6] and self.compare_platforms_index_to_frog_height_index(y, frog_height_index):
                    if self.frog_pos[0] - 15 >= self.rows_of_platforms[y][x] and self.frog_pos[0] <= self.rows_of_platforms[y][x] + 35:
                        is_in_platform = True
                elif y in [2, 5] and frog_height_index in [2, 5] and self.compare_platforms_index_to_frog_height_index(y, frog_height_index):
                    if self.frog_pos[0] >= self.rows_of_platforms[y][x] and self.frog_pos[0] <= self.rows_of_platforms[y][x] + 235:
                        is_in_platform = True

        return is_in_platform

    def compare_platforms_index_to_frog_height_index(self, platforms_index, frog_height_index):
        if platforms_index == 6 and frog_height_index == 1:
            return True
        elif platforms_index == 5 and frog_height_index == 2:
            return True
        elif platforms_index == 4 and frog_height_index == 3:
            return True
        elif platforms_index == 3 and frog_height_index == 4:
            return True
        elif platforms_index == 2 and frog_height_index == 5:
            return True
        elif platforms_index == 1 and frog_height_index == 6:
            return True
        elif platforms_index == 0 and frog_height_index == 7:
            return True
        else:
            return False

    def updating_the_frog_position_on_top_of_the_platforms(self):
        frog_height_index = 0
        for index in range(len(self.frog_heights)):
            if self.frog_heights[index] == self.frog_pos[1]:
                frog_height_index = index

        for y in range(len(self.rows_of_platforms)):
            for x in range(len(self.rows_of_platforms[y])):
                if y in [0, 3, 6] and frog_height_index in [1, 4, 7] and self.compare_platforms_index_to_frog_height_index(y, frog_height_index):
                    if self.frog_pos[0]>= self.rows_of_platforms[y][x] and self.frog_pos[0] <= self.rows_of_platforms[y][x] + 40:
                        self.frog_pos[0] -= 1
                elif y in [1, 4] and frog_height_index in [3, 6] and self.compare_platforms_index_to_frog_height_index(y, frog_height_index):
                    if self.frog_pos[0] - 15 >= self.rows_of_platforms[y][x] and self.frog_pos[0] <= self.rows_of_platforms[y][x] + 35:
                        self.frog_pos[0] += 1
                elif y in [2, 5] and frog_height_index in [2, 5] and self.compare_platforms_index_to_frog_height_index(y, frog_height_index):
                    if self.frog_pos[0] >= self.rows_of_platforms[y][x] and self.frog_pos[0] <= self.rows_of_platforms[y][x] + 235:
                        self.frog_pos[0] -= 2

    def reset_frog_position(self):
        if self.frog_is_on_the_platform() == False:
            self.frog_pos = [420, 860]

    def rendering_frog(self):
        self.window.blit(self.frog, (self.frog_pos[0], self.frog_pos[1]))

    def update_platforms(self):
        for y in range(len(self.rows_of_platforms)):
            for x in range(len(self.rows_of_platforms[y])):
                if y == 0 or y == 3 or y == 6:
                    if self.rows_of_platforms[y][x] - 1 == -100:
                        self.rows_of_platforms[y][x] = 900
                    else:
                        self.rows_of_platforms[y][x] -= 1
                elif y == 1 or y == 4:
                    if self.rows_of_platforms[y][x] + 1 == 900:
                        self.rows_of_platforms[y][x] = -120
                    else:
                        self.rows_of_platforms[y][x] += 1
                elif y == 2 or y == 5:
                    if self.rows_of_platforms[y][x] - 2 == -300:
                        self.rows_of_platforms[y][x] = 900
                    else:
                        self.rows_of_platforms[y][x] -= 2

    def move(self, key):
        if key == 'w' or key == 'up':
            height = 0
            for i in range(len(self.frog_heights)):
                if self.frog_heights[i] == self.frog_pos[1]:
                    height = i
            if height == 8:
                self.frog_pos[1] = self.frog_heights[height]
            else:
                self.frog_pos[1] = self.frog_heights[height + 1]
        elif key == 'a' or key == 'left':
            if self.frog_pos[0] > 20:
                self.frog_pos[0] -= 50
                if self.frog_is_on_the_platform() == False:
                    self.frog_pos[0] += 50
        elif key == 's' or key == 'down':
            height = 0
            for i in range(len(self.frog_heights)):
                if self.frog_heights[i] == self.frog_pos[1]:
                    height = i
            if height == 0:
                self.frog_pos[1] = self.frog_heights[height]
            else:
                self.frog_pos[1] = self.frog_heights[height - 1]
        elif key == 'd' or key == 'right':
            if self.frog_pos[0] < 875:
                self.frog_pos[0] += 50
                if self.frog_is_on_the_platform() == False:
                    self.frog_pos[0] -= 50
        elif key == 'r':
            self.frog_pos = [420, 860]

jogo = RiverCrossing()


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
    jogo.update_platforms()
    jogo.updating_the_frog_position_on_top_of_the_platforms()
    jogo.rendering_platforms()
    jogo.reset_frog_position()
    jogo.rendering_frog()

    pg.display.update()
