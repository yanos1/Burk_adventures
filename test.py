import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))
lead_x = 230
lead_y = 230
lead_x_change = 0
lead_y_change = 0


clock = pygame.time.Clock()

def drawgame():
    win.fill((0,0,0))


def game_mechanics():
    if lead_x >= 481:
        pygame.quit()



run = True


while run:
    pygame.display.update()
    clock.tick(10)

    drawgame()
    game_mechanics()

    snake = pygame.draw.rect(win, (250, 250, 250), (lead_x, lead_y, 20, 20))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                lead_x_change = 5
                lead_y_change = 0

            if event.key == pygame.K_LEFT:
                lead_x_change = -5
                lead_y_change = 0

            if event.key == pygame.K_UP:
                lead_y_change = -5
                lead_x_change = 0

            if event.key == pygame.K_DOWN:
                lead_y_change = 5
                lead_x_change = 0

    lead_x += lead_x_change
    lead_y += lead_y_change




