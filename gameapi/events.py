import pygame
import calls
import actions

# handler for key down
on_key_down = None

def get():
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            raise calls.IntCall
            
        elif event.type == pygame.KEYDOWN:
            if on_key_down is not None:
                on_key_down(event.key)
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                left()
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                right()
            if event.key == pygame.K_p:
                pause()
            if event.key == pygame.K_UP or event.key == pygame.K_SPACE or event.key == pygame.K_w:
                jump()
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                crouch()
                

##        elif event.type == pygame.KEYUP:
            
