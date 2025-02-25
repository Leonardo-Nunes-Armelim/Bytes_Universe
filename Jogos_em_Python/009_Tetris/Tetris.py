import pygame as pg
import random
import time

class Tetris:
    def __init__(self, window_size):
        # Window game setup
        self.window = pg.display.set_mode((window_size * 14, window_size * 20))

        # Fonte setup
        pg.font.init()
        self.font = pg.font.SysFont("Courier New", window_size, bold=True)

        self.clock = pg.time.Clock()
        self.time = 0

        # Colors
        self.black       = (  0,   0,   0)
        self.white       = (255, 255, 255)
        self.gray        = (150, 150, 150) # color code 'x'
        self.purple      = (171,  57, 219) # color code 'p'
        self.blue        = ( 23,  31, 223) # color code 'b'
        self.light_blue  = (  3, 133, 166) # color code 'l'
        self.red         = (246,  51,  73) # color code 'r'
        self.orange      = (250, 123,  21) # color code 'o'
        self.yellow      = (245, 198,  42) # color code 'y'
        self.green       = ( 99, 209,  21) # color code 'g'

        # Mouse variables
        self.last_click_status = (False, False, False)

        # Game variables
        self.starting_first_game = True
        self.show_restart_button = True
        self.board_square = window_size
        self.next_shapes_list = ['', '', '', '']
        self.score = 0
        self.speed = 1
        self.selected_form = 'shape_1'
        self.shape_pos = [4, 0]
        self.shape_matrix = [[]]
        self.new_shape = True

        # Game shapes
        self.shape = {
            'shape_1': {
                'shape': [[1, 1],
                          [1, 1]],
                'color': self.yellow
            },
            'shape_2': {
                'shape': [[0, 1, 0],
                          [1, 1, 1]],
                'color': self.purple
            },
            'shape_3': {
                'shape': [[1, 1, 1, 1]],
                'color': self.light_blue
            },
            'shape_4': {
                'shape': [[1, 1, 0],
                          [0, 1, 1]],
                'color': self.red
            },
            'shape_5': {
                'shape': [[0, 1, 1],
                          [1, 1, 0]],
                'color': self.green
            },
            'shape_6': {
                'shape': [[1, 0, 0],
                          [1, 1, 1]],
                'color': self.blue
            },
            'shape_7': {
                'shape': [[0, 0, 1],
                          [1, 1, 1]],
                'color': self.orange
            }
        }

        self.map = [['', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', '']]

    def clear_window(self):
        pg.draw.rect(self.window, self.black, (0, 0, self.window.get_width(), self.window.get_height()))

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

    def board(self):
        # Game grid
        for y in range(20):
            for x in range(10):
                pg.draw.rect(self.window, self.gray, (self.board_square * x, self.board_square * y, self.board_square, self.board_square), 1)
        pg.draw.rect(self.window, self.white, (0, 0, self.board_square * 10, self.board_square * 20), 2)

        # Shape in game
        self.draw_shapes_in_game()

        # Next box
        self.text_box('Next', 10, 0, 4, 1, True)
        self.text_box('', 10, 1, 4, 13, False)
        self.draw_next_shapes()

        # Score box
        self.text_box('Score', 10, 14, 4, 1, True)
        self.text_box(str(self.score), 10, 15, 4, 2, False)

        # Speed box
        self.text_box('Speed', 10, 17, 4, 1, True)
        self.text_box(str(self.speed) + 'x', 10, 18, 4, 2, False)

    def text_box(self, text, x, y, width, height, background_fill):
        next_square_x = self.board_square * x
        next_square_y = self.board_square * y
        next_square_w = self.board_square * width
        next_square_h = self.board_square * height
        if background_fill:
            pg.draw.rect(self.window, self.white, (next_square_x, next_square_y, next_square_w, next_square_h))
            next_text = self.font.render(text, 1, self.black)
        else:
            pg.draw.rect(self.window, self.white, (next_square_x, next_square_y, next_square_w, next_square_h), 1)
            next_text = self.font.render(text, 1, self.white)
        next_text_w = next_text.get_width()
        next_text_h = next_text.get_height()
        blit_x = next_square_x + ((next_square_w / 2) - (next_text_w / 2))
        blit_y = next_square_y + ((next_square_h / 2) - (next_text_h / 2))
        self.window.blit(next_text, (blit_x, blit_y))

    def new_random_shape(self):
        return 'shape_' + str(random.randint(1, 7))

    def add_random_shape(self):
        for i in range(len(self.next_shapes_list)):
            if i != 0:
                self.next_shapes_list[i - 1] = self.next_shapes_list[i]
        self.next_shapes_list[-1] = self.new_random_shape()

    def init_random_shapes(self):
        for i in range(4):
            self.next_shapes_list[i] = self.new_random_shape()

    def draw_next_shapes(self):
        for i in range(len(self.next_shapes_list)):
            next_shape_code = self.next_shapes_list[i]
            next_shape_x = self.board_square * 12 - ((len(self.shape[next_shape_code]['shape'][0]) / 2) * self.board_square)
            next_shape_y = self.board_square * 3 - ((len(self.shape[next_shape_code]['shape']) / 2) * self.board_square) + (i * 3 * self.board_square)
            border_color = tuple(min(rgb + 50, 255) for rgb in self.shape[next_shape_code]['color'])
            for y in range(len(self.shape[next_shape_code]['shape'])):
                for x in range(len(self.shape[next_shape_code]['shape'][0])):
                    if self.shape[next_shape_code]['shape'][y][x] == 1:
                        pos_x = (self.board_square * x) + next_shape_x
                        pos_y = (self.board_square * y) + next_shape_y
                        pg.draw.rect(self.window, self.shape[next_shape_code]['color'], (pos_x, pos_y, self.board_square, self.board_square))
                        pg.draw.rect(self.window, border_color, (pos_x, pos_y, self.board_square, self.board_square), 1)

    def get_next_shape(self):
        self.selected_form = self.next_shapes_list[0]
        self.shape_matrix = self.shape[self.selected_form]['shape']
        self.add_random_shape()
        self.new_shape = False
        self.shape_pos = [4, 0]

    def did_shape_collide_sideways(self):
        shape_pos_x = self.shape_pos[0]
        shape_pos_y = self.shape_pos[1]
        for y in range(len(self.shape_matrix)):
            for x in range(len(self.shape_matrix[0])):
                if self.shape_matrix[y][x] == 1:
                    shape_unit_pos_x = shape_pos_x + x
                    shape_unit_pos_y = shape_pos_y + y
                    if self.map[shape_unit_pos_y][shape_unit_pos_x] == '':
                        pass
                    else:
                        return True
        return False

    def is_shape_in_the_game(self):
        shape_pos_x = self.shape_pos[0]
        for y in range(len(self.shape_matrix)):
            for x in range(len(self.shape_matrix[0])):
                if self.shape_matrix[y][x] == 1:
                    shape_unit = shape_pos_x + x
                    if shape_unit >= 0 and shape_unit <= 9:
                        pass
                    else:
                        return False
        return True

    def rotate_shape_to_the_right(self):
        # Transpose the matrix (swap rows for columns)
        transpose_matrix = list(zip(*self.shape_matrix))

        # Flip the rows of the transposed matrix to rotate it 90° to the right
        self.shape_matrix = [list(row[::-1]) for row in transpose_matrix]

    def rotate_shape_to_the_left(self):
        # Transpose the matrix (swap rows for columns)
        transpose_matrix = list(zip(*self.shape_matrix))

        # Flip the rows of the transposed matrix to rotate it 90° to the left
        self.shape_matrix = [list(row) for row in transpose_matrix[::-1]]

    def send_shape_to_end(self):
        for i in range(20):
            # Moving shape 1 down
            self.shape_pos[1] += 1
            # Check if the shape collided with something
            shape_pos_x = self.shape_pos[0]
            shape_pos_y = self.shape_pos[1]
            for y in range(len(self.shape_matrix)):
                for x in range(len(self.shape_matrix[0])):
                    if self.shape_matrix[y][x] == 1:
                        try:
                            if self.map[y + shape_pos_y][x + shape_pos_x] != '':
                                self.shape_pos[1] -= 1
                                self.lock_shape()
                                return
                        except:
                            self.shape_pos[1] -= 1
                            self.lock_shape()
                            return

    def move(self, key):
        if key == 'a' or key == 'left':
            self.shape_pos[0] -= 1
            if self.is_shape_in_the_game() == False or self.did_shape_collide_sideways():
                self.shape_pos[0] += 1
        elif key == 's' or key == 'down':
            self.shape_pos[1] += 1
        elif key == 'd' or key == 'right':
            self.shape_pos[0] += 1
            if self.is_shape_in_the_game() == False or self.did_shape_collide_sideways():
                self.shape_pos[0] -= 1
        elif key == 'q':
            self.rotate_shape_to_the_left()
            if self.is_shape_in_the_game() == False:
                self.rotate_shape_to_the_right()
        elif key == 'e':
            self.rotate_shape_to_the_right()
            if self.is_shape_in_the_game() == False:
                self.rotate_shape_to_the_left()
        elif key == 'space':
            self.send_shape_to_end()

    def get_color(self, color_code):
        if color_code == 'p':
            return self.purple
        elif color_code == 'b':
            return self.blue
        elif color_code == 'l':
            return self.light_blue
        elif color_code == 'r':
            return self.red
        elif color_code == 'o':
            return self.orange
        elif color_code == 'y':
            return self.yellow
        elif color_code == 'g':
            return self.green
        elif color_code == 'x':
            return self.gray
        else:
            return None

    def get_color_code(self, color):
        if color == self.purple:
            return 'p'
        elif color == self.blue:
            return 'b'
        elif color == self.light_blue:
            return 'l'
        elif color == self.red:
            return 'r'
        elif color == self.orange:
            return 'o'
        elif color == self.yellow:
            return 'y'
        elif color == self.green:
            return 'g'
        else:
            return None

    def draw_shapes_in_game(self):
        # Draws shapes already placed
        for y in range(20):
            for x in range(10):
                if self.map[y][x] != '':
                    color = self.get_color(self.map[y][x])
                    border_color = tuple(min(rgb + 50, 255) for rgb in color)
                    pg.draw.rect(self.window, color, (self.board_square * x, self.board_square * y, self.board_square, self.board_square))
                    pg.draw.rect(self.window, border_color, (self.board_square * x, self.board_square * y, self.board_square, self.board_square), 1)

        # Draw shape in game
        shape_pos_x = self.shape_pos[0]
        shape_pos_y = self.shape_pos[1]
        color = self.shape[self.selected_form]['color']
        border_color = tuple(min(rgb + 50, 255) for rgb in color)
        for y in range(len(self.shape_matrix)):
            for x in range(len(self.shape_matrix[0])):
                if self.shape_matrix[y][x] == 1:
                    pg.draw.rect(self.window, color, (self.board_square * (x + shape_pos_x), self.board_square * (y +shape_pos_y), self.board_square, self.board_square))
                    pg.draw.rect(self.window, border_color, (self.board_square * (x + shape_pos_x), self.board_square * (y + shape_pos_y), self.board_square, self.board_square), 1)

    def game_speed(self):
        self.speed = min(1 + (self.score // 100), 50)

    def add_point(self, rows):
        # Points from shape
        for y in range(len(self.shape_matrix)):
            for x in range(len(self.shape_matrix[0])):
                if self.shape_matrix[y][x] == 1:
                    self.score += 1
        # Points from rows
        self.score += rows * 10
        # Updating game speed
        self.game_speed()
        self.time = 0

    def lock_shape(self):
        shape_pos_x = self.shape_pos[0]
        shape_pos_y = self.shape_pos[1]
        for y in range(len(self.shape_matrix)):
            for x in range(len(self.shape_matrix[0])):
                if self.shape_matrix[y][x] == 1:
                    self.map[shape_pos_y + y][shape_pos_x + x] = self.get_color_code(self.shape[self.selected_form]['color'])
        self.get_next_shape()

        # Updating score
        completed_row_count = 0
        for y in range(20):
            row_count = 0
            for x in range(10):
                if self.map[y][x] != '':
                    row_count += 1
            if row_count == 10:
                completed_row_count += 1

        self.add_point(completed_row_count)
        if completed_row_count >= 1:
            self.remove_completed_rows()

    def game_step(self):
        # Logic for walking with the shape down in the game
        self.time += 1
        if self.time == 61 - self.speed:
            self.shape_pos[1] += 1
            self.time = 0
        # Check if the shape collided with something
        shape_pos_x = self.shape_pos[0]
        shape_pos_y = self.shape_pos[1]
        for y in range(len(self.shape_matrix)):
            for x in range(len(self.shape_matrix[0])):
                if self.shape_matrix[y][x] == 1:
                    try:
                        if self.map[y + shape_pos_y][x + shape_pos_x] != '':
                            self.shape_pos[1] -= 1
                            self.lock_shape()
                            return
                    except:
                        self.shape_pos[1] -= 1
                        self.lock_shape()
                        return

    def remove_completed_rows(self):
        # Changing color of complete lines to gray (color code 'x')
        completed_rows_list = []
        for y in range(20):
            columns = 0
            for x in range(10):
                if self.map[y][x] != '':
                    columns += 1
            if columns == 10:
                completed_rows_list.append(y)
                for x in range(10):
                    self.map[y][x] = 'x'

        # Refreshing the screen and waiting 1 second
        self.clear_window()
        self.board()
        pg.display.update()
        time.sleep(1)

        # Deleting complete line
        for row in completed_rows_list:
            for x in range(10):
               self.map[row][x] = ''

        # Moving incomplete rows down
        for rows in range(len(completed_rows_list)):
            for y in range(20):
                bottom_to_top_y = 19 - y
                columns = 0
                for x in range(10):
                    if self.map[bottom_to_top_y][x] == '':
                        columns += 1
                if columns == 10:
                    shift_y = 1
                    while bottom_to_top_y - shift_y >= 0:
                        for x in range(10):
                            self.map[bottom_to_top_y - shift_y + 1][x] = self.map[bottom_to_top_y - shift_y][x]
                        shift_y += 1

    def is_game_end(self):
        shape_pos_x = self.shape_pos[0]
        shape_pos_y = self.shape_pos[1]
        if self.show_restart_button == False:
            for y in range(len(self.shape_matrix)):
                for x in range(len(self.shape_matrix[0])):
                    if self.shape_matrix[y][x] == 1 and self.map[shape_pos_y + y][shape_pos_x + x] != '':
                        self.show_restart_button = True
                        self.shape_matrix = [[]]
                        return

    def restart_button(self, mouse):
        if self.show_restart_button:
            button_color = (0, 200, 0)
            button_width = self.window.get_width() / 2.5
            button_height = button_width / 2.5
            button_x = (self.window.get_width() / 2) - (button_width / 2)
            button_y = (self.window.get_height() / 2) - (button_height / 2)
            button_border = int(self.board_square / 5)
            if mouse[0][0] >= button_x and mouse[0][0] <= button_x + button_width and mouse[0][1] >= button_y and mouse[0][1] <= button_y + button_height:
                button_hover_color = tuple(min(rgb + 50, 255) for rgb in button_color)
                pg.draw.rect(self.window, button_hover_color, (button_x, button_y, button_width, button_height))
                if mouse[2][0]:
                    self.restart_game(True)
            else:
                pg.draw.rect(self.window, button_color, (button_x, button_y, button_width, button_height))
            pg.draw.rect(self.window, self.white, (button_x, button_y, button_width, button_height), button_border)
            text = self.font.render('Restart', 1, self.black)
            blit_x = (self.window.get_width() / 2) - (text.get_width() / 2)
            blit_y = (self.window.get_height() / 2) - (text.get_height() / 2)
            self.window.blit(text, (blit_x, blit_y))

    def restart_game(self, restart=False):
        if self.starting_first_game or restart:
            self.init_random_shapes()
            self.score = 0
            self.speed = 1
            # Cleaning map
            for y in range(20):
                for x in range(10):
                    self.map[y][x] = ''
            self.show_restart_button = False
            self.starting_first_game = False
            self.get_next_shape()


tetris = Tetris(42)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            tetris.move(pg.key.name(event.key))
            if pg.key.name(event.key) == 'escape':
                pg.quit()
                quit()

    # Mouse info
    mouse_position  = pg.mouse.get_pos()
    mouse_input = pg.mouse.get_pressed()
    mouse_click = tetris.mouse_has_clicked(mouse_input)
    mouse = (mouse_position, mouse_input, mouse_click)

    # Game
    tetris.clock.tick(60)
    tetris.clear_window()

    tetris.restart_game()

    if tetris.new_shape:
        tetris.get_next_shape()

    tetris.board()
    tetris.game_step()

    tetris.is_game_end()

    tetris.restart_button(mouse)

    tetris.last_click_status = mouse_input

    pg.display.update()
