import pygame
import calls

# handler for key down
on_key_down = None

def get():
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            raise calls.IntCall
            
        elif event.type == pygame.KEYDOWN:
            if on_key_down is not None:
                on_key_down(event.key)

        #elif event.type == pygame.
