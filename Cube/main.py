import pygame
from sys import exit
import Cube.colorMode

# this initalizes the agme
pygame.init()

#the resualtion of the box
res = (1000,800)
print(pygame.display.get_desktop_sizes)
#this sets the size of the game
screen = pygame.display.set_mode((res))
#sounds
pygame.mixer.music.load("sounds/ping.mp3")
# colors
rgb = [255,0,0]
rgb = colorMode.rgbMode(rgb)

#this sets the name of the program
pygame.display.set_caption("test")

#this sest the games tick rate
clock = pygame.time.Clock()

#this makes the walls and colors them
leftWallSurf = pygame.Surface((10,600))
leftWallSurf.fill("Red")
leftWallRect = leftWallSurf.get_rect(topleft = (10,10))

#this makes an obj and a hitbox for it
ballSurf = pygame.Surface((5,5))
ballSurf.fill(rgb)
ballRect = ballSurf.get_rect(topleft = (100,30))

# speed and direction
inc = .9 # how much is added per bounce
directionY = 1
speedY = 1
speedX = 1
directionX = 1
grav = 0
temp = 0
# color


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            exit()

    #this displays test surf at x,y
    #screen.blit(leftWallSurf,(200,100))

    #this sets the balls "sprite to the balls hit box"
    screen.blit(ballSurf, ballRect)
    # this sets the walls sprite to the hix box

    #screen.blit(leftWallSurf, leftWallRect)



    """keep in mind box length and hight """
    #bonce handeling X
    if ballRect.x <= 0 :
        speedX = -speedX
        speedX += inc
        pygame.mixer.music.play()


    if ballRect.x >= res[0] -5 :
        speedX = -speedX
        speedX += inc
        pygame.mixer.music.play()


    # bonce handeling y
    if ballRect.y <=0 and ballRect.y >=-5:
        speedY = -speedY
        speedY += inc
        pygame.mixer.music.play()


    if ballRect.y >= res[1] - 5:
        speedY = -speedY
        speedY += inc
        pygame.mixer.music.play()



    # x and y speed
    ballRect.x += speedX
    ballRect.y += (speedY)

    speedY += grav
    print(ballRect.x,ballRect.y)


    #updates screen
    rgb = colorMode.rgbMode(rgb)
    ballSurf.fill(rgb)
    pygame.display.flip()
    #sets game tick

    clock.tick(600)