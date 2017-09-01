import pygame

flags = pygame.DOUBLEBUF
resolution = (600, 800)
screen = None
scene = None

def init(caption = "mygame"):
    print "Screen initialization"
    pygame.display.init()
    title(caption)
    update_mode()

def update_mode():
    global screen
    screen = pygame.display.set_mode(resolution, flags)

def title(caption):
    pygame.display.set_caption(caption)

def update():
    
    # update scene
    if scene is not None:
        scene.update(pygame.display)
    
    # update screen
    pygame.display.flip()

def toggle_fullscreen():
    flags ^= pygame.FULLSCREEN
    update_mode()

def set_resolution(x, y):
    resolution = (x, y)

def quit():
    pygame.display.quit()
