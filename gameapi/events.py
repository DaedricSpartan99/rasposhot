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
                if gameloop == True:
                    left()
                else:
                    pass
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if gameloop == True:
                    right()
                else:
                    pass
            if event.key == pygame.K_p:
                if gameloop == True:
                    pause()
                else:
                    pass
            if event.key == pygame.K_UP or event.key == pygame.K_SPACE or event.key == pygame.K_w:
                if gameloop == True:
                    jump()
                else:
                    pass
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if gameloop == True:
                    crouch()
                else:
                    pass
                

       elif event.type == pygame.KEYUP:
           if on_key_down is not None:
                on_key_down(event.key)
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                stop()
            
