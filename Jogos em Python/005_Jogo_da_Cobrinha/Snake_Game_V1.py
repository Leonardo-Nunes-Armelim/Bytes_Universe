from Bytes_Universe_Game_Engine_V1 import Window
import pygame as pg
import random
import time



class Snake_Game:
    def __init__(self):
        # Game Colors
        self.color = {
            'black': (  0,   0,   0),
            'gray':  (150, 150, 150),
            'white': (255, 255, 255),
            'red':   (255,   0,   0),
            'green': (  0, 255,   0),
            'blue':  (  0,   0, 255)
        }

        # Init score font
        pg.font.init()
        self.font = pg.font.SysFont("Courier New", 50, bold=True)

        self.map_size = (53, 30)
        self.map = [['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
                    ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']]
        self.apple_position = (10, 10)
        self.snake_position = [(41, 20), (41, 21), (41, 22), (41, 23), (42, 23), (43, 23)]
        self.snake_direction = (-1, 0)
        self.score = 0
        self.countdown = 3
        self.end_game = False
        self.key_pressed = False
        self.key_pressed_log = ''

    def snake_change_direction(self, key):
        if (key == 'w' or key == 'up') and self.snake_direction != (0, 1):
            self.snake_direction = (0, -1)
        elif (key == 'a' or key == 'left') and self.snake_direction != (1, 0):
            self.snake_direction = (-1, 0)
        elif (key == 's' or key == 'down') and self.snake_direction != (0, -1):
            self.snake_direction = (0, 1)
        elif (key == 'd' or key == 'right') and self.snake_direction != (-1, 0):
            self.snake_direction = (1, 0)

    def game_start_countdown(self, window):
        # Draw circle at screen center
        pg.draw.circle(window, self.color['white'], (636, 360), 50)

        # Draw center text
        if self.countdown == 3:
            countdown_text = self.font.render('3', True, self.color['black'])
            window.blit(countdown_text, (620, 336))
            self.countdown -= 1
        elif self.countdown == 2:
            countdown_text = self.font.render('2', True, self.color['black'])
            window.blit(countdown_text, (620, 336))
            self.countdown -= 1
        elif self.countdown == 1:
            countdown_text = self.font.render('1', True, self.color['black'])
            window.blit(countdown_text, (620, 336))
            self.countdown -= 1
        elif self.countdown == 0:
            countdown_text = self.font.render('Go!', True, self.color['black'])
            window.blit(countdown_text, (595, 336))
            self.countdown -= 1

        pg.display.update()
        time.sleep(1)

    def draw_map_elements(self, window):
        # Square side size
        side = window.get_height() / self.map_size[1]

        # Loop to find elements in the map
        for y in range(self.map_size[1]):
            for x in range(self.map_size[0]):
                # Draw snake square position
                if self.map[y][x] == 's':
                    pg.draw.rect(window, self.color['green'], (x * side , y * side, side, side))
                # Draw apple square position
                if self.map[y][x] == 'a':
                    pg.draw.rect(window, self.color['red'], (x * side , y * side, side, side))

    def update_snake_position(self, snake):
        snake_size = len(snake) - 1
        for i in range(len(snake)):
            if snake_size - i == 0:
                self.snake_position[0] = (self.snake_position[0][0] + self.snake_direction[0], self.snake_position[0][1] + self.snake_direction[1])
            else:
                self.snake_position[snake_size - i] = self.snake_position[snake_size - i - 1]

    def sort_apple_position(self):
        map_x = len(self.map[0])
        map_y = len(self.map)
        x = random.randint(0, map_x - 1)
        y = random.randint(0, map_y - 1)
        self.apple_position = (x, y)

    def clear_map(self, target_map):
        for y in range(len(target_map)):
            for x in range(len(target_map[0])):
                target_map[y][x] = ''

    def add_snake_position(self, map_size, snake):
        for y in range(map_size[1]):
            for x in range(map_size[0]):
                for s in range(len(snake)):
                    if snake[s][0] == x and snake[s][1] == y:
                        self.map[y][x] = 's'

    def add_apple_position(self, map_size, apple):
        for y in range(map_size[1]):
            for x in range(map_size[0]):
                if y == apple[1] and x == apple[0]:
                    self.map[y][x] = 'a'

    def snake_get_apple(self):
        # Check if the apple was captured by the snake
        if self.snake_position[0] == self.apple_position:
            self.snake_position.append(self.snake_position[len(self.snake_position) - 1])
            self.sort_apple_position()
            self.score += 1

    def draw_score(self, window):
        score_text = self.font.render('Score: ' + str(self.score), True, self.color['white'])
        window.blit(score_text, (0, 0))

    def end_of_game(self):
        # Check if the snake left the game screen
        if self.snake_position[0][0] < 0 or self.snake_position[0][1] < 0 or self.snake_position[0][0] > self.map_size[0] - 1 or self.snake_position[0][1] > self.map_size[1] - 1:
            self.end_game = True

        # Check if the snake has hit your own body
        for i in range(1, len(self.snake_position)):
            if self.snake_position[0] == self.snake_position[i]:
                self.end_game = True

    def draw_end_game(self, window):
        # Draw end of game screen
        if self.end_game == True:
            score_text = self.font.render('End Game', True, self.color['white'])
            window.blit(score_text, (525, 336))

    def home_screen_animation(self, window):
        # Update snake position
        self.update_snake_position(self.snake_position)

        # Animation script
        if self.snake_position[0] == (12, 20) and len(self.snake_position) <= 25:
            self.snake_direction = (0, -1)
        elif self.snake_position[0] == (12, 15):
            self.snake_direction = (-1, 0)
        elif self.snake_position[0] == (10, 15):
            self.snake_direction = (0, -1)
        elif self.snake_position[0] == (10, 10):
            self.snake_position.append(self.snake_position[len(self.snake_position) - 1])
            self.score += 1
            self.apple_position = (40, 15)
        elif self.snake_position[0] == (10, 5):
            self.snake_direction = (1, 0)
        elif self.snake_position[0] == (41, 5):
            self.snake_direction = (0, 1)
        elif self.snake_position[0] == (41, 10):
            self.snake_direction = (-1, 0)
        elif self.snake_position[0] == (40, 10):
            self.snake_direction = (0, 1)
        elif self.snake_position[0] == (40, 15):
            self.snake_position.append(self.snake_position[len(self.snake_position) - 1])
            self.score += 1
            self.apple_position = (10, 10)
        elif self.snake_position[0] == (40, 20):
            self.snake_direction = (-1, 0)
        elif self.snake_position[0] == (-30, 20):
            self.score = 0
            self.snake_position = [(55, 20), (56, 20), (57, 20), (58, 20), (59, 20)]

        self.clear_map(self.map)

        self.add_snake_position(self.map_size, self.snake_position)
        self.add_apple_position(self.map_size, self.apple_position)

        self.draw_map_elements(window)
        self.draw_score(window)

    def reset_game(self):
        self.end_game = False
        self.score = 0
        self.snake_position = [(40, 20), (41, 20), (41, 21), (41, 22), (41, 23), (42, 23)]
        self.apple_position = (10, 10)
        self.snake_direction = (-1, 0)

w = Window(screen_resolution=(1272, 720))
snake_game = Snake_Game()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            if w.home_menu == False:
                snake_game.key_pressed_log = pg.key.name(event.key)
                if snake_game.key_pressed == False:
                    snake_game.snake_change_direction(pg.key.name(event.key))
                    snake_game.key_pressed = True
            if pg.key.name(event.key) == 'escape':
                w.pause_menu = w.pause_menu == False

    # Mouse Info ###################################################################################
    mouse_position  = pg.mouse.get_pos()
    mouse_input = pg.mouse.get_pressed()
    mouse_click = w.mouse_has_clicked(mouse_input)
    w.mouse = (mouse_position, mouse_input, mouse_click)

    # Home Screen ##################################################################################
    w.clear_window('black')

    if w.home_menu == True:
        # Home Screen Animation ####################################################################
        snake_game.home_screen_animation(w.window)

        # Home Screen Menu #########################################################################
        button_action = w.home_screen([('Start', 'green', 'gray')])

        if button_action == 'Start':
            w.home_menu = False
            snake_game.snake_position = [(40, 20), (41, 20), (41, 21), (41, 22), (41, 23), (42, 23)]
            snake_game.snake_direction = (-1, 0)
            snake_game.sort_apple_position()
    else:
        # Game #####################################################################################
        if w.pause_menu == False and snake_game.countdown == -1 and snake_game.end_game == False:
            snake_game.update_snake_position(snake_game.snake_position)

        snake_game.clear_map(snake_game.map)
        snake_game.add_snake_position(snake_game.map_size, snake_game.snake_position)
        snake_game.add_apple_position(snake_game.map_size, snake_game.apple_position)
        snake_game.draw_map_elements(w.window)
        snake_game.draw_score(w.window)
        snake_game.snake_get_apple()
        snake_game.end_of_game()

        if w.pause_menu == False and snake_game.countdown >= 0 and snake_game.end_game == False:
            snake_game.game_start_countdown(w.window)

        if snake_game.end_game == True:
            snake_game.draw_end_game(w.window)

        # Pause Screen #############################################################################
        if w.pause_menu == True:
            button_action = w.pause_screen([('Home Menu', 'green'), ('Restart', 'blue light 2'), ('Quit Game', 'red')], button_layout=(3, 3))
            snake_game.countdown = 3
            if button_action == 'Home Menu':
                w.pause_menu = False
                w.home_menu = True
                snake_game.reset_game()
            elif button_action == 'Restart':
                w.pause_menu = False
                snake_game.reset_game()
            elif button_action == 'Quit Game':
                pg.quit()
                quit()

    w.last_click_status = mouse_input

    pg.display.update()
    w.fps(30)
    snake_game.key_pressed = False
    snake_game.snake_change_direction(snake_game.key_pressed_log)
