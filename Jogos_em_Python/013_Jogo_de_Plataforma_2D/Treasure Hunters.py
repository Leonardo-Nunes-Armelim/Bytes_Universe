import pygame as pg


class TreasureHunters:
    def __init__(self):
        self.white        = (255, 255, 255)
        self.black        = (  0,   0,   0)
        self.purple_dark  = (181, 181, 255)
        self.purple_light = (230, 230, 255)
        self.green        = (  0, 255,   0)
        self.green_light  = (180, 255, 180)
        self.blue         = (  0,   0, 255)

        self.window = pg.display.set_mode((1280, 768))

        pg.font.init()
        self.font = pg.font.SysFont("Courier New", 50, bold=True)

        self.clock = pg.time.Clock()

        self.map = [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1','3',' ','1','2','2'],
                    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1','2','3',' ','7','9',' ','4','5','5'],
                    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','7','8','9',' ',' ',' ',' ','4','5','5'],
                    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','4','5','5'],
                    ['2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','5','5','5']]

        self.gravity = 1

        self.big_clouds_pos = 0
        self.small_cloud_1_pos = 0
        self.small_cloud_2_pos = 0
        self.small_cloud_3_pos = 0
        
        self.player_animation = 0
        self.player_animation_frame = 0
        self.player_pos = [300, 600]
        self.player_jump_force = -22
        self.player_vertical_speed = 0
        self.player_box_colider = [46, 54]

        # Mouse variables
        self.last_click_status = (False, False, False)

        # Captain Clown Nose (Idle)
        player_idle_1_img = pg.image.load('./Sprites/Captain Clown Nose/Captain Clown Nose without Sword/01-Idle/Idle 01.png')
        self.player_idle_1 = pg.transform.scale(player_idle_1_img, (128, 80))
        player_idle_2_img = pg.image.load('./Sprites/Captain Clown Nose/Captain Clown Nose without Sword/01-Idle/Idle 02.png')
        self.player_idle_2 = pg.transform.scale(player_idle_2_img, (128, 80))
        player_idle_3_img = pg.image.load('./Sprites/Captain Clown Nose/Captain Clown Nose without Sword/01-Idle/Idle 03.png')
        self.player_idle_3 = pg.transform.scale(player_idle_3_img, (128, 80))
        player_idle_4_img = pg.image.load('./Sprites/Captain Clown Nose/Captain Clown Nose without Sword/01-Idle/Idle 04.png')
        self.player_idle_4 = pg.transform.scale(player_idle_4_img, (128, 80))
        player_idle_5_img = pg.image.load('./Sprites/Captain Clown Nose/Captain Clown Nose without Sword/01-Idle/Idle 05.png')
        self.player_idle_5 = pg.transform.scale(player_idle_5_img, (128, 80))
        # Captain Clown Nose (Idle left)
        player_idle_left_1_img = pg.image.load('./Sprites/Captain Clown Nose/Captain Clown Nose without Sword/01-Idle/Idle 01.png')
        player_idle_left_1_img = pg.transform.flip(player_idle_left_1_img, True, False)
        self.player_idle_left_1 = pg.transform.scale(player_idle_left_1_img, (128, 80))
        player_idle_left_2_img = pg.image.load('./Sprites/Captain Clown Nose/Captain Clown Nose without Sword/01-Idle/Idle 02.png')
        player_idle_left_2_img = pg.transform.flip(player_idle_left_2_img, True, False)
        self.player_idle_left_2 = pg.transform.scale(player_idle_left_2_img, (128, 80))
        player_idle_left_3_img = pg.image.load('./Sprites/Captain Clown Nose/Captain Clown Nose without Sword/01-Idle/Idle 03.png')
        player_idle_left_3_img = pg.transform.flip(player_idle_left_3_img, True, False)
        self.player_idle_left_3 = pg.transform.scale(player_idle_left_3_img, (128, 80))
        player_idle_left_4_img = pg.image.load('./Sprites/Captain Clown Nose/Captain Clown Nose without Sword/01-Idle/Idle 04.png')
        player_idle_left_4_img = pg.transform.flip(player_idle_left_4_img, True, False)
        self.player_idle_left_4 = pg.transform.scale(player_idle_left_4_img, (128, 80))
        player_idle_left_5_img = pg.image.load('./Sprites/Captain Clown Nose/Captain Clown Nose without Sword/01-Idle/Idle 05.png')
        player_idle_left_5_img = pg.transform.flip(player_idle_left_5_img, True, False)
        self.player_idle_left_5 = pg.transform.scale(player_idle_left_5_img, (128, 80))
        # Captain Clown Nose (Run right)
        player_right_1_img = pg.image.load('./Sprites/Captain Clown Nose/Captain Clown Nose without Sword/02-Run/Run 01.png')
        self.player_right_1 = pg.transform.scale(player_right_1_img, (128, 80))
        player_right_2_img = pg.image.load('./Sprites/Captain Clown Nose/Captain Clown Nose without Sword/02-Run/Run 02.png')
        self.player_right_2 = pg.transform.scale(player_right_2_img, (128, 80))
        player_right_3_img = pg.image.load('./Sprites/Captain Clown Nose/Captain Clown Nose without Sword/02-Run/Run 03.png')
        self.player_right_3 = pg.transform.scale(player_right_3_img, (128, 80))
        player_right_4_img = pg.image.load('./Sprites/Captain Clown Nose/Captain Clown Nose without Sword/02-Run/Run 04.png')
        self.player_right_4 = pg.transform.scale(player_right_4_img, (128, 80))
        player_right_5_img = pg.image.load('./Sprites/Captain Clown Nose/Captain Clown Nose without Sword/02-Run/Run 05.png')
        self.player_right_5 = pg.transform.scale(player_right_5_img, (128, 80))
        player_right_6_img = pg.image.load('./Sprites/Captain Clown Nose/Captain Clown Nose without Sword/02-Run/Run 06.png')
        self.player_right_6 = pg.transform.scale(player_right_6_img, (128, 80))
        # Captain Clown Nose (Run left)
        player_left_1_img = pg.image.load('./Sprites/Captain Clown Nose/Captain Clown Nose without Sword/02-Run/Run 01.png')
        player_left_1_img = pg.transform.flip(player_left_1_img, True, False)
        self.player_left_1 = pg.transform.scale(player_left_1_img, (128, 80))
        player_left_2_img = pg.image.load('./Sprites/Captain Clown Nose/Captain Clown Nose without Sword/02-Run/Run 02.png')
        player_left_2_img = pg.transform.flip(player_left_2_img, True, False)
        self.player_left_2 = pg.transform.scale(player_left_2_img, (128, 80))
        player_left_3_img = pg.image.load('./Sprites/Captain Clown Nose/Captain Clown Nose without Sword/02-Run/Run 03.png')
        player_left_3_img = pg.transform.flip(player_left_3_img, True, False)
        self.player_left_3 = pg.transform.scale(player_left_3_img, (128, 80))
        player_left_4_img = pg.image.load('./Sprites/Captain Clown Nose/Captain Clown Nose without Sword/02-Run/Run 04.png')
        player_left_4_img = pg.transform.flip(player_left_4_img, True, False)
        self.player_left_4 = pg.transform.scale(player_left_4_img, (128, 80))
        player_left_5_img = pg.image.load('./Sprites/Captain Clown Nose/Captain Clown Nose without Sword/02-Run/Run 05.png')
        player_left_5_img = pg.transform.flip(player_left_5_img, True, False)
        self.player_left_5 = pg.transform.scale(player_left_5_img, (128, 80))
        player_left_6_img = pg.image.load('./Sprites/Captain Clown Nose/Captain Clown Nose without Sword/02-Run/Run 06.png')
        player_left_6_img = pg.transform.flip(player_left_6_img, True, False)
        self.player_left_6 = pg.transform.scale(player_left_6_img, (128, 80))
        # Background
        background_img = pg.image.load('./Sprites/Palm Tree Island/Background/BG Image.png')
        self.background = pg.transform.scale(background_img, (1280, 768))
        big_clouds_img = pg.image.load('./Sprites/Palm Tree Island/Background/Big Clouds.png')
        self.big_clouds = pg.transform.scale(big_clouds_img, (896, 202))
        # Clouds
        small_cloud_1_img = pg.image.load('./Sprites/Palm Tree Island/Background/Small Cloud 1.png')
        self.small_cloud_1 = pg.transform.scale(small_cloud_1_img, (148, 48))
        small_cloud_2_img = pg.image.load('./Sprites/Palm Tree Island/Background/Small Cloud 2.png')
        self.small_cloud_2 = pg.transform.scale(small_cloud_2_img, (266, 70))
        small_cloud_3_img = pg.image.load('./Sprites/Palm Tree Island/Background/Small Cloud 3.png')
        self.small_cloud_3 = pg.transform.scale(small_cloud_3_img, (280, 78))
        # Water (Big)
        self.big_water_animation_frame = 0
        big_water_1_img = pg.image.load('./Sprites/Palm Tree Island/Background/Water Reflect Big 01.png')
        self.big_water_1 = pg.transform.scale(big_water_1_img, (340, 20))
        big_water_2_img = pg.image.load('./Sprites/Palm Tree Island/Background/Water Reflect Big 02.png')
        self.big_water_2 = pg.transform.scale(big_water_2_img, (340, 20))
        big_water_3_img = pg.image.load('./Sprites/Palm Tree Island/Background/Water Reflect Big 03.png')
        self.big_water_3 = pg.transform.scale(big_water_3_img, (340, 20))
        big_water_4_img = pg.image.load('./Sprites/Palm Tree Island/Background/Water Reflect Big 04.png')
        self.big_water_4 = pg.transform.scale(big_water_4_img, (340, 20))
        # Water (Medium)
        self.medium_water_animation_frame = 0
        medium_water_1_img = pg.image.load('./Sprites/Palm Tree Island/Background/Water Reflect Medium 01.png')
        self.medium_water_1 = pg.transform.scale(medium_water_1_img, (106, 6))
        medium_water_2_img = pg.image.load('./Sprites/Palm Tree Island/Background/Water Reflect Medium 02.png')
        self.medium_water_2 = pg.transform.scale(medium_water_2_img, (106, 6))
        medium_water_3_img = pg.image.load('./Sprites/Palm Tree Island/Background/Water Reflect Medium 03.png')
        self.medium_water_3 = pg.transform.scale(medium_water_3_img, (106, 6))
        medium_water_4_img = pg.image.load('./Sprites/Palm Tree Island/Background/Water Reflect Medium 04.png')
        self.medium_water_4 = pg.transform.scale(medium_water_4_img, (106, 6))
        # Water (Small)
        self.small_water_animation_frame = 0
        small_water_1_img = pg.image.load('./Sprites/Palm Tree Island/Background/Water Reflect Small 01.png')
        self.small_water_1 = pg.transform.scale(small_water_1_img, (70, 6))
        small_water_2_img = pg.image.load('./Sprites/Palm Tree Island/Background/Water Reflect Small 02.png')
        self.small_water_2 = pg.transform.scale(small_water_2_img, (70, 6))
        small_water_3_img = pg.image.load('./Sprites/Palm Tree Island/Background/Water Reflect Small 03.png')
        self.small_water_3 = pg.transform.scale(small_water_3_img, (70, 6))
        small_water_4_img = pg.image.load('./Sprites/Palm Tree Island/Background/Water Reflect Small 04.png')
        self.small_water_4 = pg.transform.scale(small_water_4_img, (70, 6))
        # Terrain
        ground_1_img = pg.image.load('./Sprites/Palm Tree Island/Terrain/ground_1.png')
        self.ground_1 = pg.transform.scale(ground_1_img, (64, 64))
        ground_2_img = pg.image.load('./Sprites/Palm Tree Island/Terrain/ground_2.png')
        self.ground_2 = pg.transform.scale(ground_2_img, (64, 64))
        ground_3_img = pg.image.load('./Sprites/Palm Tree Island/Terrain/ground_3.png')
        self.ground_3 = pg.transform.scale(ground_3_img, (64, 64))
        ground_4_img = pg.image.load('./Sprites/Palm Tree Island/Terrain/ground_4.png')
        self.ground_4 = pg.transform.scale(ground_4_img, (64, 64))
        ground_5_img = pg.image.load('./Sprites/Palm Tree Island/Terrain/ground_5.png')
        self.ground_5 = pg.transform.scale(ground_5_img, (64, 64))
        ground_6_img = pg.image.load('./Sprites/Palm Tree Island/Terrain/ground_6.png')
        self.ground_6 = pg.transform.scale(ground_6_img, (64, 64))
        ground_7_img = pg.image.load('./Sprites/Palm Tree Island/Terrain/ground_7.png')
        self.ground_7 = pg.transform.scale(ground_7_img, (64, 64))
        ground_8_img = pg.image.load('./Sprites/Palm Tree Island/Terrain/ground_8.png')
        self.ground_8 = pg.transform.scale(ground_8_img, (64, 64))
        ground_9_img = pg.image.load('./Sprites/Palm Tree Island/Terrain/ground_9.png')
        self.ground_9 = pg.transform.scale(ground_9_img, (64, 64))


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

    def background_imgs(self):
        # Background
        self.window.blit(self.background, (0, 0))
        # Big Clouds
        if self.big_clouds_pos > -896:
            self.big_clouds_pos -= 0.05
        else:
            self.big_clouds_pos = 0
        self.window.blit(self.big_clouds, (self.big_clouds_pos, 315))
        self.window.blit(self.big_clouds, (self.big_clouds_pos + 896, 315))
        self.window.blit(self.big_clouds, (self.big_clouds_pos + (896 * 2), 315))
        # Small Cloud 1
        if self.small_cloud_1_pos > -1500:
            self.small_cloud_1_pos -= 0.3
        else:
            self.small_cloud_1_pos = 0
        self.window.blit(self.small_cloud_1, (120 + self.small_cloud_1_pos, 100))
        self.window.blit(self.small_cloud_1, (120 + self.small_cloud_1_pos + 1500, 100))
        self.window.blit(self.small_cloud_1, (900 + self.small_cloud_1_pos, 50))
        self.window.blit(self.small_cloud_1, (900 + self.small_cloud_1_pos + 1500, 50))
        # Small Cloud 2
        if self.small_cloud_2_pos > -1500:
            self.small_cloud_2_pos -= 0.2
        else:
            self.small_cloud_2_pos = 0
        self.window.blit(self.small_cloud_2, (250 + self.small_cloud_2_pos, 200))
        self.window.blit(self.small_cloud_2, (250 + self.small_cloud_2_pos + 1500, 200))
        self.window.blit(self.small_cloud_2, (1000 + self.small_cloud_2_pos, 150))
        self.window.blit(self.small_cloud_2, (1000 + self.small_cloud_2_pos + 1500, 150))
        # Small Cloud 3
        if self.small_cloud_2_pos > -1500:
            self.small_cloud_3_pos -= 0.2
        else:
            self.small_cloud_3_pos = 0
        self.window.blit(self.small_cloud_3, (650 + self.small_cloud_3_pos, 250))
        self.window.blit(self.small_cloud_3, (650 + self.small_cloud_3_pos + 1500, 250))
        # Big water effect
        if self.big_water_animation_frame <= 12:
            self.window.blit(self.big_water_1, (300, 550))
        if self.big_water_animation_frame <= 24:
            self.window.blit(self.big_water_2, (300, 550))
        if self.big_water_animation_frame <= 36:
            self.window.blit(self.big_water_3, (300, 550))
        if self.big_water_animation_frame <= 48:
            self.window.blit(self.big_water_4, (300, 550))
        self.big_water_animation_frame += 1
        if self.big_water_animation_frame > 48:
            self.big_water_animation_frame = 0
        # Medium water effect
        if self.medium_water_animation_frame <= 12:
            self.window.blit(self.medium_water_1, (250, 600))
            self.window.blit(self.medium_water_1, (500, 625))
        if self.big_water_animation_frame <= 24:
            self.window.blit(self.medium_water_2, (250, 600))
            self.window.blit(self.medium_water_2, (500, 625))
        if self.big_water_animation_frame <= 36:
            self.window.blit(self.medium_water_3, (250, 600))
            self.window.blit(self.medium_water_3, (500, 625))
        if self.big_water_animation_frame <= 48:
            self.window.blit(self.medium_water_4, (250, 600))
            self.window.blit(self.medium_water_4, (500, 625))
        self.medium_water_animation_frame += 1
        if self.medium_water_animation_frame > 48:
            self.medium_water_animation_frame = 0
        # Small water effect
        if self.small_water_animation_frame <= 12:
            self.window.blit(self.small_water_1, (1000, 600))
            self.window.blit(self.small_water_1, (900, 625))
        if self.small_water_animation_frame <= 24:
            self.window.blit(self.small_water_2, (1000, 600))
            self.window.blit(self.small_water_3, (900, 625))
        if self.small_water_animation_frame <= 36:
            self.window.blit(self.small_water_3, (1000, 600))
            self.window.blit(self.small_water_3, (900, 625))
        if self.small_water_animation_frame <= 48:
            self.window.blit(self.small_water_4, (1000, 600))
            self.window.blit(self.small_water_4, (900, 625))
        self.small_water_animation_frame += 1
        if self.small_water_animation_frame > 48:
            self.small_water_animation_frame = 0

    def tiles(self):
        range_y = len(self.map)
        range_x = len(self.map[0])
        for y in range(range_y):
            for x in range(range_x):
                if self.map[y][x] != ' ':
                    if self.map[y][x] == '1':
                        self.window.blit(self.ground_1, (x * 64, y * 64))
                    elif self.map[y][x] == '2':
                        self.window.blit(self.ground_2, (x * 64, y * 64))
                    elif self.map[y][x] == '3':
                        self.window.blit(self.ground_3, (x * 64, y * 64))
                    elif self.map[y][x] == '4':
                        self.window.blit(self.ground_4, (x * 64, y * 64))
                    elif self.map[y][x] == '5':
                        self.window.blit(self.ground_5, (x * 64, y * 64))
                    elif self.map[y][x] == '6':
                        self.window.blit(self.ground_6, (x * 64, y * 64))
                    elif self.map[y][x] == '7':
                        self.window.blit(self.ground_7, (x * 64, y * 64))
                    elif self.map[y][x] == '8':
                        self.window.blit(self.ground_8, (x * 64, y * 64))
                    elif self.map[y][x] == '9':
                        self.window.blit(self.ground_9, (x * 64, y * 64))

    def player_idle(self):
        if self.player_animation_frame <= 7:
            self.window.blit(self.player_idle_1, (self.player_pos[0], self.player_pos[1]))
        elif self.player_animation_frame <= 14:
            self.window.blit(self.player_idle_2, (self.player_pos[0], self.player_pos[1]))
        elif self.player_animation_frame <= 21:
            self.window.blit(self.player_idle_3, (self.player_pos[0], self.player_pos[1]))
        elif self.player_animation_frame <= 28:
            self.window.blit(self.player_idle_4, (self.player_pos[0], self.player_pos[1]))
        elif self.player_animation_frame <= 35:
            self.window.blit(self.player_idle_5, (self.player_pos[0], self.player_pos[1]))
        self.player_animation_frame += 1
        if self.player_animation_frame > 35:
            self.player_animation_frame = 0

    def player_idle_left(self):
        if self.player_animation_frame <= 7:
            self.window.blit(self.player_idle_left_1, (self.player_pos[0], self.player_pos[1]))
        elif self.player_animation_frame <= 14:
            self.window.blit(self.player_idle_left_2, (self.player_pos[0], self.player_pos[1]))
        elif self.player_animation_frame <= 21:
            self.window.blit(self.player_idle_left_3, (self.player_pos[0], self.player_pos[1]))
        elif self.player_animation_frame <= 28:
            self.window.blit(self.player_idle_left_4, (self.player_pos[0], self.player_pos[1]))
        elif self.player_animation_frame <= 35:
            self.window.blit(self.player_idle_left_5, (self.player_pos[0], self.player_pos[1]))
        self.player_animation_frame += 1
        if self.player_animation_frame > 35:
            self.player_animation_frame = 0

    def player_right(self):
        if self.player_animation_frame <= 7:
            self.window.blit(self.player_right_1, (self.player_pos[0], self.player_pos[1]))
        elif self.player_animation_frame <= 14:
            self.window.blit(self.player_right_2, (self.player_pos[0], self.player_pos[1]))
        elif self.player_animation_frame <= 21:
            self.window.blit(self.player_right_3, (self.player_pos[0], self.player_pos[1]))
        elif self.player_animation_frame <= 28:
            self.window.blit(self.player_right_4, (self.player_pos[0], self.player_pos[1]))
        elif self.player_animation_frame <= 35:
            self.window.blit(self.player_right_5, (self.player_pos[0], self.player_pos[1]))
        elif self.player_animation_frame <= 42:
            self.window.blit(self.player_right_6, (self.player_pos[0], self.player_pos[1]))
        self.player_animation_frame += 1
        if self.player_animation_frame > 42:
            self.player_animation_frame = 0

    def player_left(self):
        if self.player_animation_frame <= 7:
            self.window.blit(self.player_left_1, (self.player_pos[0], self.player_pos[1]))
        elif self.player_animation_frame <= 14:
            self.window.blit(self.player_left_2, (self.player_pos[0], self.player_pos[1]))
        elif self.player_animation_frame <= 21:
            self.window.blit(self.player_left_3, (self.player_pos[0], self.player_pos[1]))
        elif self.player_animation_frame <= 28:
            self.window.blit(self.player_left_4, (self.player_pos[0], self.player_pos[1]))
        elif self.player_animation_frame <= 35:
            self.window.blit(self.player_left_5, (self.player_pos[0], self.player_pos[1]))
        elif self.player_animation_frame <= 42:
            self.window.blit(self.player_left_6, (self.player_pos[0], self.player_pos[1]))
        self.player_animation_frame += 1
        if self.player_animation_frame > 42:
            self.player_animation_frame = 0

    def player_collider(self):
        pos_x = self.player_pos[0] + 40
        pos_y = self.player_pos[1] + 8
        box = [[pos_x, pos_y],
                [pos_x + self.player_box_colider[0], pos_y],
                [pos_x, pos_y + self.player_box_colider[1]],
                [pos_x + self.player_box_colider[0], pos_y + self.player_box_colider[1]]]
        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                if self.map[y][x] != ' ':
                    for i in range(len(box)):
                        if x * 64 <= box[i][0] and y * 64 <= box[i][1] and (x * 64) + 64 >= box[i][0] and (y * 64) + 64 >= box[i][1]:
                            return True
        return False

    def player(self):
        self.player_vertical_speed += self.gravity
        self.player_pos[1] += self.player_vertical_speed
        if self.player_collider():
            self.player_pos[1] -= self.player_vertical_speed
            self.player_vertical_speed = 0
        if self.player_animation == 0:
            self.player_idle()
        if self.player_animation == 1:
            self.player_idle_left()
        if self.player_animation == 2:
            self.player_right()
        if self.player_animation == 3:
            self.player_left()

    def move(self, array, key):
        buttom_press = False

        # Left
        if array[97] == True:
            self.player_pos[0] -= 5
            if self.player_collider():
                self.player_pos[0] += 5
            else:
                self.player_animation = 3
                buttom_press = True
        # Right
        if array[100] == True:
            self.player_pos[0] += 5
            if self.player_collider():
                self.player_pos[0] -= 5
            else:
                self.player_animation = 2
                buttom_press = True

        if buttom_press == False and self.player_animation == 2:
            self.player_animation = 0
        elif buttom_press == False and self.player_animation == 3:
            self.player_animation = 1

        if key == 'space':
            self.player_vertical_speed = self.player_jump_force


jogo = TreasureHunters()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            jogo.move(pg.key.get_pressed(), pg.key.name(event.key))
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
    jogo.move(pg.key.get_pressed(), '')
    jogo.background_imgs()
    jogo.tiles()
    jogo.player()

    jogo.last_click_status = mouse_input

    pg.display.update()
