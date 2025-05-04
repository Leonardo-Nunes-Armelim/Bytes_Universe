import pygame as pg
import time


class Flow:
    def __init__(self, scale):
        self.white        = (255, 255, 255)
        self.gray         = (100, 100, 100)
        self.black        = (  0,   0,   0)
        self.red          = (255,   0,   0) # 0 5x5
        self.yellow       = (235, 235,   3) # 1 5x5
        self.green        = (  0, 140,   0) # 2 5x5
        self.blue         = ( 15,  40, 250) # 3 5x5
        self.orange       = (250, 135,   0) # 4 5x5
        self.light_blue   = (  0, 255, 255) # 5 6x6
        self.pink         = (255,  10, 200) # 6 9x9
        self.purple       = (125,   0, 125) # 7 9x9
        self.brown        = (165,  40,  45) # 8 9x9

        self.window = pg.display.set_mode((scale * 8, scale * 10))

        pg.font.init()
        self.font = pg.font.SysFont("Courier New", int(scale / 2), bold=True)

        self.clock = pg.time.Clock()

        # Mouse variables
        self.last_click_status = (False, False, False)

        self.scale = scale

        self.drawing_in_progress = False
        self.selected_color = ''
        self.steps = 0

        self.red_path        = [] # 0 5x5
        self.yellow_path     = [] # 1 5x5
        self.green_path      = [] # 2 5x5
        self.blue_path       = [] # 3 5x5
        self.orange_path     = [] # 4 5x5
        self.light_blue_path = [] # 5 6x6
        self.pink_path       = [] # 6 9x9
        self.purple_path     = [] # 7 9x9
        self.brown_path      = [] # 8 9x9

        self.level = 1

        self.levels = {
            '1': [['0',' ','2',' ','1'],
                  [' ',' ','3',' ','4'],
                  [' ',' ',' ',' ',' '],
                  [' ','2',' ','1',' '],
                  [' ','0','3','4',' ']],

            '2': [['2','1','5',' ','0','3'],
                  [' ',' ',' ',' ','4',' '],
                  [' ',' ','5',' ',' ',' '],
                  [' ',' ','0',' ',' ',' '],
                  ['2',' ','4',' ',' ',' '],
                  ['1',' ','3',' ',' ',' ']],

            '3': [[' ',' ',' ',' ',' ',' ','3'],
                  [' ',' ',' ',' ',' ','4','0'],
                  [' ','4',' ',' ',' ',' ',' '],
                  [' ',' ',' ','2','5',' ',' '],
                  [' ',' ','2',' ','1',' ',' '],
                  [' ',' ',' ',' ','0','1',' '],
                  [' ',' ',' ',' ',' ','3','5']],

            '4': [[' ',' ',' ',' ','0',' ',' ',' '],
                  [' ',' ',' ',' ','5',' ','2','1'],
                  [' ',' ',' ',' ','2','1',' ','5'],
                  [' ',' ',' ','4','3',' ',' ',' '],
                  [' ',' ',' ',' ','4',' ',' ',' '],
                  [' ',' ',' ',' ','3',' ',' ',' '],
                  [' ',' ',' ',' ',' ',' ',' ',' '],
                  [' ','0',' ',' ',' ',' ',' ',' ']],

            '5': [[' ',' ',' ',' ',' ',' ',' ',' ',' '],
                  [' ','0','5','3',' ',' ',' ',' ',' '],
                  [' ',' ',' ','5','4',' ','4','3',' '],
                  [' ',' ',' ',' ',' ',' ',' ','6',' '],
                  [' ','2',' ','2','0',' ',' ',' ',' '],
                  ['1','6',' ',' ',' ',' ',' ','8','7'],
                  [' ','7','1',' ',' ',' ',' ',' ',' '],
                  [' ','8',' ',' ',' ',' ',' ',' ',' '],
                  [' ',' ',' ',' ',' ',' ',' ',' ',' ']],

            '6': [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                  [' ',' ',' ',' ',' ',' ',' ','1',' ',' '],
                  [' ','5','1',' ',' ',' ',' ',' ','5',' '],
                  [' ','4',' ',' ',' ','2','7',' ','3',' '],
                  [' ',' ',' ',' ',' ','6',' ',' ',' ',' '],
                  [' ',' ','0','7','6',' ',' ',' ',' ',' '],
                  [' ',' ',' ',' ',' ',' ',' ',' ',' ','8'],
                  [' ','2',' ','4',' ',' ',' ',' ',' ','3'],
                  [' ','8',' ',' ',' ',' ',' ',' ',' ','0']],
        }

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
        pg.draw.rect(self.window, self.black, (0, 0, self.window.get_width(), self.window.get_height()))

    def draw_color_dots(self, x, y):
        level_size = len(self.levels[str(self.level)])
        square = self.window.get_width() / level_size

        if self.levels[str(self.level)][y][x] == '0':
            pg.draw.circle(self.window, self.red, ((x * square) + (square / 2), (y * square)  + (square / 2)), square * 0.375)
        if self.levels[str(self.level)][y][x] == '1':
            pg.draw.circle(self.window, self.yellow, ((x * square) + (square / 2), (y * square)  + (square / 2)), square * 0.375)
        if self.levels[str(self.level)][y][x] == '2':
            pg.draw.circle(self.window, self.green, ((x * square) + (square / 2), (y * square)  + (square / 2)), square * 0.375)
        if self.levels[str(self.level)][y][x] == '3':
            pg.draw.circle(self.window, self.blue, ((x * square) + (square / 2), (y * square)  + (square / 2)), square * 0.375)
        if self.levels[str(self.level)][y][x] == '4':
            pg.draw.circle(self.window, self.orange, ((x * square) + (square / 2), (y * square)  + (square / 2)), square * 0.375)
        if self.levels[str(self.level)][y][x] == '5':
            pg.draw.circle(self.window, self.light_blue, ((x * square) + (square / 2), (y * square)  + (square / 2)), square * 0.375)
        if self.levels[str(self.level)][y][x] == '6':
            pg.draw.circle(self.window, self.pink, ((x * square) + (square / 2), (y * square)  + (square / 2)), square * 0.375)
        if self.levels[str(self.level)][y][x] == '7':
            pg.draw.circle(self.window, self.purple, ((x * square) + (square / 2), (y * square)  + (square / 2)), square * 0.375)
        if self.levels[str(self.level)][y][x] == '8':
            pg.draw.circle(self.window, self.brown, ((x * square) + (square / 2), (y * square)  + (square / 2)), square * 0.375)

    def draw_color_paths_loop(self, color_path_obj, color, square):
        for cell in range(len(color_path_obj)):
            if cell < len(color_path_obj) - 1 and len(color_path_obj) > 1:
                start_x = (color_path_obj[cell][0]   * square) + (square / 2)
                start_y = (color_path_obj[cell][1]   * square) + (square / 2)
                end_x   = (color_path_obj[cell+1][0] * square) + (square / 2)
                end_y   = (color_path_obj[cell+1][1] * square) + (square / 2)
                pg.draw.line(self.window, color, (start_x, start_y), (end_x, end_y), int(square * 0.35))
                pg.draw.circle(self.window, color, (end_x, end_y), int(square * 0.35 / 2) - 1)

    def draw_color_paths(self):
        level_size = len(self.levels[str(self.level)])
        square = self.window.get_width() / level_size

        self.draw_color_paths_loop(self.red_path,        self.red,        square)
        self.draw_color_paths_loop(self.yellow_path,     self.yellow,     square)
        self.draw_color_paths_loop(self.green_path,      self.green,      square)
        self.draw_color_paths_loop(self.blue_path,       self.blue,       square)
        self.draw_color_paths_loop(self.orange_path,     self.orange,     square)
        self.draw_color_paths_loop(self.light_blue_path, self.light_blue, square)
        self.draw_color_paths_loop(self.pink_path,       self.pink,       square)
        self.draw_color_paths_loop(self.purple_path,     self.purple,     square)
        self.draw_color_paths_loop(self.brown_path,      self.brown,      square)

    def check_complete_flow(self, color_code, color_path):
        flow_dots = []
        for y in range(len(self.levels[str(self.level)])):
            for x in range(len(self.levels[str(self.level)][0])):
                if self.levels[str(self.level)][y][x] == color_code:
                    flow_dots.append([x, y])
        if len(flow_dots) == 2 and len(color_path) > 2:
            if flow_dots[0] in color_path and flow_dots[-1] in color_path:
                return True
        else:
            return False

    def get_complete_flows(self):
        complete_flows = 0
        if self.check_complete_flow('0', self.red_path):
            complete_flows += 1
        if self.check_complete_flow('1', self.yellow_path):
            complete_flows += 1
        if self.check_complete_flow('2', self.green_path):
            complete_flows += 1
        if self.check_complete_flow('3', self.blue_path):
            complete_flows += 1
        if self.check_complete_flow('4', self.orange_path):
            complete_flows += 1
        if self.check_complete_flow('5', self.light_blue_path):
            complete_flows += 1
        if self.check_complete_flow('6', self.pink_path):
            complete_flows += 1
        if self.check_complete_flow('7', self.purple_path):
            complete_flows += 1
        if self.check_complete_flow('8', self.brown_path):
            complete_flows += 1

        return complete_flows

    def get_flows_quantity(self):
        count = 0
        for y in range(len(self.levels[str(self.level)])):
            for x in range(len(self.levels[str(self.level)][0])):
                if self.levels[str(self.level)][y][x] != ' ':
                    count += 1

        return int(count / 2)

    def add_step(self, color_code):
        if self.selected_color == 'red' and color_code != '0':
            self.steps += 1
        elif self.selected_color == 'yellow' and color_code != '1':
            self.steps += 1
        elif self.selected_color == 'green' and color_code != '2':
            self.steps += 1
        elif self.selected_color == 'blue' and color_code != '3':
            self.steps += 1
        elif self.selected_color == 'orange' and color_code != '4':
            self.steps += 1
        elif self.selected_color == 'light_blue' and color_code != '5':
            self.steps += 1
        elif self.selected_color == 'pink' and color_code != '6':
            self.steps += 1
        elif self.selected_color == 'purple' and color_code != '7':
            self.steps += 1
        elif self.selected_color == 'brown' and color_code != '8':
            self.steps += 1
        elif self.selected_color == '':
            self.steps += 1

    def get_completeness_of_flows(self):
        squares_quantity_in_level = len(self.levels[str(self.level)]) ** 2
        count_of_filled_squares = 0
        count_of_filled_squares += len(self.red_path)
        count_of_filled_squares += len(self.yellow_path)
        count_of_filled_squares += len(self.green_path)
        count_of_filled_squares += len(self.blue_path)
        count_of_filled_squares += len(self.orange_path)
        count_of_filled_squares += len(self.light_blue_path)
        count_of_filled_squares += len(self.pink_path)
        count_of_filled_squares += len(self.purple_path)
        count_of_filled_squares += len(self.brown_path)

        percentage = (count_of_filled_squares / squares_quantity_in_level) * 100

        rounded = round(percentage, 1)
        if rounded.is_integer():
            return int(rounded)
        else:
            return rounded

    def game_info(self):
        complete_flows = self.get_complete_flows()
        flows_count = self.get_flows_quantity()
        completeness = self.get_completeness_of_flows()
        level_size = len(self.levels[str(self.level)])
        text_1 = self.font.render(f'Level: {str(self.level)} | Fluxos: {complete_flows}/{flows_count}', 1, self.white)
        text_2 = self.font.render(f'Passos: {self.steps} | Melhor: {flows_count}', 1, self.white)
        text_3 = self.font.render(f'{level_size}x{level_size} | Canos: {completeness}%', 1, self.white)
        text_1_x = (self.window.get_width() / 2) - (text_1.get_width() / 2)
        text_2_x = (self.window.get_width() / 2) - (text_2.get_width() / 2)
        text_3_x = (self.window.get_width() / 2) - (text_3.get_width() / 2)
        self.window.blit(text_1, (text_1_x, (self.scale) * 8.1 ))
        self.window.blit(text_2, (text_2_x, (self.scale) * 8.75 ))
        self.window.blit(text_3, (text_3_x, (self.scale) * 9.3 ))

    def board(self):
        level_size = len(self.levels[str(self.level)])
        square = self.window.get_width() / level_size
        for y in range(len(self.levels[str(self.level)])):
            for x in range(len(self.levels[str(self.level)][0])):
                # Grid
                pg.draw.rect(self.window, self.gray, (x * square, y * square, square + 1, square + 1), 1)
                # Dots
                self.draw_color_dots(x, y)

        # Paths
        self.draw_color_paths()
        # Game info
        self.game_info()

    def get_cell_index(self, mouse):
        level_size = len(self.levels[str(self.level)])
        square = self.window.get_width() / level_size

        mouse_x = mouse[0][0]
        mouse_y = mouse[0][1]

        cell_index = [int(mouse_x // square), int(mouse_y // square)]

        if cell_index[0] > (level_size - 1):
            cell_index[0] = level_size - 1
        if cell_index[1] > (level_size - 1):
            cell_index[1] = level_size - 1
        if cell_index[0] < 0:
            cell_index[0] = 0
        if cell_index[1] < 0:
            cell_index[1] = 0

        return cell_index

    def get_color_path(self, position):
        if position in self.red_path:
            return self.red_path
        elif position in self.yellow_path:
            return self.yellow_path
        elif position in self.green_path:
            return self.green_path
        elif position in self.blue_path:
            return self.blue_path
        elif position in self.orange_path:
            return self.orange_path
        elif position in self.light_blue_path:
            return self.light_blue_path
        elif position in self.pink_path:
            return self.pink_path
        elif position in self.purple_path:
            return self.purple_path
        elif position in self.brown_path:
            return self.brown_path
        else:
            return None

    def removing_overlapping_paths(self, position, path):
        while path:
            if path[-1] == position:
                path.pop()
                return path
            else:
                path.pop()

    def first_color_click(self, cell_index, color):
        if color == 'red':
            self.red_path = []
            self.red_path.append(cell_index)
            self.selected_color = 'red'
            self.drawing_in_progress = True
            return self.red_path
        elif color == 'yellow':
            self.yellow_path = []
            self.yellow_path.append(cell_index)
            self.selected_color = 'yellow'
            self.drawing_in_progress = True
            return self.yellow_path
        elif color == 'green':
            self.green_path = []
            self.green_path.append(cell_index)
            self.selected_color = 'green'
            self.drawing_in_progress = True
            return self.green_path
        elif color == 'blue':
            self.blue_path = []
            self.blue_path.append(cell_index)
            self.selected_color = 'blue'
            self.drawing_in_progress = True
            return self.blue_path
        elif color == 'orange':
            self.orange_path = []
            self.orange_path.append(cell_index)
            self.selected_color = 'orange'
            self.drawing_in_progress = True
            return self.orange_path
        elif color == 'light_blue':
            self.light_blue_path = []
            self.light_blue_path.append(cell_index)
            self.selected_color = 'light_blue'
            self.drawing_in_progress = True
            return self.light_blue_path
        elif color == 'pink':
            self.pink_path = []
            self.pink_path.append(cell_index)
            self.selected_color = 'pink'
            self.drawing_in_progress = True
            return self.pink_path
        elif color == 'purple':
            self.purple_path = []
            self.purple_path.append(cell_index)
            self.selected_color = 'purple'
            self.drawing_in_progress = True
            return self.purple_path
        elif color == 'brown':
            self.brown_path = []
            self.brown_path.append(cell_index)
            self.selected_color = 'brown'
            self.drawing_in_progress = True
            return self.brown_path

    def continue_color_click(self, color_code):
        if color_code == '0':
            self.selected_color = 'red'
            self.drawing_in_progress = True
            return self.red_path
        elif color_code == '1':
            self.selected_color = 'yellow'
            self.drawing_in_progress = True
            return self.yellow_path
        elif color_code == '2':
            self.selected_color = 'green'
            self.drawing_in_progress = True
            return self.green_path
        elif color_code == '3':
            self.selected_color = 'blue'
            self.drawing_in_progress = True
            return self.blue_path
        elif color_code == '4':
            self.selected_color = 'orange'
            self.drawing_in_progress = True
            return self.orange_path
        elif color_code == '5':
            self.selected_color = 'light_blue'
            self.drawing_in_progress = True
            return self.light_blue_path
        elif color_code == '6':
            self.selected_color = 'pink'
            self.drawing_in_progress = True
            return self.pink_path
        elif color_code == '7':
            self.selected_color = 'purple'
            self.drawing_in_progress = True
            return self.purple_path
        elif color_code == '8':
            self.selected_color = 'brown'
            self.drawing_in_progress = True
            return self.brown_path

    def updating_cells_to_the_color_path(self, color_code, color_path_obj, cell_index, color_path):
        if self.levels[str(self.level)][cell_index[1]][cell_index[0]] != color_code and self.levels[str(self.level)][cell_index[1]][cell_index[0]] != ' ':
            self.drawing_in_progress = False
        elif self.levels[str(self.level)][cell_index[1]][cell_index[0]] == color_code and cell_index != color_path_obj[0]:
            color_path_obj.append(cell_index)
            self.drawing_in_progress = False
        elif self.levels[str(self.level)][cell_index[1]][cell_index[0]] == color_code and cell_index == color_path_obj[0] and len(color_path_obj) > 1:
            color_path_obj = []
            color_path_obj.append(cell_index)
        elif color_path == None:
            color_path_obj.append(cell_index)
        else:
            self.removing_overlapping_paths(cell_index, color_path)
            color_path_obj.append(cell_index)

    def adding_cells_to_the_color_path(self, mouse):
        if self.drawing_in_progress and mouse[1][0] == False:
            self.drawing_in_progress = False

        cell_index = self.get_cell_index(mouse)
        color_path = self.get_color_path(cell_index)

        if mouse[2][0]:
            if self.levels[str(self.level)][cell_index[1]][cell_index[0]] == '0':
                self.add_step('0')
                color_path = self.first_color_click(cell_index, 'red')
            elif self.levels[str(self.level)][cell_index[1]][cell_index[0]] == '1':
                self.add_step('1')
                color_path = self.first_color_click(cell_index, 'yellow')
            elif self.levels[str(self.level)][cell_index[1]][cell_index[0]] == '2':
                self.add_step('2')
                color_path = self.first_color_click(cell_index, 'green')
            elif self.levels[str(self.level)][cell_index[1]][cell_index[0]] == '3':
                self.add_step('3')
                color_path = self.first_color_click(cell_index, 'blue')
            elif self.levels[str(self.level)][cell_index[1]][cell_index[0]] == '4':
                self.add_step('4')
                color_path = self.first_color_click(cell_index, 'orange')
            elif self.levels[str(self.level)][cell_index[1]][cell_index[0]] == '5':
                self.add_step('5')
                color_path = self.first_color_click(cell_index, 'light_blue')
            elif self.levels[str(self.level)][cell_index[1]][cell_index[0]] == '6':
                self.add_step('6')
                color_path = self.first_color_click(cell_index, 'pink')
            elif self.levels[str(self.level)][cell_index[1]][cell_index[0]] == '7':
                self.add_step('7')
                color_path = self.first_color_click(cell_index, 'purple')
            elif self.levels[str(self.level)][cell_index[1]][cell_index[0]] == '8':
                self.add_step('8')
                color_path = self.first_color_click(cell_index, 'brown')

        if mouse[2][0] and color_path != None:
            color_code = self.levels[str(self.level)][color_path[0][1]][color_path[0][0]]
            self.add_step(color_code)
            color_path = self.continue_color_click(color_code)

        if self.drawing_in_progress and self.selected_color == 'red':
            self.updating_cells_to_the_color_path('0', self.red_path, cell_index, color_path)
        elif self.drawing_in_progress and self.selected_color == 'yellow':
            self.updating_cells_to_the_color_path('1', self.yellow_path, cell_index, color_path)
        elif self.drawing_in_progress and self.selected_color == 'green':
            self.updating_cells_to_the_color_path('2', self.green_path, cell_index, color_path)
        elif self.drawing_in_progress and self.selected_color == 'blue':
            self.updating_cells_to_the_color_path('3', self.blue_path, cell_index, color_path)
        elif self.drawing_in_progress and self.selected_color == 'orange':
            self.updating_cells_to_the_color_path('4', self.orange_path, cell_index, color_path)
        elif self.drawing_in_progress and self.selected_color == 'light_blue':
            self.updating_cells_to_the_color_path('5', self.light_blue_path, cell_index, color_path)
        elif self.drawing_in_progress and self.selected_color == 'pink':
            self.updating_cells_to_the_color_path('6', self.pink_path, cell_index, color_path)
        elif self.drawing_in_progress and self.selected_color == 'purple':
            self.updating_cells_to_the_color_path('7', self.purple_path, cell_index, color_path)
        elif self.drawing_in_progress and self.selected_color == 'brown':
            self.updating_cells_to_the_color_path('8', self.brown_path, cell_index, color_path)

    def next_level(self):
        self.drawing_in_progress = False
        self.selected_color = ''
        self.steps = 0

        self.red_path        = []
        self.yellow_path     = []
        self.green_path      = []
        self.blue_path       = []
        self.orange_path     = []
        self.light_blue_path = []
        self.pink_path       = []
        self.purple_path     = []
        self.brown_path      = []

        self.level += 1

        if str(self.level) not in self.levels:
            self.level = 1

    def end_game(self):
        complete_flows = self.get_complete_flows()
        flows_count = self.get_flows_quantity()
        if complete_flows == flows_count:
            if self.steps == flows_count:
                text = self.font.render('Excelente', 1, self.black)
            else:
                text = self.font.render('Da para melhorar', 1, self.black)

            text_x = (self.window.get_width() / 2) - (text.get_width() / 2)
            text_y = (self.window.get_height() / 2) - (text.get_height() / 2)
            text_width = text.get_width()
            text_height = text.get_height()
            padding = 10
            pg.draw.rect(self.window, self.white, (text_x - padding, text_y - padding, text_width + (padding * 2), text_height + (padding * 2)))
            pg.draw.rect(self.window, self.gray, (text_x - padding, text_y - padding, text_width + (padding * 2), text_height + (padding * 2)), 5)
            self.window.blit(text, (text_x, text_y))
            pg.display.update()

            time.sleep(3)

            self.next_level()

jogo = Flow(80)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
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
    jogo.adding_cells_to_the_color_path(mouse)
    jogo.board()
    jogo.end_game()


    jogo.last_click_status = mouse_input

    pg.display.update()
