import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def draw_tree(screen, x, y):
    pygame.draw.rect(screen, RED, [60+x, 170+y, 30, 45])
    pygame.draw.polygon(screen, GREEN, [[150+x,170+y],[75+x,20+y], [x,170+y]])
    pygame.draw.polygon(screen, GREEN, [[140+x,120+y], [75+x,y], [10+x,120+y]])  
def sum_two_numbers(a, b):
    result = a + b
    return result
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
draw_tree(screen, 0, 230)
draw_tree(screen, 200, 230)
draw_tree(screen, 400, 230) 
# Store the function's result into a variable
my_result = sum_two_numbers(22, 15)
print(my_result) 
    # --- Go ahead and update the screen with what we've drawn.
pygame.display.flip()
 
    # --- Limit to 60 frames per second
clock.tick(60)
 
# Close the window and quit.
pygame.quit()