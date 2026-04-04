import pygame as pg
import time


class SnakePuzzle:
    def __init__(self):
        self.black       = (  0,   0,   0)
        self.brown       = (140,  90,  50)
        self.brown_light = (180, 130,  90)

        self.window = pg.display.set_mode((1386, 756))

        pg.font.init()
        self.font = pg.font.SysFont("Courier New", 50, bold=True)

        self.clock = pg.time.Clock()

        self.snake_position_by_level = {
            '1': {'level': [[ 7, 4], [ 6, 4], [ 5, 4]], 'direction': [1, 0]},
            '2': {'level': [[ 8, 6], [ 7, 6], [ 6, 6]], 'direction': [1, 0]},
            '3': {'level': [[ 9, 7], [ 8, 7], [ 7, 7]], 'direction': [1, 0]},
            '4': {'level': [[10, 5], [10, 6], [10, 7]], 'direction': [0,-1]},
            '5': {'level': [[ 8, 7], [ 7, 7], [ 6, 7]], 'direction': [1, 0]}
            }

        self.level = 1
        self.level_completed = True
        self.game_over = False
        self.rock_falling = False
        self.time = 0

        self.snake_position = [[0, 0],[0, 0],[0, 0]]
        self.snake_direction = self.snake_position_by_level[str(self.level)]['direction']
        self.snake_head_animation_mode = 1
        self.snake_just_eat_apple = True
        self.snake_falling = False
        self.last_snake_position = []

        background      = pg.image.load('./background.jpg')
        head_1          = pg.image.load('./head 1.png')
        head_2          = pg.image.load('./head 2.png')
        head_3          = pg.image.load('./head 3.png')
        head_4          = pg.image.load('./head 4.png')
        head_5          = pg.image.load('./head 5.png')
        straight_body   = pg.image.load('./straight body.png')
        curves_outwards = pg.image.load('./curves outwards.png')
        curves_inward   = pg.image.load('./curves inward.png')
        tail            = pg.image.load('./tail.png')
        apple           = pg.image.load('./apple.png')           # A
        rock            = pg.image.load('./rock.png')            # R
        thorns          = pg.image.load('./thorns.png')          # w
        circular_saw    = pg.image.load('./circular saw.png')    # *
        black_hole      = pg.image.load('./black hole.png')      # O
        self.background      = pg.transform.scale(background,      (1386, 756))
        self.head_1          = pg.transform.scale(head_1,          (  63,  63))
        self.head_2          = pg.transform.scale(head_2,          (  63,  63))
        self.head_3          = pg.transform.scale(head_3,          (  63,  63))
        self.head_4          = pg.transform.scale(head_4,          (  63,  63))
        self.head_5          = pg.transform.scale(head_5,          (  63,  63))
        self.straight_body   = pg.transform.scale(straight_body,   (  63,  63))
        self.curves_outwards = pg.transform.scale(curves_outwards, (  63,  63))
        self.curves_inward   = pg.transform.scale(curves_inward,   (  63,  63))
        self.tail            = pg.transform.scale(tail,            (  63,  63))
        self.apple           = pg.transform.scale(apple,           (  63,  63))
        self.rock            = pg.transform.scale(rock,            (  63,  63))
        self.thorns          = pg.transform.scale(thorns,          (  63,  63))
        self.circular_saw    = pg.transform.scale(circular_saw,    (  63,  63))
        self.black_hole      = pg.transform.scale(black_hole,      (  63,  63))

        self.map = [['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']]

        self.levels = {
            'level_1': [['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '','#','#','#','#', '', '', '','O', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '','#','#','#','#','#', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']],

            'level_2': [['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', '', '', '', '', '','O', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', '','#', '', '', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '','#','A','#', '', '', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', '', '', '','R', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '','#','#','#', '','#','#','#', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '','#','#','#', '', '', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']],

            'level_3': [['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '','#', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '','#', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '','#', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '','#', '','R', '', '', '', '','O', '', '', '', '', '', ''],
                        ['', '', '', '', '', '','#','#','#','#','#', '', '', '', '','#', '', '', '', '', '', ''],
                        ['', '', '', '', '','A', '', '', '', '', '', '', '', '', '','#', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', '', '','R', '', '', '','#', '', '', '', '', '', ''],
                        ['', '', '', '','#', '','#','#','#','#','#','#','#', '', '','#', '', '', '', '', '', ''],
                        ['', '', '', '','#','#','#', '', '', '', '', '','#','#','#','#', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']],

            'level_4': [['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '','#', '', '','A','#', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '','#', '', '', '', '','O', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '','#','#', '', '','#','#', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', '', '','W','#', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '','#','#','#','#', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']],

            'level_5': [['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '','#', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '','#', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '','#', '', '', '','*','#', '', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '','#','#', '', '','#','#', '', '', '','A', '', '', '', '', '', ''],
                        ['', '', '', '', '','A', '', '', '', '', '','#','#', '', '','#', '','#', '', '', '', ''],
                        ['', '', '', '','A', '', '','#','#', '', '','#','#', '','*','#','#','#', '', '', '', ''],
                        ['', '', '', '', '', '','#','#','#', '', '', '', '', '', '','O', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']]
        }

    def clear_window(self):
        self.window.blit(self.background, (0, 0))

    def is_level_completed(self):
        if self.level_completed:
            self.load_level()
            self.level_completed = False

    def board(self):
        level_text = self.font.render(f'Level {self.level}', True, self.black)
        self.window.blit(level_text, (0, 0))

        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                if self.map[y][x] == '#':
                    pg.draw.rect(self.window, self.brown, (x*63, y*63, 63, 63), border_radius=5)
                    pg.draw.rect(self.window, self.brown_light, (x*63, y*63, 63, 63), 6, 5)
                    pg.draw.rect(self.window, self.black, (x*63, y*63, 63, 63), 3, 5)
                elif self.map[y][x] == 'A':
                    self.window.blit(self.apple, (x*63, y*63))
                elif self.map[y][x] == 'R':
                    self.window.blit(self.rock, (x*63, y*63))
                elif self.map[y][x] == 'W':
                    self.window.blit(self.thorns, (x*63, y*63))
                elif self.map[y][x] == '*':
                    self.window.blit(self.circular_saw, (x*63, y*63))
                elif self.map[y][x] == 'O':
                    self.window.blit(self.black_hole, (x*63, y*63))

    def snake_blinking(self):
        self.time += 1
        if self.time >= 300:
            self.time = 1

    def snake_head_animation(self):
        if self.snake_head_animation_mode not in [3, 4, 5] and self.time >= 270:
            rotated_image = self.snake_segmentation_rotation(self.head_2, 0)
        elif self.snake_head_animation_mode == 1:
            rotated_image = self.snake_segmentation_rotation(self.head_1, 0)
        elif self.snake_head_animation_mode == 3:
            rotated_image = self.snake_segmentation_rotation(self.head_3, 0)
        elif self.snake_head_animation_mode == 4:
            rotated_image = self.snake_segmentation_rotation(self.head_4, 0)
        elif self.snake_head_animation_mode == 5:
            rotated_image = self.snake_segmentation_rotation(self.head_5, 0)

        return rotated_image

    def snake_segmentation_rotation(self, image, snake_segmentation):
        if snake_segmentation == 0:
            if self.snake_direction == [1, 0]:
                rotated_image = pg.transform.rotate(image, 0)
            elif self.snake_direction == [-1, 0]:
                rotated_image = pg.transform.rotate(image, 180)
            elif self.snake_direction == [0, 1]:
                rotated_image = pg.transform.rotate(image, -90)
            elif self.snake_direction == [0, -1]:
                rotated_image = pg.transform.rotate(image, 90)
        else:
            x = self.snake_position[snake_segmentation - 1][0] - self.snake_position[snake_segmentation][0]
            y = self.snake_position[snake_segmentation - 1][1] - self.snake_position[snake_segmentation][1]
            if [x, y] == [1, 0]:
                rotated_image = pg.transform.rotate(image, 0)
            elif [x, y] == [-1, 0]:
                rotated_image = pg.transform.rotate(image, 180)
            elif [x, y] == [0, 1]:
                rotated_image = pg.transform.rotate(image, -90)
            elif [x, y] == [0, -1]:
                rotated_image = pg.transform.rotate(image, 90)

        return rotated_image

    def is_snake_body_inwards_or_outwards(self, segmentation):
        previous_snake_segmentation_x = self.snake_position[segmentation + 1][0]
        previous_snake_segmentation_y = self.snake_position[segmentation + 1][1]
        current_snake_segmentation_x  = self.snake_position[segmentation][0]
        current_snake_segmentation_y  = self.snake_position[segmentation][1]
        next_snake_segmentation_x     = self.snake_position[segmentation - 1][0]
        next_snake_segmentation_y     = self.snake_position[segmentation - 1][1]

        if previous_snake_segmentation_x < next_snake_segmentation_x:
            if previous_snake_segmentation_y > next_snake_segmentation_y:
                if current_snake_segmentation_x > previous_snake_segmentation_x:
                    return 'outward'
                elif current_snake_segmentation_y < previous_snake_segmentation_y:
                    return 'inward'
            elif previous_snake_segmentation_y < next_snake_segmentation_y:
                if current_snake_segmentation_x > previous_snake_segmentation_x:
                    return 'inward'
                elif current_snake_segmentation_y > previous_snake_segmentation_y:
                    return 'outward'
        elif previous_snake_segmentation_x > next_snake_segmentation_x:
            if previous_snake_segmentation_y > next_snake_segmentation_y:
                if current_snake_segmentation_x < previous_snake_segmentation_x:
                    return 'inward'
                elif current_snake_segmentation_y < previous_snake_segmentation_y:
                    return 'outward'
            elif previous_snake_segmentation_y < next_snake_segmentation_y:
                if current_snake_segmentation_x < previous_snake_segmentation_x:
                    return 'outward'
                elif current_snake_segmentation_y > previous_snake_segmentation_y:
                    return 'inward'

    def draw_snake(self):
        for segmentation in range(len(self.snake_position)):
            segmentation_x = self.snake_position[segmentation][0]
            segmentation_y = self.snake_position[segmentation][1]
            if segmentation == 0:
                image = self.snake_head_animation()
                self.window.blit(image, (segmentation_x * 63, segmentation_y * 63))
            else:
                if segmentation == len(self.snake_position) - 1:
                    image = self.snake_segmentation_rotation(self.tail, segmentation)
                    self.window.blit(image, (segmentation_x * 63, segmentation_y * 63))
                else:
                    previous_snake_segmentation_x = self.snake_position[segmentation + 1][0]
                    previous_snake_segmentation_y = self.snake_position[segmentation + 1][1]
                    next_snake_segmentation_x     = self.snake_position[segmentation - 1][0]
                    next_snake_segmentation_y     = self.snake_position[segmentation - 1][1]
                    if ((previous_snake_segmentation_x == segmentation_x and segmentation_x == next_snake_segmentation_x)
                        or (previous_snake_segmentation_y == segmentation_y and segmentation_y == next_snake_segmentation_y)):
                        image = self.snake_segmentation_rotation(self.straight_body, segmentation)
                        self.window.blit(image, (segmentation_x * 63, segmentation_y * 63))
                    elif self.is_snake_body_inwards_or_outwards(segmentation) == 'inward':
                        image = self.snake_segmentation_rotation(self.curves_inward, segmentation)
                        self.window.blit(image, (segmentation_x * 63, segmentation_y * 63))
                    elif self.is_snake_body_inwards_or_outwards(segmentation) == 'outward':
                        image = self.snake_segmentation_rotation(self.curves_outwards, segmentation)
                        self.window.blit(image, (segmentation_x * 63, segmentation_y * 63))

    def load_level(self):
        # Reset game_over variable
        self.game_over = False
        # Reset snake head direction
        self.snake_direction = self.snake_position_by_level[str(self.level)]['direction']
        # Reset snake body position
        self.snake_position = [[0, 0],[0, 0],[0, 0]]
        for segmentation in range(len(self.snake_position_by_level[str(self.level)]['level'])):
            self.snake_position[segmentation][0] = self.snake_position_by_level[str(self.level)]['level'][segmentation][0]
            self.snake_position[segmentation][1] = self.snake_position_by_level[str(self.level)]['level'][segmentation][1]
        # Reset map
        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                self.map[y][x] = self.levels[f'level_{self.level}'][y][x]

    def action(self, key):
        if (key == 'w' or key == 'up') and self.snake_direction != [0, 1]:
            self.snake_move([0, -1])
        elif (key == 'a' or key == 'left') and self.snake_direction != [1, 0]:
            self.snake_move([-1, 0])
        elif (key == 's' or key == 'down') and self.snake_direction != [0, -1]:
            self.snake_move([0, 1])
        elif (key == 'd' or key == 'right') and self.snake_direction != [-1, 0]:
            self.snake_move([1, 0])
        elif key == 'r':
            self.load_level()

    def snake_move(self, direction):
        # Update self.last_snake_position
        self.last_snake_position = self.snake_position[len(self.snake_position)-1].copy()

        if self.game_over == False:
            # Check for special condition for the snake to eat an apple
            x = self.snake_position[0][0] + direction[0]
            y = self.snake_position[0][1] + direction[1]
            if self.map[y][x] == 'A':
                self.snake_position.insert(0, [x, y])
                self.map[y][x] = ''
                self.snake_just_eat_apple = True
                self.snake_head_animation_mode = 4
                self.snake_direction = direction
                return

            x = self.snake_position[0][0] + direction[0]
            y = self.snake_position[0][1] + direction[1]

            # Is snake colide with your own body
            for segmentation in self.snake_position:
                if segmentation == [x, y]:
                    return

            # Is snake colide with brick
            if self.map[y][x] == '#':
                return

            # Updating snake head direction 
            last_direction = self.snake_direction.copy()       
            self.snake_direction = direction

            # Check if is a valid move
            is_fall_valid = 0
            for segmentation in range(len(self.snake_position)):
                x = self.snake_position[segmentation][0]
                y = self.snake_position[segmentation][1] + 1
                if self.map[y][x] not in ['#', 'A', 'R']:
                    is_fall_valid += 1

            # Updating snake body position
            for segmentation in range(len(self.snake_position) - 1, -1, -1):
                if segmentation == 0:
                    self.snake_position[segmentation][0] += direction[0]
                    self.snake_position[segmentation][1] += direction[1]
                else:
                    if segmentation == len(self.snake_position) - 1:
                        last_position = self.snake_position[segmentation].copy()
                    self.snake_position[segmentation] = self.snake_position[segmentation - 1].copy()

            # Returning snake move if it is not valid
            if (is_fall_valid == len(self.snake_position) and self.snake_direction == [0, -1]) or self.pushing_stone():
                self.snake_direction = last_direction
                for segmentation in range(len(self.snake_position)):
                    if segmentation == 0:
                        self.snake_position[segmentation][0] -= direction[0]
                        self.snake_position[segmentation][1] -= direction[1]
                    else:
                        if segmentation == len(self.snake_position) - 1:
                            self.snake_position[segmentation] = last_position
                        else:
                            self.snake_position[segmentation] = self.snake_position[segmentation + 1].copy()
            else:
                if self.snake_just_eat_apple:
                    self.snake_head_animation_mode = 1
                    self.snake_just_eat_apple = False

    def snake_fall(self):
        if self.game_over == False:
            is_fall_valid = 0
            for segmentation in range(len(self.snake_position)):
                x = self.snake_position[segmentation][0]
                y = self.snake_position[segmentation][1] + 1
                if self.map[y][x] not in ['#', 'A', 'R']:
                    is_fall_valid += 1

            if is_fall_valid == len(self.snake_position):
                self.snake_falling = True
                for segmentation in range(len(self.snake_position)):
                    self.snake_position[segmentation][1] += 1
            else:
                self.snake_falling = False

    def snake_fall_animation(self):
        if self.snake_falling:
            time.sleep(0.250)
            pg.display.update()

    def pushing_stone(self):
        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                if self.map[y][x] == 'R':
                    if self.snake_position[0][0] == x and self.snake_position[0][1] == y:
                        if self.map[y + self.snake_direction[1]][x + self.snake_direction[0]] == '':
                            self.map[y][x] = ''
                            self.map[y + self.snake_direction[1]][x + self.snake_direction[0]] = 'R'
                            return False
                        else:
                            return True

    def stone_fall(self):
        falling_rock_count = 0
        falling_rocks = []
        skip_stone = False

        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                if self.map[y][x] == 'R':
                    if x < len(self.map[0])-1 and y < len(self.map)-1:
                        for segmentation in range(len(self.snake_position)):
                            if self.snake_position[segmentation][0] == x and self.snake_position[segmentation][1] == y + 1:
                                skip_stone = True
                        if skip_stone:
                            skip_stone = False
                            continue
                        elif self.map[y+1][x] == '':
                            falling_rocks.append([x, y])
                            falling_rock_count += 1

        if falling_rock_count >= 1:
            for rock in range(len(falling_rocks)):
                self.map[falling_rocks[rock][1]][falling_rocks[rock][0]] = ''
                self.map[falling_rocks[rock][1]+1][falling_rocks[rock][0]] = 'R'
                self.rock_falling = True
        else:
            self.rock_falling = False

    def stone_fall_animation(self):
        if self.rock_falling:
            pg.display.update()
            time.sleep(0.250)

    def snake_eat_apple(self):
        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                if self.map[y][x] == 'A':
                    if self.snake_position[0] == [x, y]:
                        self.snake_just_eat_apple = True
                        self.snake_head_animation_mode = 4
                        self.map[y][x] = ''
                        self.snake_position.append(self.last_snake_position)
                    elif self.snake_position[0] in [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]:
                        self.snake_head_animation_mode = 3
                    else:
                        self.snake_head_animation_mode = 1

    def snake_game_over(self):
        for segmentation in range(len(self.snake_position)):
            x = self.snake_position[segmentation][0]
            y = self.snake_position[segmentation][1]
            if self.map[y][x] in ['W', '*']:
                self.game_over = True
                self.snake_head_animation_mode = 5

    def snake_win(self):
        if self.game_over == False:
            for y in range(len(self.map)):
                for x in range(len(self.map[0])):
                    if self.map[y][x] == 'O':
                        if self.snake_position[0] == [x, y]:
                            self.level_completed = True
                            self.level += 1
                            if self.level > len(self.levels):
                                self.level = 1

    def is_snake_outsise_map(self):
        for segmentation in range(len(self.snake_position)):
            if self.snake_position[segmentation][1] == 11:
                self.load_level()
        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                if self.map[y][x] == 'R':
                    if y == 11:
                        self.load_level()


snake_puzzle = SnakePuzzle()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            snake_puzzle.action(pg.key.name(event.key))
            if pg.key.name(event.key) == 'escape':
                pg.quit()
                quit()

    # Game
    snake_puzzle.clock.tick(60)
    snake_puzzle.clear_window()

    snake_puzzle.is_level_completed()
    snake_puzzle.snake_blinking()
    snake_puzzle.draw_snake()
    snake_puzzle.snake_eat_apple()
    snake_puzzle.board()
    snake_puzzle.snake_win()
    snake_puzzle.stone_fall()
    snake_puzzle.snake_fall_animation()
    snake_puzzle.snake_fall()
    snake_puzzle.stone_fall_animation()
    snake_puzzle.snake_game_over()
    snake_puzzle.is_snake_outsise_map()

    pg.display.update()
