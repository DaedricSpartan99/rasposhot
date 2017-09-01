import screen
import pygame
import calls
import events

fps = 60
delta_time = 1.0 / fps

def init():
    pygame.init()

def start(gameloop, onquit = None):

    global delta_time

    clock = pygame.time.Clock()

    print "Starting game"

    quitcause = None

    while(True):

        try:
            
            # sleep and update delta_time in seconds
            delta_time = clock.tick(fps) / 1000.0
            
            # process events
            events.get()

            #exec game loop
            gameloop()

            # update all
            screen.update()
            
        except calls.SkipCall:
            continue
        except calls.IntCall as call:
            quitcause = call
            break
        except Exception as error:
            quitcause = calls.GameError(error)
            break

    print "Stopping game"

    if onquit is not None:
        onquit(quitcause)

    # close screen
    screen.quit()
    # close game
    pygame.quit()

def quit():
    raise calls.IntCall

def skip():
    raise calls.SkipCall
