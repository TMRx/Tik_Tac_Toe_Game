import pygame

# pygame setup
pygame.init()
WINDOW_WIDTH = 720
PIXEL_WIDTH = WINDOW_WIDTH // 3
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_WIDTH))
clock = pygame.time.Clock()
running = True
font = pygame.font.SysFont('Arial', 32)

text = font.render('', True, 'green')
textRect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_WIDTH // 2))


def load_icon(path, resolution):
    try:
        icon = pygame.image.load(path)
        return pygame.transform.scale(icon, resolution)
    except pygame.error as e:
        print(f"Cannot load image: {path}. Error: {e}")
        return pygame.Surface(resolution)


board = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

grid = load_icon('Icons/white_grid.png', (WINDOW_WIDTH, WINDOW_WIDTH))
icon_x = load_icon('Icons/x_icon2.png', (PIXEL_WIDTH, PIXEL_WIDTH))
icon_0 = load_icon('Icons/0_icon2.png', (PIXEL_WIDTH, PIXEL_WIDTH))
PLAYER_1 = 0
PLAYER_2 = 1
player = PLAYER_1


def play_turn(curr_player):
    curr_coord = pygame.math.Vector2(pygame.mouse.get_pos()) // PIXEL_WIDTH
    col, row = map(int, curr_coord)
    if 0 <= row < 3 and 0 <= col < 3:  # Ensure click is within board limits
        if pygame.mouse.get_pressed()[0] and board[row][col] is None:  # Left mouse button clicked
            board[row][col] = curr_player
            global player
            player = 1 - player
            print(board)


def draw_icons():
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == 0:
                screen.blit(icon_0, (j * PIXEL_WIDTH, i * PIXEL_WIDTH))
            elif col == 1:
                screen.blit(icon_x, (j * PIXEL_WIDTH, i * PIXEL_WIDTH))


def equal_icons(elements, game_player):
    for element in elements:
        if element != game_player:
            return False
    return True


def winning_row(game_player):
    return equal_icons(board[0], game_player) \
        or equal_icons(board[1], game_player) \
        or equal_icons(board[2], game_player)


def winning_col(game_player):
    return equal_icons([board[0][0], board[1][0], board[2][0]], game_player) \
        or equal_icons([board[0][1], board[1][1], board[2][1]], game_player) \
        or equal_icons([board[0][2], board[1][2], board[2][2]], game_player)


def winning_diagonal(game_player):
    return equal_icons([board[0][0], board[1][1], board[2][2]], game_player) \
        or equal_icons([board[0][2], board[1][1], board[2][0]], game_player)


def is_winner(game_player):
    return winning_row(game_player) \
        or winning_col(game_player) \
        or winning_diagonal(game_player)


def check_victory():
    global text
    if is_winner(PLAYER_1):
        text = font.render('Player 1 Winner!!!', True, 'green')
        return True
    elif is_winner(PLAYER_2):
        text = font.render('Player 2 Winner!!!', True, 'green')
        return True
    return False


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Detect mouse click
            play_turn(player)

    screen.fill('white')
    screen.blit(grid, (0, 0))
    draw_icons()

    if check_victory():
        screen.blit(text, textRect)
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False
    else:
        pygame.display.flip()

    clock.tick(60)

pygame.quit()
