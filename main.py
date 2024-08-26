import pygame

# pygame setup
pygame.init()
WINDOW_WIDTH = 720
PIXEL_WIDTH = WINDOW_WIDTH // 3
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_WIDTH))
clock = pygame.time.Clock()
running = True

def load_icon(path, resolution):
    icon = pygame.image.load(path)
    return pygame.transform.scale(icon, resolution)

board = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

grid = load_icon('Icons/white_grid.png', (WINDOW_WIDTH, WINDOW_WIDTH))
icon_x = load_icon('Icons/x_icon.png', (PIXEL_WIDTH, PIXEL_WIDTH))
icon_0 = load_icon('Icons/0_icon.png', (PIXEL_WIDTH, PIXEL_WIDTH))
player = 0

def play_turn(curr_player):
    curr_coord = pygame.math.Vector2(pygame.mouse.get_pos()) // PIXEL_WIDTH
    if pygame.mouse.get_pressed()[0]:  # Left mouse button clicked
        col, row = map(int, curr_coord)
        if board[row][col] is None:  # Only place icon if the cell is empty
            board[row][col] = 0 if curr_player == 0 else 1
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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Detect mouse click
            play_turn(player)

    screen.fill('white')
    screen.blit(grid, (0, 0))
    draw_icons()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
