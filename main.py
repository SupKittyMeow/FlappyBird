import pygame
import random

from pygame.sprite import Group, Group

__version__ = "1.0.0"
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

# group setup
bird = pygame.sprite.AbstractGroup()
pipes = pygame.sprite.AbstractGroup()

# player setup
playerImage = pygame.image.load('Images/Bird/0.png')
playerAnimation = 0
shouldChangeAnimation = 0
velocity = 0
gravity = 0.5
jumpHeight = 10
player_pos = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
hasFlapped = True
shouldStart = False
canFlap = True

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.transform.scale(playerImage, (85, 60))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image, 0)

    def update(self, playerAnimation) -> None:
        self.image = pygame.transform.scale(pygame.image.load('Images/Bird/' + str(playerAnimation) + '.png'), (85, 60))

bird = Player()

#pipe setup
bottomPipeImage = pygame.image.load('Images/Obsticles/PipeUp.png')
bottomPipe1 = pygame.transform.scale(bottomPipeImage, (26*3, 160*3))
bottomPipe1 = pygame.sprite.Sprite()
bottomPipe1.add()
topPipeImage = pygame.image.load('Images/Obsticles/PipeDown.png')
topPipe1 = pygame.transform.scale(topPipeImage, (26*3, 160*3))
topPipe1 = pygame.sprite.Sprite()
pipes.add(topPipe1)
pipeScrollingSpeed = 5
pipePos = SCREEN_WIDTH
pipeY1 = random.randint(300, 700)
alreadyAwardedPoint1 = False
alreadyAwardedPoint2 = False

class Pipe(pygame.sprite.Sprite):
    def __init__(self, pI) -> None:
        super().__init__()
        self.image = pygame.transform.scale(pI, (78, 480))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image, 0)

bottomPipe1 = Pipe(bottomPipeImage)
bottomPipe2 = Pipe(bottomPipeImage)
topPipe1 = Pipe(topPipeImage)
topPipe2 = Pipe(topPipeImage)

pipePos = SCREEN_WIDTH
pipePos2 = SCREEN_WIDTH + 500
pipeY1 = random.randint(300, 700)
pipeY2 = random.randint(300, 700)

bottomPipe1.rect.x = pipePos
bottomPipe1.rect.y = pipeY1
topPipe1.rect.x = pipePos
topPipe1.rect.y = pipeY1 - 700

bottomPipe2.rect.x = pipePos2
bottomPipe2.rect.y = pipeY2
topPipe2.rect.x = pipePos2
topPipe2.rect.y = pipeY2 - 700

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
uiTimer = 0

gameOver = pygame.image.load('Images/UI/GameOver.png')
gameOver = pygame.transform.scale(gameOver, (374.4, 81.9))
gameOver_x = (SCREEN_WIDTH - gameOver.get_width()) / 2

class ReplayButton(pygame.sprite.Sprite):
    def __init__(self, image) -> None:
        super().__init__()
        self.image = pygame.transform.scale(image, (156, 87))
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()

replayButton = ReplayButton(pygame.image.load('Images/UI/Play.png'))

# score setup
score = 0

# numbers = pygame.font.Font("Fonts/FlappyBirdFont.ttf", 30)
numbers = pygame.font.SysFont("Roboto", 30)

def resetGame():
    print('Replay')
    pygame.mixer.Sound.play(pygame.mixer.Sound("SFX/sfx_swooshing.wav"))
    exec(open("main.py").read())

while running:
    ev = pygame.event.get()

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in ev:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if hasFlapped == False:
                if canFlap:
                    pygame.mixer.Sound.play(pygame.mixer.Sound("SFX/sfx_wing.wav"))
                    hasFlapped = True
                    velocity = -jumpHeight
                    shouldStart = True
                    print("Flap")
        elif event.type == pygame.MOUSEBUTTONUP and uiTimer >= 60:
            mousePos = pygame.mouse.get_pos()
            if replayButton.rect.collidepoint(mousePos):
                resetGame()

    # fill the screen with a scrolling bg to wipe away anything from last frame
    if canFlap:
        bg1Pos -= bgScrollingSpeed
        bg2Pos -= bgScrollingSpeed 
    if bg1Pos <= -SCREEN_WIDTH:
        bg1Pos = SCREEN_WIDTH
    if bg2Pos <= -SCREEN_WIDTH:
        bg2Pos = SCREEN_WIDTH

    screen.blit(background1, (bg1Pos, 0))
    screen.blit(background2, (bg2Pos, 0)) 

    if shouldStart:
        bottomPipe1.rect.x = pipePos
        bottomPipe1.rect.y = pipeY1
        topPipe1.rect.x = pipePos
        topPipe1.rect.y = pipeY1 - 700
        bottomPipe2.rect.x = pipePos2
        bottomPipe2.rect.y = pipeY2
        topPipe2.rect.x = pipePos2
        topPipe2.rect.y = pipeY2 - 700
        screen.blit(bottomPipe1.image, (pipePos, pipeY1))
        screen.blit(topPipe1.image, (pipePos, pipeY1 - 700))
        screen.blit(bottomPipe2.image, (pipePos2, pipeY2))
        screen.blit(topPipe2.image, (pipePos2, pipeY2 - 700))
        
        if canFlap:
            pipePos -= pipeScrollingSpeed
            if pipePos <= -SCREEN_WIDTH:
                pipePos = SCREEN_WIDTH
                pipeY1 = random.randint(300, 700)
                alreadyAwardedPoint1 = False

            pipePos2 -= pipeScrollingSpeed
            if pipePos2 <= -SCREEN_WIDTH:
                pipePos2 = SCREEN_WIDTH
                pipeY2 = random.randint(300, 700)
                alreadyAwardedPoint2 = False
            if pipePos <= bird.rect.x and not alreadyAwardedPoint1:
                score += 1
                pygame.mixer.Sound.play(pygame.mixer.Sound("SFX/sfx_point.wav"))
                alreadyAwardedPoint1 = True
            elif pipePos2 <= bird.rect.x and not alreadyAwardedPoint2:
                score += 1
                pygame.mixer.Sound.play(pygame.mixer.Sound("SFX/sfx_point.wav"))
                alreadyAwardedPoint2 = True
    else:
        # Draw the image on the screen at its center point
        screen.blit(getReady, (getReady_x, 100))
        screen.blit(tapToFly, (tapToFly_x, 190))
     
    if not canFlap:
        uiTimer += 1
        if uiTimer == 20:
            pygame.mixer.Sound.play(pygame.mixer.Sound("SFX/sfx_fall.wav"))
        if uiTimer >= 60:
            screen.blit(gameOver, (gameOver_x, 175))
            replayButton.rect.x = int(SCREEN_WIDTH - replayButton.image.get_width() * 2)
            replayButton.rect.y = 350 
            screen.blit(replayButton.image, (replayButton.rect.x, 350))
            
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if uiTimer >= 60 and hasFlapped == False:
            resetGame()
        if hasFlapped == False:
            hasFlapped = True
            if canFlap:
                pygame.mixer.Sound.play(pygame.mixer.Sound("SFX/sfx_wing.wav"))
                velocity = -jumpHeight
                shouldStart = True
                print("Flap")
    else:
        hasFlapped = False
    
    player_pos.y += velocity
    bird.update(playerAnimation)
    bird.rect.x = 50
    bird.rect.y = int(player_pos.y)
    screen.blit(pygame.transform.rotate(bird.image, -velocity * 5), (50, player_pos.y))

    if shouldStart:
        velocity += gravity

    if pygame.sprite.collide_mask(bird, bottomPipe1) or pygame.sprite.collide_mask(bird, topPipe1) or pygame.sprite.collide_mask(bird, bottomPipe2) or pygame.sprite.collide_mask(bird, topPipe2):
        if canFlap:
            canFlap = False
            pygame.mixer.Sound.play(pygame.mixer.Sound("SFX/sfx_die.wav"))

    if player_pos.y > SCREEN_HEIGHT or player_pos.y < -40:
        if canFlap:
            canFlap = False
            pygame.mixer.Sound.play(pygame.mixer.Sound("SFX/sfx_die.wav"))

    shouldChangeAnimation += 1

    if shouldChangeAnimation == 5:
        shouldChangeAnimation = 0

        # sets to next image
        if playerAnimation == 2:
            playerAnimation = 0
        else:
            playerAnimation += 1

    font = pygame.font.Font('Fonts/FlappyBirdFont.ttf', 50)
    scoreTextSurface = font.render(str(score), True, (240,240,240), None)
    scoreTextRect = scoreTextSurface.get_rect()
    scoreTextRect.center  = (int(SCREEN_WIDTH / 2), 50)
    screen.blit(scoreTextSurface, scoreTextRect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

    if(not running):
        pygame.quit() 
