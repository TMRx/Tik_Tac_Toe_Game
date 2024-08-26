import pygame

# pygame setup
pygame.init()
WINDOW_WIDTH = 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_WIDTH))
clock = pygame.time.Clock()
running = True


def load_icon(path, resolution):
    icon = pygame.image.load(path)
    return pygame.transform.scale(icon, resolution)

grid_image = load_icon('Icons/white_grid.png', (WINDOW_WIDTH, WINDOW_WIDTH))
icon_x = load_icon('Icons/x_icon.png', [WINDOW_WIDTH // 3, WINDOW_WIDTH // 3])
icon_0 = load_icon('Icons/0_icon.png', [WINDOW_WIDTH // 3, WINDOW_WIDTH // 3])


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    screen.blit(grid_image, (0, 0))
    screen.blit(icon_x, (0, 0))
    screen.blit(icon_0, (WINDOW_WIDTH // 3 ,WINDOW_WIDTH // 3))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
