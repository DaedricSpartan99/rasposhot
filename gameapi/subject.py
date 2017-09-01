import pygame
import os

class Subject(pygame.sprite.Sprite):
    def __init__(self, image):
        self.image = image
        self.rect = image.get_rect()

def load(path):

    path = None
    
    try:
        path = os.path.join(path)
    except:
        return path
        
    return pygame.image.load(path)

def surface(size, color):
    surf = pygame.Surface(size)
    surf.fill(color)
    return surf

# TODO all transformations

