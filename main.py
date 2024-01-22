# Example file showing a circle moving on screen
import pygame
 
# pygame setup
pygame.init()
screen = pygame.display.set_mode((432, 768)) 
clock = pygame.time.Clock()
running = True
dt = 0

# player setup
player = pygame.image.load('Images/Bird/0.png')
player = pygame.transform.scale(player, (85, 60))

playerAnimation = 0
shouldChangeAnimation = 0

velocity = 0
gravity = 0.5
jumpHeight = 10
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
hasFlapped = False

# background setup
background = pygame.image.load('Images/Deco/BGDay.png')
background = pygame.transform.scale(background, (432, 768))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.blit(background, (0, 0))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if hasFlapped == False:
            hasFlapped = True
            velocity = -jumpHeight
            print("Flap")
    else:
        hasFlapped = False

    player_pos.y += velocity
    screen.blit(pygame.transform.rotate(player, -velocity * 5), (50, player_pos.y))
    velocity += gravity

    shouldChangeAnimation += 1

    if shouldChangeAnimation == 10:
        shouldChangeAnimation = 0

        # sets to next image
        if playerAnimation == 2:
            playerAnimation = 0
        else:
            playerAnimation += 1

    player = pygame.image.load('Images/Bird/' + str(playerAnimation) + '.png')
    player = pygame.transform.scale(player, (85, 60))
    dt2 = clock.tick(10) / 1000

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()