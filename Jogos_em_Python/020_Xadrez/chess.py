import pygame as pg


class Chess:
    def __init__(self):
        self.green        = (115, 150,  80)
        self.green_light  = (235, 235, 210)
        self.black_alpha  = (  0,   0,   0,  50)

        self.window = pg.display.set_mode((800, 800))

        pg.font.init()
        self.font = pg.font.SysFont("Courier New", 25, bold=True)

        self.clock = pg.time.Clock()

        # Mouse variables
        self.last_click_status = (False, False, False)

        self.player_view = 'white'
        self.player_turn = 'white'
        self.selected_piece = None
        self.last_selected_piece = None
        self.click_position = None
        self.last_click_position = None
        self.en_passant = None
        self.white_castling_movement_condition = [True, True, True]
        self.black_castling_movement_condition = [True, True, True]

        self.board_map = [['b_rk','b_kn','b_bs','b_qn','b_kg','b_bs','b_kn','b_rk'],
                          ['b_pw','b_pw','b_pw','b_pw','b_pw','b_pw','b_pw','b_pw'],
                          [    '',    '',    '',    '',    '',    '',    '',    ''],
                          [    '',    '',    '',    '',    '',    '',    '',    ''],
                          [    '',    '',    '',    '',    '',    '',    '',    ''],
                          [    '',    '',    '',    '',    '',    '',    '',    ''],
                          ['w_pw','w_pw','w_pw','w_pw','w_pw','w_pw','w_pw','w_pw'],
                          ['w_rk','w_kn','w_bs','w_qn','w_kg','w_bs','w_kn','w_rk']]

        self.actions_board_map = [['','','','','','','',''],
                                  ['','','','','','','',''],
                                  ['','','','','','','',''],
                                  ['','','','','','','',''],
                                  ['','','','','','','',''],
                                  ['','','','','','','',''],
                                  ['','','','','','','',''],
                                  ['','','','','','','','']]

        black_pawn   = pg.image.load('./pawn black.png')
        black_knight = pg.image.load('./knight black.png')
        black_bishop = pg.image.load('./bishop black.png')
        black_rook   = pg.image.load('./rook black.png')
        black_queen  = pg.image.load('./queen black.png')
        black_king   = pg.image.load('./king black.png')
        white_pawn   = pg.image.load('./pawn white.png')
        white_knight = pg.image.load('./knight white.png')
        white_bishop = pg.image.load('./bishop white.png')
        white_rook   = pg.image.load('./rook white.png')
        white_queen  = pg.image.load('./queen white.png')
        white_king   = pg.image.load('./king white.png')
        self.black_pawn   = pg.transform.scale(black_pawn  , (100, 100))
        self.black_knight = pg.transform.scale(black_knight, (100, 100))
        self.black_bishop = pg.transform.scale(black_bishop, (100, 100))
        self.black_rook   = pg.transform.scale(black_rook  , (100, 100))
        self.black_queen  = pg.transform.scale(black_queen , (100, 100))
        self.black_king   = pg.transform.scale(black_king  , (100, 100))
        self.white_pawn   = pg.transform.scale(white_pawn  , (100, 100))
        self.white_knight = pg.transform.scale(white_knight, (100, 100))
        self.white_bishop = pg.transform.scale(white_bishop, (100, 100))
        self.white_rook   = pg.transform.scale(white_rook  , (100, 100))
        self.white_queen  = pg.transform.scale(white_queen , (100, 100))
        self.white_king   = pg.transform.scale(white_king  , (100, 100))

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

    def position_board_pieces(self):
        for y in range(8):
            for x in range(8):
                if self.board_map[y][x] == 'b_pw':
                    self.window.blit(self.black_pawn, (x*100, y*100))
                elif self.board_map[y][x] == 'b_rk':
                    self.window.blit(self.black_rook, (x*100, y*100))
                elif self.board_map[y][x] == 'b_kn':
                    self.window.blit(self.black_knight, (x*100, y*100))
                elif self.board_map[y][x] == 'b_bs':
                    self.window.blit(self.black_bishop, (x*100, y*100))
                elif self.board_map[y][x] == 'b_qn':
                    self.window.blit(self.black_queen, (x*100, y*100))
                elif self.board_map[y][x] == 'b_kg':
                    self.window.blit(self.black_king, (x*100, y*100))
                elif self.board_map[y][x] == 'w_pw':
                    self.window.blit(self.white_pawn, (x*100, y*100))
                elif self.board_map[y][x] == 'w_rk':
                    self.window.blit(self.white_rook, (x*100, y*100))
                elif self.board_map[y][x] == 'w_kn':
                    self.window.blit(self.white_knight, (x*100, y*100))
                elif self.board_map[y][x] == 'w_bs':
                    self.window.blit(self.white_bishop, (x*100, y*100))
                elif self.board_map[y][x] == 'w_qn':
                    self.window.blit(self.white_queen, (x*100, y*100))
                elif self.board_map[y][x] == 'w_kg':
                    self.window.blit(self.white_king, (x*100, y*100))

    def draw_pieces_next_moves(self):
        circle_surf = pg.Surface((100, 100), pg.SRCALPHA)
        pg.draw.circle(circle_surf, self.black_alpha, (50, 50), 50, 10)

        dot_surf = pg.Surface((100, 100), pg.SRCALPHA)
        pg.draw.circle(dot_surf, self.black_alpha, (50, 50), 15)

        for y in range(8):
            for x in range(8):
                if self.actions_board_map[y][x] == 'o':
                    self.window.blit(circle_surf, (x*100, y*100))
                elif self.actions_board_map[y][x] == '.':
                    self.window.blit(dot_surf, (x*100, y*100))

    def board(self):
        columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        for y in range(8):
            for x in range(8):
                if (y % 2) == 0 and (x % 2) == 0 or (y % 2) != 0 and (x % 2) != 0:
                        pg.draw.rect(self.window, self.green_light, (x * 100, y * 100, 100, 100))
                elif (y % 2) != 0 and (x % 2) == 0 or (y % 2) == 0 and (x % 2) != 0:
                        pg.draw.rect(self.window, self.green, ((x * 100, y * 100, 100, 100)))
                if x == 0 and y % 2 == 0:
                    if self.player_view == 'white':
                        score_text = self.font.render(str(8-y), 1, self.green)
                        self.window.blit(score_text, (5, (y * 100) + 5))
                    else:
                        score_text = self.font.render(str(y+1), 1, self.green)
                        self.window.blit(score_text, (5, (y * 100) + 5))
                elif x == 0 and y % 2 == 1:
                    if self.player_view == 'white':
                        score_text = self.font.render(str(8-y), 1, self.green_light)
                        self.window.blit(score_text, (5, (y * 100) + 5))
                    else:
                        score_text = self.font.render(str(y+1), 1, self.green_light)
                        self.window.blit(score_text, (5, (y * 100) + 5))
                if y == 7 and x % 2 == 1:
                    if self.player_view == 'white':
                        score_text = self.font.render(columns[x], 1, self.green)
                        self.window.blit(score_text, ((x * 100) + 80, 775))
                    else:
                        score_text = self.font.render(columns[7-x], 1, self.green)
                        self.window.blit(score_text, ((x * 100) + 80, 775))
                elif y == 7 and x % 2 == 0:
                    if self.player_view == 'white':
                        score_text = self.font.render(columns[x], 1, self.green_light)
                        self.window.blit(score_text, ((x * 100) + 80, 775))
                    else:
                        score_text = self.font.render(columns[7-x], 1, self.green_light)
                        self.window.blit(score_text, ((x * 100) + 80, 775))

        self.position_board_pieces()

        self.draw_pieces_next_moves()

    def pawn_promotion(self):
        x = self.click_position[0]
        y = self.click_position[1]
        if self.board_map[y][x] == 'w_pw':
            if self.player_view == 'white' and y == 0:
                self.board_map[y][x] = 'w_qn'
            if self.player_view == 'black' and y == 7:
                self.board_map[y][x] = 'w_qn'
        elif self.board_map[y][x] == 'b_pw':
            if self.player_view == 'white' and y == 7:
                self.board_map[y][x] = 'b_qn'
            if self.player_view == 'black' and y == 0:
                self.board_map[y][x] = 'b_qn'

    def en_passant_move(self):
        x = self.click_position[0]
        y = self.click_position[1]
        last_y = self.last_click_position[1]
        if self.selected_piece[2:5] == 'pw':
            if y == 3 and last_y == 1:
                self.en_passant = [x, last_y+1]
            elif y == 4 and last_y == 6:
                self.en_passant = [x, last_y-1]

    def castling(self):
        x = self.click_position[0]
        y = self.click_position[1]
        last_x = self.last_click_position[0]
        last_y = self.last_click_position[1]
        last_selected_piece = self.board_map[last_y][last_x]
        if self.player_view == 'white' and self.player_turn == 'white' and last_selected_piece == 'w_kg':
            if x == 6 and y == 7 and last_x == 4 and last_y == 7:
                self.board_map[7][7] = ''
                self.board_map[7][5] = 'w_rk'
                self.white_castling_movement_condition[2] = False
                self.white_castling_movement_condition[1] = False
            elif x == 2 and y == 7 and last_x == 4 and last_y == 7:
                self.board_map[7][0] = ''
                self.board_map[7][3] = 'w_rk'
                self.white_castling_movement_condition[0] = False
                self.white_castling_movement_condition[1] = False
        elif self.player_view == 'white' and self.player_turn == 'black' and last_selected_piece == 'b_kg':
            if x == 6 and y == 0  and last_x == 4 and last_y == 0:
                self.board_map[0][7] = ''
                self.board_map[0][5] = 'b_rk'
                self.black_castling_movement_condition[2] = False
                self.black_castling_movement_condition[1] = False
            elif x == 2 and y == 0 and last_x == 4 and last_y == 0:
                self.board_map[0][0] = ''
                self.board_map[0][3] = 'b_rk'
                self.black_castling_movement_condition[0] = False
                self.black_castling_movement_condition[1] = False
        elif self.player_view == 'black' and self.player_turn == 'white' and last_selected_piece == 'w_kg':
            if x == 5 and y == 0 and last_x == 3 and last_y == 0:
                self.board_map[0][7] = ''
                self.board_map[0][4] = 'w_rk'
                self.white_castling_movement_condition[2] = False
                self.white_castling_movement_condition[1] = False
            elif x == 1 and y == 0 and last_x == 3 and last_y == 0:
                self.board_map[0][0] = ''
                self.board_map[0][2] = 'w_rk'
                self.white_castling_movement_condition[0] = False
                self.white_castling_movement_condition[1] = False
        elif self.player_view == 'black' and self.player_turn == 'black' and last_selected_piece == 'b_kg':
            if x == 5 and y == 7 and last_x == 3 and last_y == 7:
                self.board_map[7][7] = ''
                self.board_map[7][4] = 'b_rk'
                self.black_castling_movement_condition[2] = False
                self.black_castling_movement_condition[1] = False
            elif x == 1 and y == 7 and last_x == 3 and last_y == 7:
                self.board_map[7][0] = ''
                self.board_map[7][2] = 'b_rk'
                self.black_castling_movement_condition[0] = False
                self.black_castling_movement_condition[1] = False

    def castling_path(self):
        x = self.click_position[0]
        y = self.click_position[1]
        last_selected_piece = self.board_map[y][x]
        if self.player_view == 'white' and self.player_turn == 'white' and last_selected_piece == 'w_kg':
            if self.white_castling_movement_condition[1]:
                if self.white_castling_movement_condition[0]:
                    if self.board_map[7][3] == '' and self.board_map[7][2] == '' and self.board_map[7][1] == '':
                        if self.is_king_in_check('b', 4, 7) == False and self.is_king_in_check('b', 3, 7) == False and self.is_king_in_check('b', 2, 7) == False:
                            self.actions_board_map[7][2] = '.'
                if self.white_castling_movement_condition[2]:
                    if self.board_map[7][5] == '' and self.board_map[7][6] == '':
                        if self.is_king_in_check('b', 4, 7) == False and self.is_king_in_check('b', 5, 7) == False and self.is_king_in_check('b', 6, 7) == False:
                            self.actions_board_map[7][6] = '.'
        elif self.player_view == 'white' and self.player_turn == 'black' and last_selected_piece == 'b_kg':
            if self.black_castling_movement_condition[1]:
                if self.black_castling_movement_condition[0]:
                    if self.board_map[0][3] == '' and self.board_map[0][2] == '' and self.board_map[0][1] == '':
                        if self.is_king_in_check('w', 4, 0) == False and self.is_king_in_check('w', 3, 0) == False and self.is_king_in_check('w', 2, 0) == False:
                            self.actions_board_map[0][2] = '.'
                if self.black_castling_movement_condition[2]:
                    if self.board_map[0][5] == '' and self.board_map[0][6] == '':
                        if self.is_king_in_check('w', 4, 0) == False and self.is_king_in_check('w', 5, 0) == False and self.is_king_in_check('w', 6, 0) == False:
                            self.actions_board_map[0][6] = '.'
        elif self.player_view == 'black' and self.player_turn == 'white' and last_selected_piece == 'w_kg':
            if self.white_castling_movement_condition[1]:
                if self.white_castling_movement_condition[0]:
                    if self.board_map[0][2] == '' and self.board_map[0][1] == '':
                        if self.is_king_in_check('b', 3, 0) == False and self.is_king_in_check('b', 2, 0) == False and self.is_king_in_check('b', 1, 0) == False:
                            self.actions_board_map[0][1] = '.'
                if self.white_castling_movement_condition[2]:
                    if self.board_map[0][4] == '' and self.board_map[0][5] == '' and self.board_map[0][6] == '':
                        if self.is_king_in_check('b', 3, 0) == False and self.is_king_in_check('b', 4, 0) == False and self.is_king_in_check('b', 5, 0) == False:
                            self.actions_board_map[0][5] = '.'
        elif self.player_view == 'black' and self.player_turn == 'black' and last_selected_piece == 'b_kg':
            if self.black_castling_movement_condition[1]:
                if self.black_castling_movement_condition[0]:
                    if self.board_map[7][2] == '' and self.board_map[7][1] == '':
                        if self.is_king_in_check('w', 3, 7) == False and self.is_king_in_check('w', 2, 7) == False and self.is_king_in_check('w', 1, 7) == False:
                            self.actions_board_map[7][1] = '.'
                if self.black_castling_movement_condition[2]:
                    if self.board_map[7][4] == '' and self.board_map[7][5] == '' and self.board_map[7][6] == '':
                        if self.is_king_in_check('w', 3, 7) == False and self.is_king_in_check('w', 4, 7) == False and self.is_king_in_check('w', 5, 7) == False:
                            self.actions_board_map[7][5] = '.'

    def castling_variables_update(self):
        x = self.click_position[0]
        y = self.click_position[1]
        last_x = self.last_click_position[0]
        last_y = self.last_click_position[1]
        moved_piece = self.board_map[last_y][last_x]
        if moved_piece[2:5] in ['rk', 'kg']:
            if self.player_view == 'white' and self.player_turn == 'white':
                if self.white_castling_movement_condition[0] == True and last_x == 0 and last_y == 7:
                    self.white_castling_movement_condition[0] = False
                elif self.white_castling_movement_condition[1] == True and last_x == 4 and last_y == 7:
                    if x >= 3 and y >= 6 and x <= 5:
                        self.white_castling_movement_condition[1] = False
                elif self.white_castling_movement_condition[2] == True and last_x == 7 and last_y == 7:
                    self.white_castling_movement_condition[2] = False
            elif self.player_view == 'white' and self.player_turn == 'black':
                if self.black_castling_movement_condition[0] == True and last_x == 0 and last_y == 0:
                    self.black_castling_movement_condition[0] = False
                elif self.black_castling_movement_condition[1] == True and last_x == 4 and last_y == 0:
                    if x >= 3 and y <= 1 and x <= 5:
                        self.black_castling_movement_condition[1] = False
                elif self.black_castling_movement_condition[2] == True and last_x == 7 and last_y == 0:
                    self.black_castling_movement_condition[2] = False
            elif self.player_view == 'black' and self.player_turn == 'white':
                if self.white_castling_movement_condition[0] == True and last_x == 0 and last_y == 0:
                    self.white_castling_movement_condition[0] = False
                elif self.white_castling_movement_condition[1] == True and last_x == 3 and last_y == 0:
                    if x >= 2 and y >= 1 and x <= 4:
                        self.white_castling_movement_condition[1] = False
                elif self.white_castling_movement_condition[2] == True and last_x == 7 and last_y == 0:
                    self.white_castling_movement_condition[2] = False
            elif self.player_view == 'black' and self.player_turn == 'black':
                if self.black_castling_movement_condition[0] == True and last_x == 0 and last_y == 7:
                    self.black_castling_movement_condition[0] = False
                elif self.black_castling_movement_condition[1] == True and last_x == 3 and last_y == 7:
                    if x >= 2 and y <= 6 and x <= 4:
                        self.black_castling_movement_condition[1] = False
                elif self.black_castling_movement_condition[2] == True and last_x == 7 and last_y == 7:
                    self.black_castling_movement_condition[2] = False

    def piece_move_or_capture(self):
        if self.selected_piece != None and self.last_click_position != None:
            x = self.click_position[0]
            y = self.click_position[1]
            last_x = self.last_click_position[0]
            last_y = self.last_click_position[1]
            moved_piece = self.board_map[last_y][last_x]
            # Move or capture
            if self.actions_board_map[y][x] == '.' or self.actions_board_map[y][x] == 'o':
                # Castling variables update
                self.castling_variables_update()
                # Castling Rook move
                self.castling()
                # Moving pieces
                self.board_map[y][x] = moved_piece
                self.selected_piece = moved_piece
                self.board_map[last_y][last_x] = ''
                # En Passant capture
                if moved_piece[2:5] == 'pw':
                    if self.en_passant != None:
                        x_ep = self.en_passant[0]
                        y_ep = self.en_passant[1]
                        if x_ep == x and y_ep == y:
                            if last_y > y:
                                self.board_map[y+1][x] = ''
                            elif last_y < y:
                                self.board_map[y-1][x] = ''
                self.pawn_promotion()
                if self.player_turn == 'white':
                    self.player_turn = 'black'
                    self.en_passant = None
                elif self.player_turn == 'black':
                    self.player_turn = 'white'
                    self.en_passant = None
                self.en_passant_move()

    def piece_path(self, path, opposing_piece, step_x, step_y):
        x = self.click_position[0]
        y = self.click_position[1]
        if x + step_x <= -1 or y + step_y <= -1:
            return False
        try:
            if path == True:
                if self.board_map[y+step_y][x+step_x] == '':
                    self.actions_board_map[y+step_y][x+step_x] = '.'
                    return True
                elif self.board_map[y+step_y][x+step_x][0:1] == opposing_piece:
                    self.actions_board_map[y+step_y][x+step_x] = 'o'
                    return False
            else:
                return False
        except:
            return False

    def clear_map_actions(self):
        # Clear self.actions_board_map
        for y in range(8):
            for x in range(8):
                self.actions_board_map[y][x] = ''

    def pawn_move(self):
        # Pawn next moves
        if self.selected_piece != None:
            if self.selected_piece[2:5] == 'pw':
                x = self.click_position[0]
                y = self.click_position[1]
                if self.player_view == 'white' and self.player_turn == 'white' and self.selected_piece[0:1] == 'w':
                    if y >= 1:
                        if self.board_map[y-1][x-1][0:1] == 'b':
                            self.actions_board_map[y-1][x-1] = 'o'
                        if self.board_map[y-1][x] == '':
                            self.actions_board_map[y-1][x] = '.'
                            if y == 6 and self.board_map[y-2][x] == '':
                                self.actions_board_map[y-2][x] = '.'
                        if x < 7 and self.board_map[y-1][x+1][0:1] == 'b':
                            self.actions_board_map[y-1][x+1] = 'o'
                        if self.en_passant != None:
                            x_ep = self.en_passant[0]
                            y_ep = self.en_passant[1]
                            if y_ep == y-1 and x_ep == x-1:
                                self.actions_board_map[y-1][x-1] = 'o'
                            elif y_ep == y-1 and x_ep == x+1:
                                self.actions_board_map[y-1][x+1] = 'o'
                if self.player_view == 'white' and self.player_turn == 'black' and self.selected_piece[0:1] == 'b':
                    if y <= 6:
                        if self.board_map[y+1][x-1][0:1] == 'w':
                            self.actions_board_map[y+1][x-1] = 'o'
                        if self.board_map[y+1][x] == '':
                            self.actions_board_map[y+1][x] = '.'
                            if y == 1 and self.board_map[y+2][x] == '':
                                self.actions_board_map[y+2][x] = '.'
                        if x < 7 and self.board_map[y+1][x+1][0:1] == 'w':
                            self.actions_board_map[y+1][x+1] = 'o'
                        if self.en_passant != None:
                            x_ep = self.en_passant[0]
                            y_ep = self.en_passant[1]
                            if y_ep == y+1 and x_ep == x-1:
                                self.actions_board_map[y+1][x-1] = 'o'
                            elif y_ep == y+1 and x_ep == x+1:
                                self.actions_board_map[y+1][x+1] = 'o'
                if self.player_view == 'black' and self.player_turn == 'black' and self.selected_piece[0:1] == 'b':
                    if y >= 1:
                        if self.board_map[y-1][x-1][0:1] == 'w':
                            self.actions_board_map[y-1][x-1] = 'o'
                        if self.board_map[y-1][x] == '':
                            self.actions_board_map[y-1][x] = '.'
                            if y == 6 and self.board_map[y-2][x] == '':
                                self.actions_board_map[y-2][x] = '.'
                        if x < 7 and self.board_map[y-1][x+1][0:1] == 'w':
                            self.actions_board_map[y-1][x+1] = 'o'
                        if self.en_passant != None:
                            x_ep = self.en_passant[0]
                            y_ep = self.en_passant[1]
                            if y_ep == y-1 and x_ep == x-1:
                                self.actions_board_map[y-1][x-1] = 'o'
                            elif y_ep == y-1 and x_ep == x+1:
                                self.actions_board_map[y-1][x+1] = 'o'
                if self.player_view == 'black' and self.player_turn == 'white' and self.selected_piece[0:1] == 'w':
                    if y <= 6:
                        if self.board_map[y+1][x-1][0:1] == 'b':
                            self.actions_board_map[y+1][x-1] = 'o'
                        if self.board_map[y+1][x] == '':
                            self.actions_board_map[y+1][x] = '.'
                            if y == 1 and self.board_map[y+2][x] == '':
                                self.actions_board_map[y+2][x] = '.'
                        if x < 7 and self.board_map[y+1][x+1][0:1] == 'b':
                            self.actions_board_map[y+1][x+1] = 'o'
                        if self.en_passant != None:
                            x_ep = self.en_passant[0]
                            y_ep = self.en_passant[1]
                            if y_ep == y+1 and x_ep == x-1:
                                self.actions_board_map[y+1][x-1] = 'o'
                            elif y_ep == y+1 and x_ep == x+1:
                                self.actions_board_map[y+1][x+1] = 'o'

    def knight_move(self):
        # Knight next moves
        if self.selected_piece != None:
            if self.selected_piece[2:5] == 'kn':
                x = self.click_position[0]
                y = self.click_position[1]
                direction = True
                moves = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1 , 2]]
                for move in moves:
                    # Up + Right
                    if self.player_turn == 'white' and self.board_map[y][x][0:1] == 'w':
                        _ = self.piece_path(direction, 'b', move[0], move[1])
                    elif self.player_turn == 'black' and self.board_map[y][x][0:1] == 'b':
                        _ = self.piece_path(direction, 'w', move[0], move[1])

    def bishop_move(self):
        # Bishop next moves
        if self.selected_piece != None:
            if self.selected_piece[2:5] == 'bs':
                x = self.click_position[0]
                y = self.click_position[1]
                direction = [True, True, True, True]
                for move in range(1, 8):
                    # Up + Right
                    if self.player_turn == 'white' and self.board_map[y][x][0:1] == 'w':
                        direction[0] = self.piece_path(direction[0], 'b', move, -move)
                    elif self.player_turn == 'black' and self.board_map[y][x][0:1] == 'b':
                        direction[0] = self.piece_path(direction[0], 'w', move, -move)
                    # Down + Right
                    if self.player_turn == 'white' and self.board_map[y][x][0:1] == 'w':
                        direction[1] = self.piece_path(direction[1], 'b', move, move)
                    elif self.player_turn == 'black' and self.board_map[y][x][0:1] == 'b':
                        direction[1] = self.piece_path(direction[1], 'w', move, move)
                    # Down + Left
                    if self.player_turn == 'white' and self.board_map[y][x][0:1] == 'w':
                        direction[2] = self.piece_path(direction[2], 'b', -move, move)
                    elif self.player_turn == 'black' and self.board_map[y][x][0:1] == 'b':
                        direction[2] = self.piece_path(direction[2], 'w', -move, move)
                    # Up + Left
                    if self.player_turn == 'white' and self.board_map[y][x][0:1] == 'w':
                        direction[3] = self.piece_path(direction[3], 'b', -move, -move)
                    elif self.player_turn == 'black' and self.board_map[y][x][0:1] == 'b':
                        direction[3] = self.piece_path(direction[3], 'w', -move, -move)

    def rook_move(self):
        # Rook next moves
        if self.selected_piece != None:
            if self.selected_piece[2:5] == 'rk':
                x = self.click_position[0]
                y = self.click_position[1]
                direction = [True, True, True, True]
                for move in range(1, 8):
                    # Up
                    if self.player_turn == 'white' and self.board_map[y][x][0:1] == 'w':
                        direction[0] = self.piece_path(direction[0], 'b', 0, -move)
                    elif self.player_turn == 'black' and self.board_map[y][x][0:1] == 'b':
                        direction[0] = self.piece_path(direction[0], 'w', 0, -move)
                    # Right
                    if self.player_turn == 'white' and self.board_map[y][x][0:1] == 'w':
                        direction[1] = self.piece_path(direction[1], 'b', move, 0)
                    elif self.player_turn == 'black' and self.board_map[y][x][0:1] == 'b':
                        direction[1] = self.piece_path(direction[1], 'w', move, 0)
                    # Left
                    if self.player_turn == 'white' and self.board_map[y][x][0:1] == 'w':
                        direction[2] = self.piece_path(direction[2], 'b', 0, move)
                    elif self.player_turn == 'black' and self.board_map[y][x][0:1] == 'b':
                        direction[2] = self.piece_path(direction[2], 'w', 0, move)
                    # Down
                    if self.player_turn == 'white' and self.board_map[y][x][0:1] == 'w':
                        direction[3] = self.piece_path(direction[3], 'b', -move, 0)
                    elif self.player_turn == 'black' and self.board_map[y][x][0:1] == 'b':
                        direction[3] = self.piece_path(direction[3], 'w', -move, 0)

    def queen_move(self):
        # Queen next moves
        if self.selected_piece != None:
            if self.selected_piece[2:5] == 'qn':
                x = self.click_position[0]
                y = self.click_position[1]
                direction = [True, True, True, True, True, True, True, True]
                for move in range(1, 8):
                    # Up
                    if self.player_turn == 'white' and self.board_map[y][x][0:1] == 'w':
                        direction[0] = self.piece_path(direction[0], 'b', 0, -move)
                    elif self.player_turn == 'black' and self.board_map[y][x][0:1] == 'b':
                        direction[0] = self.piece_path(direction[0], 'w', 0, -move)
                    # Up + Right
                    if self.player_turn == 'white' and self.board_map[y][x][0:1] == 'w':
                        direction[1] = self.piece_path(direction[1], 'b', move, -move)
                    elif self.player_turn == 'black' and self.board_map[y][x][0:1] == 'b':
                        direction[1] = self.piece_path(direction[1], 'w', move, -move)
                    # Right
                    if self.player_turn == 'white' and self.board_map[y][x][0:1] == 'w':
                        direction[2] = self.piece_path(direction[2], 'b', move, 0)
                    elif self.player_turn == 'black' and self.board_map[y][x][0:1] == 'b':
                        direction[2] = self.piece_path(direction[2], 'w', move, 0)
                    # Down + Right
                    if self.player_turn == 'white' and self.board_map[y][x][0:1] == 'w':
                        direction[3] = self.piece_path(direction[3], 'b', move, move)
                    elif self.player_turn == 'black' and self.board_map[y][x][0:1] == 'b':
                        direction[3] = self.piece_path(direction[3], 'w', move, move)
                    # Down
                    if self.player_turn == 'white' and self.board_map[y][x][0:1] == 'w':
                        direction[4] = self.piece_path(direction[4], 'b', 0, move)
                    elif self.player_turn == 'black' and self.board_map[y][x][0:1] == 'b':
                        direction[4] = self.piece_path(direction[4], 'w', 0, move)
                    # Down + Left
                    if self.player_turn == 'white' and self.board_map[y][x][0:1] == 'w':
                        direction[5] = self.piece_path(direction[5], 'b', -move, move)
                    elif self.player_turn == 'black' and self.board_map[y][x][0:1] == 'b':
                        direction[5] = self.piece_path(direction[5], 'w', -move, move)
                    # Left
                    if self.player_turn == 'white' and self.board_map[y][x][0:1] == 'w':
                        direction[6] = self.piece_path(direction[6], 'b', -move, 0)
                    elif self.player_turn == 'black' and self.board_map[y][x][0:1] == 'b':
                        direction[6] = self.piece_path(direction[6], 'w', -move, 0)
                    # Up + Left
                    if self.player_turn == 'white' and self.board_map[y][x][0:1] == 'w':
                        direction[7] = self.piece_path(direction[7], 'b', -move, -move)
                    elif self.player_turn == 'black' and self.board_map[y][x][0:1] == 'b':
                        direction[7] = self.piece_path(direction[7], 'w', -move, -move)

    def is_opposing_piece_checking_the_king(self, path, opposing_piece, x, y, step_x, step_y):
        if x + step_x <= -1 or y + step_y <= -1:
            return False, False
        elif x + step_x >= 8 or y + step_y >= 8:
            return False, False

        if  opposing_piece[0:1] == 'w':
            king = 'b_kg'
        else:
            king = 'w_kg'

        if path:
            if self.board_map[y+step_y][x+step_x] == opposing_piece:
                return False, True
            elif self.board_map[y+step_y][x+step_x] == king:
                return True, False
            elif self.board_map[y+step_y][x+step_x] == '':
                return True, False
            elif self.board_map[y+step_y][x+step_x] != '':
                return False, False
        else:
            return False, False

    def is_bishop_checking_the_king(self, opposing_piece, x, y):
        check = [False, False, False, False]
        final_check = False
        direction = [True, True, True, True]
        for move in range(1, 8):
            direction[0], check_pivot = self.is_opposing_piece_checking_the_king(direction[0], opposing_piece+'_bs', x, y, move, -move)
            if direction[0] == False and check_pivot == True:
                check[0] = True
            direction[1], check_pivot = self.is_opposing_piece_checking_the_king(direction[1], opposing_piece+'_bs', x, y, move, move)
            if direction[1] == False and check_pivot == True:
                check[1] = True
            direction[2], check_pivot = self.is_opposing_piece_checking_the_king(direction[2], opposing_piece+'_bs', x, y, -move, move)
            if direction[2] == False and check_pivot == True:
                check[2] = True
            direction[3], check_pivot = self.is_opposing_piece_checking_the_king(direction[3], opposing_piece+'_bs', x, y, -move, -move)
            if direction[3] == False and check_pivot == True:
                check[3] = True
        if check[0] == True or check[2] == True:
            final_check = True
        elif check[1] == True or check[3] == True:
            final_check = True
        return final_check

    def is_rook_checking_the_king(self, opposing_piece, x, y):
        check = [False, False, False, False]
        final_check = False
        direction = [True, True, True, True]
        for move in range(1, 8):
            direction[0], check_pivot = self.is_opposing_piece_checking_the_king(direction[0], opposing_piece+'_rk', x, y, 0, -move)
            if direction[0] == False and check_pivot == True:
                check[0] = True
            direction[1], check_pivot = self.is_opposing_piece_checking_the_king(direction[1], opposing_piece+'_rk', x, y, move, 0)
            if direction[1] == False and check_pivot == True:
                check[1] = True
            direction[2], check_pivot = self.is_opposing_piece_checking_the_king(direction[2], opposing_piece+'_rk', x, y, 0, move)
            if direction[2] == False and check_pivot == True:
                check[2] = True
            direction[3], check_pivot = self.is_opposing_piece_checking_the_king(direction[3], opposing_piece+'_rk', x, y, -move, 0)
            if direction[3] == False and check_pivot == True:
                check[3] = True
        if check[0] == True or check[2] == True:
            final_check = True
        elif check[1] == True or check[3] == True:
            final_check = True
        return final_check

    def is_queen_checking_the_king(self, opposing_piece, x, y):
        check = [False, False, False, False, False, False, False, False]
        final_check = False
        direction = [True, True, True, True, True, True, True, True]
        for move in range(1, 8):
            direction[0], check_pivot = self.is_opposing_piece_checking_the_king(direction[0], opposing_piece+'_qn', x, y, 0, -move)
            if direction[0] == False and check_pivot == True:
                check[0] = True
            direction[1], check_pivot = self.is_opposing_piece_checking_the_king(direction[1], opposing_piece+'_qn', x, y, move, 0)
            if direction[1] == False and check_pivot == True:
                check[1] = True
            direction[2], check_pivot = self.is_opposing_piece_checking_the_king(direction[2], opposing_piece+'_qn', x, y, 0, move)
            if direction[2] == False and check_pivot == True:
                check[2] = True
            direction[3], check_pivot = self.is_opposing_piece_checking_the_king(direction[3], opposing_piece+'_qn', x, y, -move, 0)
            if direction[3] == False and check_pivot == True:
                check[3] = True
            direction[4], check_pivot = self.is_opposing_piece_checking_the_king(direction[4], opposing_piece+'_qn', x, y, move, -move)
            if direction[4] == False and check_pivot == True:
                check[4] = True
            direction[5], check_pivot = self.is_opposing_piece_checking_the_king(direction[5], opposing_piece+'_qn', x, y, move, move)
            if direction[5] == False and check_pivot == True:
                check[5] = True
            direction[6], check_pivot = self.is_opposing_piece_checking_the_king(direction[6], opposing_piece+'_qn', x, y, -move, move)
            if direction[6] == False and check_pivot == True:
                check[6] = True
            direction[7], check_pivot = self.is_opposing_piece_checking_the_king(direction[7], opposing_piece+'_qn', x, y, -move, -move)
            if direction[7] == False and check_pivot == True:
                check[7] = True
        if check[0] == True or check[2] == True:
            final_check = True
        elif check[1] == True or check[3] == True:
            final_check = True
        elif check[4] == True or check[6] == True:
            final_check = True
        elif check[5] == True or check[7] == True:
            final_check = True
        return final_check

    def is_knight_checking_the_king(self, opposing_piece, x, y):
        moves = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1 , 2]]
        for move in moves:
            if y+move[0] <= 7 and x+move[1] <= 7 and y+move[0] >= 0 and x+move[1] >= 0:
                if self.board_map[y+move[0]][x+move[1]] == opposing_piece+'_kn':
                    return True
            else:
                continue
        return False

    def is_pawn_checking_the_king(self, opposing_piece, x, y):
        check_left = True
        check_right = True
        check_up = True
        check_down = True
        if x - 1 <= -1:
            check_left = False
        if y - 1 <= -1:
            check_up = False
        if x + 1 >= 8:
            check_right = False
        if y + 1 >= 8:
            check_down = False

        if self.player_view == 'white' and opposing_piece == 'b':
            if check_left and check_up:
                if self.board_map[y-1][x-1] == opposing_piece+'_pw':
                    return True
            if check_up and check_right:
                if self.board_map[y-1][x+1] == opposing_piece+'_pw':
                    return True
        elif self.player_view == 'white' and opposing_piece == 'w':
            if check_left and check_down:
                if self.board_map[y+1][x-1] == opposing_piece+'_pw':
                    return True
            if check_down and check_right:
                if self.board_map[y+1][x+1] == opposing_piece+'_pw':
                    return True
        elif self.player_view == 'black' and opposing_piece == 'b':
            if check_left and check_down:
                if self.board_map[y+1][x-1] == opposing_piece+'_pw':
                    return True
            if check_down and check_right:
                if self.board_map[y+1][x+1] == opposing_piece+'_pw':
                    return True
        elif self.player_view == 'black' and opposing_piece == 'w':
            if check_left and check_up:
                if self.board_map[y-1][x-1] == opposing_piece+'_pw':
                    return True
            if check_up and check_right:
                if self.board_map[y-1][x+1] == opposing_piece+'_pw':
                    return True

    def is_other_king_checking_the_king(self, opposing_piece, x, y):
        check = False
        for yy in range(-1, 2):
            for xx in range(-1, 2):
                try:
                    if self.board_map[y+yy][x+xx] == opposing_piece+'_kg':
                        check = True
                except:
                    continue
        return check

    def is_king_in_check(self, opposing_piece, x, y):
        check = False

        if self.is_bishop_checking_the_king(opposing_piece, x, y):
            check = True
        elif self.is_rook_checking_the_king(opposing_piece, x, y):
            check = True
        elif self.is_queen_checking_the_king(opposing_piece, x, y):
            check = True
        elif self.is_knight_checking_the_king(opposing_piece, x, y):
            check = True
        elif self.is_pawn_checking_the_king(opposing_piece, x, y):
            check = True
        elif self.is_other_king_checking_the_king(opposing_piece, x, y):
            check = True

        return check

    def king_move(self):
        # King next moves
        if self.selected_piece != None:
            if self.selected_piece[2:5] == 'kg':
                x = self.click_position[0]
                y = self.click_position[1]
                if self.player_turn == 'white' and self.board_map[y][x][0:1] == 'w':
                    # Up
                    if self.is_king_in_check('b', x, y-1) == False:
                        _ = self.piece_path(True, 'b', 0, -1)
                    # Up + Right
                    if self.is_king_in_check('b', x+1, y-1) == False:
                        _ = self.piece_path(True, 'b', 1, -1)
                    # Right
                    if self.is_king_in_check('b', x+1, y) == False:
                        _ = self.piece_path(True, 'b', 1, 0)
                    # Down + Right
                    if self.is_king_in_check('b', x+1, y+1) == False:
                        _ = self.piece_path(True, 'b', 1, 1)
                    # Down
                    if self.is_king_in_check('b', x, y+1) == False:
                        _ = self.piece_path(True, 'b', 0, 1)
                    # Down Left
                    if self.is_king_in_check('b', x-1, y+1) == False:
                        _ = self.piece_path(True, 'b', -1, 1)
                    # Left
                    if self.is_king_in_check('b', x-1, y) == False:
                        _ = self.piece_path(True, 'b', -1, 0)
                    # Up + Left
                    if self.is_king_in_check('b', x-1, y-1) == False:
                        _ = self.piece_path(True, 'b', -1, -1)
                elif self.player_turn == 'black' and self.board_map[y][x][0:1] == 'b':
                    # Up
                    if self.is_king_in_check('w', x, y-1) == False:
                        _ = self.piece_path(True, 'w', 0, -1)
                    # Up + Right
                    if self.is_king_in_check('w', x+1, y-1) == False:
                        _ = self.piece_path(True, 'w', 1, -1)
                    # Right
                    if self.is_king_in_check('w', x+1, y) == False:
                        _ = self.piece_path(True, 'w', 1, 0)
                    # Down + Right
                    if self.is_king_in_check('w', x+1, y+1) == False:
                        _ = self.piece_path(True, 'w', 1, 1)
                    # Down
                    if self.is_king_in_check('w', x, y+1) == False:
                        _ = self.piece_path(True, 'w', 0, 1)
                    # Down + Left
                    if self.is_king_in_check('w', x-1, y+1) == False:
                        _ = self.piece_path(True, 'w', -1, 1)
                    # Left
                    if self.is_king_in_check('w', x-1, y) == False:
                        _ = self.piece_path(True, 'w', -1, 0)
                    # Up + Left
                    if self.is_king_in_check('w', x-1, y-1) == False:
                        _ = self.piece_path(True, 'w', -1, -1)
                self.castling_path()

    def mouse_actions(self, mouse):
        if mouse[2][0] == True:
            for y in range(8):
                for x in range(8):
                    if mouse[0][0] >= (x * 100) and mouse[0][0] <= (x * 100) + 100 and mouse[0][1] >= (y * 100) and mouse[0][1] <= (y * 100) + 100:
                        if self.click_position != None:
                            last_x = self.click_position[0]
                            last_y = self.click_position[1]
                            self.last_click_position = [last_x, last_y]
                            self.last_selected_piece = self.board_map[last_y][last_x]
                        self.selected_piece = self.board_map[y][x]
                        self.click_position = [x, y]

    def new_game(self):
        self.player_view = 'white'
        self.player_turn = 'white'
        self.selected_piece = None
        self.last_selected_piece = None
        self.click_position = None
        self.last_click_position = None
        self.en_passant = None
        self.white_castling_movement_condition = [True, True, True]
        self.black_castling_movement_condition = [True, True, True]

        self.board_map = [['b_rk','b_kn','b_bs','b_qn','b_kg','b_bs','b_kn','b_rk'],
                          ['b_pw','b_pw','b_pw','b_pw','b_pw','b_pw','b_pw','b_pw'],
                          [    '',    '',    '',    '',    '',    '',    '',    ''],
                          [    '',    '',    '',    '',    '',    '',    '',    ''],
                          [    '',    '',    '',    '',    '',    '',    '',    ''],
                          [    '',    '',    '',    '',    '',    '',    '',    ''],
                          ['w_pw','w_pw','w_pw','w_pw','w_pw','w_pw','w_pw','w_pw'],
                          ['w_rk','w_kn','w_bs','w_qn','w_kg','w_bs','w_kn','w_rk']]

        self.actions_board_map = [['','','','','','','',''],
                                  ['','','','','','','',''],
                                  ['','','','','','','',''],
                                  ['','','','','','','',''],
                                  ['','','','','','','',''],
                                  ['','','','','','','',''],
                                  ['','','','','','','',''],
                                  ['','','','','','','','']]

    def rotate_board(self):
        # Flip board view
        self.board_map = [row[::-1] for row in self.board_map[::-1]]
        # Flip variable click_position
        if self.click_position != None:
            self.click_position = [7 - self.click_position[0], 7 - self.click_position[1]]
        # Flip variable last_click_position
        if self.last_click_position != None:
            self.last_click_position = [7 - self.last_click_position[0], 7 - self.last_click_position[1]]
        # Flip en_passant variable position
        if self.en_passant != None:
            self.en_passant = [7 - self.en_passant[0], 7 - self.en_passant[1]]
        # Flip castling variable position
        pivot = self.white_castling_movement_condition[0]
        self.white_castling_movement_condition[0] = self.white_castling_movement_condition[2]
        self.white_castling_movement_condition[2] = pivot
        pivot = self.black_castling_movement_condition[0]
        self.black_castling_movement_condition[0] = self.black_castling_movement_condition[2]
        self.black_castling_movement_condition[2] = pivot
        # Change board view variable
        if self.player_view == 'white':
            self.player_view = 'black'
        elif self.player_view == 'black':
            self.player_view = 'white'

    def actions(self, key):
        if key == 'r':
            self.rotate_board()
        if key == 'n':
            self.new_game()


jogo = Chess()


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
    jogo.board()
    jogo.mouse_actions(mouse)
    jogo.piece_move_or_capture()
    jogo.clear_map_actions()
    jogo.pawn_move()
    jogo.knight_move()
    jogo.bishop_move()
    jogo.rook_move()
    jogo.queen_move()
    jogo.king_move()

    jogo.last_click_status = mouse_input

    pg.display.update()