import pygame

class Scene(pygame.sprite.Group):
    def __init__(self, background):
        pygame.sprite.Group.__init__(self)

    def update(screen):
        # TODO, find a way to blit only a part of the background
        img = background
        
        self.clear(screen, img)
        self.update()
        self.draw(screen)
        
    # TODO, override Group methods to fit with your game
