# Basic Pygame Structure

import pygame                               # Imports pygame and other libraries
import random
# Define Classes (sprites) here
class FallingObject(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.timecreated = pygame.time.get_ticks()
        self.image = pygame.Surface([100,100])
        self.image.set_colorkey(black)

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,670)
        self.rect.y = 0

    def setImage(self,graphiSelected):
        fallingObjectsImage = pygame.image.load(graphiSelected)
        self.image.blit(fallingObjectsImage,(0,0))

    def moveFallingObjects(self, distance):
        if self.rect.y <= 470:
            self.rect.y = self.rect.y + distance

    def deleteFallingObjects(self,oldscore):
        if self.rect.y > 470:
            self.kill()
            newscore = oldscore + 1
            return newscore
        else:
            return oldscore



class Character(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50,68])
        self.image.set_colorkey(black)



        self.rect = self.image.get_rect()
        self.rect.x = 310
        self.rect.y = 420

        self.image.blit(pygame.image.load("Superhero.png"),(0,0))
    #def deleteApple(self):
       #if FallingObject.rect.y = Character.rect.y:
            #self.kill()



    def moveCharacter(self,movement):
        if self.rect.x >= 5 and self.rect.x <= 645:
            self.rect.x = self.rect.x + movement
        if self.rect.x<5:
            self.rect.x = 5
        if self.rect.x>645:
            self.rect.x = 645


pygame.init()                               # Pygame is initialised (starts running)

screen = pygame.display.set_mode([700,500]) # Set the width and height of the screen [width,height]
pygame.display.set_caption("Dodge") # Name your window
background_image = pygame.image.load("OrchardBackground.jpg").convert()
done = False                                # Loop until the user clicks the close button.
clock = pygame.time.Clock()                 # Used to manage how fast the screen updates
black    = (   0,   0,   0)    # Define some colors using rgb values.  These can be
Blue    = (   0,   0,   255)
green    = (   0,  255,   0)
red    = (   255,   0,   0)
purple    = (   130,   0,   130)
white    = ( 255, 255, 255)        # used throughout the game instead of using rgb values.
font = pygame.font.Font(None, 36)

# Define additional Functions and Procedures here
lp = 3
lifepoints = (f'Lp:')

allFallingObjects = pygame.sprite.Group()
spdke = 2500
nextApple = pygame.time.get_ticks() + spdke

charactersGroup = pygame.sprite.Group()
character = Character()
charactersGroup.add(character)

movement = 0

score = 0
#add abilities




# -------- Main Program Loop -----------
while done == False:

    for event in pygame.event.get():        # Check for an event (mouse click, key press)
        if event.type == pygame.QUIT:       # If user clicked close window
            done = True                     # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movement = -5
            if event.key == pygame.K_RIGHT:
                movement = 5
        if event.type == pygame.KEYUP:
            movement = 0

    # Update sprites here
    if pygame.time.get_ticks() > nextApple:
        nextObject = FallingObject()
        nextObject.setImage("pixil-frame-0.png") # asndias bb ljnfvs bdisdfhjedf kfdsbnvhd fidgvdskhf bshel
        allFallingObjects.add(nextObject)
        nextApple = pygame.time.get_ticks() + 1500

    for eachobject in (allFallingObjects.sprites()):
        eachobject.moveFallingObjects(5)

        score = eachobject.deleteFallingObjects(score)

    character.moveCharacter(movement)

    collisions = pygame.sprite.groupcollide(allFallingObjects,charactersGroup,True,False)
    if len(collisions)>0:
        lp = lp-1
        print(f'{lp}')


    if lp == 0:

        done = True

    #display player health accor



    screen.blit(background_image, [0,0])
    allFallingObjects.draw(screen)
    charactersGroup.draw(screen)
    textImg = font.render(str(score),1,white)
    screen.blit( textImg, (10,10) )
    textImg = font.render(str(lifepoints),1,red)
    screen.blit( textImg, (640,5) )
    textImg = font.render(str(lp),1,red)
    screen.blit( textImg, (680,5) )




    pygame.display.flip()                   # Go ahead and update the screen with what we've drawn.
    clock.tick(40)                          # Limit to 20 frames per second

pygame.quit()                               # Close the window and quit.
