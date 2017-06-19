 
import pygame
 
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
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (1280, 900)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")


 
# Loop until the user clicks the close button.
done = False

def drawtree(screen, x, y):
    pygame.draw.rect(screen, BLACK, [x, y, 70, 110],4)    
    pygame.draw.rect(screen, TREEBARK, [x, y, 70, 110])
    pygame.draw.ellipse(screen, DARKERGREEN, [-40+x, -130+y, 150, 150])     
def drawhouse(screen, x, y):
    #House body
    pygame.draw.rect(screen, BROWN, [280+x, 530+y, 400, 300])
    pygame.draw.rect(screen, BLACK, [280+x, 530+y, 400, 300],3)
    pygame.draw.rect(screen, BLACK, [350+x, 730+y, 55, 100])
    pygame.draw.rect(screen, WHITE, [360+x,740+y,33,10])
    pygame.draw.rect(screen, WHITE, [393+x,783+y,5,5])
       
    #Windows
    pygame.draw.rect(screen, BLACK, [550+x,600+y,60,60],5)
    pygame.draw.rect(screen, WHITE, [550+x,600+y,60,60])
    pygame.draw.rect(screen, BLACK, [350+x,600+y,60,60],5)
    pygame.draw.rect(screen, WHITE, [350+x,600+y,60,60])

    # Roof
    pygame.draw.polygon(screen, ROOFCOLOUR, [[250+x, 530+y], [480+x, 350+y], [710+x, 530+y]], )
    pygame.draw.polygon(screen, BLACK, [[250+x, 530+y], [480+x, 350+y], [710+x, 530+y]],3 )
    pygame.draw.polygon(screen, MAROON, [[600+x,295+y], [600+x,445+y], [550+x,405+y], [550+x,280+y]])
    pygame.draw.polygon(screen, BLACK, [[600+x,295+y], [600+x,445+y], [550+x,405+y], [550+x,280+y]],2)
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
x = 0
y = 0
x_coord = 0
y_coord = 0
# -------- Main Program Loop -----------
pygame.key.set_repeat(1,1)
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        elif event.type == pygame.KEYDOWN:
                # Figure out if it was an arrow key. If so
                # adjust speed.
            if event.key == pygame.K_LEFT:
                if(x <= -240):
                    break
                else:
                    x += -30
            elif event.key == pygame.K_RIGHT:
                if(x >= 570):
                    break
                else:
                    x += 30
            elif event.key == pygame.K_UP:
                if(y <= -270):
                    break
                else:
                    y += -30
            elif event.key == pygame.K_DOWN:
                if(y >= 50):
                    break
                else:
                    y += 30
        
               
                   
            # User let up on a key
        elif event.type == pygame.KEYUP:
                # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0        
        
        
 
    screen.fill(BLACK)
    drawhouse(screen, x, y)
    drawtree(screen, x_coord, y_coord)
    
    
    
  
    
    
    # --- Game logic should go here
    pos = pygame.mouse.get_pos()
    x_coord = pos[0]
    y_coord = pos[1]    
    # Hide the mouse cursor
    pygame.mouse.set_visible(False)    
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    
    
    pygame.display.flip()
    
    
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
