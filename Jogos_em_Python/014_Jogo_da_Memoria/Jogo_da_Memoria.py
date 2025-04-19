import pygame as pg
import random
import time


class JogoDaMemoria:
    def __init__(self):
        self.white        = (255, 255, 255)
        self.black        = (  0,   0,   0)
        self.red          = (255,   0,   0)
        self.green        = (  0, 255,   0)
        self.green_light  = (180, 255, 180)

        self.window = pg.display.set_mode((1050, 850))

        pg.font.init()
        self.font = pg.font.SysFont("Courier New", 100, bold=True)

        # Mouse variables
        self.last_click_status = (False, False, False)

        # Game variables
        self.shuffle_cards = True
        self.cards_in_play = []
        self.restart_option = False

        self.cards = [['#', '#', '#', '#', '#'],
                      ['#', '#', '#', '#', '#'],
                      ['#', '#', '#', '#', '#'],
                      ['#', '#', '#', '#', '#']]

        self.cards_map = [['', '', '', '', ''],
                          ['', '', '', '', ''],
                          ['', '', '', '', ''],
                          ['', '', '', '', '']]

        # Cards
        card_down = pg.image.load('./Carta para baixo.png')
        card_up   = pg.image.load('./Carta para cima.png')
        card_0    = pg.image.load('./GalaxyBrain.png')
        card_1    = pg.image.load('./GitHubSponsorBadge.png')
        card_2    = pg.image.load('./HeartOnYourSleeve.png')
        card_3    = pg.image.load('./OpenSourcerer.png')
        card_4    = pg.image.load('./PairExtraordinaire.png')
        card_5    = pg.image.load('./PullShark.png')
        card_6    = pg.image.load('./QuickDraw.png')
        card_7    = pg.image.load('./StarStruck_Gold.png')
        card_8    = pg.image.load('./StarStruck.png')
        card_9   = pg.image.load('./YOLO_Badge.png')
        self.card_down = pg.transform.scale(card_down, (150, 150)) # '#'
        self.card_up   = pg.transform.scale(card_up  , (150, 150))
        self.card_0    = pg.transform.scale(card_0   , (100, 100)) # '0'
        self.card_1    = pg.transform.scale(card_1   , (100, 100)) # '1'
        self.card_2    = pg.transform.scale(card_2   , (100, 100)) # '2'
        self.card_3    = pg.transform.scale(card_3   , (100, 100)) # '3'
        self.card_4    = pg.transform.scale(card_4   , (100, 100)) # '4'
        self.card_5    = pg.transform.scale(card_5   , (100, 100)) # '5'
        self.card_6    = pg.transform.scale(card_6   , (100, 100)) # '6'
        self.card_7    = pg.transform.scale(card_7   , (100, 100)) # '7'
        self.card_8    = pg.transform.scale(card_8   , (100, 100)) # '8'
        self.card_9    = pg.transform.scale(card_9   , (100, 100)) # '9'

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
        pg.draw.rect(self.window, self.white, (0, 0, self.window.get_width(), self.window.get_height()))

    def blit_card(self, card, x, y):
        card_x_pos = 50 + ((150 + 50) * x)
        card_y_pos = 50 + ((150 + 50) * y)
        if card == '#':
            self.window.blit(self.card_down, (card_x_pos, card_y_pos))
        elif card == '':
            pass
        else:
            self.window.blit(self.card_up, (card_x_pos, card_y_pos))
            img_x_pos = 50 + ((150 + 50) * x - 1) + 25
            img_y_pos = 50 + ((150 + 50) * y - 1) + 25
            if card == '0':
                self.window.blit(self.card_0, (img_x_pos, img_y_pos))
            elif card == '1':
                self.window.blit(self.card_1, (img_x_pos, img_y_pos))
            elif card == '2':
                self.window.blit(self.card_2, (img_x_pos, img_y_pos))
            elif card == '3':
                self.window.blit(self.card_3, (img_x_pos, img_y_pos))
            elif card == '4':
                self.window.blit(self.card_4, (img_x_pos, img_y_pos))
            elif card == '5':
                self.window.blit(self.card_5, (img_x_pos, img_y_pos))
            elif card == '6':
                self.window.blit(self.card_6, (img_x_pos, img_y_pos))
            elif card == '7':
                self.window.blit(self.card_7, (img_x_pos, img_y_pos))
            elif card == '8':
                self.window.blit(self.card_8, (img_x_pos, img_y_pos))
            elif card == '9':
                self.window.blit(self.card_9, (img_x_pos, img_y_pos))

    def board(self):
        for y in range(len(self.cards)):
            for x in range(len(self.cards[0])):
                self.blit_card(self.cards[y][x], x, y)

    def place_card_in_first_empty_space(self, card):
        for y in range(len(self.cards_map)):
            for x in range(len(self.cards_map[0])):
                if self.cards_map[y][x] == '':
                    self.cards_map[y][x] = str(card)
                    return

    def shuffling_cards(self):
        if self.shuffle_cards:
            for card in range(20):
                card_pos = random.randint(0, 19)
                card_count = 0
                for y in range(len(self.cards_map)):
                    for x in range(len(self.cards_map[0])):
                        if card_count == card_pos and self.cards_map[y][x] == '':
                            self.cards_map[y][x] = str(card//2)
                        elif card_count == card_pos and self.cards_map[y][x] != '':
                            self.place_card_in_first_empty_space(card//2)
                        card_count += 1

            self.shuffle_cards = False

    def card_selection(self, mouse):
        for y in range(len(self.cards)):
            for x in range(len(self.cards[0])):
                if self.cards[y][x] == '#':
                    card_x_pos = 50 + ((150 + 50) * x)
                    card_y_pos = 50 + ((150 + 50) * y)
                    if mouse[0][0] >= card_x_pos and mouse[0][1] >= card_y_pos and mouse[0][0] <= card_x_pos + 150 and mouse[0][1] <= card_y_pos + 150:
                        pg.draw.rect(self.window, self.red, (card_x_pos - 15, card_y_pos - 15, 180, 180), 10, 30)
                        if mouse[2][0] == True:
                            self.cards_in_play.append([x, y])
                            self.cards[y][x] = self.cards_map[y][x]

    def card_combinations(self):
        if len(self.cards_in_play) == 2:
            card_1_x = self.cards_in_play[0][0]
            card_1_y = self.cards_in_play[0][1]
            card_2_x = self.cards_in_play[1][0]
            card_2_y = self.cards_in_play[1][1]
            self.board()
            pg.display.update()
            time.sleep(1)
            if self.cards_map[card_1_y][card_1_x] == self.cards_map[card_2_y][card_2_x]:
                self.cards[card_1_y][card_1_x] = ''
                self.cards[card_2_y][card_2_x] = ''
            else:
                self.cards[card_1_y][card_1_x] = '#'
                self.cards[card_2_y][card_2_x] = '#'
            self.cards_in_play = []

    def end_of_game(self):
        if self.restart_option == False:
            count_cards = 0
            for y in range(len(self.cards)):
                for x in range(len(self.cards[0])):
                    if self.cards[y][x] == '':
                        count_cards += 1
            if count_cards == 20:
                self.restart_option = True

    def restart_game(self):
        for y in range(len(self.cards)):
            for x in range(len(self.cards[0])):
                self.cards[y][x] = '#'
                self.cards_map[y][x] = ''
        self.restart_option = False
        self.shuffle_cards = True
        self.cards_in_play = []

    def restart_button(self, mouse):
        if self.restart_option:
            restart_text = self.font.render('Restart', 1, self.black)
            box_width = restart_text.get_width() + 100
            box_height = restart_text.get_height() + 100
            box_x = (self.window.get_width() / 2) - (box_width / 2)
            box_y = (self.window.get_height() / 2) - (box_height / 2)
            if mouse[0][0] >= box_x and mouse[0][1] >= box_y and mouse[0][0] <= box_x + box_width and mouse[0][1] <= box_y + box_height:
                pg.draw.rect(self.window, self.green_light, (box_x, box_y, box_width, box_height))
                if mouse[2][0]:
                    self.restart_game()
            else:
                pg.draw.rect(self.window, self.green, (box_x, box_y, box_width, box_height))

            pg.draw.rect(self.window, self.black, (box_x, box_y, box_width, box_height), 5)

            blit_x = (self.window.get_width() / 2) - (restart_text.get_width() / 2)
            blit_y = (self.window.get_height() / 2) - (restart_text.get_height() / 2)
            self.window.blit(restart_text, (blit_x, blit_y))


jogo = JogoDaMemoria()


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
    jogo.clear_window()

    jogo.shuffling_cards()
    jogo.board()
    jogo.card_selection(mouse)
    jogo.card_combinations()
    jogo.end_of_game()
    jogo.restart_button(mouse)

    jogo.last_click_status = mouse_input

    pg.display.update()
