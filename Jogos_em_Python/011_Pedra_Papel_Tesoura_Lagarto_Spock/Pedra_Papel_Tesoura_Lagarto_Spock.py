import pygame as pg
import random


class PPTLS:
    def __init__(self, window_size):
        self.white = (255, 255, 255)
        self.black = (  0,   0,   0)

        self.window = pg.display.set_mode(window_size)

        pg.font.init()
        self.font_1 = pg.font.SysFont("Courier New", 300, bold=True)
        self.font_2 = pg.font.SysFont("Courier New", 40, bold=True)

        self.clock = pg.time.Clock()

        # Mouse variables
        self.last_click_status = (False, False, False)

        self.actions = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        self.action = None
        self.adversary_action = None

        # Rock
        self.rock_jpg = pg.image.load('./rock.png')
        self.rock_img = pg.transform.scale(self.rock_jpg, (300, 300))
        self.rock_img_action = pg.transform.scale(self.rock_jpg, (100, 100))
        # Paper
        self.paper_jpg = pg.image.load('./paper.png')
        self.paper_img = pg.transform.scale(self.paper_jpg, (300, 300))
        self.paper_img_action = pg.transform.scale(self.paper_jpg, (100, 100))
        # Scissors
        self.scissors_jpg = pg.image.load('./scissors.png')
        self.scissors_img = pg.transform.scale(self.scissors_jpg, (300, 300))
        self.scissors_img_action = pg.transform.scale(self.scissors_jpg, (100, 100))
        # Lizard
        self.lizard_jpg = pg.image.load('./lizard.png')
        self.lizard_img = pg.transform.scale(self.lizard_jpg, (300, 300))
        self.lizard_img_action = pg.transform.scale(self.lizard_jpg, (100, 100))
        # Spock
        self.spock_jpg = pg.image.load('./spock.png')
        self.spock_img = pg.transform.scale(self.spock_jpg, (300, 300))
        self.spock_img_action = pg.transform.scale(self.spock_jpg, (100, 100))

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

    def board(self):
        pg.draw.circle(self.window, self.black, (375, 200), 150, 5)
        question_text = self.font_1.render('?', 1, self.black)
        blit_x = (self.window.get_width() / 2) - (question_text.get_width() / 2)
        blit_y = 200 - (question_text.get_height() / 2)
        self.window.blit(question_text, (blit_x, blit_y))

        pg.draw.circle(self.window, self.black, (375, 550), 150, 5)
        question_text = self.font_1.render('?', 1, self.black)
        blit_x = (self.window.get_width() / 2) - (question_text.get_width() / 2)
        blit_y = 550 - (question_text.get_height() / 2)
        self.window.blit(question_text, (blit_x, blit_y))

        self.window.blit(self.rock_img_action, (42, 750))
        self.window.blit(self.paper_img_action, (184, 750))
        self.window.blit(self.scissors_img_action, (326, 750))
        self.window.blit(self.lizard_img_action, (470, 750))
        self.window.blit(self.spock_img_action, (612, 750))

    def random_action(self):
        action = random.randint(0, 4)
        self.adversary_action = self.actions[action]

    def adversary_selected_play(self):
        if self.adversary_action == 'rock':
            self.window.blit(self.rock_img, (225, 50))
        elif self.adversary_action == 'paper':
            self.window.blit(self.paper_img, (225, 50))
        elif self.adversary_action == 'scissors':
            self.window.blit(self.scissors_img, (225, 50))
        elif self.adversary_action == 'lizard':
            self.window.blit(self.lizard_img, (225, 50))
        elif self.adversary_action == 'spock':
            self.window.blit(self.spock_img, (225, 50))

    def selected_play(self):
        if self.action == 'rock':
            self.window.blit(self.rock_img, (225, 400))
        elif self.action == 'paper':
            self.window.blit(self.paper_img, (225, 400))
        elif self.action == 'scissors':
            self.window.blit(self.scissors_img, (225, 400))
        elif self.action == 'lizard':
            self.window.blit(self.lizard_img, (225, 400))
        elif self.action == 'spock':
            self.window.blit(self.spock_img, (225, 400))

    def actions_buttons(self, mouse):
        if mouse[0][0] >= 32 and mouse[0][0] <= 152 and mouse[0][1] >= 740 and mouse[0][1] <= 860:
            pg.draw.rect(self.window, self.black, (32, 740, 120, 120))
            if mouse[2][0] == True:
                self.random_action()
                self.action = 'rock'
        if mouse[0][0] >= 174 and mouse[0][0] <= 294 and mouse[0][1] >= 740 and mouse[0][1] <= 860:
            pg.draw.rect(self.window, self.black, (174, 740, 120, 120))
            if mouse[2][0] == True:
                self.random_action()
                self.action = 'paper'
        if mouse[0][0] >= 316 and mouse[0][0] <= 436 and mouse[0][1] >= 740 and mouse[0][1] <= 860:
            pg.draw.rect(self.window, self.black, (316, 740, 120, 120))
            if mouse[2][0] == True:
                self.random_action()
                self.action = 'scissors'
        if mouse[0][0] >= 460 and mouse[0][0] <= 580 and mouse[0][1] >= 740 and mouse[0][1] <= 860:
            pg.draw.rect(self.window, self.black, (460, 740, 120, 120))
            if mouse[2][0] == True:
                self.random_action()
                self.action = 'lizard'
        if mouse[0][0] >= 602 and mouse[0][0] <= 722 and mouse[0][1] >= 740 and mouse[0][1] <= 860:
            pg.draw.rect(self.window, self.black, (602, 740, 120, 120))
            if mouse[2][0] == True:
                self.random_action()
                self.action = 'spock'

    def match_result_text(self, is_victory, result):
        if is_victory != None:
            if is_victory:
                victory_text = self.font_2.render('Você ganhou!', 1, self.black)
            else:
                victory_text = self.font_2.render('Você perdeu', 1, self.black)

            result_text = self.font_2.render(result, 1, self.black)

            blit_victory_x = (self.window.get_width() / 2) - (victory_text.get_width() / 2)
            blit_victory_y = (self.window.get_height() / 2) - victory_text.get_height() - 100
            blit_result_x = (self.window.get_width() / 2) - (result_text.get_width() / 2)
            blit_result_y = (self.window.get_height() / 2) + result_text.get_height() - 100

            self.window.blit(victory_text, (blit_victory_x, blit_victory_y))
            self.window.blit(result_text, (blit_result_x, blit_result_y))
        else:
            result_text = self.font_2.render('Empate!', 1, self.black)

            blit_result_x = (self.window.get_width() / 2) - (result_text.get_width() / 2)
            blit_result_y = (self.window.get_height() / 2) + (result_text.get_height() / 2) - 120

            self.window.blit(result_text, (blit_result_x, blit_result_y))

    def match_result(self):
        if self.adversary_action == 'scissors' and self.action == 'paper':
            self.match_result_text(False, 'Tesoura corta o papel')
        elif self.adversary_action == 'paper' and self.action == 'scissors':
            self.match_result_text(True, 'Tesoura corta o papel')
        elif self.adversary_action == 'paper' and self.action == 'rock':
            self.match_result_text(False, 'Papel cobre a pedra')
        elif self.adversary_action == 'rock' and self.action == 'paper':
            self.match_result_text(True, 'Papel cobre a pedra')
        elif self.adversary_action == 'rock' and self.action == 'lizard':
            self.match_result_text(False, 'Pedra esmaga o lagarto')
        elif self.adversary_action == 'lizard' and self.action == 'rock':
            self.match_result_text(True, 'Pedra esmaga o lagarto')
        elif self.adversary_action == 'lizard' and self.action == 'spock':
            self.match_result_text(False, 'Lagarto envenena o Spock')
        elif self.adversary_action == 'spock' and self.action == 'lizard':
            self.match_result_text(True, 'Lagarto envenena o Spock')
        elif self.adversary_action == 'spock' and self.action == 'scissors':
            self.match_result_text(False, 'Spock quebra a tesoura')
        elif self.adversary_action == 'scissors' and self.action == 'spock':
            self.match_result_text(True, 'Spock quebra a tesoura')
        elif self.adversary_action == 'scissors' and self.action == 'lizard':
            self.match_result_text(False, 'Tesoura decapita o lagarto')
        elif self.adversary_action == 'lizard' and self.action == 'scissors':
            self.match_result_text(True, 'Tesoura decapita o lagarto')
        elif self.adversary_action == 'lizard' and self.action == 'paper':
            self.match_result_text(False, 'Lagarto come o papel')
        elif self.adversary_action == 'paper' and self.action == 'lizard':
            self.match_result_text(True, 'Lagarto come o papel')
        elif self.adversary_action == 'paper' and self.action == 'spock':
            self.match_result_text(False, 'Papel refuta o Spock')
        elif self.adversary_action == 'spock' and self.action == 'paper':
            self.match_result_text(True, 'Papel refuta o Spock')
        elif self.adversary_action == 'spock' and self.action == 'rock':
            self.match_result_text(False, 'Spock vaporiza a pedra')
        elif self.adversary_action == 'rock' and self.action == 'spock':
            self.match_result_text(True, 'Spock vaporiza a pedra')
        elif self.adversary_action == 'rock' and self.action == 'scissors':
            self.match_result_text(False, 'Pedra amassa a tesoura')
        elif self.adversary_action == 'scissors' and self.action == 'rock':
            self.match_result_text(True, 'Pedra amassa a tesoura')
        elif self.adversary_action == self.action and self.action != None:
            self.match_result_text(None, '')


pptls = PPTLS((750, 900))


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
    mouse_click = pptls.mouse_has_clicked(mouse_input)
    mouse = (mouse_position, mouse_input, mouse_click)

    # Game
    pptls.clock.tick(60)
    pptls.clear_window()
    pptls.actions_buttons(mouse)
    pptls.board()
    pptls.adversary_selected_play()
    pptls.selected_play()
    pptls.match_result()

    pptls.last_click_status = mouse_input

    pg.display.update()
