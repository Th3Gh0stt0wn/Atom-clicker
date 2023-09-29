import pygame
from pygame import mixer 
import math #needed for square root function

pygame.init()#initializes Pygame
print(pygame.font.get_fonts())
pygame.display.set_caption("Atom Clicker")#sets the window title
screen = pygame.display.set_mode((400,400))#creates game screen



#player variables
xpos = 0
ypos = 0
mousePos = (xpos, ypos) #variable mousePos stores TWO numbers
numClicks = 0

#circle variables: circX and circY are the coordinates of the center (where it's drawn), and the radius is how big it is
circX = 200
circY = 200
radius = 100

font = pygame.font.Font('freesansbold.ttf', 32)
text1 = font.render('score:', False, (200, 0, 103))
text2 = font.render(str(int(numClicks)), 1, (200, 0, 103))

imgPic = pygame.transform.scale(pygame.image.load("atom-12414-2.jpg"),(200,200))
imgRect = imgPic.get_rect(topleft=(100,100))

img2Pic = pygame.transform.scale(pygame.image.load("atom-12414.jpg"),(210,210))
img2Rect = img2Pic.get_rect(topleft=(110,110))

mixer.init()
click = pygame.mixer.Sound("mouse-click.mp3")

isBig = False


#gameloop###################################################
while True:
#event queue (bucket that holds stuff that happens in game and passes to one of the sections below)
    event = pygame.event.wait()

    if event.type == pygame.QUIT: #close game window
        break
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        pygame.mixer.Sound.play(click)

    if event.type == pygame.MOUSEBUTTONDOWN: #check if clicked
        if math.sqrt((mousePos[0] - circX)**2 + (mousePos[1] - circY)**2)<radius:
            numClicks +=1
        print("CLICK")

    if event.type == pygame.MOUSEMOTION: #check if mouse moved
        mousePos = event.pos #refreshes mouse position
        print("mouse position: (",mousePos[0]," , ",mousePos[1], ")")
       
    if event.type == pygame.MOUSEMOTION:
        mousePos = event.pos
        print("mouse position: (",mousePos[0]," , ",mousePos[1], ")")
        if math.sqrt((mousePos[0] - circX)**2 + (mousePos[1] - circY)**2)<radius:
            isBig = True
        else:
            isBig = False
        
            
    print("CLICK")

    if event.type == pygame.MOUSEMOTION: #check if mouse moved
        mousePos = event.pos #refreshes mouse position
        print("mouse position: (",mousePos[0]," , ",mousePos[1], ")")
  
 
#render section---------------------------------------------
    screen.fill((183, 209, 237)) #wipe screen (without this, things smear)
    
    text2 = font.render(str(int(numClicks)), 1, (200, 0, 103))
    screen.blit(text1, (10, 10))
    screen.blit(text2, (110, 10))
            
    if isBig == False:
        screen.blit(imgPic, (100, 100))
    else:
        screen.blit(img2Pic, (110, 110))
        
    pygame.display.flip()
    pygame.draw.circle(screen, (200, 0, 200), (circX,circY), radius)
    print("clicks:", numClicks) #uncomment this once collision is set up
    
    

#end game loop##############################################

pygame.quit()
