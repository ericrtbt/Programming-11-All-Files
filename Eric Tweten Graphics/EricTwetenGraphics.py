import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Load Background image
background_image = pygame.image.load("saturn_family1.bmp").convert()
player_image = pygame.image.load("player.bmp").convert()
click_sound = pygame.mixer.Sound("laser5.ogg")
player_image.set_colorkey(WHITE) 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click_sound.play()

    # --- Game logic should go here
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]     
    
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    #screen.fill(WHITE)
    screen.blit(background_image, [0, 0])
    # Copy image to screen:
    screen.blit(player_image, [x, y])         
    
    # --- Drawing code should go here
        
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()