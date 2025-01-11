from Bytes_Universe_Game_Engine_V2 import Window
import pygame as pg



class TicTacToe:
    def __init__(self):
        # Game Colors
        self.color = {
            'black':      (  0,   0,   0),
            'white':      (255, 255, 255),
            'red':        (255,   0,   0),
            'green':      (  0, 255,   0),
            'blue':       (  0,   0, 255),
            'light blue': (200, 200, 255)
        }

        # Init score font
        pg.font.init()
        self.font = pg.font.SysFont("Courier New", 50, bold=True)

        self.offset = 50
        self.map = [['', '', ''],
                    ['', '', ''],
                    ['', '', '']]
        self.turn = 'x'
        self.score = [0, 0]
        self.end_game = False
        self.count_end_game = 0

    def board(self, window):
        pg.draw.line(window, self.color['black'], (self.offset + 200, self.offset), (self.offset + 200, self.offset + 600), 9)
        pg.draw.line(window, self.color['black'], (self.offset + 400, self.offset), (self.offset + 400, self.offset + 600), 9)
        pg.draw.line(window, self.color['black'], (self.offset, self.offset + 200), (self.offset + 600, self.offset + 200), 9)
        pg.draw.line(window, self.color['black'], (self.offset, self.offset + 400), (self.offset + 600, self.offset + 400), 9)

    def scoreboard(self, window):
        # Draw X
        pg.draw.line(window, self.color['red'], (700, 60), (750, 110), 9)
        pg.draw.line(window, self.color['red'], (750, 60), (700, 110), 9)

        # Draw O
        pg.draw.circle(window, self.color['blue'], (725, 175), 25, 9)

        # Draw x Points
        score_x = self.font.render(str(self.score[0]), True, self.color['black'])
        window.blit(score_x, (775, 60))

        # Draw o Points
        score_o = self.font.render(str(self.score[1]), True, self.color['black'])
        window.blit(score_o, (775, 150))

    def board_hover(self, window, mouse):
        for y in range(3):
            for x in range(3):
                if mouse[0][0] >= self.offset + (x * 200) and mouse[0][0] < self.offset + (x * 200) + 200 and \
                    mouse[0][1] >= self.offset + (y * 200) and mouse[0][1] < self.offset + (y * 200) + 200:
                    pg.draw.rect(window, self.color['light blue'], (self.offset + (x * 200), self.offset + (y * 200), 200, 200))

    def click_event(self, mouse):
        for y in range(3):
            for x in range(3):
                if mouse[0][0] >= self.offset + (x * 200) and mouse[0][0] < self.offset + (x * 200) + 200 and \
                    mouse[0][1] >= self.offset + (y * 200) and mouse[0][1] < self.offset + (y * 200) + 200:
                    if mouse[2][0] == True and self.map[y][x] == '' and self.end_game == False:
                        self.map[y][x] = self.turn
                        self.change_turn()

    def change_turn(self):
        if self.turn == 'x':
            self.turn = 'o'
        else:
            self.turn = 'x'

    def draw_x_and_o (self, window):
        for y in range(3):
            for x in range(3):
                if self.map[y][x] == 'x':
                    pg.draw.line(window, self.color['red'], (self.offset + (x * 200) + 50, self.offset + (y * 200) + 50), \
                                                            (self.offset + (x * 200) + 150, self.offset + (y * 200) + 150), 16)
                    pg.draw.line(window, self.color['red'], (self.offset + (x * 200) + 150, self.offset + (y * 200) + 50), \
                                                            (self.offset + (x * 200) + 50, self.offset + (y * 200) + 150), 16)
                elif self.map[y][x] == 'o':
                    pg.draw.circle(window, self.color['blue'], (self.offset + (x * 200) + 100, self.offset + (y * 200) + 100), 50, 16)

    def draw_win_line(self, window):
        if self.map[0][0] == self.map[0][1] and self.map[0][1] == self.map[0][2] and self.map[0][0] != '':
            pg.draw.line(window, self.color['green'], (self.offset + 25, self.offset + 100), (self.offset + 575, self.offset + 100), 9)
            self.add_point(self.map[0][0])
        if self.map[1][0] == self.map[1][1] and self.map[1][1] == self.map[1][2] and self.map[1][0] != '':
            pg.draw.line(window, self.color['green'], (self.offset + 25, self.offset + 300), (self.offset + 575, self.offset + 300), 9)
            self.add_point(self.map[1][0])
        if self.map[2][0] == self.map[2][1] and self.map[2][1] == self.map[2][2] and self.map[2][0] != '':
            pg.draw.line(window, self.color['green'], (self.offset + 25, self.offset + 500), (self.offset + 575, self.offset + 500), 9)
            self.add_point(self.map[2][0])
        if self.map[0][0] == self.map[1][0] and self.map[1][0] == self.map[2][0] and self.map[0][0] != '':
            pg.draw.line(window, self.color['green'], (self.offset + 100, self.offset + 25), (self.offset + 100, self.offset + 575), 9)
            self.add_point(self.map[0][0])
        if self.map[0][1] == self.map[1][1] and self.map[1][1] == self.map[2][1] and self.map[0][1] != '':
            pg.draw.line(window, self.color['green'], (self.offset + 300, self.offset + 25), (self.offset + 300, self.offset + 575), 9)
            self.add_point(self.map[0][1])
        if self.map[0][2] == self.map[1][2] and self.map[1][2] == self.map[2][2] and self.map[0][2] != '':
            pg.draw.line(window, self.color['green'], (self.offset + 500, self.offset + 25), (self.offset + 500, self.offset + 575), 9)
            self.add_point(self.map[0][2])
        if self.map[0][0] == self.map[1][1] and self.map[1][1] == self.map[2][2] and self.map[0][0] != '':
            pg.draw.line(window, self.color['green'], (self.offset + 25, self.offset + 25), (self.offset + 575, self.offset + 575), 9)
            self.add_point(self.map[0][0])
        if self.map[0][2] == self.map[1][1] and self.map[1][1] == self.map[2][0] and self.map[0][2] != '':
            pg.draw.line(window, self.color['green'], (self.offset + 575, self.offset + 25), (self.offset + 25, self.offset + 575), 9)
            self.add_point(self.map[0][2])

    def add_point(self, player):
        if self.end_game == False:
            if player == 'x':
                self.score[0] += 1
            else:
                self.score[1] += 1
            self.end_game = True

    def new_game(self):
        if self.end_game == True:
            self.map = [['', '', ''], ['', '', ''], ['', '', '']]
            self.turn = 'x'
            self.end_game = False
            self.count_end_game = 0

    def reset_game(self):
        self.map = [['', '', ''], ['', '', ''], ['', '', '']]
        self.turn = 'x'
        self.score = [0, 0]
        self.end_game = False
        self.count_end_game = 0

    def check_end_game(self):
        self.count_end_game = 0
        for y in range(3):
            for x in range(3):
                if self.map[y][x] != '':
                    self.count_end_game += 1

        if self.count_end_game == 9:
            self.end_game = True

w = Window(screen_resolution=(900, 700), color='white', window_title='Tic Tac Toe')
tic_tac_toe = TicTacToe()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            if pg.key.name(event.key) == 'escape':
                w.pause_menu = w.pause_menu == False

    # Mouse Info ###################################################################################
    mouse_position  = pg.mouse.get_pos()
    mouse_input = pg.mouse.get_pressed()
    mouse_click = w.mouse_has_clicked(mouse_input)
    w.mouse = (mouse_position, mouse_input, mouse_click)


    # Game #####################################################################################
    w.clear_window('white')
    tic_tac_toe.board_hover(w.window, w.mouse)
    tic_tac_toe.click_event(w.mouse)
    tic_tac_toe.board(w.window)
    tic_tac_toe.scoreboard(w.window)
    tic_tac_toe.draw_x_and_o (w.window)
    tic_tac_toe.draw_win_line(w.window)
    tic_tac_toe.check_end_game()
    button_new_game = w.botao((675, 225), (200, 75), w.colors['green'], 'New Game', w.mouse)
    button_reset = w.botao((675, 325), (200, 75), w.colors['orange'], 'Reset', w.mouse)

    if button_new_game == 'New Game':
        tic_tac_toe.new_game()
    if button_reset == 'Reset':
        tic_tac_toe.reset_game()

    # Pause Screen #############################################################################
    if w.pause_menu == True:
        button_action = w.pause_screen([('Quit Game', 'red')], button_layout=(1, 1))
        if button_action == 'Quit Game':
            pg.quit()
            quit()

    w.last_click_status = mouse_input

    pg.display.update()
