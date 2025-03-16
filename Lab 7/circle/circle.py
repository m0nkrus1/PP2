import pygame

pygame.init()

screen = pygame.display.set_mode((800, 480))
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)

ball_pos = [400, 240]
ball_radius = 25
move_step = 20

clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ball_pos[1] - ball_radius > 0:
        ball_pos[1] -= move_step
    if keys[pygame.K_DOWN] and ball_pos[1] + ball_radius < 480:
        ball_pos[1] += move_step
    if keys[pygame.K_LEFT] and ball_pos[0] - ball_radius > 0:
        ball_pos[0] -= move_step
    if keys[pygame.K_RIGHT] and ball_pos[0] + ball_radius < 800:
        ball_pos[0] += move_step

    screen.fill(COLOR_WHITE)
    pygame.draw.circle(screen, COLOR_RED, ball_pos, ball_radius)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
