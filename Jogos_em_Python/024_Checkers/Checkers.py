import pygame as pg


class Checkers:
    def __init__(self, scale):
        self.white       = (255, 255, 255)
        self.black       = (  0,   0,   0)
        self.gray        = ( 70,  70,  80)
        self.brown       = (190, 150, 115)
        self.brown_light = (245, 220, 190)
        self.brown_move  = (210, 170, 120)

        self.window = pg.display.set_mode((scale * 8, scale * 8))

        self.clock = pg.time.Clock()

        # Mouse variables
        self.last_click_status = (False, False, False)

        self.scale = scale
        self.click_position = None
        self.last_click_position = None
        self.last_selected_piece = ''
        self.selected_piece = ''
        self.player_turn = 'white'
        self.more_moves = False

        self.map = [[ '', 'b',  '', 'b',  '', 'b',  '', 'b'],
                    ['b',  '', 'b',  '', 'b',  '', 'b',  ''],
                    [ '', 'b',  '', 'b',  '', 'b',  '', 'b'],
                    [ '',  '',  '',  '',  '',  '',  '',  ''],
                    [ '',  '',  '',  '',  '',  '',  '',  ''],
                    ['w',  '', 'w',  '', 'w',  '', 'w',  ''],
                    [ '', 'w',  '', 'w',  '', 'w',  '', 'w'],
                    ['w',  '', 'w',  '', 'w',  '', 'w',  '']]

        self.move_map = [[ '', '',  '', '',  '', '',  '', ''],
                         [ '', '',  '', '',  '', '',  '', ''],
                         [ '', '',  '', '',  '', '',  '', ''],
                         [ '', '',  '', '',  '', '',  '', ''],
                         [ '', '',  '', '',  '', '',  '', ''],
                         [ '', '',  '', '',  '', '',  '', ''],
                         [ '', '',  '', '',  '', '',  '', ''],
                         [ '', '',  '', '',  '', '',  '', '']]

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

    def promotion(self):
        for x in range(8):
            if self.map[0][x] == 'w':
                self.map[0][x] = 'wq'
            if self.map[7][x] == 'b':
                self.map[7][x] = 'bq'

    def board(self):
        radius = int(self.scale * 0.35)
        border = int(self.scale * 0.1)
        for y in range(8):
            for x in range(8):
                if (y % 2) == 0 and (x % 2) == 0 or (y % 2) != 0 and (x % 2) != 0:
                        pg.draw.rect(self.window, self.brown_light, (x * self.scale, y * self.scale, self.scale, self.scale))
                elif (y % 2) != 0 and (x % 2) == 0 or (y % 2) == 0 and (x % 2) != 0:
                        pg.draw.rect(self.window, self.brown, ((x * self.scale, y * self.scale, self.scale, self.scale)))
                pos_x = (x * self.scale) + (self.scale / 2)
                pos_y = (y * self.scale) + (self.scale / 2)
                crown = [(pos_x, pos_y-border), (pos_x+int(border/2), pos_y), (pos_x+border, pos_y-border),
                         (pos_x+border, pos_y+border), (pos_x-border, pos_y+border), (pos_x-border, pos_y-border),
                         (pos_x-int(border/2), pos_y)]
                if self.move_map[y][x] == 'o':
                    move_x = (x * self.scale) + (self.scale / 2)
                    move_y = (y * self.scale) + (self.scale / 2)
                    pg.draw.circle(self.window, self.brown_move, (move_x, move_y), radius)
                if self.map[y][x] == 'w':
                    pg.draw.circle(self.window, self.white, (pos_x, pos_y), radius)
                    pg.draw.circle(self.window, self.black, (pos_x, pos_y), radius, border)
                elif self.map[y][x] == 'wq':
                    pg.draw.circle(self.window, self.white, (pos_x, pos_y), radius)
                    pg.draw.circle(self.window, self.black, (pos_x, pos_y), radius, border)
                    pg.draw.polygon(self.window, self.black, crown)
                elif self.map[y][x] == 'b':
                    pg.draw.circle(self.window, self.gray, (pos_x, pos_y), radius)
                    pg.draw.circle(self.window, self.black, (pos_x, pos_y), radius, border)
                elif self.map[y][x] == 'bq':
                    pg.draw.circle(self.window, self.gray, (pos_x, pos_y), radius)
                    pg.draw.circle(self.window, self.black, (pos_x, pos_y), radius, border)
                    pg.draw.polygon(self.window, self.white, crown)

    def get_piece(self, x, y):
        if x < 0 or x > 7 or y < 0 or y > 7:
            return None
        try:
            piece = self.map[y][x]
        except:
            piece = ''

        return piece

    def clear_move_map(self):
        self.move_map = [[ '', '',  '', '',  '', '',  '', ''],
                         [ '', '',  '', '',  '', '',  '', ''],
                         [ '', '',  '', '',  '', '',  '', ''],
                         [ '', '',  '', '',  '', '',  '', ''],
                         [ '', '',  '', '',  '', '',  '', ''],
                         [ '', '',  '', '',  '', '',  '', ''],
                         [ '', '',  '', '',  '', '',  '', ''],
                         [ '', '',  '', '',  '', '',  '', '']]

    def move(self):
        if self.click_position != None and self.last_click_position != None:
            x = self.click_position[0]
            y = self.click_position[1]
            last_x = self.last_click_position[0]
            last_y = self.last_click_position[1]
            if self.player_turn == 'white':
                if self.map[last_y][last_x] == 'w' or self.map[last_y][last_x] == 'wq':
                    if self.move_map[y][x] == 'o':
                        if abs(x - last_x) == 2:
                            xx = int((x - last_x) / 2)
                            yy = int((y - last_y) / 2)
                            self.map[y][x] = self.map[last_y][last_x]
                            self.map[last_y+yy][last_x+xx] = ''
                            if self.there_is_more_moves() == False:
                                self.player_turn = 'black'
                        else:
                            self.map[y][x] = self.map[last_y][last_x]
                            self.player_turn = 'black'
                        self.map[last_y][last_x] = ''
            elif self.player_turn == 'black':
                if self.map[last_y][last_x] == 'b' or self.map[last_y][last_x] == 'bq':
                    if self.move_map[y][x] == 'o':
                        if abs(x - last_x) == 2:
                            xx = int((x - last_x) / 2)
                            yy = int((y - last_y) / 2)
                            self.map[y][x] = self.map[last_y][last_x]
                            self.map[last_y+yy][last_x+xx] = ''
                            if self.there_is_more_moves() == False:
                                self.player_turn = 'white'
                        else:
                            self.map[y][x] = self.map[last_y][last_x]
                            self.player_turn = 'white'
                        self.map[last_y][last_x] = ''
        self.clear_move_map()

    def piece_direction(self, x, y):
        if self.map[y][x] == 'bq' or self.map[y][x] == 'wq':
            directions = [[-1,-1],[1,-1],[1,1],[-1,1]]
        elif self.map[y][x] == 'w':
            directions = [[-1,-1],[1,-1]]
        elif self.map[y][x] == 'b':
            directions = [[1,1],[-1,1]]
        else:
            directions = []

        return directions

    def there_is_more_moves(self):
        if self.click_position != None:
            x = self.click_position[0]
            y = self.click_position[1]
            directions = self.piece_direction(x, y)
            if self.player_turn == 'white':
                if self.map[y][x] == 'w' or self.map[y][x] == 'wq':
                    for direction in directions:
                        if self.get_piece(x+direction[0], y+direction[1]) == 'b' or self.get_piece(x+direction[0], y+direction[1]) == 'bq':
                            if self.get_piece(x+(direction[0]*2), y+(direction[1]*2)) == '':
                                self.more_moves = True
                                return True
            elif self.player_turn == 'black':
                if self.map[y][x] == 'b' or self.map[y][x] == 'bq':
                    for direction in directions:
                        if self.get_piece(x+direction[0], y+direction[1]) == 'w' or self.get_piece(x+direction[0], y+direction[1]) == 'wq':
                            if self.get_piece(x+(direction[0]*2), y+(direction[1]*2)) == '':
                                self.more_moves = True
                                return True
        self.more_moves = False
        return False

    def next_move(self):
        if self.click_position != None:
            x = self.click_position[0]
            y = self.click_position[1]
            directions = self.piece_direction(x, y)
            if self.player_turn == 'white':
                if self.map[y][x] == 'w' or self.map[y][x] == 'wq':
                    for direction in directions:
                        if self.get_piece(x+direction[0], y+direction[1]) == '' and self.more_moves == False:
                            self.move_map[y+direction[1]][x+direction[0]] = 'o'
                        elif self.get_piece(x+direction[0], y+direction[1]) == 'b' or self.get_piece(x+direction[0], y+direction[1]) == 'bq':
                            if self.get_piece(x+(direction[0]*2), y+(direction[1]*2)) == '':
                                self.move_map[y+(direction[1]*2)][x+(direction[0]*2)] = 'o'
            elif self.player_turn == 'black':
                if self.map[y][x] == 'b' or self.map[y][x] == 'bq':
                    for direction in directions:
                        if self.get_piece(x+direction[0], y+direction[1]) == '' and self.more_moves == False:
                            self.move_map[y+direction[1]][x+direction[0]] = 'o'
                        elif self.get_piece(x+direction[0], y+direction[1]) == 'w' or self.get_piece(x+direction[0], y+direction[1]) == 'wq':
                            if self.get_piece(x+(direction[0]*2), y+(direction[1]*2)) == '':
                                self.move_map[y+(direction[1]*2)][x+(direction[0]*2)] = 'o'

    def mouse_actions(self, mouse):
        if mouse[2][0] == True:
            for y in range(8):
                for x in range(8):
                    if mouse[0][0] >= (x * 100) and mouse[0][0] <= (x * 100) + 100 and mouse[0][1] >= (y * 100) and mouse[0][1] <= (y * 100) + 100:
                        if self.click_position != None:
                            last_x = self.click_position[0]
                            last_y = self.click_position[1]
                            self.last_click_position = [last_x, last_y]
                            self.last_selected_piece = self.map[last_y][last_x]
                        self.selected_piece = self.map[y][x]
                        self.click_position = [x, y]

    def restart(self):
        self.click_position = None
        self.last_click_position = None
        self.last_selected_piece = ''
        self.selected_piece = ''
        self.player_turn = 'white'
        self.more_moves = False

        self.map = [[ '', 'b',  '', 'b',  '', 'b',  '', 'b'],
                    ['b',  '', 'b',  '', 'b',  '', 'b',  ''],
                    [ '', 'b',  '', 'b',  '', 'b',  '', 'b'],
                    [ '',  '',  '',  '',  '',  '',  '',  ''],
                    [ '',  '',  '',  '',  '',  '',  '',  ''],
                    ['w',  '', 'w',  '', 'w',  '', 'w',  ''],
                    [ '', 'w',  '', 'w',  '', 'w',  '', 'w'],
                    ['w',  '', 'w',  '', 'w',  '', 'w',  '']]

        self.move_map = [[ '', '',  '', '',  '', '',  '', ''],
                         [ '', '',  '', '',  '', '',  '', ''],
                         [ '', '',  '', '',  '', '',  '', ''],
                         [ '', '',  '', '',  '', '',  '', ''],
                         [ '', '',  '', '',  '', '',  '', ''],
                         [ '', '',  '', '',  '', '',  '', ''],
                         [ '', '',  '', '',  '', '',  '', ''],
                         [ '', '',  '', '',  '', '',  '', '']]

    def actions(self, key):
        if key == 'return':
            self.clear_move_map()
            self.more_moves = False
            if self.player_turn == 'white':
                self.player_turn = 'black'
            else:
                self.player_turn = 'white'
        elif key == 'r':
            self.restart()

jogo = Checkers(100)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            jogo.actions(pg.key.name(event.key))
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
    jogo.promotion()
    jogo.board()
    jogo.mouse_actions(mouse)
    jogo.move()
    jogo.next_move()

    jogo.last_click_status = mouse_input

    pg.display.update()
