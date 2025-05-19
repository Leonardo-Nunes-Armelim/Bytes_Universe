import pygame as pg
import random
import time


class Uno:
    def __init__(self, window_size):
        self.white       = (255, 255, 255)
        self.dark_gray   = ( 70,  70,  80)
        self.black       = (  0,   0,   0)
        self.blue        = ( 15, 105, 185)
        self.green       = ( 50, 185,  70)
        self.yellow      = (255, 190,  50)
        self.red         = (255,  95,  90)
        self.purple      = (150,  90, 150)
        self.orange      = (255, 145,  50)
        self.light_blue  = (  0, 195, 240)
        self.light_green = (125, 200,  60)
        self.brown_1     = (240, 140, 100)
        self.brown_2     = (170,  90,  65)
        self.brown_3     = (145,  65,  40)
        self.brown_4     = (115,  50,  30)
        self.brown_5     = ( 60,  25,  10)

        self.window = pg.display.set_mode(window_size)

        pg.font.init()
        self.font_1 = pg.font.SysFont("Courier New", 100, bold=True)
        self.font_2 = pg.font.SysFont("Courier New", 50, bold=True)
        self.font_3 = pg.font.SysFont("Courier New", 80, bold=True)
        self.font_4 = pg.font.SysFont("Courier New", 40, bold=True)

        self.clock = pg.time.Clock()

        # Mouse variables
        self.last_click_status = (False, False, False)

        self.last_color_choose = None
        self.next_color_button = False
        self.next_index_card_play = None
        self.in_play = False
        self.player_turn = 0
        self.winner = None
        self.play_or_pass = False
        self.game_direction = 'clockwise' # clockwise / counterclockwise
        self.table_card = []
        self.player_0 = []
        self.player_1 = []
        self.player_2 = []
        self.player_3 = []

        self.cards = [['+4',None], ['+4',None], ['+4',None], ['+4',None],
                      ['0',self.blue], ['0',self.green], ['0',self.yellow], ['0',self.red],
                      ['1',self.blue], ['1',self.green], ['1',self.yellow], ['1',self.red],
                      ['1',self.blue], ['1',self.green], ['1',self.yellow], ['1',self.red],
                      ['2',self.blue], ['2',self.green], ['2',self.yellow], ['2',self.red],
                      ['2',self.blue], ['2',self.green], ['2',self.yellow], ['2',self.red],
                      ['3',self.blue], ['3',self.green], ['3',self.yellow], ['3',self.red],
                      ['3',self.blue], ['3',self.green], ['3',self.yellow], ['3',self.red],
                      ['4',self.blue], ['4',self.green], ['4',self.yellow], ['4',self.red],
                      ['4',self.blue], ['4',self.green], ['4',self.yellow], ['4',self.red],
                      ['5',self.blue], ['5',self.green], ['5',self.yellow], ['5',self.red],
                      ['5',self.blue], ['5',self.green], ['5',self.yellow], ['5',self.red],
                      ['6',self.blue], ['6',self.green], ['6',self.yellow], ['6',self.red],
                      ['6',self.blue], ['6',self.green], ['6',self.yellow], ['6',self.red],
                      ['7',self.blue], ['7',self.green], ['7',self.yellow], ['7',self.red],
                      ['7',self.blue], ['7',self.green], ['7',self.yellow], ['7',self.red],
                      ['8',self.blue], ['8',self.green], ['8',self.yellow], ['8',self.red],
                      ['8',self.blue], ['8',self.green], ['8',self.yellow], ['8',self.red],
                      ['9',self.blue], ['9',self.green], ['9',self.yellow], ['9',self.red],
                      ['9',self.blue], ['9',self.green], ['9',self.yellow], ['9',self.red],
                      ['+1',self.blue], ['+1',self.green], ['+1',self.yellow], ['+1',self.red],
                      ['+1',self.blue], ['+1',self.green], ['+1',self.yellow], ['+1',self.red],
                      ['+2',self.blue], ['+2',self.green], ['+2',self.yellow], ['+2',self.red],
                      ['+2',self.blue], ['+2',self.green], ['+2',self.yellow], ['+2',self.red],
                      ['new color',None], ['new color',None], ['new color',None], ['new color',None],
                      ['block',self.blue], ['block',self.green], ['block',self.yellow], ['block',self.red],
                      ['block',self.blue], ['block',self.green], ['block',self.yellow], ['block',self.red],
                      ['invert',self.blue], ['invert',self.green], ['invert',self.yellow], ['invert',self.red],
                      ['invert',self.blue], ['invert',self.green], ['invert',self.yellow], ['invert',self.red]]

        card_back = pg.image.load('./card back.png')
        card_back = pg.transform.scale(card_back, (160, 240))
        self.card_back_left  = self.round_card_edges(pg.transform.rotate(card_back, -90), 20)
        self.card_back_up    = self.round_card_edges(pg.transform.rotate(card_back, 180), 20)
        self.card_back_right = self.round_card_edges(pg.transform.rotate(card_back, 90), 20)

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
        pg.draw.rect(self.window, self.brown_4, (0, 0, self.window.get_width(), self.window.get_height()))

    def is_color_card(self, string):
        if string in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+1', '+2', 'block', 'invert']:
            return True
        else:
            return False

    def draw_normal_cards_content(self, x, y, symbol, color):
        card_text = self.font_1.render(symbol, 1, color)
        text_x = x + 80 - (card_text.get_width() / 2)
        text_y = y + 120 - (card_text.get_height() / 2)
        self.window.blit(card_text, (text_x, text_y))

        card_text = self.font_2.render(symbol, 1, self.white)
        card_text_upside_down = pg.transform.rotate(card_text, 180)
        self.window.blit(card_text, (x + 20, y + 10))
        if symbol == '+1' or symbol == '+2' or symbol == '+4':
            shift_to_left = card_text_upside_down.get_width() / 2
            self.window.blit(card_text_upside_down, (x + 110 - shift_to_left, y + 170))
        else:
            self.window.blit(card_text_upside_down, (x + 110, y + 170))

    def draw_blocking_card_content(self, x, y, color):
        pg.draw.circle(self.window, color, (x+80, y+120), 40, 12)
        pg.draw.line(self.window, color, (x+57, y+97), (x+102, y+142), 20)
        pg.draw.circle(self.window, self.white, (x+40, y+40), 20, 5)
        pg.draw.line(self.window, self.white, (x+28, y+28), (x+50, y+50), 10)
        pg.draw.circle(self.window, self.white, (x+120, y+200), 20, 5)
        pg.draw.line(self.window, self.white, (x+108, y+188), (x+130, y+210), 10)

    def draw_reverse_card_content(self, x, y, color):
        pg.draw.circle(self.window, color, (x+80, y+120), 35, 10)
        pg.draw.line(self.window, self.white, (x+40, y+120), (x+120, y+120), 10)
        pg.draw.polygon(self.window, color, [(x+42, y+115), (x+42, y+85), (x+72, y+115)])
        pg.draw.polygon(self.window, color, [(x+116, y+125), (x+86, y+125), (x+116, y+155)])
        pg.draw.circle(self.window, self.white, (x+40, y+40), 20, 5)
        pg.draw.line(self.window, color, (x+15, y+38), (x+65, y+38), 6)
        pg.draw.polygon(self.window, self.white, [(x+20, y+36), (x+20, y+19), (x+37, y+36)])
        pg.draw.polygon(self.window, self.white, [(x+60, y+42), (x+43, y+42), (x+60, y+59)])
        pg.draw.circle(self.window, self.white, (x+120, y+200), 20, 5)
        pg.draw.line(self.window, color, (x+95, y+200), (x+145, y+200), 6)
        pg.draw.polygon(self.window, self.white, [(x+100, y+198), (x+100, y+181), (x+117, y+198)])
        pg.draw.polygon(self.window, self.white, [(x+139, y+204), (x+122, y+204), (x+139, y+221)])

    def draw_card_content_plus_4(self, x, y):
        card_text = self.font_3.render('+4', 1, self.dark_gray)
        text_x = x + 80 - (card_text.get_width() / 2)
        text_y = y + 125 - (card_text.get_height() / 2)
        self.window.blit(card_text, (text_x, text_y))

        card_text = self.font_4.render('+4', 1, self.white)
        card_text_upside_down = pg.transform.rotate(card_text, 180)
        self.window.blit(card_text, (x + 20, y + 10))
        self.window.blit(card_text_upside_down, (x + 95, y + 180))

    def draw_new_color_card_content(self, x, y):
        pg.draw.rect(self.window, self.blue, (x+40, y+80, 40, 40))
        pg.draw.rect(self.window, self.green, (x+80, y+80, 40, 40))
        pg.draw.rect(self.window, self.yellow, (x+40, y+120, 40, 40))
        pg.draw.rect(self.window, self.red, (x+80, y+120, 40, 40))
        pg.draw.circle(self.window, self.white, (x+80, y+120), 15)
        pg.draw.line(self.window, self.white, (x+79, y+80), (x+79, y+160), 4)
        pg.draw.line(self.window, self.white, (x+40, y+121), (x+120, y+121), 4)
        pg.draw.circle(self.window, self.white, (x+80, y+120), 48, 8)
        pg.draw.polygon(self.window, self.white, [(x+40, y+80), (x+40, y+95), (x+55, y+80)])
        pg.draw.polygon(self.window, self.white, [(x+120, y+80), (x+120, y+95), (x+105, y+80)])
        pg.draw.polygon(self.window, self.white, [(x+40, y+160), (x+40, y+145), (x+55, y+160)])
        pg.draw.polygon(self.window, self.white, [(x+120, y+160), (x+105, y+160), (x+120, y+145)])

    def draw_card(self, x, y, symbol, color):
        if self.is_color_card(symbol):
            pg.draw.rect(self.window, color, (x, y, 160, 240), 0, 20)
        else:
            pg.draw.rect(self.window, self.yellow, (x, y, 160, 120), 0, 20)
            pg.draw.rect(self.window, self.purple, (x, y + 120, 160, 120), 0, 20)
            pg.draw.polygon(self.window, self.light_green, [(x+80, y+120), (x, y+20), (x, y+150)])
            pg.draw.polygon(self.window, self.light_blue,  [(x+80, y+120), (x, y+150), (x+10, y+230), (x+60, y+239)])
            pg.draw.polygon(self.window, self.red,         [(x+80, y+120), (x+155, y+200), (x+155, y+100)])
            pg.draw.polygon(self.window, self.orange,      [(x+80, y+120), (x+155, y+100), (x+155, y+10), (x+120, y)])

        pg.draw.rect(self.window, self.white, (x, y, 160, 240), 10, 20)
        pg.draw.rect(self.window, self.black, (x, y, 160, 240),  5, 20)

        pg.draw.rect(self.window, self.white, (x + 20, y +  70, 120, 100), 0, 40)
        pg.draw.rect(self.window, self.white, (x + 20, y + 120,  50,  50), 0, 15)
        pg.draw.rect(self.window, self.white, (x + 90, y +  70,  50,  50), 0, 15)

        if self.is_color_card(symbol) and symbol not in ['block', 'invert']:
            self.draw_normal_cards_content(x, y, symbol, color)
        elif symbol == "block":
            self.draw_blocking_card_content(x, y, color)
        elif symbol == "invert":
            self.draw_reverse_card_content(x, y, color)
        elif symbol == "+4":
            self.draw_card_content_plus_4(x, y)
        elif symbol == "new color":
            self.draw_new_color_card_content(x, y)

    def round_card_edges(self, image, radius):
        width, height = image.get_size()
        mask = pg.Surface((width, height), pg.SRCALPHA)
        mask.fill((0, 0, 0, 0))

        pg.draw.rect(mask, (255, 255, 255, 255), (0, 0, width, height), border_radius=radius)
        image_with_rounded_corners = image.copy()
        image_with_rounded_corners.blit(mask, (0, 0), special_flags=pg.BLEND_RGBA_MULT)

        return image_with_rounded_corners

    def draw_table(self):
        height = self.window.get_height()
        width = self.window.get_width()
        pg.draw.circle(self.window, self.brown_5, (640, 440), 350, 20)
        pg.draw.rect(self.window, self.brown_4, (0, (height/2)-210, width, 350))
        pg.draw.rect(self.window, self.brown_4, ((width/2)-175, 0, 350, height))

        if self.game_direction == 'clockwise':
            pg.draw.polygon(self.window, self.brown_5, [((width/2)+175, (height/2)+270), ((width/2)+175, (height/2)+220), ((width/2)+225, (height/2)+270)])
            pg.draw.polygon(self.window, self.brown_5, [((width/2)-303, (height/2)+135), ((width/2)-303, (height/2)+185), ((width/2)-253, (height/2)+135)])
            pg.draw.polygon(self.window, self.brown_5, [((width/2)+302, (height/2)-210), ((width/2)+302, (height/2)-260), ((width/2)+252, (height/2)-210)])
            pg.draw.polygon(self.window, self.brown_5, [((width/2)-175, (height/2)-340), ((width/2)-225, (height/2)-340), ((width/2)-175, (height/2)-290)])
        if self.game_direction == 'counterclockwise':
            pg.draw.polygon(self.window, self.brown_5, [((width/2)+302, (height/2)+135), ((width/2)+302, (height/2)+185), ((width/2)+252, (height/2)+135)])
            pg.draw.polygon(self.window, self.brown_5, [((width/2)-175, (height/2)+270), ((width/2)-175, (height/2)+220), ((width/2)-225, (height/2)+270)])
            pg.draw.polygon(self.window, self.brown_5, [((width/2)+175, (height/2)-340), ((width/2)+225, (height/2)-340), ((width/2)+175, (height/2)-290)])
            pg.draw.polygon(self.window, self.brown_5, [((width/2)-303, (height/2)-210), ((width/2)-303, (height/2)-260), ((width/2)-253, (height/2)-210)])

        if self.player_turn == 0:
            pg.draw.rect(self.window, self.brown_2, (490, 475, 300, 260), 0, 20)
        if self.player_turn == 1:
            pg.draw.rect(self.window, self.brown_2, (330, 290, 300, 300), 0, 20)
        if self.player_turn == 2:
            pg.draw.rect(self.window, self.brown_2, (490, 150, 300, 400), 0, 20)
        if self.player_turn == 3:
            pg.draw.rect(self.window, self.brown_2, (650, 290, 300, 300), 0, 20)

        pg.draw.circle(self.window, self.brown_2, (640, 440), 200)
        pg.draw.circle(self.window, self.brown_4, (640, 440), 190)
        pg.draw.circle(self.window, self.brown_3, (640, 440), 180)

        you_text = self.font_3.render('YOU', 1, self.brown_1)
        text_x = (width/2) - (you_text.get_width() / 2)
        self.window.blit(you_text, (text_x, 650))

        will_text = self.font_3.render('Will', 1, self.brown_5)
        will_text = pg.transform.rotate(will_text, -90)
        will_text_y = (self.window.get_height()/2) - (will_text.get_height()/2) - 35
        self.window.blit(will_text, (330, will_text_y))

        cesar_text = self.font_3.render('Cesar', 1, self.brown_5)
        cesar_text_x = (self.window.get_width()/2) - (cesar_text.get_width()/2)
        self.window.blit(cesar_text, (cesar_text_x, 150))

        meg_text = self.font_3.render('Meg', 1, self.brown_5)
        meg_text = pg.transform.rotate(meg_text, 90)
        meg_text_y = (self.window.get_height()/2) - (meg_text.get_height()/2) - 35
        self.window.blit(meg_text, (850, meg_text_y))

    def pick_a_card_from_the_deck(self, player):
        if player == -1:
            for card in range(len(self.cards)):
                if self.cards[card][0] not in ['+4', '+2', '+1', 'new color', 'block', 'invert']:
                    self.table_card.append(self.cards[card])
                    self.cards.pop(card)
                    break
        elif player == 0:
            self.player_0.append(self.cards[-1])
        elif player == 1:
            self.player_1.append(self.cards[-1])
        elif player == 2:
            self.player_2.append(self.cards[-1])
        elif player == 3:
            self.player_3.append(self.cards[-1])
        self.cards.pop()

    def deal_cards(self):
        for cards in range(7):
            for player in range(4):
                self.pick_a_card_from_the_deck(player)
        self.pick_a_card_from_the_deck(-1)

    def shuffle_cards(self):
        self.cards = [['+4',None], ['+4',None], ['+4',None], ['+4',None],
                      ['0',self.blue], ['0',self.green], ['0',self.yellow], ['0',self.red],
                      ['1',self.blue], ['1',self.green], ['1',self.yellow], ['1',self.red],
                      ['1',self.blue], ['1',self.green], ['1',self.yellow], ['1',self.red],
                      ['2',self.blue], ['2',self.green], ['2',self.yellow], ['2',self.red],
                      ['2',self.blue], ['2',self.green], ['2',self.yellow], ['2',self.red],
                      ['3',self.blue], ['3',self.green], ['3',self.yellow], ['3',self.red],
                      ['3',self.blue], ['3',self.green], ['3',self.yellow], ['3',self.red],
                      ['4',self.blue], ['4',self.green], ['4',self.yellow], ['4',self.red],
                      ['4',self.blue], ['4',self.green], ['4',self.yellow], ['4',self.red],
                      ['5',self.blue], ['5',self.green], ['5',self.yellow], ['5',self.red],
                      ['5',self.blue], ['5',self.green], ['5',self.yellow], ['5',self.red],
                      ['6',self.blue], ['6',self.green], ['6',self.yellow], ['6',self.red],
                      ['6',self.blue], ['6',self.green], ['6',self.yellow], ['6',self.red],
                      ['7',self.blue], ['7',self.green], ['7',self.yellow], ['7',self.red],
                      ['7',self.blue], ['7',self.green], ['7',self.yellow], ['7',self.red],
                      ['8',self.blue], ['8',self.green], ['8',self.yellow], ['8',self.red],
                      ['8',self.blue], ['8',self.green], ['8',self.yellow], ['8',self.red],
                      ['9',self.blue], ['9',self.green], ['9',self.yellow], ['9',self.red],
                      ['9',self.blue], ['9',self.green], ['9',self.yellow], ['9',self.red],
                      ['+1',self.blue], ['+1',self.green], ['+1',self.yellow], ['+1',self.red],
                      ['+1',self.blue], ['+1',self.green], ['+1',self.yellow], ['+1',self.red],
                      ['+2',self.blue], ['+2',self.green], ['+2',self.yellow], ['+2',self.red],
                      ['+2',self.blue], ['+2',self.green], ['+2',self.yellow], ['+2',self.red],
                      ['new color',None], ['new color',None], ['new color',None], ['new color',None],
                      ['block',self.blue], ['block',self.green], ['block',self.yellow], ['block',self.red],
                      ['block',self.blue], ['block',self.green], ['block',self.yellow], ['block',self.red],
                      ['invert',self.blue], ['invert',self.green], ['invert',self.yellow], ['invert',self.red],
                      ['invert',self.blue], ['invert',self.green], ['invert',self.yellow], ['invert',self.red]]
        random.shuffle(self.cards)
        self.deal_cards()

    def can_i_play_this_card(self, card):
        if self.table_card[-1][0] == card[0]:
            return True
        elif self.table_card[-1][1] == card[1]:
            return True
        elif card[0] == 'new color':
            return True
        elif card[0] == '+4':
            return True
        else:
            return False

    def positioning_opponents_cards(self):
        width = self.window.get_width()
        height = self.window.get_height()

        # Player 1 (Will)
        player_1_cards_count = len(self.player_1)
        hand_y = ((height - (player_1_cards_count * 50)) / 2) - ((160 - 50) / 2)
        for card in range(len(self.player_1)):
            self.window.blit(self.card_back_left, (-120, hand_y + (card * 50)))

        # Player 2 (Cesar)
        player_2_cards_count = len(self.player_2)
        hand_x = ((width - (player_2_cards_count * 50)) / 2) - ((160 - 50) / 2)
        for card in range(len(self.player_2)):
            self.window.blit(self.card_back_up, (hand_x + (card * 50), -120))

        # Player 3 (Meg)
        player_3_cards_count = len(self.player_3)
        hand_y = ((height - (player_3_cards_count * 50)) / 2) - ((160 - 50) / 2)
        for card in range(len(self.player_3)):
            self.window.blit(self.card_back_right, (1160, hand_y + (card * 50)))

    def next_player(self):
        if self.game_direction == 'clockwise':
            self.player_turn += 1
        elif self.game_direction == 'counterclockwise':
            self.player_turn -= 1

        if self.player_turn == -1:
            self.player_turn = 3
        elif self.player_turn == 4:
            self.player_turn = 0

        self.play_or_pass = False

    def buy_n_cards(self, player, number_of_cards):
        for i in range(number_of_cards):
            player.append(self.cards[-1])
            self.cards.pop()

    def update_window(self):
        self.clear_window()
        self.draw_table()
        self.positioning_of_players_cards(((0, 0),(False, False, False),(False, False, False)))

    def playing_card(self, player_cards, card_index):
        if player_cards[card_index][0] == '+4' and self.player_turn != 0:
            color_options = [self.blue, self.green, self.yellow, self.red]
            self.last_color_choose = random.choice(color_options)
            player_cards[card_index][1] = self.last_color_choose
            self.next_player()
            if self.player_turn == 0:
                self.buy_n_cards(self.player_0, 4)
            if self.player_turn == 1:
                self.buy_n_cards(self.player_1, 4)
            if self.player_turn == 2:
                self.buy_n_cards(self.player_2, 4)
            if self.player_turn == 3:
                self.buy_n_cards(self.player_3, 4)
        elif player_cards[card_index][0] == 'new color' and self.player_turn != 0:
            color_options = [self.blue, self.green, self.yellow, self.red]
            self.last_color_choose = random.choice(color_options)
            player_cards[card_index][1] = self.last_color_choose
        elif player_cards[card_index][0] == '+2':
            self.next_player()
            if self.player_turn == 0:
                self.buy_n_cards(self.player_0, 2)
            if self.player_turn == 1:
                self.buy_n_cards(self.player_1, 2)
            if self.player_turn == 2:
                self.buy_n_cards(self.player_2, 2)
            if self.player_turn == 3:
                self.buy_n_cards(self.player_3, 2)
        elif player_cards[card_index][0] == '+1':
            self.next_player()
            if self.player_turn == 0:
                self.buy_n_cards(self.player_0, 1)
            if self.player_turn == 1:
                self.buy_n_cards(self.player_1, 1)
            if self.player_turn == 2:
                self.buy_n_cards(self.player_2, 1)
            if self.player_turn == 3:
                self.buy_n_cards(self.player_3, 1)
        elif player_cards[card_index][0] == 'block':
            self.next_player()
        elif player_cards[card_index][0] == 'invert':
            if self.game_direction == 'clockwise':
                self.game_direction = 'counterclockwise'
            else:
                self.game_direction = 'clockwise'
        self.table_card.append(player_cards[card_index])
        player_cards.pop(card_index)
        self.next_player()

    def buy_card(self):
        if self.player_turn == 0:
            width = self.window.get_width()
            height = self.window.get_height()

            play_text = self.font_2.render('Comprar', 1, self.white)
            text_x = (width /2)- (play_text.get_width() / 2) + 250
            text_y = (height/2) - (play_text.get_height() / 2) - 35 + 150
            button_x = (width /2)- (play_text.get_width() / 2) - 25 + 250
            button_y = (height/2) - (play_text.get_height() / 2) - 60 + 150
            button_h = play_text.get_height() + 50
            button_w = play_text.get_width() + 50
            if mouse[0][0] >= button_x and mouse[0][1] >= button_y and mouse[0][0] <= (button_x+button_w) and mouse[0][1] <= (button_y+button_h):
                hover_color = tuple(min(rgb + 50, 255) for rgb in self.green)
                pg.draw.rect(self.window, hover_color, (button_x, button_y, button_w, button_h), 0, 20)
                if mouse[2][0]:
                    try:
                        self.draw_card(button_x+(button_w/2)-80, button_y, self.cards[-1][0], self.cards[-1][1])
                        pg.display.update()
                        time.sleep(2)
                        self.player_0.append(self.cards[-1])
                        self.cards.pop()
                        self.play_or_pass = True
                    except:
                        pass
            else:
                pg.draw.rect(self.window, self.green, (button_x, button_y, button_w, button_h), 0, 20)
            self.window.blit(play_text, (text_x, text_y))

    def choose_new_color_for_the_game(self, mouse):
        x = (self.window.get_width()/2) + 100
        y = (self.window.get_height()/2) + 65
        if mouse[0][0] >= x and mouse[0][1] >= y and mouse[0][0] <= x + 45 and mouse[0][1] <= y + 45:
            hover_color = tuple(min(rgb + 50, 255) for rgb in self.blue)
            pg.draw.rect(self.window, hover_color, (x, y, 45, 45))
            if mouse[2][0]:
                self.last_color_choose = self.blue
                self.table_card[-1][1] = self.blue
                self.player_0.pop(self.next_index_card_play)
                self.next_player()
                self.next_color_button = False
        else:
            pg.draw.rect(self.window, self.blue, (x, y, 45, 45))
        if mouse[0][0] >= x + 45 and mouse[0][1] >= y and mouse[0][0] <= x + 90 and mouse[0][1] <= y + 45:
            hover_color = tuple(min(rgb + 50, 255) for rgb in self.green)
            pg.draw.rect(self.window, hover_color, (x+45, y, 45, 45))
            if mouse[2][0]:
                self.last_color_choose = self.green
                self.table_card[-1][1] = self.green
                self.player_0.pop(self.next_index_card_play)
                self.next_player()
                self.next_color_button = False
        else:
            pg.draw.rect(self.window, self.green, (x+45, y, 45, 45))
        if mouse[0][0] >= x and mouse[0][1] >= y + 45and mouse[0][0] <= x + 45 and mouse[0][1] <= y + 90:
            hover_color = tuple(min(rgb + 50, 255) for rgb in self.yellow)
            pg.draw.rect(self.window, hover_color, (x, y+45, 45, 45))
            if mouse[2][0]:
                self.last_color_choose = self.yellow
                self.table_card[-1][1] = self.yellow
                self.player_0.pop(self.next_index_card_play)
                self.next_player()
                self.next_color_button = False
        else:
            pg.draw.rect(self.window, self.yellow, (x, y+45, 45, 45))
        if mouse[0][0] >= x + 45 and mouse[0][1] >= y + 45 and mouse[0][0] <= x + 90 and mouse[0][1] <= y + 90:
            hover_color = tuple(min(rgb + 50, 255) for rgb in self.red)
            pg.draw.rect(self.window, hover_color, (x+45, y+45, 45, 45))
            if mouse[2][0]:
                self.last_color_choose = self.red
                self.table_card[-1][1] = self.red
                self.player_0.pop(self.next_index_card_play)
                self.next_player()
                self.next_color_button = False
        else:
            pg.draw.rect(self.window, self.red, (x+45, y+45, 45, 45))

        if self.table_card[-1][0] == '+4' and self.next_color_button == False:
            if self.player_turn == 1:
                for i in range(4):
                    self.player_1.append(self.cards[-1])
                    self.cards.pop()
            if self.player_turn == 3:
                for i in range(4):
                    self.player_3.append(self.cards[-1])
                    self.cards.pop()
            self.next_player()

        pg.draw.rect(self.window, self.white, (x, y, 50, 50), 5)
        pg.draw.rect(self.window, self.white, (x+45, y, 50, 50), 5)
        pg.draw.rect(self.window, self.white, (x, y+45, 50, 50), 5)
        pg.draw.rect(self.window, self.white, (x+45, y+45, 50, 50), 5)
        pg.draw.rect(self.window, self.black, (x-5, y-5, 105, 105), 5)

    def positioning_of_players_cards(self, mouse):
        width = self.window.get_width()
        height = self.window.get_height()

        # Player 0 (You)
        card_index = None
        playable_card_count = 0
        player_0_cards_count = len(self.player_0)
        hand_x = ((width - (player_0_cards_count * 75)) / 2) - ((160 - 75) / 2)
        for card in range(len(self.player_0)):
            if self.player_turn != 0:
                self.draw_card(hand_x + (card*75), 800, self.player_0[card][0], self.player_0[card][1])
            else:
                card_x_pos = hand_x + (card*75)
                if self.can_i_play_this_card(self.player_0[card]) and self.player_turn == 0:
                    self.draw_card(hand_x + (card*75), 750, self.player_0[card][0], self.player_0[card][1])
                    playable_card_count += 1
                    next_card = False
                    try:
                        next_card = self.can_i_play_this_card(self.player_0[card+1])
                    except:
                        next_card = False
                    if next_card == True:
                        if mouse[0][0] >= card_x_pos and mouse[0][1] >= 750 and mouse[0][0] <= card_x_pos + 75:
                            if mouse[2][0]:
                                card_index = card
                    else:
                        if mouse[0][0] >= card_x_pos and mouse[0][1] >= 750 and mouse[0][0] <= card_x_pos + 160:
                            if mouse[2][0]:
                                card_index = card
                else:
                    self.draw_card(hand_x + (card*75), 800, self.player_0[card][0], self.player_0[card][1])

        if card_index != None:
            if self.player_0[card_index][0] in ['+4', 'new color'] and self.next_color_button == False:
                self.next_index_card_play = card_index
                self.next_color_button = True
                self.table_card.append(self.player_0[card_index])
        if self.in_play:
            if self.next_color_button:
                self.next_color = self.choose_new_color_for_the_game(mouse)
            else:
                if card_index != None:
                    self.playing_card(self.player_0, card_index)

        if len(self.table_card) >= 1:
            self.draw_card((self.window.get_width()/2) - 80, (self.window.get_height()/2) - 155, self.table_card[-1][0], self.table_card[-1][1])
            if self.table_card[-1][0] in ['+4', 'new color']:
                if self.next_color_button == False:
                    pg.draw.circle(self.window, self.last_color_choose, ((width/2) + 120, (height/2) + 65), 20)
                    pg.draw.circle(self.window, self.white, ((width/2) + 120, (height/2) + 65), 25, 5)
                    pg.draw.circle(self.window, self.black, ((width/2) + 120, (height/2) + 65), 30, 5)

        self.positioning_opponents_cards()

        if playable_card_count == 0 and self.in_play == True and self.play_or_pass == False:
            self.buy_card()
        elif playable_card_count == 0 and self.in_play == True and self.play_or_pass == True and self.player_turn == 0:
            self.next_player()

    def opponent_move(self):
        if self.in_play:
            if self.player_turn == 1:
                if self.game_direction == 'clockwise':
                    self.update_window()
                    pg.display.update()
                    time.sleep(1)
                for card in range(len(self.player_1)):
                    if self.can_i_play_this_card(self.player_1[card]):
                        self.draw_card((self.window.get_width()/2) - 80, (self.window.get_height()/2) - 155, self.player_1[card][0], self.player_1[card][1])
                        pg.display.update()
                        time.sleep(2)
                        self.playing_card(self.player_1, card)
                        break
                if self.player_turn == 1:
                    self.player_1.append(self.cards[-1])
                    self.cards.pop()
                    for card in range(len(self.player_1)):
                        if self.can_i_play_this_card(self.player_1[card]):
                            self.draw_card((self.window.get_width()/2) - 80, (self.window.get_height()/2) - 155, self.player_1[card][0], self.player_1[card][1])
                            pg.display.update()
                            time.sleep(2)
                            self.playing_card(self.player_1, card)
                            break
                if self.player_turn == 1:
                    self.update_window()
                    if self.game_direction != 'clockwise':
                        time.sleep(2)
                    self.next_player()
            elif self.player_turn == 2:
                self.update_window()
                pg.display.update()
                time.sleep(1)
                for card in range(len(self.player_2)):
                    if self.can_i_play_this_card(self.player_2[card]):
                        self.draw_card((self.window.get_width()/2) - 80, (self.window.get_height()/2) - 155, self.player_2[card][0], self.player_2[card][1])
                        pg.display.update()
                        time.sleep(2)
                        self.playing_card(self.player_2, card)
                        break
                if self.player_turn == 2:
                    self.player_2.append(self.cards[-1])
                    self.cards.pop()
                    for card in range(len(self.player_2)):
                        if self.can_i_play_this_card(self.player_2[card]):
                            self.draw_card((self.window.get_width()/2) - 80, (self.window.get_height()/2) - 155, self.player_2[card][0], self.player_2[card][1])
                            pg.display.update()
                            time.sleep(2)
                            self.playing_card(self.player_2, card)
                            break
                if self.player_turn == 2:
                    self.update_window()
                    time.sleep(2)
                    self.next_player()
            elif self.player_turn == 3:
                self.update_window()
                pg.display.update()
                time.sleep(1)
                for card in range(len(self.player_3)):
                    if self.can_i_play_this_card(self.player_3[card]):
                        self.draw_card((self.window.get_width()/2) - 80, (self.window.get_height()/2) - 155, self.player_3[card][0], self.player_3[card][1])
                        pg.display.update()
                        time.sleep(2)
                        self.playing_card(self.player_3, card)
                        break
                if self.player_turn == 3:
                    self.player_3.append(self.cards[-1])
                    self.cards.pop()
                    for card in range(len(self.player_3)):
                        if self.can_i_play_this_card(self.player_3[card]):
                            self.draw_card((self.window.get_width()/2) - 80, (self.window.get_height()/2) - 155, self.player_3[card][0], self.player_3[card][1])
                            pg.display.update()
                            time.sleep(2)
                            self.playing_card(self.player_3, card)
                            break
                if self.player_turn == 3:
                    self.update_window()
                    if self.game_direction != 'counterclockwise':
                        time.sleep(2)
                    self.next_player()

    def do_we_have_a_winner(self):
        if self.in_play:
            if len(self.player_0) == 0:
                self.in_play = False
                self.winner = 'Você ganhou!'
            if len(self.player_1) == 0:
                self.in_play = False
                self.winner = 'Will ganhou!'
            if len(self.player_2) == 0:
                self.in_play = False
                self.winner = 'Cesar ganhou!'
            if len(self.player_3) == 0:
                self.in_play = False
                self.winner = 'Meg ganhou!'

    def restart_game(self):
        self.last_color_choose = None
        self.next_color_button = False
        self.next_index_card_play = None
        self.in_play = True
        self.player_turn = 0
        self.winner = None
        self.play_or_pass = False
        self.game_direction = 'clockwise'
        self.table_card = []
        self.player_0 = []
        self.player_1 = []
        self.player_2 = []
        self.player_3 = []
        self.shuffle_cards()

    def winner_announcement(self):
        if self.winner != None and self.in_play == False:
            height = self.window.get_height()
            width = self.window.get_width()
            winner_text = self.font_2.render(self.winner, 1, self.white)
            winner_text_x = (width /2)- (winner_text.get_width() / 2)
            winner_text_y = (height/2) - (winner_text.get_height() / 2) - 35 - 200
            button_x = (width /2)- (winner_text.get_width() / 2) - 25
            button_y = (height/2) - (winner_text.get_height() / 2) - 60 - 200
            button_h = winner_text.get_height() + 50
            button_w = winner_text.get_width() + 50
            pg.draw.rect(self.window, self.green, (button_x, button_y, button_w, button_h), 0, 20)
            pg.draw.rect(self.window, self.white, (button_x, button_y, button_w, button_h), 10, 20)
            pg.draw.rect(self.window, self.black, (button_x, button_y, button_w, button_h), 5, 20)
            self.window.blit(winner_text, (winner_text_x, winner_text_y))

    def restart_game_menu(self, mouse):
        if self.in_play == False:
            height = self.window.get_height()
            width = self.window.get_width()
            if self.winner == None:
                play_text = self.font_1.render('Jogar', 1, self.white)
            else:
                play_text = self.font_1.render('Restart', 1, self.white)
            text_x = (width /2)- (play_text.get_width() / 2)
            text_y = (height/2) - (play_text.get_height() / 2) - 35
            button_x = (width /2)- (play_text.get_width() / 2) - 25
            button_y = (height/2) - (play_text.get_height() / 2) - 60
            button_h = play_text.get_height() + 50
            button_w = play_text.get_width() + 50
            if mouse[0][0] >= button_x and mouse[0][1] >= button_y and mouse[0][0] <= (button_x+button_w) and mouse[0][1] <= (button_y+button_h):
                hover_color = tuple(min(rgb + 50, 255) for rgb in self.green)
                pg.draw.rect(self.window, hover_color, (button_x, button_y, button_w, button_h), 0, 20)
                if mouse[2][0]:
                    self.restart_game()
            else:
                pg.draw.rect(self.window, self.green, (button_x, button_y, button_w, button_h), 0, 20)
            self.window.blit(play_text, (text_x, text_y))


jogo = Uno((1280, 950))


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
    jogo.draw_table()
    jogo.positioning_of_players_cards(mouse)
    jogo.opponent_move()
    jogo.do_we_have_a_winner()
    jogo.winner_announcement()
    jogo.restart_game_menu(mouse)

    jogo.last_click_status = mouse_input

    pg.display.update()
