# Import a library of functions called 'pygame'
import pygame
import math 
# Initialize the game engine
pygame.init()
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
NIGHTBLUE = (42,67,122)
GREEN = (0, 255, 0)
DARKERGREEN = (73, 168, 56)
RED = (255, 0, 0)
BROWN = (122, 83, 70)
TREEBARK = (92, 39, 13)
MAROON = (128, 0, 0)
ROOFCOLOUR = (122, 61, 10)
GREY = (211, 211, 211)
TREEGREEN = (41, 112, 26)
PI = 3.141592653
 
# Set the height and width of the screen
size = (900, 900)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("House")
 
# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
# Loop as long as done == False
while not done:
 
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while not done loop.
 
    # Clear the screen and set the screen background
    screen.fill(NIGHTBLUE)
 
    #Smoke
    for i in range(200):
     
        radians_x = i /25
        radians_y = i /10
     
        x = int(300 * math.sin(radians_x)) + 600
        y = int(300 * math.cos(radians_y)) + 600
     
        pygame.draw.line(screen, GREY, [600,800], [565+5,220], 35)    
    #Floor
    pygame.draw.rect(screen, TREEGREEN, [0, 830, 900, 600])
 
    #House body
    pygame.draw.rect(screen, BROWN, [280, 530, 400, 300])
    pygame.draw.rect(screen, BLACK, [280, 530, 400, 300],3)
    pygame.draw.rect(screen, BLACK, [350, 730, 55, 100])
    pygame.draw.rect(screen, WHITE, [360,740,33,10])
    pygame.draw.rect(screen, WHITE, [393,783,5,5])
       
        
    #Windows
    pygame.draw.rect(screen, BLACK, [550,600,60,60],5)
    pygame.draw.rect(screen, WHITE, [550,600,60,60])
    pygame.draw.rect(screen, BLACK, [350,600,60,60],5)
    pygame.draw.rect(screen, WHITE, [350,600,60,60])    
    
     
    #Moon
    pygame.draw.ellipse(screen, WHITE, [700, 50, 150, 150]) 
    pygame.draw.ellipse(screen, BLACK, [700, 50, 150, 150],1)
 
    # Roof
    pygame.draw.polygon(screen, ROOFCOLOUR, [[250, 530], [480, 350], [710, 530]], )
    pygame.draw.polygon(screen, BLACK, [[250, 530], [480, 350], [710, 530]],3 )
    pygame.draw.polygon(screen, MAROON, [[600,295], [600,445], [550,405], [550,280]])
    pygame.draw.polygon(screen, BLACK, [[600,295], [600,445], [550,405], [550,280]],2)
    
    #Tree
       
    pygame.draw.rect(screen, BLACK, [120, 720, 70, 110],4)
    pygame.draw.ellipse(screen, BLACK, [80, 600, 150, 150],20)    
    pygame.draw.rect(screen, TREEBARK, [120, 720, 70, 110])
    pygame.draw.ellipse(screen, DARKERGREEN, [80, 600, 150, 150])      
    
    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)
 
    # Render the text. "True" means anti-aliased text.
    # Black is the color. This creates an image of the
    # letters, but does not put it on the screen
    text = font.render("Merry Christmas", True, WHITE)
 
    # Put the image of the text on the screen at 250x250
    screen.blit(text, [100, 100])
 
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)
 
# Be IDLE friendly
pygame.quit()