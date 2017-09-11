#!/usr/bin/env python

# main test rasposhot

##colpa di tumittu

import api_linkage
import gameapi

loop = 0

def keydown(key):
    if key == K_ESCAPE:
        gameapi.game.quit()

# bind key callback
gameapi.events.on_key_down = keydown

def gameloop():
    global loop

    print "Loop number:", loop
    print "Sleep time:", gameapi.game.delta_time

    loop += 1

def onquit(reason):
    
    if reason.isError():
        reason.printStackTrace()

def main():
    gameapi.game.init()
    gameapi.screen.init("Test")

    gameapi.game.start(gameloop, onquit)

if __name__ == "__main__":
    main()
