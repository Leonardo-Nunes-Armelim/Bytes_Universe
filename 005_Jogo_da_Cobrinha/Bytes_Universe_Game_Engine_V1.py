import pygame as pg
import time

# Default game colors
white   = (255, 255, 255)
gray    = (150, 150, 150)
black   = (  0,   0,   0)
red     = (255,   0,   0)
green   = (  0, 255,   0)
blue    = (  0,   0, 255)

class Window:
    def __init__(self, screen_resolution='HD', window_title='New Game', icon=None, fps=60):
        # Window valiables
        self.resolutions = {
            'HD': (1280, 720),
            'FHD': (1920, 1080)
        }
        try:
            self.window = pg.display.set_mode(self.resolutions[screen_resolution])
        except:
            self.window = pg.display.set_mode(screen_resolution)
        # pg.display.set_caption(title=self.window_title, icontitle=self.icon)

        # Mouse Infos
        self.mouse_0 = {'x': None, 'y': None, 'left button': None, 'clicked': False}
        self.mouse = ((0, 0), (False, False, False), (False, False, False))

        # Others variables
        pg.font.init()
        self.fonte = pg.font.SysFont("Courier New", 50, bold=True)
        self.fonte_rb = pg.font.SysFont("Courier New", 30, bold=True)

        self.last_click_status = (False, False, False)

        self.home_menu = True
        self.pause_menu = False
        self.game_difficulty = 0

        # Default colors
        self.colors = {
            'white':            (255, 255, 255),
            'gray':             (150, 150, 150),
            'black':            (  0,   0,   0),
            'red':              (255,   0,   0),
            'red light 1':      ( 50, 100,  50),
            'red light 2':      (100, 150, 100),
            'red light 3':      (150, 200, 150),
            'green':            (  0, 255,   0),
            'green light 1':    ( 50, 255,  50),
            'green light 2':    (100, 255, 100),
            'green light 3':    (150, 255, 150),
            'blue':             (  0,   0, 255),
            'blue light 1':     ( 50,  50, 255),
            'blue light 2':     (100, 100, 255),
            'blue light 3':     (150, 150, 255)
        }

    # times ########################################################################################

    def fps(self, fps=60):
        time.sleep(1 / fps)

    # Infos ########################################################################################

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

            self.last_click_status
            # last_click_status[2] = input[2]

            return (left_button, center_button, right_button)

    # Draw #########################################################################################

    def clear_window(self, color, alpha=128):
        pg.draw.rect(self.window, color, (0, 0, self.window.get_width(), self.window.get_height()))

    def transparent_background(self, color):
        surface = pg.Surface((self.window.get_width(), self.window.get_height()))
        surface.set_alpha(128)
        surface.fill(self.colors[color])
        self.window.blit(surface, (0, 0))

    def transparent_surface(self, position_x, position_y, size_x, size_y):
        surface = pg.Surface((size_x, size_y))
        surface.set_alpha(128)
        surface.fill(white)
        self.window.blit(surface, (position_x, position_y))

    # Elements #####################################################################################

    def botao(self, position, size, background_color, text, mouse, index_of_qtd=(1, 1), border_color=black, border_width=5, font_color=black, text_size=32):
        # Logic for Button "position"
        if type(position) == tuple:
            position_x = position[0]
            position_y = position[1]
        elif type(position) == str:
            if position == 'center':
                if index_of_qtd[1] == 1:
                    position_x = (self.window.get_width() / 2) - (size[0] / 2)
                    position_y = (self.window.get_height() / 2) - (size[1] / 2)
                else:
                    position_x = self.window.get_width() / 2 - (size[0] / 2)
                    sum_btn_height = size[1] * index_of_qtd[1]
                    sum_gap_btn_height = (size[1] / 2) * (index_of_qtd[1] - 1)
                    btn_set_height = sum_btn_height + sum_gap_btn_height
                    margin_y   = (self.window.get_height() - btn_set_height) / 2
                    position_y = margin_y + ((size[1] * 1.5) * (index_of_qtd[0] - 1))

        # Button "size"
        size_x = size[0]
        size_y = size[1]

        # Draw Button Background
        pg.draw.rect(self.window, background_color, (position_x, position_y, size_x, size_y))

        # Hover
        if mouse[0][0] >= position_x and mouse[0][0] <= position_x + size_x and mouse[0][1] >= position_y and mouse[0][1] <= position_y + size_y:
            position_x, position_y, size_x, size_y
            self.transparent_surface(position_x, position_y, size_x, size_y)

        # Draw Button Border
        pg.draw.rect(self.window, border_color, (position_x, position_y, size_x, size_y), border_width)

        # Draw Button Text
        fonte_botao = pg.font.SysFont("Consolas", text_size, bold=True)
        text_render = fonte_botao.render(text, True, font_color)
        text_size_x = text_render.get_width()
        text_size_y = text_render.get_height()
        text_position_x = position_x + (size_x / 2) - (text_size_x / 2)
        text_position_y = position_y + (size_y / 2) - (text_size_y / 2)
        self.window.blit(text_render, (text_position_x, text_position_y))

        if mouse[0][0] >= position_x and mouse[0][0] <= position_x + size_x and mouse[0][1] >= position_y and mouse[0][1] <= position_y + size_y and mouse[2][0] == True:
            return text
        else:
            return None

    # Home Screen ##################################################################################

    def home_screen(self, button_list, button_layout=(1, 1)):
        # button_list   = list(tuple(name, color))
        # button_layout = tuple(row, column)

        button_list_len = len(button_list)
        button_action = []

        for i in range(button_list_len):
            button_action.append(None)

        for i in range(button_list_len):
            try:
                button_action[i] = self.botao("center", (300, 100), self.colors[button_list[i][1]], button_list[i][0], self.mouse, index_of_qtd=(i + 1, button_layout[1]), border_color=self.colors[button_list[i][2]])
            except:
                button_action[i] = self.botao("center", (300, 100), self.colors[button_list[i][1]], button_list[i][0], self.mouse, index_of_qtd=(i + 1, button_layout[1]))

        for i in range(button_list_len):
            if button_action[i] != None:
                return button_action[i]

    # Pause Screen #################################################################################

    def pause_screen(self, button_list, button_layout=(1, 1)):
        # button_list   = list(tuple(name, color))
        # button_layout = tuple(row, column)

        self.transparent_background('white')

        button_list_len = len(button_list)
        button_action = []

        for i in range(button_list_len):
            button_action.append(None)

        for i in range(button_list_len):
            button_action[i] = self.botao("center", (300, 100), self.colors[button_list[i][1]], button_list[i][0], self.mouse, index_of_qtd=(i + 1, button_layout[1]))

        for i in range(button_list_len):
            if button_action[i] != None:
                return button_action[i]
