import pygame as pg

white        = (255, 255, 255)
black        = (  0,   0,   0)
purple_dark  = (181, 181, 255)
purple_light = (230, 230, 255)
green        = (  0, 255,   0)
green_light  = (180, 255, 180)
blue         = (  0,   0, 255)

window = pg.display.set_mode((800, 500))

pg.font.init()
fonte = pg.font.SysFont("Courier New", 50, bold=True)

game_map = [['x', 'x', 'o', 'o', 'o', 'x', 'x'],
            ['x', 'x', 'o', 'o', 'o', 'x', 'x'],
            ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
            ['o', 'o', 'o', '_', 'o', 'o', 'o'],
            ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
            ['x', 'x', 'o', 'o', 'o', 'x', 'x'],
            ['x', 'x', 'o', 'o', 'o', 'x', 'x']]

# Variáveis de mouse
last_click_status = (False, False, False)

# Variáveis de posição do jogo
selected = [-2, -2]
last_selected = [-2, -2]

def mouse_has_clicked(input):
        if last_click_status == input:
            return (False, False, False)
        else:
            left_button = False
            center_button = False
            right_button = False
            if last_click_status[0] == False and input[0] == True:
                left_button = True
            if last_click_status[1] == False and input[1] == True:
                center_button = True
            if last_click_status[2] == False and input[2] == True:
                right_button = True

            return (left_button, center_button, right_button)

def clear_window():
    pg.draw.rect(window, white, (0, 0, window.get_width(), window.get_height()))

def heigh_light(mouse):
    off_set = 50
    size = (window.get_height() - (off_set / 2)) / len(game_map)

    for y in range(len(game_map)):
        for x in range(len(game_map[0])):
            square_x = (mouse[0][0] + ((size / 2) - off_set)) // size
            square_y = (mouse[0][1] + ((size / 2) - off_set)) // size
            if game_map[y][x] != 'x' and square_x <= 6  and square_y <= 6 and square_x == x  and square_y == y:
                pg.draw.rect(window, purple_light, \
                             ((square_x * size) + off_set - (size / 2), (square_y * size) + off_set - (size / 2), size, size))
                if mouse[2][0]:
                    last_selected[0] = int(selected[0])
                    last_selected[1] = int(selected[1])
                    selected[0] = int(square_x)
                    selected[1] = int(square_y)
                    return selected, last_selected
    return selected, last_selected

def select():
    off_set = 50
    size = (window.get_height() - (off_set / 2)) / len(game_map)

    pg.draw.rect(window, purple_dark, ((selected[0] * size) + off_set - (size / 2), (selected[1] * size) + off_set - (size / 2), size, size))

def draw_board():
    off_set = 50
    size = (window.get_height() - (off_set / 2)) / len(game_map)
    radius = (size * 0.8) / 2
    width = int(radius * 0.2)

    for y in range(len(game_map)):
        for x in range(len(game_map[0])):
            if game_map[y][x] == 'o':
                pg.draw.circle(window, blue, ((x * size) + off_set, (y * size) + off_set), radius)
                pg.draw.circle(window, black, ((x * size) + off_set, (y * size) + off_set), radius, width)
            elif game_map[y][x] == '_':
                pg.draw.circle(window, (100, 100, 100), ((x * size) + off_set, (y * size) + off_set), radius / 2)

def change():
    if last_selected[0] == -2:
        pass
    else:
        if game_map[selected[1]][selected[0]] == '_' and game_map[last_selected[1]][last_selected[0]] == 'o':
            if selected[0] == last_selected[0]:
                if selected[1] == last_selected[1] - 2 and game_map[last_selected[1] - 1][last_selected[0]] == 'o':
                    game_map[selected[1]][selected[0]] = 'o'
                    game_map[last_selected[1]][last_selected[0]] = '_'
                    game_map[last_selected[1] - 1][last_selected[0]] = '_'
                elif selected[1] == last_selected[1] + 2 and game_map[last_selected[1] + 1][last_selected[0]] == 'o':
                    game_map[selected[1]][selected[0]] = 'o'
                    game_map[last_selected[1]][last_selected[0]] = '_'
                    game_map[last_selected[1] + 1][last_selected[0]] = '_'
            if selected[1] == last_selected[1]:
                if selected[0] == last_selected[0] - 2 and game_map[last_selected[1]][last_selected[0] - 1] == 'o':
                    game_map[selected[1]][selected[0]] = 'o'
                    game_map[last_selected[1]][last_selected[0]] = '_'
                    game_map[last_selected[1]][last_selected[0] - 1] = '_'
                if selected[0] == last_selected[0] + 2 and game_map[last_selected[1]][last_selected[0] + 1] == 'o':
                    game_map[selected[1]][selected[0]] = 'o'
                    game_map[last_selected[1]][last_selected[0]] = '_'
                    game_map[last_selected[1]][last_selected[0] + 1] = '_'
            return game_map
        
def count_o():
    count = 0
    for y in range(len(game_map)):
        for x in range(len(game_map[0])):
            if game_map[y][x] == 'o':
                count += 1

    texto = fonte.render(f'Restam {count}', 1, black)
    window.blit(texto, (window.get_width() * 0.63, window.get_height() * 0.05))

def restart():
    new_game_map = [['x', 'x', 'o', 'o', 'o', 'x', 'x'],
                    ['x', 'x', 'o', 'o', 'o', 'x', 'x'],
                    ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
                    ['o', 'o', 'o', '_', 'o', 'o', 'o'],
                    ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
                    ['x', 'x', 'o', 'o', 'o', 'x', 'x'],
                    ['x', 'x', 'o', 'o', 'o', 'x', 'x']]
    for y in range(len(new_game_map)):
        for x in range(len(new_game_map[0])):
            game_map[y][x] = new_game_map[y][x]
    selected[0] = -2
    selected[1] = -2
    last_selected[0] = -2
    last_selected[1] = -2
    
    return game_map, selected, last_selected

def restart_b(mouse):
    if mouse[0][0] >= (window.get_width() * 0.64) and mouse[0][1] >= (window.get_height() * 0.20) and \
       mouse[0][0] <= (window.get_width() * 0.64) + 250 and mouse[0][1] <= (window.get_height() * 0.20) + 75:
        pg.draw.rect(window, green_light, (window.get_width() * 0.64, window.get_height() * 0.20, 250, 75))
        if mouse[2][0]:
            restart()
    else:
        pg.draw.rect(window, green, (window.get_width() * 0.64, window.get_height() * 0.20, 250, 75))
    
    pg.draw.rect(window, black, (window.get_width() * 0.64, window.get_height() * 0.20, 250, 75), 7)
    texto = fonte.render('Restart', 1, black)
    window.blit(texto, (window.get_width() * 0.665, window.get_height() * 0.22))

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
    mouse_click = mouse_has_clicked(mouse_input)
    mouse = (mouse_position, mouse_input, mouse_click)

    # Jogo
    clear_window()
    heigh_light(mouse)
    select()
    draw_board()
    change()
    count_o()
    restart_b(mouse)

    last_click_status = mouse_input

    pg.display.update()
