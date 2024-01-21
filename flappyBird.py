# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# player setup
velocity = 0
gravity = 0.5
jumpHeight = 10
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
hasFlapped = False

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if hasFlapped == False:
            hasFlapped = True
            velocity = -jumpHeight
            print("Flap")
    else:
        hasFlapped = False

    player_pos.y += velocity
    pygame.draw.circle(screen, "red", player_pos, (40 + -velocity))
    velocity += gravity

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()