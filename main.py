from pickle import TRUE
import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((432, 768)) 
pygame.display.set_caption('Flappy Bird')
pygame.display.set_icon(pygame.image.load('Images/Bird/0.png'))
clock = pygame.time.Clock()
SCREEN_WIDTH = screen.get_width()
SCREEN_HEIGHT = screen.get_height()
running = True
dt = 0

# player setup
player = pygame.sprite.Sprite()
player = pygame.image.load('Images/Bird/0.png')
playerAnimation = 0
shouldChangeAnimation = 0
velocity = 0
gravity = 0.5
jumpHeight = 10
player_pos = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
hasFlapped = False
shouldStart = False
canFlap = True

#pipe setup
bottomPipe = pygame.sprite.Sprite()
bottomPipe = pygame.image.load('Images/Obsticles/PipeUp.png')
bottomPipe = pygame.transform.scale(bottomPipe, (26*3, 160*3))
topPipe = pygame.sprite.Sprite()
topPipe = pygame.image.load('Images/Obsticles/PipeDown.png')
topPipe = pygame.transform.scale(topPipe, (26*3, 160*3))
pipeScrollingSpeed = 5
pipePos = SCREEN_WIDTH
pipeY = random.randint(300, 700)

# background setup
background1 = pygame.image.load('Images/Deco/BGDay.png')
background1 = pygame.transform.scale(background1, (432, 768))
bg1Pos = 0
background2 = pygame.image.load('Images/Deco/BGDay.png')
background2 = pygame.transform.scale(background2, (432, 768))
bg2Pos = SCREEN_WIDTH
bgScrollingSpeed = 0.5

# start ui setup
getReady = pygame.image.load('Images/UI/GetReady.png')
getReady = pygame.transform.scale(getReady, (276, 75))
tapToFly = pygame.image.load('Images/UI/TapToFly.png')
tapToFly = pygame.transform.scale(tapToFly, (171, 147))
getReady_x = (SCREEN_WIDTH - getReady.get_width()) / 2
tapToFly_x = (SCREEN_WIDTH - tapToFly.get_width()) / 2

# end ui setup
gameOver = pygame.image.load('Images/UI/GameOver.png')
gameOver = pygame.transform.scale(gameOver, (374.4, 81.9))
gameOver_x = (SCREEN_WIDTH - gameOver.get_width()) / 2
replayButton = pygame.image.load('Images/UI/Play.png')
replayButton = pygame.transform.scale(replayButton, (156, 87))
replay_x = (SCREEN_WIDTH - replayButton.get_width()) / 2
uiTimer = 0


while running:
    ev = pygame.event.get()

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in ev:
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a scrolling bg to wipe away anything from last frame
    bg1Pos -= bgScrollingSpeed
    if bg1Pos <= -SCREEN_WIDTH:
        bg1Pos = SCREEN_WIDTH
    bg2Pos -= bgScrollingSpeed 
    if bg2Pos <= -SCREEN_WIDTH:
        bg2Pos = SCREEN_WIDTH

    screen.blit(background1, (bg1Pos, 0))
    screen.blit(background2, (bg2Pos, 0)) 

    if shouldStart:
        pipePos -= pipeScrollingSpeed
        if canFlap:
            if pipePos <= -SCREEN_WIDTH:
                pipePos = SCREEN_WIDTH
                pipeY = random.randint(300, 700)
        screen.blit(bottomPipe, (pipePos, pipeY)) 
        screen.blit(topPipe, (pipePos, pipeY - 700)) 
    else:
        # Draw the image on the screen at its center point
        screen.blit(getReady, (getReady_x, 100))
        screen.blit(tapToFly, (tapToFly_x, 175))

    if not canFlap:
        uiTimer += 1
        if uiTimer >= 60:
            screen.blit(gameOver, (gameOver_x, 175))
            screen.blit(replayButton, (replay_x, 350))
            
    keys = pygame.key.get_pressed()

        # handle MOUSEBUTTONUP
    for event in ev:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if hasFlapped == False:
                if canFlap:
                    hasFlapped = True
                    velocity = -jumpHeight
                    shouldStart = True
                    print("Flap")
            
    if keys[pygame.K_SPACE]:
        if hasFlapped == False:
            if canFlap:
                hasFlapped = True
                velocity = -jumpHeight
                shouldStart = True
                print("Flap")
    else:
        hasFlapped = False
    
    player_pos.y += velocity
    screen.blit(pygame.transform.rotate(player, -velocity * 5), (50, player_pos.y))

    if shouldStart:
        velocity += gravity

    if player_pos.y > SCREEN_HEIGHT or player_pos.y < -40:
        canFlap = False

    shouldChangeAnimation += 1

    if shouldChangeAnimation == 5:
        shouldChangeAnimation = 0

        # sets to next image
        if playerAnimation == 2:
            playerAnimation = 0
        else:
            playerAnimation += 1

    player = pygame.image.load('Images/Bird/' + str(playerAnimation) + '.png')
    player = pygame.transform.scale(player, (85, 60))

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

    if(not running):
        pygame.quit() 