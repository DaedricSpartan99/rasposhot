import pygame
import calls

# handler for key down
on_key_down = None

block_size = 0
lead_x_change = 0
lead_y_change = 0

def get():
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            raise calls.IntCall
            
        elif event.type == pygame.KEYDOWN:
            if on_key_down is not None:
                on_key_down(event.key)
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                lead_x_change = -block_size
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                lead_x_change = block_size
            if event.key == pygame.K_p:
                pause()
                

##        elif event.type == pygame.KEYUP:
            
