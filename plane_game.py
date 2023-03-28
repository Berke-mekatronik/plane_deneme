import pygame
import random
pygame.init()
clock = pygame.time.Clock()

WIDTH = 1000
LENGTH = 600
BACK = (244,244,244)
FPS = (150)

RED=(255,0,0)
BACK =(244,244,244)
BLUE= (0,0,255)

surface = pygame.display.set_mode((WIDTH, LENGTH))
pygame.display.set_caption("Plane Game")
ship = pygame.image.load("C:/Users/hp/PycharmProjects/plane_deneme/aircraft.png")

ship_x = 100
ship_y = 100
ship_xvel = 0
ship_yvel = 0

step = 10

last_direction = 'right'

reward_x = round(random.randrange(0, WIDTH - step) / 10.0) * 10.0
reward_y = round(random.randrange(0, LENGTH - step) / 10.0) * 10.0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship_xvel = 1
                ship_yvel = 0
                last_direction = 'right'
            if event.key == pygame.K_LEFT:
                ship_xvel = -1
                ship_yvel = 0
                last_direction = 'left'
            if event.key == pygame.K_UP:
                ship_yvel = -1
                ship_xvel = 0
                last_direction = 'up'
            if event.key == pygame.K_DOWN:
                ship_yvel = 1
                ship_xvel = 0
                last_direction = 'down'

    ship_x = ship_x + ship_xvel
    ship_y = ship_y + ship_yvel

    r_ship = ship.copy()
    if last_direction == 'up':
        r_ship = pygame.transform.rotate(ship, 90)
    if last_direction == 'right':
        r_ship = pygame.transform.rotate(ship, 0)
    if last_direction == 'left':
        r_ship = pygame.transform.rotate(ship, 180)
    if last_direction == 'down':
        r_ship = pygame.transform.rotate(ship, -90)

    kirmiz_kare = pygame.Surface((20,20))
    kirmiz_kare.fill(RED)
    kirmizi_kare_rect = kirmiz_kare.get_rect()
    kirmizi_kare_rect.center = (reward_x, reward_y)

    r_ship_rect = ship.get_rect()
    r_ship_rect.center = (ship_x, ship_y)

    if ship_x >= WIDTH-30 or ship_x < 30 or ship_y >= LENGTH-30 or ship_y < 30:
        running = False

    if r_ship_rect.colliderect(kirmizi_kare_rect):
        reward_x = round(random.randrange(0, WIDTH - step) / 10.0) * 10.0
        reward_y = round(random.randrange(0, LENGTH - step) / 10.0) * 10.0

    surface.fill(BACK)
    surface.blit(r_ship, r_ship_rect)
    surface.blit(kirmiz_kare, kirmizi_kare_rect)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()
